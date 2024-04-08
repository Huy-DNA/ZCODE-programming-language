from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class UninferredType(Type):
    pass

class FuncType(Type):
    def __init__(self, params, ret, defined):
        self.params = params
        self.ret = ret
        self.__list_of_uninferred_id = []
        self.defined = defined
    def addUninferredId(self, id, scope):
        self.__list_of_uninferred_id.append((id, scope))
    def resolveRet(self):
        pass

class Scope:
    def __init__(self, parent = None, associatedBlock = None):
        self.__parent = parent
        self.__varSymbolTable = dict()
        self.__fnSymbolTable = dict()
        self.associatedBlock = associatedBlock
        if associatedBlock:
            associatedBlock.scope = self
        if isinstance(associatedBlock, FuncDecl):
            self.associatedFn = associatedBlock
        elif isinstance(parent.associatedFn, FuncDecl):
            self.associatedFn = parent.associatedFn
        else:
            self.associatedFn = None

    def set(self, name, typ, kind):
        if not isinstance(typ, Type):
            raise Exception("Only symbols can be added")
        if not isinstance(kind, Kind):
            raise Exception("Invalid kind")

        if isinstance(kind, Function):
            self.__fnSymbolTable[name] = typ
        else:
            self.__varSymbolTable[name] = typ

    def get(self, name, kind):
        if not isinstance(kind, Kind):
            raise Exception("Invalid kind")
        if isinstance(kind, Function):
            return self.__fnSymbolTable[name]
        else:
            return self.__varSymbolTable[name]

    def lookup(self, name, kind):
        if not isinstance(kind, Kind):
            raise Exception("Invalid kind")
        if isinstance(kind, Function):
            if name in self.__fnSymbolTable[name]:
                return self.__fnSymbolTable[name], self
            if self.__parent is not None:
                return self.__parent.lookup(name, kind)
            return None, None
        else:
            if name in self.__varSymbolTable[name]:
                return self.__varSymbolTable[name], self
            if self.__parent is not None:
                return self.__parent.lookup(name, kind)
            return None, None

    def has(self, name, kind):
        if not isinstance(kind, Kind):
            raise Exception("Invalid kind")
        if isinstance(kind, Function):
            return name in self.__fnSymbolTable
        else:
            return name in self.__varSymbolTable

    def parent(self):
        return self.__parent

    def delegate(self, associatedBlock):
        return Scope(self, associatedBlock)

class CheckerParam:
    def __init__(self, scope, isLoop = False, lookupKind = None):
        self.scope = scope
        self.isLoop = isLoop
        self.lookupKind = lookupKind

class CheckerResult:
    def __init__(self, typ, scope, exprNode = None, fnType = None, isLvalue = False):
        self.type = typ
        self.scope = scope
        self.exprNode = exprNode
        self.fnType = fnType
        self.isLvalue = isLvalue

def isSameType(type1, type2):
    if isinstance(type1, ArrayType):
        return isinstance(type2, ArrayType) and isSameType(type1.eleType, type2.eleType) and type1.size == type2.size
    return isinstance(type1, type2.__class__) or isinstance(type2, type1.__class__) or type1 is type2 or isinstance(type1, type2) or isinstance(type2, type1)

def resolveUninferredType(checkerRes, typeHint):
    if checkerRes.fnType:
        checkerRes.fnType.ret = typeHint
        checkerRes.fnType.resolveRet()
    else:
        checkerRes.scope.set(checkerRes.exprNode.name, typeHint, Variable())

