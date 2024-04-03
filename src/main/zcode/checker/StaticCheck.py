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
            return self.__symbolTable[name]
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

        leftType = self.visit(ast.left, param)
        rightType = self.visit(ast.right, param)

        if op in ['+', '-', '*', '/', '%']:
            if leftType.__class__ is UninferredType:
                param.scope.set(leftType.name, NumberType())
                leftType = NumberType()
            if rightType.__class__ is UninferredType:
                param.scope.set(rightType.name, NumberType())
                rightType = NumberType()
            if leftType.__class__ is not NumberType or rightType.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        if op in ['and', 'or']:
            if leftType.__class__ is UninferredType:
                param.scope.set(leftType.name, BoolType())
                leftType = BoolType()
            if rightType.__class__ is UninferredType:
                param.scope.set(rightType.name, BoolType())
                rightType = BoolType()
            if leftType.__class__ is not BoolType or rightType.__class__ is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if op == '...':
            if leftType.__class__ is UninferredType:
                param.scope.set(leftType.name, StringType())
                leftType = StringType()
            if rightType.__class__ is UninferredType:
                param.scope.set(rightType.name, StringType())
                rightType = StringType()
            if leftType.__class__ is not StringType or rightType.__class__ is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()
        if op in ['=', '!=', '<', '>', '<=', '>=']:
            if leftType.__class__ is UninferredType:
                param.scope.set(leftType.name, NumberType())
                leftType = NumberType()
            if rightType.__class__ is UninferredType:
                param.scope.set(rightType.name, NumberType())
                rightType = NumberType()
            if leftType.__class__ is not NumberType or rightType.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if op == '==':
            if leftType.__class__ is UninferredType:
                param.scope.set(leftType.name, StringType())
                leftType = StringType()
            if rightType.__class__ is UninferredType:
                param.scope.set(rightType.name, StringType())
                rightType = StringType()
            if leftType.__class__ is not StringType or rightType.__class__ is not StringType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        raise Exception('Unreachable')

    def visitUnaryOp(self, ast, param):
        op = ast.op

        typ = self.visit(ast.operand, param)

        if op == '-':
            if typ.__class__ is UninferredType:
                param.scope.set(typ.name, NumberType())
                return NumberType()
            if typ.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        if op == 'not':
            if typ.__class__ is UninferredType:
                param.scope.set(typ.name, BoolType())
                return BoolType()
            if typ.__class__ is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        raise Exception('Unreachable')

    def visitCallExpr(self, ast, param):
        try:
            calleeType = self.visit(ast.name, param)
        except Undeclared:
            raise NoDefinition(ast)
        if calleeType.__class__ is not FuncType:
            raise NoDefinition(ast)
        if calleeType.params.length != ast.args.length:
            raise TypeMismatchInExpression(ast)
        paramTypes = calleeType.params
        for index, paramTyp in enumerate(paramTypes):
            argTyp = self.visit(ast.args[index], param)
            if paramTyp.__class__ is UninferredType:
                paramTypes[index] = argTyp
            if paramTyp.__class__ is not argTyp.__class__:
                raise TypeMismatchInExpression(ast)
        return calleeType.ret

    def visitId(self, ast, param):
        typ = param.scope.lookup(ast.name)
        if typ is None:
            raise Undeclared(Identifier(), ast.name)
        return typ

    def visitArrayCell(self, ast, param):
        arrType = self.visit(ast.arr, param)
        if arrType.__class__ is not ArrayType:
            raise TypeMismatchInExpression(ast)
        size = arrType.size
        if ast.idx.length != size.length:
            raise TypeMismatchInExpression(ast)
        for expr in ast.idx:
            typ = self.visit(expr, param)
            if typ.__class__ is UninferredType:
                param.scope.set(expr.name, NumberType())
            if typ.__class__ is not NumberType:
                raise TypeMismatchInExpression(expr)
        return arrType.eleType

    def visitBlock(self, ast, param):
        param = CheckerParam(param.scope.delegate(), param.isLoop)
        for stmt in ast.stmt:
            self.visit(stmt, param)

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, param):
        if not param.inLoop:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if not param.inLoop:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        pass

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


