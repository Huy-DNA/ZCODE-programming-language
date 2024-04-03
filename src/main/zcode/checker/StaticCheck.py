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
    def __init__(self, scope, isLoop = False, retType = None):
        self.scope = scope
        self.isLoop = isLoop
        self.retType = retType

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
        param = CheckerParam(param.scope.delegate(), param.isLoop, param.retType)
        retType = None
        retScope = param.scope
        for stmt in ast.stmt:
            if stmt.__class__ is Return:
                retRes = self.visit(stmt, param)
                retType = retRes.type
                retScope = retRes.scope
            else:
                self.visit(stmt, param)
        return CheckerResult(retType, retScope)

    def visitIf(self, ast, param):
        condRes = self.visit(ast.expr, param)
        condType = condRes.type
        condScope = condRes.scope
        if condType.__class__ is UninferredType:
            condScope.set(ast.expr.name, BoolType())
        elif condType.__class__ is not BoolType:
            raise TypeMismatchInStatement(ast.expr)
        retType = None
        retScope = param.scope
        thenParam = CheckerParam(param.scope.delegate(), param.isLoop, param.retType)
        thenRes = self.visit(ast.thenstmt, thenParam)
        retType = thenRes.type
        retScope = thenRes.scope

        for elifStmt in ast.elifStmt:
            elifCondRes = self.visit(elifStmt[0])
            elifCondType = elifCondRes.type
            elifCondScope = elifCondRes.scope
            if elifCondType.__class__ is UninferredType:
                elifCondScope.set(elifStmt[0].name, BoolType())
            elif elifCondType.__class__ is not BoolType:
                raise TypeMismatchInStatement(ast.expr)
            elifThenParam = CheckerParam(param.scope.delegate(), param.isLoop, retType)
            elifThenRes = self.visit(ast.thenstmt, elifThenParam)
            elifRetType = elifThenRes.type
            elifRetScope = elifThenRes.scope
            if retType is None:
                retType = elifRetType
                retScope = elifRetScope

        if ast.elseStmt is not None:
            elseCondRes = self.visit(ast.elseStmt, param)
            elseCondType = elseCondRes.type
            elseCondScope = elseCondRes.scope
            if elseCondType.__class__ is UninferredType:
                elseCondScope.set(ast.elseStmt.name, BoolType())
            elif elseCondType.__class__ is not BoolType:
                raise TypeMismatchInStatement(ast.expr)
            elseThenParam = CheckerParam(param.scope.delegate(), param.isLoop, retType)
            elseThenRes = self.visit(ast.thenstmt, elseThenParam)
            if retType is None:
                retType = elseThenRes.type
                retScope = elseThenRes.scope
        return CheckerResult(retType, retScope)

    def visitFor(self, ast, param):
        iterRes = self.visit(ast.name, param)
        iterType = iterRes.type
        iterScope = iterRes.scope
        if iterType.__class__ is UninferredType:
            iterScope.set(ast.name, NumberType())
        elif iterType.__class__ is not NumberType:
            raise TypeMismatchInStatement(ast.name)
        condRes = self.visit(ast.condExpr, param)
        condType = condRes.type
        condScope = condRes.scope
        if condType.__class__ is UninferredType:
            condScope.set(ast.condExpr.name, BoolType())
        elif condType.__class__ is not BoolType():
            raise TypeMismatchInStatement(ast.condExpr)
        updRes = self.visit(ast.updExpr, param)
        updType = updRes.type
        updScope = updRes.scope
        if updType.__class__ is UninferredType:
            updScope.set(ast.condExpr.name, NumberType())
        elif updType.__class__ is not NumberType():
            raise TypeMismatchInStatement(ast.updExpr)

        param = CheckerParam(param.scope.delegate(), True)
        retType = None
        retScope = param.scope
        for stmt in ast.stmt:
            if stmt.__class__ is Return:
                retRes = self.visit(stmt, param)
                retType = retRes.type
                retScope = retRes.scope
            else:
                self.visit(stmt, param)
        return CheckerResult(retType, retScope)


    def visitContinue(self, ast, param):
        if not param.inLoop:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if not param.inLoop:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        if ast.expr is None:
            if param.retType is not None and param.retType.__class__ is not VoidType:
                raise TypeMismatchInStatement(ast)
            return CheckerResult(VoidType(), param.scope)
        res = self.visit(ast.expr, param)
        if param.retType is not None and param.retType.__class__ is not res.type.__class__:
            raise TypeMismatchInStatement(ast)
        return res

    def visitAssign(self, ast, param):
        lhsRes = self.visit(ast.lhs)
        lhsType = lhsRes.type
        lhsScope = lhsScope.scope
        lhsIsLvalue = lhsScope.isLvalue

        if not lhsIsLvalue:
            # TODO: raise another error
            raise TypeMismatchInStatement(ast)

        exprRes = self.visit(ast.expr)
        exprType = exprRes.type

        if lhsType is UninferredType:
            lhsScope.set(ast.lhs.name, exprType)
        elif lhsType.__class__ is not exprType.__class__:
            raise TypeMismatchInExpression(ast)

        return CheckerResult(None, param.scope)

    def visitCallStmt(self, ast, param):
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