class StaticChecker(BaseVisitor, Utils):
    def visitProgram(self, ast, param):
        param = CheckerParam(Scope(None, ast), False, Variable())

    def visitVarDecl(self, ast, param):
        if param.scope.has(ast.name, Variable()):
            raise Redeclared(Variable(), ast.name) if isinstance(param.lookupKind, Parameter) else Redeclared(Parameter(), ast.name)
        if ast.varType:
            param.scope.set(ast.name, ast.varType, Variable())
            if ast.varInit:
                initRes = self.visit(ast.varInit, (param.scope, param.isLoop, Variable()))
                initType = initRes.type
                if not isSameType(ast.varType, initType):
                    raise TypeMismatchInStatement(ast)
        elif ast.varInit:
            typ = self.visit(ast.varInit, param).type
            if isSameType(typ, UninferredType):
                raise TypeCannotBeInferred(ast)
            param.scope.set(ast.name, typ, Variable())
        else:
            param.scope.set(ast.name, UninferredType(), Variable())

    def visitFuncDecl(self, ast, param):
        if param.scope.has(ast.name.name, Function()) and param.scope.get(ast.name.name, Function()).defined() and ast.body is not None:
            raise Redeclared(Function(), ast.name.name)

        paramParam = CheckerParam(param.scope.delegate(ast), None, Parameter())
        paramTypes = []
        for parameter in ast.param:
            res = self.visit(parameter, paramParam)
            paramTypes.append(res.type)
        retType = UninferredType()

        if param.scope.has(ast.name.name, Function()):
            fnType = param.scope.get(ast.name.name, Function())
            if len(fnType.params) != len(paramTypes):
                raise TypeMismatchInStatement(ast)
            for index, paramType in enumerate(paramTypes):
                if not isSameType(paramType, fnType.params[index]):
                    raise TypeMismatchInStatement(ast)
        fnType = FuncType(paramTypes, retType, ast.body is not None)
        if not param.scope.has(ast.name.name, Function()):
            param.scope.set(ast.name.name, fnType, Function())

        if ast.body is None:
            return CheckerResult(None, None, None, fnType)

        bodyParam = CheckerParam(paramParam.scope.delegate(ast.body), False, Variable())
        self.visit(ast.body, bodyParam)
        fnType.resolveRet()
        return CheckerResult(None, None)

    def visitBinaryOp(self, ast, param):
        op = ast.op

        leftRes = self.visit(ast.left, param)
        leftType = leftRes.type
        rightRes = self.visit(ast.right, param)
        rightType = rightRes.type

        if op in ['+', '-', '*', '/', '%']:
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, NumberType())
                leftType = NumberType()
            if isSameType(rightType, UninferredType):
                resolveUninferredType(rightRes, NumberType())
                rightType = NumberType()
            if not isSameType(leftType, NumberType) or not isSameType(rightType, NumberType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(NumberType(), param.scope, ast)
        if op in ['and', 'or']:
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, BoolType())
                leftType = BoolType()
            if isSameType(rightType, UninferredType):
                resolveUninferredType(rightRes, BoolType())
                rightType = BoolType()
            if not isSameType(leftType, BoolType) or not isSameType(rightType, BoolType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope, ast)
        if op == '...':
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, StringType())
                leftType = StringType()
            if isSameType(rightType, UninferredType):
                resolveUninferredType(leftRes, StringType())
                rightType = StringType()
            if not isSameType(leftType, StringType) or not isSameType(rightType, StringType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(StringType(), param.scope, ast)
        if op in ['=', '!=', '<', '>', '<=', '>=']:
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, NumberType())
                leftType = NumberType()
            if isSameType(rightType, UninferredType):
                resolveUninferredType(leftRes, NumberType())
                rightType = NumberType()
            if not isSameType(leftType, NumberType) or not isSameType(rightType, NumberType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope, ast)
        if op == '==':
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, StringType())
                leftType = StringType()
            if isSameType(rightType, UninferredType):
                resolveUninferredType(leftRes, StringType())
                rightType = StringType()
            if not isSameType(leftType, StringType) or not isSameType(rightType, StringType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope, ast)

        raise Exception('Unreachable')

    def visitUnaryOp(self, ast, param):
        op = ast.op

        res = self.visit(ast.operand, param)
        typ = res.type

        if op == '-':
            if isSameType(typ, UninferredType):
                resolveUninferredType(res, NumberType())
                return CheckerResult(NumberType(), param.scope, ast)
            if isSameType(typ, NumberType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(NumberType(), param.scope, ast)
        if op == 'not':
            if isSameType(typ, UninferredType):
                resolveUninferredType(res, BoolType())
                return CheckerResult(BoolType(), param.scope, ast)
            if isSameType(typ, BoolType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope, ast)

        raise Exception('Unreachable')

    def visitCallExpr(self, ast, param):
        calleeType = self.visit(ast.name, (param.scope, param.isLoop, Function())).type
        if isSameType(calleeType.ret, VoidType()):
            raise TypeMismatchInExpression(ast)
        if len(calleeType.params) != len(ast.args):
            raise TypeMismatchInExpression(ast)
        paramTypes = calleeType.params
        for index, paramTyp in enumerate(paramTypes):
            argRes = self.visit(ast.args[index], param)
            argTyp = argRes.type
            if isSameType(argTyp, UninferredType):
                resolveUninferredType(argRes, paramTyp)
            if not isSameType(paramTyp, argTyp):
                raise TypeMismatchInExpression(ast)
        return CheckerResult(calleeType.ret, param.scope, ast, calleeType)

    def visitId(self, ast, param):
        typ, scope = param.scope.lookup(ast.name, param.lookupKind)
        if typ is None:
            raise Undeclared(param.lookupKind, ast.name)
        return CheckerResult(typ, scope, ast, None, True)

    def visitArrayCell(self, ast, param):
        arrType = self.visit(ast.arr, param).type
        if not isSameType(arrType, ArrayType):
            raise TypeMismatchInExpression(ast)
        size = arrType.size
        if len(ast.idx) != len(size):
            raise TypeMismatchInExpression(ast)
        for expr in ast.idx:
            exprRes = self.visit(expr, param)
            if isSameType(exprType, UninferredType):
                resolveUninferredType(exprRes, NumberType())
            if not isSameType(exprType, NumberType):
                raise TypeMismatchInExpression(expr)
        return CheckerResult(arrType.eleType, param.scope, ast, None, True)

    def visitBlock(self, ast, param):
        param = CheckerParam(param.scope.delegate(ast), param.isLoop)
        for stmt in ast.stmt:
            self.visit(stmt, param)
        return CheckerResult(None, param.scope)

    def visitIf(self, ast, param):
        condRes = self.visit(ast.expr, param)
        condType = condRes.type
        if isSameType(condType, UninferredType):
            resolveUninferredType(condRes, BoolType())
        elif not isSameType(condType, BoolType):
            raise TypeMismatchInStatement(ast.expr)
        thenParam = CheckerParam(param.scope.delegate(ast.thenstmt), param.isLoop)
        self.visit(ast.thenstmt, thenParam)

        for elifStmt in ast.elifStmt:
            elifCondRes = self.visit(elifStmt[0])
            elifCondType = elifCondRes.type
            if isSameType(elifCondType, UninferredType):
                resolveUninferredType(elifCondRes, BoolType())
            elif isSameType(elifCondType, BoolType):
                raise TypeMismatchInStatement(ast.expr)
            elifThenParam = CheckerParam(param.scope.delegate(elifStmt[1]), param.isLoop)
            self.visit(elifStmt[1], elifThenParam)

        if ast.elseStmt is not None:
            elseParam = CheckerParam(param.scope.delegate(ast.elseStmt), param.isLoop)
            self.visit(ast.elseStmt, elseParam)
        return CheckerResult(None, None)

    def visitFor(self, ast, param):
        iterRes = self.visit(ast.name, param)
        iterType = iterRes.type
        if isSameType(iterType, UninferredType):
            resolveUninferredType(iterRes, NumberType())
        elif not isSameType(iterType, NumberType):
            raise TypeMismatchInStatement(ast.name)
        condRes = self.visit(ast.condExpr, param)
        condType = condRes.type
        if isSameType(condType, UninferredType):
            resolveUninferredType(condRes, BoolType())
        elif not isSameType(condType, BoolType):
            raise TypeMismatchInStatement(ast.condExpr)
        updRes = self.visit(ast.updExpr, param)
        updType = updRes.type
        if isSameType(updType, UninferredType):
            resolveUninferredType(updRes, NumberType())
        elif not isSameType(updType, NumberType):
            raise TypeMismatchInStatement(ast.updExpr)

        param = CheckerParam(param.scope.delegate(ast.body), True)
        self.visit(ast.body, param)
        return CheckerResult(None, None)


    def visitContinue(self, ast, param):
        if not param.inLoop:
            raise MustInLoop(ast)
        return CheckerResult(None, None)

    def visitBreak(self, ast, param):
        if not param.inLoop:
            raise MustInLoop(ast)
        return CheckerResult(None, None)

    def visitReturn(self, ast, param):
        if ast.expr is None:
            if param.scope.associatedFn is not None and isSameType(param.scope.associatedFn.type.ret, UninferredType):
                param.scope.associatedFn.type.ret = VoidType()
            if param.scope.associatedFn is not None and not isSameType(param.scope.associatedFn.type, VoidType):
                raise TypeMismatchInStatement(ast)
            return CheckerResult(None, None)
        res = self.visit(ast.expr, param)
        if isSameType(res.type, UninferredType):
            param.scope.associatedFn.type.addUninferredType((ast.expr, res.scope))
        elif param.scope.associatedFn is not None and not isSameType(param.scope.associatedFn.type.ret, res.type):
            raise TypeMismatchInStatement(ast)
        return CheckerResult(None, None)

    def visitAssign(self, ast, param):
        lhsRes = self.visit(ast.lhs, param)
        lhsType = lhsRes.type
        lhsIsLvalue = lhsRes.isLvalue

        if not lhsIsLvalue:
            # TODO: raise another error
            raise TypeMismatchInStatement(ast)

        exprRes = self.visit(ast.expr)
        exprType = exprRes.type

        if isSameType(lhsType, UninferredType) and isSameType(exprType, UninferredType):
            raise TypeCannotBeInferred(ast)
        elif isSameType(lhsType, UninferredType):
            resolveUninferredType(lhsRes, exprType)
        elif isSameType(exprType, UninferredType):
            resolveUninferredType(exprRes, lhsType)
        elif not isSameType(lhsType, exprType):
            raise TypeMismatchInExpression(ast)

        return CheckerResult(None, param.scope)

    def visitCallStmt(self, ast, param):
        calleeType = self.visit(ast.name, param).type
        if isSameType(calleeType.ret, UninferredType):
            raise TypeMismatchInStatement(ast)
        if not isSameType(calleeType.ret, VoidType):
            raise TypeMismatchInStatement(ast)
        if len(calleeType.params) != len(ast.args):
            raise TypeMismatchInStatement(ast)
        paramTypes = calleeType.params
        for index, paramTyp in enumerate(paramTypes):
            argRes = self.visit(ast.args[index], param)
            argTyp = argRes.type
            argScope = argRes.scope
            if isSameType(argTyp, UninferredType):
                argScope.set(ast.args[index].name, paramTyp, Variable())
            if not isSameType(paramTyp, argTyp):
                raise TypeMismatchInStatement(ast)
        return CheckerResult(VoidType(), param.scope, ast)

    def visitNumberLiteral(self, ast, param):
        return CheckerResult(NumberType(), param.scope, ast)

    def visitBooleanLiteral(self, ast, param):
        return CheckerResult(BoolType(), param.scope, ast)

    def visitStringLiteral(self, ast, param):
        return CheckerResult(StringType(), param.scope, ast)

    def visitArrayLiteral(self, ast, param):
        typ = None
        for value in ast.value:
            curType = self.visit(value, param).type
            if typ is not None and not isSameType(typ, curType):
                raise TypeMismatchInExpression(ast)
            typ = curType
        if not isSameType(typ, ArrayType):
            return CheckerResult(ArrayType([len(ast.value)], typ), param.scope, ast)
        else:
            return CheckerResult(ArrayType([len(ast.value)] + typ.size, typ.eleType), param.scope, ast)
