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
        self.__list_of_uninferred_expr = []
        self.defined = defined
    def addUninferredExpr(self, checkerRes, ast):
        self.__list_of_uninferred_expr.append((checkerRes, ast))
    def resolveRet(self, ast):
        if len(self.__list_of_uninferred_expr) == 0:
            self.ret = VoidType()
        elif isSameType(self.ret, UninferredType):
            raise TypeCannotBeInferred(ast)
        for expr in self.__list_of_uninferred_expr:
            resolveUninferredType(expr[0], expr[1], self.ret, False)
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
        elif parent and isinstance(parent.associatedFn, FuncDecl):
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
            if name in self.__fnSymbolTable:
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

    def checkNoBodyFunction(self):
        for name, typ in self.__fnSymbolTable.items():
            if not typ.defined:
                raise NoDefinition(name)

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
    if isinstance(type1, type2.__class__) or isinstance(type2, type1.__class__) or type1 is type2:
        return True
    try:
        return isinstance(type1, type2)
    except Exception:
        pass
    try:
        return isinstance(type2, type1)
    except Exception:
        return False

def resolveUninferredType(checkerRes, ast, typeHint, inExpression = True):
    if checkerRes.fnType:
        if not isSameType(checkerRes.fnType.ret, UninferredType) and not isSameType(checkerRes.fnType.ret, typeHint):
            raise TypeMismatchInExpression(ast) if inExpression else TypeMismatchInStatement(ast)
        checkerRes.fnType.ret = typeHint
    else:
        varType = checkerRes.scope.get(checkerRes.exprNode.name, Variable())
        if not isSameType(varType, UninferredType) and not isSameType(varType, typeHint):
            raise TypeMismatchInExpression(ast) if inExpression else TypeMismatchInStatement(ast)
        checkerRes.scope.set(checkerRes.exprNode.name, typeHint, Variable())

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        param = CheckerParam(Scope(None, self.ast), False, Variable())
        self.visit(self.ast, param)
        return []
    def visitProgram(self, ast, param):
        for decl in ast.decl:
            self.visit(decl, param)
        if not param.scope.has("main", Function()):
            raise NoEntryPoint()
        param.scope.checkNoBodyFunction()

    def visitVarDecl(self, ast, param):
        if param.scope.has(ast.name.name, Variable()):
            raise Redeclared(Variable(), ast.name.name) if isinstance(param.lookupKind, Parameter) else Redeclared(Parameter(), ast.name.name)
        if ast.varType:
            param.scope.set(ast.name.name, ast.varType, Variable())
            if ast.varInit:
                initRes = self.visit(ast.varInit, CheckerParam(param.scope, param.isLoop, Variable()))
                initType = initRes.type
                if isSameType(initType, UninferredType):
                    resolveUninferredType(initRes, ast, ast.varType, False)
                elif not isSameType(ast.varType, initType):
                    raise TypeMismatchInStatement(ast)
        elif ast.varInit:
            typ = self.visit(ast.varInit, param).type
            if isSameType(typ, UninferredType):
                raise TypeCannotBeInferred(ast)
            param.scope.set(ast.name, typ, Variable())
        else:
            param.scope.set(ast.name, UninferredType(), Variable())

    def visitFuncDecl(self, ast, param):
        if param.scope.has(ast.name.name, Function()) and param.scope.get(ast.name.name, Function()).defined and ast.body is not None:
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
        if not param.scope.has(ast.name.name, Function()) or not param.scope.get(ast.name.name, Function()).defined:
            param.scope.set(ast.name.name, fnType, Function())

        if ast.body is None:
            return CheckerResult(None, None, None, fnType)

        ast.type = fnType
        bodyParam = CheckerParam(paramParam.scope.delegate(ast.body), False, Variable())
        self.visit(ast.body, bodyParam)
        fnType.resolveRet(ast)
        bodyParam.scope.checkNoBodyFunction()
        return CheckerResult(None, None)

    def visitBinaryOp(self, ast, param):
        op = ast.op

        leftRes = self.visit(ast.left, param)
        leftType = leftRes.type
        rightRes = self.visit(ast.right, param)
        rightType = rightRes.type

        if op in ['+', '-', '*', '/', '%']:
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, ast, NumberType())
                leftType = NumberType()
            elif not isSameType(leftType, NumberType):
                raise TypeMismatchInExpression(ast)
            if isSameType(rightType, UninferredType):
                resolveUninferredType(rightRes, ast, NumberType())
                rightType = NumberType()
            elif not isSameType(rightType, NumberType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(NumberType(), param.scope, ast)
        if op in ['and', 'or']:
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, ast, BoolType())
                leftType = BoolType()
            elif not isSameType(leftType, BoolType):
                raise TypeMismatchInExpression(ast)

            if isSameType(rightType, UninferredType):
                resolveUninferredType(rightRes, ast, BoolType())
                rightType = BoolType()
            elif not isSameType(rightType, BoolType):
                raise TypeMismatchInExpression(ast)

            return CheckerResult(BoolType(), param.scope, ast)
        if op == '...':
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, ast, StringType())
                leftType = StringType()
            elif not isSameType(leftType, StringType):
                raise TypeMismatchInExpression(ast)

            if isSameType(rightType, UninferredType):
                resolveUninferredType(leftRes, ast, StringType())
                rightType = StringType()
            elif not isSameType(rightType, StringType):
                raise TypeMismatchInExpression(ast)

            return CheckerResult(StringType(), param.scope, ast)
        if op in ['=', '!=', '<', '>', '<=', '>=']:
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, ast, NumberType())
                leftType = NumberType()
            elif not isSameType(leftType, NumberType):
                raise TypeMismatchInExpression(ast)

            if isSameType(rightType, UninferredType):
                resolveUninferredType(leftRes, ast, NumberType())
                rightType = NumberType()
            elif not isSameType(rightType, NumberType):
                raise TypeMismatchInExpression(ast)

            return CheckerResult(BoolType(), param.scope, ast)
        if op == '==':
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, ast, StringType())
                leftType = StringType()
            elif not isSameType(leftType, StringType):
                raise TypeMismatchInExpression(ast)

            if isSameType(rightType, UninferredType):
                resolveUninferredType(leftRes, ast, StringType())
                rightType = StringType()
            elif not isSameType(rightType, StringType):
                raise TypeMismatchInExpression(ast)

            return CheckerResult(BoolType(), param.scope, ast)

        raise Exception('Unreachable')

    def visitUnaryOp(self, ast, param):
        op = ast.op

        res = self.visit(ast.operand, param)
        typ = res.type

        if op == '-':
            if isSameType(typ, UninferredType):
                resolveUninferredType(res, ast, NumberType())
                return CheckerResult(NumberType(), param.scope, ast)
            elif isSameType(typ, NumberType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(NumberType(), param.scope, ast)
        if op == 'not':
            if isSameType(typ, UninferredType):
                resolveUninferredType(res, ast, BoolType())
                return CheckerResult(BoolType(), param.scope, ast)
            elif isSameType(typ, BoolType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope, ast)

        raise Exception('Unreachable')

    def visitCallExpr(self, ast, param):
        calleeType = self.visit(ast.name, CheckerParam(param.scope, param.isLoop, Function())).type
        if isSameType(calleeType.ret, VoidType):
            raise TypeMismatchInExpression(ast)
        if len(calleeType.params) != len(ast.args):
            raise TypeMismatchInExpression(ast)
        paramTypes = calleeType.params
        for index, paramTyp in enumerate(paramTypes):
            argRes = self.visit(ast.args[index], param)
            argTyp = argRes.type
            if isSameType(argTyp, UninferredType):
                resolveUninferredType(argRes, ast, paramTyp)
            elif not isSameType(paramTyp, argTyp):
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
                resolveUninferredType(exprRes, ast, NumberType())
            elif not isSameType(exprType, NumberType):
                raise TypeMismatchInExpression(expr)

        return CheckerResult(arrType.eleType, param.scope, ast, None, True)

    def visitBlock(self, ast, param):
        param = CheckerParam(param.scope.delegate(ast), param.isLoop)
        for stmt in ast.stmt:
            self.visit(stmt, param)
        param.scope.checkNoBodyFunction()
        return CheckerResult(None, param.scope)

    def visitIf(self, ast, param):
        condRes = self.visit(ast.expr, param)
        condType = condRes.type
        if isSameType(condType, UninferredType):
            resolveUninferredType(condRes, ast.expr, BoolType())
        elif not isSameType(condType, BoolType):
            raise TypeMismatchInStatement(ast.expr)
        thenParam = CheckerParam(param.scope.delegate(ast.thenstmt), param.isLoop)
        self.visit(ast.thenstmt, thenParam)

        for elifStmt in ast.elifStmt:
            elifCondRes = self.visit(elifStmt[0], param)
            elifCondType = elifCondRes.type
            if isSameType(elifCondType, UninferredType):
                resolveUninferredType(elifCondRes, ast.elifStmt[0], BoolType())
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
            resolveUninferredType(iterRes, ast.name, NumberType())
        elif not isSameType(iterType, NumberType):
            raise TypeMismatchInStatement(ast.name)
        condRes = self.visit(ast.condExpr, param)
        condType = condRes.type
        if isSameType(condType, UninferredType):
            resolveUninferredType(condRes, ast.condExpr, BoolType())
        elif not isSameType(condType, BoolType):
            raise TypeMismatchInStatement(ast.condExpr)
        updRes = self.visit(ast.updExpr, param)
        updType = updRes.type
        if isSameType(updType, UninferredType):
            resolveUninferredType(updRes, ast.updExpr, NumberType())
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
            param.scope.associatedFn.type.addUninferredExpr(res, ast)
        elif param.scope.associatedFn is not None and isSameType(param.scope.associatedFn.type.ret, UninferredType):
            param.scope.associatedFn.type.ret = res.type
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
            resolveUninferredType(lhsRes, ast, exprType, False)
        elif isSameType(exprType, UninferredType):
            resolveUninferredType(exprRes, ast, lhsType, False)
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
