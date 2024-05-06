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

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"


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
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        patch_Frame_class()
        patch_Machine_Code_Class()
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast, c):
        c = SubBody(None, self.env)
        [self.visit(i, c) for i in ast.decl]
        return c

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
        pass

    def visitUnaryOp(self, ast, param):
        pass

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
