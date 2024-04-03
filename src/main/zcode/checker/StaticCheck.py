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

class Scope:
    def __init__(self, parent = None):
        self.__parent = parent
        self.__symbolTable = dict()

    def set(self, name, typ):
        if typ.__class__ is not Type:
            raise Exception("Only symbols can be added")

        self.__symbolTable[name] = typ

    def get(self, name):
        return self.__symbolTable[name]

    def lookup(self, name):
        if name in self.__symbolTable[name]:
            return self.__symbolTable[name], self
        if self.__parent is not None:
            return self.__parent.lookup(name)
        return None

    def has(self, name):
        return name in self.__symbolTable

    def parent(self):
        return self.__parent

    def delegate(self):
        return Scope(self)

class CheckerParam:
    def __init__(self, scope, isLoop = False):
        self.scope = scope
        self.isLoop = isLoop

class CheckerResult:
    def __init__(self, typ, scope, isLvalue = False):
        self.type = typ
        self.scope = scope
        self.isLvalue = isLvalue

class StaticChecker(BaseVisitor, Utils):
    def visitProgram(self, ast, param):
        param = CheckerParam(Scope())

    def visitVarDecl(self, ast, param):
        pass

    def visitFuncDecl(self, ast, param):
        pass

    def visitNumberType(self, ast, param):
        pass

    def visitBoolType(self, ast, param):
        pass

    def visitStringType(self, ast, param):
        pass

    def visitArrayType(self, ast, param):
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
            if leftType.__class__ is UninferredType:
                leftScope.set(leftType.name, NumberType())
                leftType = NumberType()
            if rightType.__class__ is UninferredType:
                rightScope.set(rightType.name, NumberType())
                rightType = NumberType()
            if leftType.__class__ is not NumberType or rightType.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return CheckerResult(NumberType(), param.scope)
        if op in ['and', 'or']:
            if leftType.__class__ is UninferredType:
                leftScope.set(leftType.name, BoolType())
                leftType = BoolType()
            if rightType.__class__ is UninferredType:
                rightScope.set(rightType.name, BoolType())
                rightType = BoolType()
            if leftType.__class__ is not BoolType or rightType.__class__ is not BoolType:
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope)
        if op == '...':
            if leftType.__class__ is UninferredType:
                leftScope.set(leftType.name, StringType())
                leftType = StringType()
            if rightType.__class__ is UninferredType:
                rightScope.set(rightType.name, StringType())
                rightType = StringType()
            if leftType.__class__ is not StringType or rightType.__class__ is not StringType:
                raise TypeMismatchInExpression(ast)
            return CheckerResult(StringType(), param.scope)
        if op in ['=', '!=', '<', '>', '<=', '>=']:
            if leftType.__class__ is UninferredType:
                leftScope.set(leftType.name, NumberType())
                leftType = NumberType()
            if rightType.__class__ is UninferredType:
                rightScope.set(rightType.name, NumberType())
                rightType = NumberType()
            if leftType.__class__ is not NumberType or rightType.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope)
        if op == '==':
            if leftType.__class__ is UninferredType:
                leftScope.set(leftType.name, StringType())
                leftType = StringType()
            if rightType.__class__ is UninferredType:
                rightScope.set(rightType.name, StringType())
                rightType = StringType()
            if leftType.__class__ is not StringType or rightType.__class__ is not StringType:
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope)

        raise Exception('Unreachable')

    def visitUnaryOp(self, ast, param):
        op = ast.op

        res = self.visit(ast.operand, param)
        typ = res.type
        scope = res.scope
        if op == '-':
            if typ.__class__ is UninferredType:
                scope.set(typ.name, NumberType())
                return CheckerResult(NumberType(), param.scope)
            if typ.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return CheckerResult(NumberType(), param.scope)
        if op == 'not':
            if typ.__class__ is UninferredType:
                scope.set(typ.name, BoolType())
                return CheckerResult(BoolType(), param.scope)
            if typ.__class__ is not BoolType:
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope)

        raise Exception('Unreachable')

    def visitCallExpr(self, ast, param):
        try:
            calleeType = self.visit(ast.name, param).type
        except Undeclared:
            raise NoDefinition(ast)
        if calleeType.__class__ is not FuncType:
            raise NoDefinition(ast)
        if calleeType.params.length != ast.args.length:
            raise TypeMismatchInExpression(ast)
        paramTypes = calleeType.params
        for index, paramTyp in enumerate(paramTypes):
            argTyp = self.visit(ast.args[index], param).type
            if paramTyp.__class__ is UninferredType:
                paramTypes[index] = argTyp
            if paramTyp.__class__ is not argTyp.__class__:
                raise TypeMismatchInExpression(ast)
        return CheckerResult(calleeType.ret, param.scope)

    def visitId(self, ast, param):
        typ, scope = param.scope.lookup(ast.name)
        if typ is None:
            raise Undeclared(Identifier(), ast.name)
        return CheckerResult(typ, scope, True)

    def visitArrayCell(self, ast, param):
        arrType = self.visit(ast.arr, param).type
        if arrType.__class__ is not ArrayType:
            raise TypeMismatchInExpression(ast)
        size = arrType.size
        if ast.idx.length != size.length:
            raise TypeMismatchInExpression(ast)
        for expr in ast.idx:
            exprRes = self.visit(expr, param)
            exprType = exprRes.type
            exprScope = exprRes.scope
            if exprType.__class__ is UninferredType:
                exprScope.set(expr.name, NumberType())
            if exprType.__class__ is not NumberType:
                raise TypeMismatchInExpression(expr)
        return CheckerResult(arrType.eleType, param.scope, True)

    def visitBlock(self, ast, param):
        param = CheckerParam(param.scope.delegate(), param.isLoop)
        retTyp = None
        retScope = param.scope
        for stmt in ast.stmt:
            if stmt.__class__ is Return:
                retRes = self.visit(stmt, param)
                retTyp = retRes.type
                retScope = retRes.scope
            else:
                self.visit(stmt, param)
        return CheckerResult(retTyp, retScope)

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        iterRes = self.visit(ast.name, param)
        iterType = iterRes.type
        iterScope = iterRes.scope
        if iterType.__class__ is UninferredType:
            iterScope.set(ast.name, NumberType())
        elif iterType.__class__ is not NumberType:
            raise TypeMismatchInExpression(ast.name)
        condRes = self.visit(ast.condExpr, param)
        condType = condRes.type
        condScope = condRes.scope
        if condType.__class__ is UninferredType:
            condScope.set(ast.condExpr.name, BoolType())
        elif condType.__class__ is not BoolType():
            raise TypeMismatchInExpression(ast.condExpr)
        updRes = self.visit(ast.updExpr, param)
        updType = updRes.type
        updScope = updRes.scope
        if updType.__class__ is UninferredType:
            updScope.set(ast.condExpr.name, NumberType())
        elif updType.__class__ is not NumberType():
            raise TypeMismatchInExpression(ast.updExpr)

        param = CheckerParam(param.scope.delegate(), True)
        retTyp = None
        retScope = param.scope
        for stmt in ast.stmt:
            if stmt.__class__ is Return:
                retRes = self.visit(stmt, param)
                retTyp = retRes.type
                retScope = retRes.scope
            else:
                self.visit(stmt, param)
        return CheckerResult(retTyp, retScope)


    def visitContinue(self, ast, param):
        if not param.inLoop:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if not param.inLoop:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        if ast.expr is None:
            return CheckerResult(VoidType(), param.scope)
        return self.visit(ast.expr, param)

    def visitAssign(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass

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
            if typ.__class__ is not curType.__class__ and typ is not None:
                raise TypeMismatchInExpression(ast)
            typ = curType
        return CheckerResult(typ, param.scope)

