from Utils import *
# from StaticCheck import *
# from StaticError import *
from CodeGenError import *
import CodeGenerator as cgen
from MachineCode import JasminCode
from AST import *
from Frame import Frame

# Since the Frame.py file is not submitted, have to do it here
def patch_Frame_class():
    def getBreakLabel(self):
        if not self.brkLabel:
            raise IllegalRuntimeException("None break label")
        return self.brkLabel[-1]
    Frame.getBreakLabel = getBreakLabel

# Since the MachineCode.py file is not submitted, have to do it here
class Emitter():
    def __init__(self, filename):
        patch_Frame_class()
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()

    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is str:
            return inType
        elif typeIn is NumberType:
            return "F"
        elif typeIn is BoolType:
            return "Z"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            if len(inType.size) == 1:
                reducedType = inType.eleType
            else:
                reducedType = ArrayType(inType.size[1:], inType.eleType)
            return "[" + self.getJVMType(reducedType)
        elif typeIn is cgen.FuncType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.params))) + ")" + self.getJVMType(inType.ret)

    def getFullType(self, inType):
        typeIn = type(inType)
        if typeIn is str:
            return inType
        elif typeIn is NumberType:
            return "float"
        elif typeIn is BoolType:
            return "boolean"
        elif typeIn is StringType:
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"
        elif typeIn is ArrayType:
            return self.getJVMType(inType)

    def emitPUSHICONST(self, in_, frame):
        # in: Int or Sring
        # frame: Frame

        frame.push()
        if type(in_) is int:
            i = in_
            if i >= -1 and i <= 5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
        elif type(in_) is str:
            if in_ == "True":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "False":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)

    def emitPUSHFCONST(self, in_, frame):
        # in_: String
        # frame: Frame

        f = float(in_)
        frame.push()
        rst = "{0:.4f}".format(f)
        if rst == "0.0" or rst == "1.0" or rst == "2.0":
            return self.jvm.emitFCONST(rst)
        else:
            return self.jvm.emitLDC(in_)

    ''' 
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    '''

    def emitPUSHCONST(self, in_, typ, frame):
        # in_: String
        # typ: Type
        # frame: Frame

        if type(typ) is NumberType:
            return self.emitPUSHFCONST(in_, frame)
        elif type(typ) is BoolType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC('"' + in_ + '"')
        else:
            raise IllegalOperandException(in_)

    ##############################################################

    def emitALOAD(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index, value -> ...

        frame.pop()
        if type(in_) is NumberType:
            return self.jvm.emitFALOAD()
        # elif type(in_) is cgen.ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is StringType:
        elif type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))

    def emitASTORE(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index, value -> ...

        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is NumberType:
            return self.jvm.emitFASTORE()
        # elif type(in_) is cgen.ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is StringType:
        elif type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))

    '''    generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label  of the scope where the variable is active.
    '''

    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        # in_: Int
        # varName: String
        # inType: Type
        # fromLabel: Int
        # toLabel: Int
        # frame: Frame

        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitREADVAR(self, inType, index, frame):
        # inType: Type
        # index: Int
        # frame: Frame
        # ... -> ..., value

        frame.push()
        if type(inType) is NumberType:
            return self.jvm.emitFLOAD(index)
        # elif type(inType) is cgen.ArrayPointerType or type(inType) is cgen.ClassType or type(inType) is StringType:
        elif type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        else:
            return self.jvm.emitALOAD(index)
    ''' generate the second instruction for array cell access
    *
    '''

    def emitREADVAR2(self, name, typ, frame):
        # name: String
        # typ: Type
        # frame: Frame
        # ... -> ..., value

        # frame.push()
        raise IllegalOperandException(name)

    '''
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    '''

    def emitWRITEVAR(self, inType, index, frame):
        # inType: Type
        # index: Int
        # frame: Frame
        # ..., value -> ...

        frame.pop()

        if type(inType) is NumberType:
            return self.jvm.emitFSTORE(index)
        # elif type(inType) is cgen.ArrayPointerType or type(inType) is cgen.ClassType or type(inType) is StringType:
        if type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        else:
            return self.jvm.emitASTORE(index)

    ''' generate the second instruction for array cell access
    *
    '''

    def emitWRITEVAR2(self, name, typ, frame):
        # name: String
        # typ: Type
        # frame: Frame
        # ..., value -> ...

        # frame.push()
        raise IllegalOperandException(name)

    ''' generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme the name of the attribute.
    *   @param in the type of the attribute.
    *   @param isFinal true in case of constant; false otherwise
    '''

    def emitATTRIBUTE(self, lexeme, in_):
        # lexeme: String
        # in_: Type
        # isFinal: Boolean
        # value: String

        return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), False)

    def emitGETSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.push()
        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''

    def emitINVOKESTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.params))
        if not type(typ.ret) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a special method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''

    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        # lexeme: String
        # in_: Type
        # frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.params))
            frame.pop()
            if not type(typ.ret) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    ''' generate code to invoke a virtual method
    * @param lexeme the qualified name of the method(i.e., class-name/method-name)
    * @param in the type descriptor of the method.
    '''

    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.params))
        frame.pop()
        if not type(typ.ret) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))

    '''
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    '''

    def emitNEGOP(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., value -> ..., result

        return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame):
        # in_: Type
        # frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHCONST("True", in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST("False", in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    '''
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitADDOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        frame.pop()
        if type(in_) is NumberType:
            if lexeme == "+":
                return self.jvm.emitFADD()
            else:
                return self.jvm.emitFSUB()
        elif type(in_) is StringType:
            if lexeme == "...":
                return self.jvm.emitINVOKEVIRTUAL("java/lang/String/concat", "(Ljava/lang/String;)Ljava/lang/String;")
    '''
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitMULOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        if lexeme == "*":
            return self.emitMUL(frame)
        elif lexeme == '/':
            return self.emitDIV(frame)
        else:
            return self.emitMOD(frame)

    def emitMUL(self, frame):
        frame.pop()
        return self.jvm.emitFMUL()

    def emitDIV(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitFDIV()

    def emitMOD(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitFREM()

    '''
    *   generate iand
    '''

    def emitANDOP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    '''
    *   generate ior
    '''

    def emitOROP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, in_, frame):
        # op: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()

        if type(in_) is NumberType:
            result.append(self.jvm.emitFCMPL())
            if op == ">":
                result.append(self.jvm.emitIFLE(labelF))
            elif op == ">=":
                result.append(self.jvm.emitIFLT(labelF))
            elif op == "<":
                result.append(self.jvm.emitIFGE(labelF))
            elif op == "<=":
                result.append(self.jvm.emitIFGT(labelF))
            elif op == "!=":
                result.append(self.jvm.emitIFEQ(labelF))
            elif op == "=":
                result.append(self.jvm.emitIFNE(labelF))
        elif type(in_) is StringType:
            if op == "==":
                result.append(self.jvm.emitINVOKEVIRTUAL("java/lang/String/compareTo", "(Ljava/lang/String;)I"))
                result.append(self.jvm.emitIFNE(labelF))

        result.append(self.emitPUSHCONST("True", BoolType(), frame))
        result.append(self.emitGOTO(labelO, frame))
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHCONST("False", BoolType(), frame))
        result.append(self.emitLABEL(labelO, frame))
        
        return ''.join(result)

    '''   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''

    def emitMETHOD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), True)

    '''   generate the end directive for a function.
    '''

    def emitENDMETHOD(self, frame):
        # frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def getConst(self, ast):
        # ast: Literal
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())

    '''   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    '''

    '''   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    '''

    '''   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''

    def emitIFTRUE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFNE(label)

    '''
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''

    def emitIFFALSE(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFEQ(label)

    def emitIFICMPGT(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):
        # label: Int
        # frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)

    '''   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    '''

    def emitDUP(self, frame):
        # frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        # frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    '''   generate code to exchange an integer on top of stack to a floating-point number.
    '''

    def emitI2F(self, frame):
        # frame: Frame

        return self.jvm.emitI2F()

    def emitF2I(self, frame):
        # frame: Frame
        
        return self.jvm.emitF2I()


    ''' generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BoolType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    '''

    def emitRETURN(self, in_, frame):
        # in_: Type
        # frame: Frame

        if type(in_) is NumberType:
            frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is StringType:
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is ArrayType:
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()

    ''' generate code that represents a label	
    *   @param label the label
    *   @return code Label<label>:
    '''

    def emitLABEL(self, label, frame):
        # label: Int
        # frame: Frame

        return self.jvm.emitLABEL(label)

    ''' generate code to jump to a label	
    *   @param label the label
    *   @return code goto Label<label>
    '''

    def emitGOTO(self, label, frame):
        # label: Int
        # frame: Frame

        return self.jvm.emitGOTO(str(label))

    ''' generate some starting directives for a class.<p>
    *   .source MPC.CLASSNAME.java<p>
    *   .class public MPC.CLASSNAME<p>
    *   .super java/lang/Object<p>
    '''

    def emitFCMPL(self, name, frame):
        frame.pop()
        return self.jvm.emitFCMPL()

    def emitPROLOG(self, name, parent):
        # name: String
        # parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER(
            "java/lang/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        # num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        # num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''

    def emitNEW(self, typ, frame):
        # typ: Type
        frame.push()
        return self.jvm.emitNEW(self.getJVMType(typ))

    def emitARRAY(self, typ, frame):
        if type(typ) in [BoolType, NumberType]:
            return self.emitNEWARRAY(typ, frame)
        else:
            return self.emitANEWARRAY(typ, frame)

    def emitNEWARRAY(self, typ, frame):
        # typ: Type

        return self.jvm.emitNEWARRAY(self.getFullType(typ))

    def emitANEWARRAY(self, typ, frame):
        # typ: Type
        
        return self.jvm.emitANEWARRAY(self.getFullType(typ))

    def emitMULTIANEWARRAY(self, typ, dimensions, frame):
        # typ: Type
        # dimensions: Int
        for i in range(dimensions):
            frame.pop()
        frame.push()
        return self.jvm.emitMULTIANEWARRAY(self.getJVMType(typ), dimensions)

    def emitSWAP(self, frame):
        return self.jvm.emitSWAP()

    def printout(self, in_):
        # in_: String

        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()
