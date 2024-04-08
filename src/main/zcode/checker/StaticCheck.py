from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class UninferredType(Type):
    pass

class FuncType(Type):
    def __init__(self, params, ret):
        self.params = params
        self.ret = ret
        self.__list_of_uninferred_id = []
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
    def __init__(self, typ, scope, fnType = None, isLvalue = False):
        self.type = typ
        self.scope = scope
        self.fnType = fnType
        self.isLvalue = isLvalue

def isSameType(type1, type2):
    if isinstance(type1, ArrayType):
        return isinstance(type2, ArrayType) and isSameType(type1.eleType, type2.eleType) and type1.size == type2.size
    return isinstance(type1, type2.__class__) or isinstance(type2, type1.__class__) or type1 is type2 or isinstance(type1, type2) or isinstance(type2, type1)

class StaticChecker(BaseVisitor, Utils):
    def visitProgram(self, ast, param):
        param = CheckerParam(Scope())

    def visitVarDecl(self, ast, param):
        if param.scope.has(ast.name, Variable()):
            raise Redeclared(Variable(), ast.name)
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
        pass

    def visitBinaryOp(self, ast, param):
        op = ast.op

        leftRes = self.visit(ast.left, param)
        leftType = leftRes.type
        leftScope = leftRes.scope

        rightRes = self.visit(ast.right, param)
        rightType = rightRes.type
        rightScope = rightRes.scope

        if op in ['+', '-', '*', '/', '%']:
            if isSameType(leftType, UninferredType):
                leftScope.set(leftType.name, NumberType, Variable())
                leftType = NumberType()
            if isSameType(rightType, UninferredType):
                rightScope.set(rightType.name, NumberType, Variable())
                rightType = NumberType()
            if not isSameType(leftType, NumberType) or not isSameType(rightType, NumberType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(NumberType(), param.scope)
        if op in ['and', 'or']:
            if isSameType(leftType, UninferredType):
                leftScope.set(leftType.name, BoolType, Variable())
                leftType = BoolType()
            if isSameType(rightType, UninferredType):
                rightScope.set(rightType.name, BoolType, Variable())
                rightType = BoolType()
            if not isSameType(leftType, BoolType) or not isSameType(rightType, BoolType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope)
        if op == '...':
            if isSameType(leftType, UninferredType):
                leftScope.set(leftType.name, StringType, Variable())
                leftType = StringType()
            if isSameType(rightType, UninferredType):
                rightScope.set(rightType.name, StringType, Variable())
                rightType = StringType()
            if not isSameType(leftType, StringType) or not isSameType(rightType, StringType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(StringType(), param.scope)
        if op in ['=', '!=', '<', '>', '<=', '>=']:
            if isSameType(leftType, UninferredType):
                leftScope.set(leftType.name, NumberType, Variable())
                leftType = NumberType()
            if isSameType(rightType, UninferredType):
                rightScope.set(rightType.name, NumberType, Variable())
                rightType = NumberType()
            if not isSameType(leftType, NumberType) or not isSameType(rightType, NumberType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope)
        if op == '==':
            if isSameType(leftType, UninferredType):
                leftScope.set(leftType.name, StringType, Variable())
                leftType = StringType()
            if isSameType(rightType, UninferredType):
                rightScope.set(rightType.name, StringType, Variable())
                rightType = StringType()
            if not isSameType(leftType, StringType) or not isSameType(rightType, StringType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope)

        raise Exception('Unreachable')

    def visitUnaryOp(self, ast, param):
        op = ast.op

        res = self.visit(ast.operand, param)
        typ = res.type
        scope = res.scope
        if op == '-':
            if isSameType(typ, UninferredType):
                scope.set(typ.name, NumberType, Variable())
                return CheckerResult(NumberType(), param.scope)
            if isSameType(typ, NumberType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(NumberType(), param.scope)
        if op == 'not':
            if isSameType(typ, UninferredType):
                scope.set(typ.name, BoolType, Variable())
                return CheckerResult(BoolType(), param.scope)
            if isSameType(typ, BoolType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope)

        raise Exception('Unreachable')

    def visitCallExpr(self, ast, param):
        calleeType = self.visit(ast.name, (param.scope, param.isLoop, Function())).type
        if isSameType(calleeType.ret, VoidType()):
            raise TypeMismatchInExpression(ast)
        if calleeType.params.length != ast.args.length:
            raise TypeMismatchInExpression(ast)
        paramTypes = calleeType.params
        for index, paramTyp in enumerate(paramTypes):
            argRes = self.visit(ast.args[index], param)
            argTyp = argRes.type
            argScope = argRes.scope
            if isSameType(argTyp, UninferredType):
                argScope.set(ast.args[index].name, paramTyp, Variable())
            if not isSameType(paramTyp, argTyp):
                raise TypeMismatchInExpression(ast)
        return CheckerResult(calleeType.ret, param.scope, calleeType)

    def visitId(self, ast, param):
        typ, scope = param.scope.lookup(ast.name, param.lookupKind)
        if typ is None:
            raise Undeclared(param.lookupKind, ast.name)
        return CheckerResult(typ, scope, True)

    def visitArrayCell(self, ast, param):
        arrType = self.visit(ast.arr, param).type
        if not isSameType(arrType, ArrayType):
            raise TypeMismatchInExpression(ast)
        size = arrType.size
        if ast.idx.length != size.length:
            raise TypeMismatchInExpression(ast)
        for expr in ast.idx:
            exprRes = self.visit(expr, param)
            exprType = exprRes.type
            exprScope = exprRes.scope
            if isSameType(exprType, UninferredType):
                exprScope.set(expr.name, NumberType, Variable())
            if isSameType(exprType, NumberType, Variable()):
                raise TypeMismatchInExpression(expr)
        return CheckerResult(arrType.eleType, param.scope, True)

    def visitBlock(self, ast, param):
        param = CheckerParam(param.scope.delegate(ast), param.isLoop)
        for stmt in ast.stmt:
            self.visit(stmt, param)
        return CheckerResult(None, param.scope)

    def visitIf(self, ast, param):
        condRes = self.visit(ast.expr, param)
        condType = condRes.type
        condScope = condRes.scope
        if isSameType(condType, UninferredType):
            condScope.set(ast.expr.name, BoolType, Variable())
        elif not isSameType(condType, BoolType):
            raise TypeMismatchInStatement(ast.expr)
        thenParam = CheckerParam(param.scope.delegate(ast.thenstmt), param.isLoop)
        self.visit(ast.thenstmt, thenParam)

        for elifStmt in ast.elifStmt:
            elifCondRes = self.visit(elifStmt[0])
            elifCondType = elifCondRes.type
            elifCondScope = elifCondRes.scope
            if isSameType(elifCondType, UninferredType):
                elifCondScope.set(elifStmt[0].name, BoolType, Variable())
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
        iterScope = iterRes.scope
        if isSameType(iterType, UninferredType):
            iterScope.set(ast.name, NumberType, Variable())
        elif not isSameType(iterType, NumberType):
            raise TypeMismatchInStatement(ast.name)
        condRes = self.visit(ast.condExpr, param)
        condType = condRes.type
        condScope = condRes.scope
        if isSameType(condType, UninferredType):
            condScope.set(ast.condExpr.name, BoolType, Variable())
        elif not isSameType(condType, BoolType):
            raise TypeMismatchInStatement(ast.condExpr)
        updRes = self.visit(ast.updExpr, param)
        updType = updRes.type
        updScope = updRes.scope
        if isSameType(updType, UninferredType):
            updScope.set(ast.condExpr.name, NumberType, Variable())
        elif not isSameType(updType, NumberType):
            raise TypeMismatchInStatement(ast.updExpr)

        param = CheckerParam(param.scope.delegate(), True)
        for stmt in ast.stmt:
            self.visit(stmt, param)
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
        lhsScope = lhsScope.scope
        lhsIsLvalue = lhsScope.isLvalue

        if not lhsIsLvalue:
            # TODO: raise another error
            raise TypeMismatchInStatement(ast)

        exprRes = self.visit(ast.expr)
        exprType = exprRes.type
        exprScope = exprRes.scope

        if isSameType(lhsType, UninferredType) and isSameType(exprType, UninferredType):
            raise TypeCannotBeInferred(ast)
        elif isSameType(lhsType, UninferredType):
            lhsScope.set(ast.lhs.name, exprType, Variable())
        elif isSameType(exprType, UninferredType):
            exprScope.set(ast.expr.name, lhsType, Variable())
        elif not isSameType(lhsType, exprType):
            raise TypeMismatchInExpression(ast)

        return CheckerResult(None, param.scope)

    def visitCallStmt(self, ast, param):
        calleeType = self.visit(ast.name, param).type
        if isSameType(calleeType.ret, UninferredType):
            raise TypeMismatchInStatement(ast)
        if not isSameType(calleeType.ret, VoidType):
            raise TypeMismatchInStatement(ast)
        if calleeType.params.length != ast.args.length:
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
        return CheckerResult(calleeType.ret, param.scope)

    def visitNumberLiteral(self, ast, param):
        return CheckerResult(NumberType(), param.scope)

    def visitBooleanLiteral(self, ast, param):
        return CheckerResult(BoolType(), param.scope)

    def visitStringLiteral(self, ast, param):
        return CheckerResult(StringType(), param.scope)

    def visitArrayLiteral(self, ast, param):
        typ = None
        for value in ast.value:
            curType = self.visit(value, param).type
            if typ is not None and not isSameType(typ, curType):
                raise TypeMismatchInExpression(ast)
            typ = curType
        if not isSameType(typ, ArrayType):
            return CheckerResult(ArrayType([ast.value.length], typ), param.scope)
        else:
            return CheckerResult(ArrayType([ast.value.length] + typ.size, typ.eleType), param.scope)


