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

class StaticChecker(BaseVisitor, Utils):
    def visitProgram(self, ast, param):
        param = Scope()

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
                param.set(leftType.name, NumberType())
                leftType = NumberType()
            if rightType.__class__ is UninferredType:
                param.set(rightType.name, NumberType())
                rightType = NumberType()
            if leftType.__class__ is not NumberType or rightType.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        if op in ['and', 'or']:
            if leftType.__class__ is UninferredType:
                param.set(leftType.name, BoolType())
                leftType = BoolType()
            if rightType.__class__ is UninferredType:
                param.set(rightType.name, BoolType())
                rightType = BoolType()
            if leftType.__class__ is not BoolType or rightType.__class__ is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if op == '...':
            if leftType.__class__ is UninferredType:
                param.set(leftType.name, StringType())
                leftType = StringType()
            if rightType.__class__ is UninferredType:
                param.set(rightType.name, StringType())
                rightType = StringType()
            if leftType.__class__ is not StringType or rightType.__class__ is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()
        if op in ['=', '!=', '<', '>', '<=', '>=']:
            if leftType.__class__ is UninferredType:
                param.set(leftType.name, NumberType())
                leftType = NumberType()
            if rightType.__class__ is UninferredType:
                param.set(rightType.name, NumberType())
                rightType = NumberType()
            if leftType.__class__ is not NumberType or rightType.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if op == '==':
            if leftType.__class__ is UninferredType:
                param.set(leftType.name, StringType())
                leftType = StringType()
            if rightType.__class__ is UninferredType:
                param.set(rightType.name, StringType())
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
                param.set(typ.name, NumberType())
                return NumberType()
            if typ.__class__ is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        if op == 'not':
            if typ.__class__ is UninferredType:
                param.set(typ.name, BoolType())
                return BoolType()
            if typ.__class__ is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        raise Exception('Unreachable')

    def visitCallExpr(self, ast, param):
        pass

    def visitId(self, ast, param):
        pass

    def visitArrayCell(self, ast, param):
        pass

    def visitBlock(self, ast, param):
        pass

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, param):
        pass

    def visitBreak(self, ast, param):
        pass

    def visitReturn(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass

    def visitNumberLiteral(self, ast, param):
        pass

    def visitBooleanLiteral(self, ast, param):
        pass

    def visitStringLiteral(self, ast, param):
        pass

    def visitArrayLiteral(self, ast, param):
        pass

