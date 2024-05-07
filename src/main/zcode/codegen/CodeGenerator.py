from Emitter import Emitter
from functools import reduce
from MachineCode import JasminCode

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *

from Utils import *

# Since the Frame.py file is not submitted, have to do it here
def patch_Frame_class():
    def getBreakLabel(self):
        if not self.brkLabel:
            raise IllegalRuntimeException("None break label")
        return self.brkLabel[-1]
    Frame.getBreakLabel = getBreakLabel

# Since the MachineCode.py file is not submitted, have to do it here
def patch_Machine_Code_class():
    def emitIREM(self):
        return JasminCode.INDENT + "irem" + JasminCode.END
    JasminCode.emitIREM = emitIREM    
    
    def emitFREM(self):
        return JasminCode.INDENT + "frem" + JasminCode.END
    JasminCode.emitFREM = emitFREM  

    def emitICONST(self, i):
        # i: Int
        if i == -1:
            return JasminCode.INDENT + "iconst_m1" + JasminCode.END
        elif i >= 0 and i <= 5:
            return JasminCode.INDENT + "iconst_" + str(i) + JasminCode.END
        else:
            raise IllegalOperandException(str(i))
    JasminCode.emitICONST = emitICONST

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readNumber", MType(list(), NumberType()), CName(self.libName)),
                Symbol("writeNumber", MType([NumberType()],
                       VoidType()), CName(self.libName)),
                Symbol("readBool", MType(
                    [BoolType()], VoidType()), CName(self.libName)),
 
                Symbol("writeBool", MType(
                    [BoolType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType(list(), StringType()), CName(self.libName)),
                Symbol("writeString", MType(
                    [StringType()], VoidType()), CName(self.libName))
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, scope, isLeft = False):
        self.frame = frame
        self.scope = scope
        self.isLeft = isLeft


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        patch_Frame_class()
        patch_Machine_Code_Class()
        StaticChecker(astTree).check()
        
        self.astTree = astTree
        self.env = env
        self.path = path
        self.classname = "ZCodeClass"
        self.emit = Emitter(path + "/" +self.classname + ".j")

    def visitProgram(self, ast, c):
        c = SubBody(None, self.env, ast.scope)
        [self.visit(i, c) for i in ast.decl]

    def visitVarDecl(self, ast, param):
        scope = param.scope
        name = param.name
        in_, foundScope = scope.lookup(name, Variable())
        if param.frame is None: 
            self.emit.printout(self.emit.emitATTRIBUTE(name, in_)) 
            if ast.varInit:
                param = SubBody(Frame(name, VoidType()), param.scope)
                code, _ = self.visit(varInit, param)
                self.emit.printout(code)
                self.emit.printout(self.emitPUTSTATIC(self.classname + "/" + name, in_, param.frame))
        
        self.emit.printout(self.emitVAR(in_, name, param.frame.getStartLabel(), param.frame.getEndLabel(), param.frame))
        index = param.frame.getNewIndex()
        foundScope.setIndex(name, index)
        if ast.varInit:
            param = SubBody(Frame(name, VoidType()), param.scope)
            code, _ = self.visit(varInit, param)
            self.emit.printout(code)
            self.emit.printout(self.emitWRITEVAR(name, in_, index, param.frame))
 
    def visitFuncDecl(self, ast, param):
        if not ast.body:
            return
        name = ast.name
        scope = param.scope
        in_, _ = scope.lookup(name, Function())
        self.emit.printout(self.emit.emitMETHOD(name, in_))
        param.frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(param.frame.getStartLabel(), param.frame))
        for paramDecl in ast.param:
            self.visit(paramDecl, SubBody(param.frame, ast.scope))
        self.visit(ast.body, SubBody(param.frame, ast.body.scope))  
        self.emit.printout(self.emit.emitLABEL(param.frame.getEndLabel(), param.frame))
        param.frame.exitScope()
        self.emit.printout(self.emit.emitENDMETHOD(param.frame))

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
        left = ast.left
        right = ast.right
        codeLeft, _ = self.visit(left, param)
        codeRight, _ = self.visit(right, param)
        if op in ["-", "+"]:
            opIns = self.emit.emitADDOP(op, NumberType(), param.frame)
            typ = NumberType()
        elif op == "...":
            opIns = self.emit.emitADDOP(op, StringType(), param.frame)
            typ = StringType()
        elif op in ['*', '/', '%']:
            opIns = self.emit.emitMULOP(op, NumberType(), param.frame)
            typ = NumberType()
        elif op in [">", ">=", "<=", "=", "!="]:
            opIns = self.emit.emitREOP(op, NumberType(), param.frame)
            typ = BoolType()
        elif op == "==":
            opIns = self.emit.emitREOP(op, StringType(), param.frame)
            typ = BoolType()
        elif op == "and":
            opIns = self.emit.emitANDOP(param.frame)
            typ = BoolType()
        elif op == "or":
            opIns = self.emit.emitOROP(param.frame)
            typ = BoolType()
        code = codeLeft + codeRight + opIns
        return code, typ

    def visitUnaryOp(self, ast, param):
        code = self.visit(ast.operand, param)
        if op == "-":
            opIns = self.emit.emitNEGOP(NumberType(), param.frame)
            typ = NumberType()
        elif op == "not":
            opIns = self.emit.emitNOT(BoolType(), param.frame)
            typ = BoolType()

        return code + opIns, typ

    def visitCallExpr(self, ast, param):
        name = ast.name
        code = ""
        scope = param.scope
        in_, _ = scope.lookup(name, Function())
        for arg in self.args:
            code += self.visit(arg, param)[0]
        code += self.emit.emitINVOKESTATIC(self.classname + "/" + name, in_, param.frame)

        return code, in_.ret

    def visitId(self, ast, param):
        scope = param.scope
        in_, foundScope = scope.lookup(name, Variable())
        name = ast.name
        index = foundScope.getIndex(name)
        if index is None:
            if param.isLeft:
                return self.emit.emitPUTSTATIC(name, in_, param.frame), in_
            return self.emit.emitGETSTATIC(name, in_, param.frame), in_
        if param.isLeft:
            return self.emit.emitWRITEVAR(name, in_, index, param.frame), in_
        return self.emit.emitREADVAR(name, in_, index, param.frame), in_

    def visitArrayCell(self, ast, param):
        subParam = SubBody(param.frame, param.scope)
        arrCode, arrTyp = self.visit(ast.arr, param)
        code = arrCode
        typ = ArrayType(array(arrTyp.size), arrTyp.eleType)
        for idx in ast.idx:
            code += self.visit(idx, param)[0]
            if len(typ.size) == 1:
                if not param.isLeft:
                    code += self.emit.ALOAD(typ.eleType, param.frame)
                else:
                    code += self.emit.ASTORE(typ.eleType, param.frame)
                typ = typ.eleType
            else:
                code += self.emit.ALOAD(typ, param.frame)
                typ.size.pop(0)
        return code, typ 

    def visitBlock(self, ast, param):
        param.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(param.frame.getStartLabel(), param.frame))
        bodyParam = SubBody(param.frame, ast.scope)
        for stmt in ast.param:
            self.visit(stmt, bodyParam)
        self.emit.printout(self.emit.emitLABEL(param.frame.getEndLabel(), param.frame))
        param.frame.exitScope()

    def visitIf(self, ast, param):
        self.emit.printout(self.visit(ast.expr, param)[0])
        endLabel = param.frame.getNewLabel()
        elifLabel = param.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(elifLabel, param.frame))
        self.visit(ast.thenStmt, param)
        self.emit.printout(self.emit.emitGOTO(endLabel, param.frame))
        for expr, stmt in self.elifStmt:
            self.emit.printout(self.emit.emitLABEL(elifLabel, param.frame))
            self.emit.printout(self.visit(expr, param)[0])
            elifLabel = param.frame.getNewLabel()
            self.emit.printout(self.emit.emitIFFALSE(elifLabel, param.frame))
            self.visit(stmt, param)
            self.emit.printout(self.emit.emitGOTO(endLabel, param.frame))
        if ast.elseStmt:
            self.emit.printout(self.emit.emitLABEL(elifLabel, param.frame))
            self.visit(ast.elseStmt, param)
        self.emit.printout(self.emit.emitLABEL(endLabel, param.frame))

    def visitFor(self, ast, param):
        name = ast.name
        scope = param.scope
        _, foundScope = scope.lookup(name.name, Variable())
        index = foundScope.getIndex(name.name)
        param.frame.enterLoop()
        startLoopLabel = param.frame.getContinueLabel()
        endLoopLabel = param.frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(startLoopLabel, param.frame))
        self.emit.printout(self.visit(ast.condExpr, param)[0])
        self.emit.printout(self.emit.emitIFFALSE(endLoopLabel, param.frame))
        self.visit(ast.body, param))
        self.emit.printout(self.visit(ast.updExpr, param)[0])
        self.emit.printout(self.visit(name, SubBody(param.frame, param.scope, True))[0])
        self.emit.printout(self.emit.emitGOTO(startLoopLabel, param.frame))
        self.emit.printout(self.emit.emitLABEL(endLoopLabel, param.frame))
        param.frame.exitLoop()

    def visitContinue(self, ast, param):
        continueLabel = param.frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(continueLabel, param.frame))

    def visitBreak(self, ast, param):
        brkLabel = param.frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(brkLabel, param.frame))

    def visitReturn(self, ast, param):
        if ast.expr:
            code, typ = self.visit(ast.expr, param)
            self.emit.printout(code)
            self.emit.printout(self.emitRETURN(typ, param.frame))
        else:
            self.emit.printout(self.emitRETURN(VoidType(), param.frame))

    def visitAssign(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        name = ast.name
        code = ""
        scope = param.scope
        in_, _ = scope.lookup(name, Function())
        for arg in self.args:
            code += self.visit(arg, param)[0]
        code += self.emit.emitINVOKESTATIC(self.classname + "/" + name, in_, param.frame)

        self.emit.printout(code)

    def visitNumberLiteral(self, ast, param):
        return self.emitPUSHCONST(str(ast.value), NumberType(), param.frame), NumberType()

    def visitBooleanLiteral(self, ast, param):
        return self.emitPUSHCONST(str(ast.value), BoolType(), param.frame), BoolType()

    def visitStringLiteral(self, ast, param):
        return self.emitPUSHCONST(self.value, StringType(), param.frame), StringType()

    def visitArrayLiteral(self, ast, param):
        size = len(ast.value)
        code = self.emit.emitPUSHICONST(size, param.frame)
        eleCode = ""
        eleTyp = None
        for index, expr in enumerate(ast.value):
            c, typ = self.visit(expr, param)
            eleTyp = typ
            eleCode += self.emit.emitDUP(param.frame)
            eleCode += self.emit.emitPUSHICONST(index, param.frame)
            eleCode += c
            eleCode += self.emit.emitASTORE(eleTyp, param.frame)
        else:
            code += self.emit.emitARRAY(eleTyp, param.frame) + eleCode

        return code, ArrayType([size], eleTyp) if type(eleTyp) is not ArrayType else ArrayType([size] + eleTyp.size, eleTyp.eleTyp)

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
        if len(self.__list_of_uninferred_expr) == 0 and isSameType(self.ret, UninferredType):
            self.ret = VoidType()
        elif isSameType(self.ret, UninferredType):
            if len(self.__list_of_uninferred_expr) > 0:
                raise TypeCannotBeInferred(self.__list_of_uninferred_expr[0][1])
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

    def setIndex(self, name, idx):
        self.__indexTable[name] = idx

    def getIndex(self, name):
        return self.__indexTable[name] if name in self.__indexTable else None

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
            if name in self.__varSymbolTable:
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
    def __init__(self, scope, inLoop = False, lookupKind = None):
        self.scope = scope
        self.inLoop = inLoop
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
        return type2 is ArrayType or isinstance(type2, ArrayType) and isSameType(type1.eleType, type2.eleType) and type1.size == type2.size
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
        param = CheckerParam(Scope(None, self.ast), False, Identifier())
        param.scope.set("readNumber", FuncType([], NumberType(), True), Function())
        param.scope.set("writeNumber", FuncType([NumberType()], VoidType(), True), Function())
        param.scope.set("readBool", FuncType([], BoolType(), True), Function())
        param.scope.set("writeBool", FuncType([BoolType()], VoidType(), True), Function())
        param.scope.set("readString", FuncType([], StringType(), True), Function())
        param.scope.set("writeString", FuncType([StringType()], VoidType(), True), Function())

        self.visit(self.ast, param)
        return ""
    def visitProgram(self, ast, param):
        for decl in ast.decl:
            self.visit(decl, param)
        param.scope.checkNoBodyFunction()
        if not param.scope.has("main", Function()):
            raise NoEntryPoint()
        mainType = param.scope.get("main", Function())
        if len(mainType.params) != 0 or not isSameType(mainType.ret, VoidType):
            raise NoEntryPoint()

    def visitVarDecl(self, ast, param):
        if param.scope.has(ast.name.name, Variable()):
            raise Redeclared(Variable(), ast.name.name) if not isinstance(param.lookupKind, Parameter) else Redeclared(Parameter(), ast.name.name)
        if ast.varType:
            param.scope.set(ast.name.name, ast.varType, Variable())
            if ast.varInit:
                initRes = self.visit(ast.varInit, CheckerParam(param.scope, param.inLoop, Identifier()))
                initType = initRes.type
                if isSameType(initType, UninferredType):
                    resolveUninferredType(initRes, ast, ast.varType, False)
                elif not isSameType(ast.varType, initType):
                    raise TypeMismatchInStatement(ast)
        elif ast.varInit:
            typ = self.visit(ast.varInit, param).type
            if isSameType(typ, UninferredType):
                raise TypeCannotBeInferred(ast)
            param.scope.set(ast.name.name, typ, Variable())
        else:
            param.scope.set(ast.name.name, UninferredType(), Variable())

    def visitFuncDecl(self, ast, param):
        lookupRes = param.scope.lookup(ast.name.name, Function())
        if lookupRes[0] and lookupRes[0].defined:
            raise Redeclared(Function(), ast.name.name)
        if lookupRes[0] and not lookupRes[0].defined and ast.body is None:
            raise Redeclared(Function(), ast.name.name)
        paramParam = CheckerParam(param.scope.delegate(ast), None, Parameter())
        paramTypes = []
        for parameter in ast.param:
            self.visit(parameter, paramParam)
            paramTypes.append(paramParam.scope.get(parameter.name.name, Parameter()))
        retType = UninferredType()

        if lookupRes[0]:
            fnType, _ = lookupRes
            fnType.defined = fnType.defined or ast.body is not None
            if len(fnType.params) != len(paramTypes):
                raise TypeMismatchInStatement(ast)
            for index, paramType in enumerate(paramTypes):
                if not isSameType(paramType, fnType.params[index]):
                    raise TypeMismatchInStatement(ast)
        else:
            fnType = FuncType(paramTypes, retType, ast.body is not None)
            param.scope.set(ast.name.name, fnType, Function())

        if ast.body is None:
            return CheckerResult(None, None, None, fnType)

        ast.type = fnType
        bodyParam = CheckerParam(paramParam.scope.delegate(ast.body), False, Identifier())
        self.visit(ast.body, bodyParam)
        fnType.resolveRet(ast)
        return CheckerResult(None, None)

    def visitBinaryOp(self, ast, param):
        op = ast.op

        leftRes = self.visit(ast.left, param)
        leftType = leftRes.type

        if op in ['+', '-', '*', '/', '%']:
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, ast, NumberType())
                leftType = NumberType()
            elif not isSameType(leftType, NumberType):
                raise TypeMismatchInExpression(ast)
            rightRes = self.visit(ast.right, param)
            rightType = rightRes.type
            if isSameType(rightType, UninferredType):
                resolveUninferredType(rightRes, ast, NumberType())
                rightType = NumberType()
            elif not isSameType(rightType, NumberType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(NumberType(), param.scope, ast)
        elif op in ['and', 'or']:
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, ast, BoolType())
                leftType = BoolType()
            elif not isSameType(leftType, BoolType):
                raise TypeMismatchInExpression(ast)
            rightRes = self.visit(ast.right, param)
            rightType = rightRes.type
            if isSameType(rightType, UninferredType):
                resolveUninferredType(rightRes, ast, BoolType())
                rightType = BoolType()
            elif not isSameType(rightType, BoolType):
                raise TypeMismatchInExpression(ast)

            return CheckerResult(BoolType(), param.scope, ast)
        elif op == '...':
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, ast, StringType())
                leftType = StringType()
            elif not isSameType(leftType, StringType):
                raise TypeMismatchInExpression(ast)
            rightRes = self.visit(ast.right, param)
            rightType = rightRes.type
            if isSameType(rightType, UninferredType):
                resolveUninferredType(leftRes, ast, StringType())
                rightType = StringType()
            elif not isSameType(rightType, StringType):
                raise TypeMismatchInExpression(ast)

            return CheckerResult(StringType(), param.scope, ast)
        elif op in ['=', '!=', '<', '>', '<=', '>=']:
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, ast, NumberType())
                leftType = NumberType()
            elif not isSameType(leftType, NumberType):
                raise TypeMismatchInExpression(ast)
            rightRes = self.visit(ast.right, param)
            rightType = rightRes.type
            if isSameType(rightType, UninferredType):
                resolveUninferredType(leftRes, ast, NumberType())
                rightType = NumberType()
            elif not isSameType(rightType, NumberType):
                raise TypeMismatchInExpression(ast)

            return CheckerResult(BoolType(), param.scope, ast)
        elif op == '==':
            if isSameType(leftType, UninferredType):
                resolveUninferredType(leftRes, ast, StringType())
                leftType = StringType()
            elif not isSameType(leftType, StringType):
                raise TypeMismatchInExpression(ast)
            rightRes = self.visit(ast.right, param)
            rightType = rightRes.type
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
            elif not isSameType(typ, NumberType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(NumberType(), param.scope, ast)
        elif op == 'not':
            if isSameType(typ, UninferredType):
                resolveUninferredType(res, ast, BoolType())
                return CheckerResult(BoolType(), param.scope, ast)
            elif not isSameType(typ, BoolType):
                raise TypeMismatchInExpression(ast)
            return CheckerResult(BoolType(), param.scope, ast)

        raise Exception('Unreachable')

    def visitCallExpr(self, ast, param):
        calleeType = self.visit(ast.name, CheckerParam(param.scope, param.inLoop, Function())).type
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
        if len(ast.idx) > len(size):
            raise TypeMismatchInExpression(ast)
        for expr in ast.idx:
            exprRes = self.visit(expr, param)
            exprType = exprRes.type
            if isSameType(exprType, UninferredType):
                resolveUninferredType(exprRes, ast, NumberType())
            elif not isSameType(exprType, NumberType):
                raise TypeMismatchInExpression(ast)

        if len(ast.idx) == len(size):
            return CheckerResult(arrType.eleType, param.scope, ast, None, True)
        else:
            return CheckerResult(ArrayType(size[len(ast.idx):], arrType.eleType), param.scope, ast, None, True)
    def visitBlock(self, ast, param):
        param = CheckerParam(param.scope.delegate(ast), param.inLoop, Identifier())
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
            raise TypeMismatchInExpression(ast.expr)
        thenParam = CheckerParam(param.scope.delegate(ast.thenStmt), param.inLoop, Identifier())
        self.visit(ast.thenStmt, thenParam)

        for elifStmt in ast.elifStmt:
            elifCondRes = self.visit(elifStmt[0], param)
            elifCondType = elifCondRes.type
            if isSameType(elifCondType, UninferredType):
                resolveUninferredType(elifCondRes, ast.elifStmt[0], BoolType())
            elif not isSameType(elifCondType, BoolType):
                raise TypeMismatchInExpression(ast.elifStmt[0])
            elifThenParam = CheckerParam(param.scope.delegate(elifStmt[1]), param.inLoop, Identifier())
            self.visit(elifStmt[1], elifThenParam)

        if ast.elseStmt is not None:
            elseParam = CheckerParam(param.scope.delegate(ast.elseStmt), param.inLoop, Identifier())
            self.visit(ast.elseStmt, elseParam)
        return CheckerResult(None, None)

    def visitFor(self, ast, param):
        iterRes = self.visit(ast.name, param)
        iterType = iterRes.type
        if isSameType(iterType, UninferredType):
            resolveUninferredType(iterRes, ast.name, NumberType())
        elif not isSameType(iterType, NumberType):
            raise TypeMismatchInExpression(ast.name)
        condRes = self.visit(ast.condExpr, param)
        condType = condRes.type
        if isSameType(condType, UninferredType):
            resolveUninferredType(condRes, ast.condExpr, BoolType())
        elif not isSameType(condType, BoolType):
            raise TypeMismatchInExpression(ast.condExpr)
        updRes = self.visit(ast.updExpr, param)
        updType = updRes.type
        if isSameType(updType, UninferredType):
            resolveUninferredType(updRes, ast.updExpr, NumberType())
        elif not isSameType(updType, NumberType):
            raise TypeMismatchInExpression(ast.updExpr)

        param = CheckerParam(param.scope.delegate(ast.body), True, Identifier())
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
            elif param.scope.associatedFn is not None and not isSameType(param.scope.associatedFn.type.ret, VoidType):
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

        exprRes = self.visit(ast.rhs, param)
        exprType = exprRes.type

        if isSameType(lhsType, UninferredType) and isSameType(exprType, UninferredType):
            raise TypeCannotBeInferred(ast)
        elif isSameType(lhsType, UninferredType):
            resolveUninferredType(lhsRes, ast, exprType, False)
        elif isSameType(exprType, UninferredType):
            resolveUninferredType(exprRes, ast, lhsType, False)
        elif not isSameType(lhsType, exprType):
            raise TypeMismatchInStatement(ast)

        return CheckerResult(None, param.scope)

    def visitCallStmt(self, ast, param):
        calleeType = self.visit(ast.name, CheckerParam(param.scope, param.inLoop, Function())).type
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
