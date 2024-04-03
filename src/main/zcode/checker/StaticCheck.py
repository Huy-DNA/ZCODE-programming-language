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

        leftType, leftScope = self.visit(ast.left, param)
        rightType, rightScope = self.visit(ast.right, param)

        if op in ['+', '-', '*', '/', '%']:
            if leftType.__class__ is UninferredType:
                leftScope.set(leftType.name, NumberType())
                leftType = NumberType()
            if rightType.__class__ is UninferredType:
                rightScope.set(rightType.name, NumberType())
                rightType = NumberType()
            if leftType.__class__ is not NumberType or rightType.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType(), param.scope
        if op in ['and', 'or']:
            if leftType.__class__ is UninferredType:
                leftScope.set(leftType.name, BoolType())
                leftType = BoolType()
            if rightType.__class__ is UninferredType:
                rightScope.set(rightType.name, BoolType())
                rightType = BoolType()
            if leftType.__class__ is not BoolType or rightType.__class__ is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType(), param.scope
        if op == '...':
            if leftType.__class__ is UninferredType:
                leftScope.set(leftType.name, StringType())
                leftType = StringType()
            if rightType.__class__ is UninferredType:
                rightScope.set(rightType.name, StringType())
                rightType = StringType()
            if leftType.__class__ is not StringType or rightType.__class__ is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType(), param.scope
        if op in ['=', '!=', '<', '>', '<=', '>=']:
            if leftType.__class__ is UninferredType:
                leftScope.set(leftType.name, NumberType())
                leftType = NumberType()
            if rightType.__class__ is UninferredType:
                rightScope.set(rightType.name, NumberType())
                rightType = NumberType()
            if leftType.__class__ is not NumberType or rightType.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return BoolType(), param.scope
        if op == '==':
            if leftType.__class__ is UninferredType:
                leftScope.set(leftType.name, StringType())
                leftType = StringType()
            if rightType.__class__ is UninferredType:
                rightScope.set(rightType.name, StringType())
                rightType = StringType()
            if leftType.__class__ is not StringType or rightType.__class__ is not StringType:
                raise TypeMismatchInExpression(ast)
            return BoolType(), param.scope

        raise Exception('Unreachable')

    def visitUnaryOp(self, ast, param):
        op = ast.op

        typ, scope = self.visit(ast.operand, param)

        if op == '-':
            if typ.__class__ is UninferredType:
                scope.set(typ.name, NumberType())
                return NumberType()
            if typ.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        if op == 'not':
            if typ.__class__ is UninferredType:
                scope.set(typ.name, BoolType())
                return BoolType()
            if typ.__class__ is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType(), param.scope

        raise Exception('Unreachable')

    def visitCallExpr(self, ast, param):
        try:
            calleeType, _ = self.visit(ast.name, param)
        except Undeclared:
            raise NoDefinition(ast)
        if calleeType.__class__ is not FuncType:
            raise NoDefinition(ast)
        if calleeType.params.length != ast.args.length:
            raise TypeMismatchInExpression(ast)
        paramTypes = calleeType.params
        for index, paramTyp in enumerate(paramTypes):
            argTyp, _ = self.visit(ast.args[index], param)
            if paramTyp.__class__ is UninferredType:
                paramTypes[index] = argTyp
            if paramTyp.__class__ is not argTyp.__class__:
                raise TypeMismatchInExpression(ast)
        return calleeType.ret, param.scope

    def visitId(self, ast, param):
        typ, scope = param.scope.lookup(ast.name)
        if typ is None:
            raise Undeclared(Identifier(), ast.name)
        return typ, scope

    def visitArrayCell(self, ast, param):
        arrType, _ = self.visit(ast.arr, param)
        if arrType.__class__ is not ArrayType:
            raise TypeMismatchInExpression(ast)
        size = arrType.size
        if ast.idx.length != size.length:
            raise TypeMismatchInExpression(ast)
        for expr in ast.idx:
            typ, exprScope = self.visit(expr, param)
            if typ.__class__ is UninferredType:
                exprScope.set(expr.name, NumberType())
            if typ.__class__ is not NumberType:
                raise TypeMismatchInExpression(expr)
        return arrType.eleType, param.scope

    def visitBlock(self, ast, param):
        param = CheckerParam(param.scope.delegate(), param.isLoop)
        retTyp = None
        retScope = param.scope
        for stmt in ast.stmt:
            if stmt.__class__ is Return:
                retTyp, retScope = self.visit(stmt, param)
            else:
                self.visit(stmt, param)
        return retTyp, retScope

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        iterType, iterScope = self.visit(ast.name, param)
        if iterType.__class__ is UninferredType:
            iterScope.set(ast.name, NumberType())
        elif iterType.__class__ is not NumberType:
            raise TypeMismatchInExpression(ast.name)
        condType, condScope = self.visit(ast.condExpr, param)
        if condType.__class__ is UninferredType:
            condScope.set(ast.condExpr.name, BoolType())
        elif condType.__class__ is not BoolType():
            raise TypeMismatchInExpression(ast.condExpr)
        updType, updScope = self.visit(ast.updExpr, param)
        if updType.__class__ is UninferredType:
            updScope.set(ast.condExpr.name, NumberType())
        elif updType.__class__ is not NumberType():
            raise TypeMismatchInExpression(ast.updExpr)

        param = CheckerParam(param.scope.delegate(), True)
        retTyp = None
        retScope = param.scope
        for stmt in ast.stmt:
            if stmt.__class__ is Return:
                retTyp, retScope = self.visit(stmt, param)
            else:
                self.visit(stmt, param)
        return retTyp, retScope


    def visitContinue(self, ast, param):
        if not param.inLoop:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if not param.inLoop:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        if ast.expr is None:
            return VoidType(), param.scope
        return self.visit(ast.expr, param)

    def visitAssign(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        typ = None
        for value in ast.value:
            curType = self.visit(value, param)
            if typ.__class__ is not curType.__class__ and typ is not None:
                raise TypeMismatchInExpression(ast)
            typ = curType
        return typ


