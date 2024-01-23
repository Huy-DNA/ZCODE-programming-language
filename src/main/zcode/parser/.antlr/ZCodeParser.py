# Generated from /home/hell/projects/ZCODE-programming-language/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,280,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,48,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,60,8,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,5,6,74,8,6,10,6,12,6,77,9,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,85,
        8,6,10,6,12,6,88,9,6,1,6,1,6,5,6,92,8,6,10,6,12,6,95,9,6,1,6,1,6,
        5,6,99,8,6,10,6,12,6,102,9,6,1,6,3,6,105,8,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,5,7,114,8,7,10,7,12,7,117,9,7,1,7,1,7,1,8,1,8,1,8,5,8,124,
        8,8,10,8,12,8,127,9,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,137,8,
        9,1,10,1,10,1,10,1,10,3,10,143,8,10,1,10,1,10,1,10,1,10,3,10,149,
        8,10,5,10,151,8,10,10,10,12,10,154,9,10,3,10,156,8,10,1,10,1,10,
        1,11,1,11,1,11,1,11,5,11,164,8,11,10,11,12,11,167,9,11,3,11,169,
        8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,3,13,189,8,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,205,8,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,218,
        8,14,10,14,12,14,221,9,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,
        230,8,14,10,14,12,14,233,9,14,3,14,235,8,14,1,14,5,14,238,8,14,10,
        14,12,14,241,9,14,1,15,1,15,1,15,1,15,1,15,3,15,248,8,15,1,16,1,
        16,1,16,1,16,1,16,5,16,255,8,16,10,16,12,16,258,9,16,3,16,260,8,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,270,8,16,1,16,1,
        16,1,16,5,16,275,8,16,10,16,12,16,278,9,16,1,16,1,93,2,28,32,17,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,5,1,1,45,45,1,0,
        27,33,1,0,23,25,2,0,21,21,26,26,1,0,35,36,309,0,37,1,0,0,0,2,47,
        1,0,0,0,4,59,1,0,0,0,6,61,1,0,0,0,8,63,1,0,0,0,10,65,1,0,0,0,12,
        68,1,0,0,0,14,106,1,0,0,0,16,120,1,0,0,0,18,131,1,0,0,0,20,138,1,
        0,0,0,22,159,1,0,0,0,24,172,1,0,0,0,26,188,1,0,0,0,28,204,1,0,0,
        0,30,247,1,0,0,0,32,269,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,39,
        1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,
        40,41,5,0,0,1,41,1,1,0,0,0,42,43,3,4,2,0,43,44,7,0,0,0,44,48,1,0,
        0,0,45,48,5,43,0,0,46,48,5,45,0,0,47,42,1,0,0,0,47,45,1,0,0,0,47,
        46,1,0,0,0,48,3,1,0,0,0,49,60,3,28,14,0,50,60,3,26,13,0,51,60,3,
        24,12,0,52,60,3,16,8,0,53,60,3,18,9,0,54,60,3,6,3,0,55,60,3,8,4,
        0,56,60,3,10,5,0,57,60,3,12,6,0,58,60,3,14,7,0,59,49,1,0,0,0,59,
        50,1,0,0,0,59,51,1,0,0,0,59,52,1,0,0,0,59,53,1,0,0,0,59,54,1,0,0,
        0,59,55,1,0,0,0,59,56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,5,1,
        0,0,0,61,62,5,1,0,0,62,7,1,0,0,0,63,64,5,2,0,0,64,9,1,0,0,0,65,66,
        5,3,0,0,66,67,3,28,14,0,67,11,1,0,0,0,68,69,5,4,0,0,69,70,5,5,0,
        0,70,71,3,28,14,0,71,75,5,6,0,0,72,74,5,45,0,0,73,72,1,0,0,0,74,
        77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,
        0,78,93,3,28,14,0,79,80,5,7,0,0,80,81,5,5,0,0,81,82,3,28,14,0,82,
        86,5,6,0,0,83,85,5,45,0,0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,
        0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,90,3,28,14,0,90,
        92,1,0,0,0,91,79,1,0,0,0,92,95,1,0,0,0,93,94,1,0,0,0,93,91,1,0,0,
        0,94,104,1,0,0,0,95,93,1,0,0,0,96,100,5,8,0,0,97,99,5,45,0,0,98,
        97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,
        1,0,0,0,102,100,1,0,0,0,103,105,3,28,14,0,104,96,1,0,0,0,104,105,
        1,0,0,0,105,13,1,0,0,0,106,107,5,9,0,0,107,108,3,28,14,0,108,109,
        5,10,0,0,109,110,3,28,14,0,110,111,5,11,0,0,111,115,3,28,14,0,112,
        114,5,45,0,0,113,112,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,
        116,1,0,0,0,116,118,1,0,0,0,117,115,1,0,0,0,118,119,3,28,14,0,119,
        15,1,0,0,0,120,121,5,12,0,0,121,125,5,45,0,0,122,124,3,2,1,0,123,
        122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,
        128,1,0,0,0,127,125,1,0,0,0,128,129,5,45,0,0,129,130,5,13,0,0,130,
        17,1,0,0,0,131,132,5,14,0,0,132,133,5,38,0,0,133,136,3,20,10,0,134,
        137,3,10,5,0,135,137,3,16,8,0,136,134,1,0,0,0,136,135,1,0,0,0,137,
        19,1,0,0,0,138,155,5,5,0,0,139,140,5,37,0,0,140,142,5,38,0,0,141,
        143,3,22,11,0,142,141,1,0,0,0,142,143,1,0,0,0,143,152,1,0,0,0,144,
        145,5,15,0,0,145,146,5,37,0,0,146,148,5,38,0,0,147,149,3,22,11,0,
        148,147,1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,144,1,0,0,0,
        151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,156,1,0,0,0,
        154,152,1,0,0,0,155,139,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,
        157,158,5,6,0,0,158,21,1,0,0,0,159,168,5,16,0,0,160,165,5,39,0,0,
        161,162,5,15,0,0,162,164,5,39,0,0,163,161,1,0,0,0,164,167,1,0,0,
        0,165,163,1,0,0,0,165,166,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,
        0,168,160,1,0,0,0,168,169,1,0,0,0,169,170,1,0,0,0,170,171,5,17,0,
        0,171,23,1,0,0,0,172,173,3,28,14,0,173,174,5,18,0,0,174,175,3,28,
        14,0,175,25,1,0,0,0,176,177,5,37,0,0,177,178,3,28,14,0,178,179,5,
        18,0,0,179,180,3,28,14,0,180,189,1,0,0,0,181,182,5,19,0,0,182,183,
        3,28,14,0,183,184,5,18,0,0,184,185,3,28,14,0,185,189,1,0,0,0,186,
        187,5,20,0,0,187,189,3,28,14,0,188,176,1,0,0,0,188,181,1,0,0,0,188,
        186,1,0,0,0,189,27,1,0,0,0,190,191,6,14,-1,0,191,192,5,5,0,0,192,
        193,3,28,14,0,193,194,5,6,0,0,194,205,1,0,0,0,195,196,5,21,0,0,196,
        205,3,28,14,6,197,198,5,22,0,0,198,205,3,28,14,5,199,200,3,30,15,
        0,200,201,7,1,0,0,201,202,3,30,15,0,202,205,1,0,0,0,203,205,3,30,
        15,0,204,190,1,0,0,0,204,195,1,0,0,0,204,197,1,0,0,0,204,199,1,0,
        0,0,204,203,1,0,0,0,205,239,1,0,0,0,206,207,10,4,0,0,207,208,7,2,
        0,0,208,238,3,28,14,5,209,210,10,3,0,0,210,211,7,3,0,0,211,238,3,
        28,14,4,212,213,10,8,0,0,213,214,5,16,0,0,214,219,3,28,14,0,215,
        216,5,15,0,0,216,218,3,28,14,0,217,215,1,0,0,0,218,221,1,0,0,0,219,
        217,1,0,0,0,219,220,1,0,0,0,220,222,1,0,0,0,221,219,1,0,0,0,222,
        223,5,17,0,0,223,238,1,0,0,0,224,225,10,7,0,0,225,234,5,5,0,0,226,
        231,3,28,14,0,227,228,5,15,0,0,228,230,3,28,14,0,229,227,1,0,0,0,
        230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,235,1,0,0,0,
        233,231,1,0,0,0,234,226,1,0,0,0,234,235,1,0,0,0,235,236,1,0,0,0,
        236,238,5,6,0,0,237,206,1,0,0,0,237,209,1,0,0,0,237,212,1,0,0,0,
        237,224,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,
        240,29,1,0,0,0,241,239,1,0,0,0,242,243,3,32,16,0,243,244,5,34,0,
        0,244,245,3,32,16,0,245,248,1,0,0,0,246,248,3,32,16,0,247,242,1,
        0,0,0,247,246,1,0,0,0,248,31,1,0,0,0,249,250,6,16,-1,0,250,259,5,
        16,0,0,251,256,3,28,14,0,252,253,5,15,0,0,253,255,3,28,14,0,254,
        252,1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,
        260,1,0,0,0,258,256,1,0,0,0,259,251,1,0,0,0,259,260,1,0,0,0,260,
        261,1,0,0,0,261,270,5,17,0,0,262,270,5,39,0,0,263,270,5,42,0,0,264,
        270,5,38,0,0,265,266,5,5,0,0,266,267,3,28,14,0,267,268,5,6,0,0,268,
        270,1,0,0,0,269,249,1,0,0,0,269,262,1,0,0,0,269,263,1,0,0,0,269,
        264,1,0,0,0,269,265,1,0,0,0,270,276,1,0,0,0,271,272,10,6,0,0,272,
        273,7,4,0,0,273,275,3,32,16,7,274,271,1,0,0,0,275,278,1,0,0,0,276,
        274,1,0,0,0,276,277,1,0,0,0,277,33,1,0,0,0,278,276,1,0,0,0,29,37,
        47,59,75,86,93,100,104,115,125,136,142,148,152,155,165,168,188,204,
        219,231,234,237,239,247,256,259,269,276
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'break'", "'continue'", "'return'", "'if'", 
                     "'('", "')'", "'elif'", "'else'", "'for'", "'until'", 
                     "'by'", "'begin'", "'end'", "'func'", "','", "'['", 
                     "']'", "'<-'", "'var'", "'dynamic'", "'-'", "'not'", 
                     "'*'", "'/'", "'%'", "'+'", "'='", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'...'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TYPE", "IDENTIFIER", "NUMBER", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "STRING", "COMMENT", "WS", "NEWLINE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_line = 1
    RULE_stm = 2
    RULE_r_break = 3
    RULE_r_continue = 4
    RULE_r_return = 5
    RULE_r_if = 6
    RULE_r_for = 7
    RULE_block = 8
    RULE_func = 9
    RULE_args = 10
    RULE_type_index = 11
    RULE_ass = 12
    RULE_decl = 13
    RULE_expr = 14
    RULE_expr_without_rel = 15
    RULE_expr_without_str_concat = 16

    ruleNames =  [ "program", "line", "stm", "r_break", "r_continue", "r_return", 
                   "r_if", "r_for", "block", "func", "args", "type_index", 
                   "ass", "decl", "expr", "expr_without_rel", "expr_without_str_concat" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    TYPE=37
    IDENTIFIER=38
    NUMBER=39
    ILLEGAL_ESCAPE=40
    UNCLOSE_STRING=41
    STRING=42
    COMMENT=43
    WS=44
    NEWLINE=45
    ERROR_CHAR=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.LineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.LineContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 49340592247358) != 0):
                self.state = 34
                self.line()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def COMMENT(self):
            return self.getToken(ZCodeParser.COMMENT, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_line




    def line(self):

        localctx = ZCodeParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 9, 12, 14, 16, 19, 20, 21, 22, 37, 38, 39, 42]:
                self.state = 42
                self.stm()
                self.state = 43
                _la = self._input.LA(1)
                if not(_la==-1 or _la==45):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [43]:
                self.state = 45
                self.match(ZCodeParser.COMMENT)
                pass
            elif token in [45]:
                self.state = 46
                self.match(ZCodeParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def ass(self):
            return self.getTypedRuleContext(ZCodeParser.AssContext,0)


        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def func(self):
            return self.getTypedRuleContext(ZCodeParser.FuncContext,0)


        def r_break(self):
            return self.getTypedRuleContext(ZCodeParser.R_breakContext,0)


        def r_continue(self):
            return self.getTypedRuleContext(ZCodeParser.R_continueContext,0)


        def r_return(self):
            return self.getTypedRuleContext(ZCodeParser.R_returnContext,0)


        def r_if(self):
            return self.getTypedRuleContext(ZCodeParser.R_ifContext,0)


        def r_for(self):
            return self.getTypedRuleContext(ZCodeParser.R_forContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm




    def stm(self):

        localctx = ZCodeParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stm)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 55
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 56
                self.r_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 57
                self.r_if()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 58
                self.r_for()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_break




    def r_break(self):

        localctx = ZCodeParser.R_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_r_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ZCodeParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_continue




    def r_continue(self):

        localctx = ZCodeParser.R_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_r_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ZCodeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_return




    def r_return(self):

        localctx = ZCodeParser.R_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_r_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ZCodeParser.T__2)
            self.state = 66
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_if




    def r_if(self):

        localctx = ZCodeParser.R_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_r_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ZCodeParser.T__3)
            self.state = 69
            self.match(ZCodeParser.T__4)
            self.state = 70
            self.expr(0)
            self.state = 71
            self.match(ZCodeParser.T__5)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 72
                self.match(ZCodeParser.NEWLINE)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.expr(0)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 79
                    self.match(ZCodeParser.T__6)
                    self.state = 80
                    self.match(ZCodeParser.T__4)
                    self.state = 81
                    self.expr(0)
                    self.state = 82
                    self.match(ZCodeParser.T__5)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==45:
                        self.state = 83
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 88
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 89
                    self.expr(0) 
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 96
                self.match(ZCodeParser.T__7)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 97
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_for




    def r_for(self):

        localctx = ZCodeParser.R_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_r_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ZCodeParser.T__8)
            self.state = 107
            self.expr(0)
            self.state = 108
            self.match(ZCodeParser.T__9)
            self.state = 109
            self.expr(0)
            self.state = 110
            self.match(ZCodeParser.T__10)
            self.state = 111
            self.expr(0)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 112
                self.match(ZCodeParser.NEWLINE)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.LineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.LineContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(ZCodeParser.T__11)
            self.state = 121
            self.match(ZCodeParser.NEWLINE)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 122
                    self.line() 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 128
            self.match(ZCodeParser.NEWLINE)
            self.state = 129
            self.match(ZCodeParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def args(self):
            return self.getTypedRuleContext(ZCodeParser.ArgsContext,0)


        def r_return(self):
            return self.getTypedRuleContext(ZCodeParser.R_returnContext,0)


        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func




    def func(self):

        localctx = ZCodeParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ZCodeParser.T__13)
            self.state = 132
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 133
            self.args()
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 134
                self.r_return()
                pass
            elif token in [12]:
                self.state = 135
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.TYPE)
            else:
                return self.getToken(ZCodeParser.TYPE, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.IDENTIFIER)
            else:
                return self.getToken(ZCodeParser.IDENTIFIER, i)

        def type_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Type_indexContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Type_indexContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_args




    def args(self):

        localctx = ZCodeParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(ZCodeParser.T__4)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 139
                self.match(ZCodeParser.TYPE)
                self.state = 140
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 141
                    self.type_index()


                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 144
                    self.match(ZCodeParser.T__14)
                    self.state = 145
                    self.match(ZCodeParser.TYPE)
                    self.state = 146
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 148
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 147
                        self.type_index()


                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 157
            self.match(ZCodeParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NUMBER)
            else:
                return self.getToken(ZCodeParser.NUMBER, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type_index




    def type_index(self):

        localctx = ZCodeParser.Type_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ZCodeParser.T__15)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 160
                self.match(ZCodeParser.NUMBER)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 161
                    self.match(ZCodeParser.T__14)
                    self.state = 162
                    self.match(ZCodeParser.NUMBER)
                    self.state = 167
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 170
            self.match(ZCodeParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ass




    def ass(self):

        localctx = ZCodeParser.AssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.expr(0)
            self.state = 173
            self.match(ZCodeParser.T__17)
            self.state = 174
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(ZCodeParser.TYPE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_decl)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(ZCodeParser.TYPE)
                self.state = 177
                self.expr(0)
                self.state = 178
                self.match(ZCodeParser.T__17)
                self.state = 179
                self.expr(0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(ZCodeParser.T__18)
                self.state = 182
                self.expr(0)
                self.state = 183
                self.match(ZCodeParser.T__17)
                self.state = 184
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.match(ZCodeParser.T__19)
                self.state = 187
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.array = None # ExprContext
            self.callee = None # ExprContext
            self.op = None # Token
            self.indexer = None # ExprContext
            self.param = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def expr_without_rel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_without_relContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_without_relContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 191
                self.match(ZCodeParser.T__4)
                self.state = 192
                self.expr(0)
                self.state = 193
                self.match(ZCodeParser.T__5)
                pass

            elif la_ == 2:
                self.state = 195
                self.match(ZCodeParser.T__20)
                self.state = 196
                self.expr(6)
                pass

            elif la_ == 3:
                self.state = 197
                self.match(ZCodeParser.T__21)
                self.state = 198
                self.expr(5)
                pass

            elif la_ == 4:
                self.state = 199
                self.expr_without_rel()
                self.state = 200
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17045651456) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 201
                self.expr_without_rel()
                pass

            elif la_ == 5:
                self.state = 203
                self.expr_without_rel()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 237
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 206
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 207
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 208
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 209
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 210
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 211
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 212
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 213
                        self.match(ZCodeParser.T__15)
                        self.state = 214
                        localctx.indexer = self.expr(0)
                        self.state = 219
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 215
                            self.match(ZCodeParser.T__14)
                            self.state = 216
                            localctx.indexer = self.expr(0)
                            self.state = 221
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 222
                        self.match(ZCodeParser.T__16)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 224
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 225
                        self.match(ZCodeParser.T__4)
                        self.state = 234
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                            self.state = 226
                            localctx.param = self.expr(0)
                            self.state = 231
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 227
                                self.match(ZCodeParser.T__14)
                                self.state = 228
                                localctx.param = self.expr(0)
                                self.state = 233
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 236
                        self.match(ZCodeParser.T__5)
                        pass

             
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_without_relContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_without_str_concat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_without_str_concatContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_without_str_concatContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_without_rel




    def expr_without_rel(self):

        localctx = ZCodeParser.Expr_without_relContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_without_rel)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.expr_without_str_concat(0)
                self.state = 243
                self.match(ZCodeParser.T__33)
                self.state = 244
                self.expr_without_str_concat(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.expr_without_str_concat(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_without_str_concatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr_without_str_concat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_without_str_concatContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_without_str_concatContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_without_str_concat



    def expr_without_str_concat(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_without_str_concatContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr_without_str_concat, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 250
                self.match(ZCodeParser.T__15)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                    self.state = 251
                    self.expr(0)
                    self.state = 256
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==15:
                        self.state = 252
                        self.match(ZCodeParser.T__14)
                        self.state = 253
                        self.expr(0)
                        self.state = 258
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 261
                self.match(ZCodeParser.T__16)
                pass
            elif token in [39]:
                self.state = 262
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [42]:
                self.state = 263
                self.match(ZCodeParser.STRING)
                pass
            elif token in [38]:
                self.state = 264
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [5]:
                self.state = 265
                self.match(ZCodeParser.T__4)
                self.state = 266
                self.expr(0)
                self.state = 267
                self.match(ZCodeParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_without_str_concatContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_without_str_concat)
                    self.state = 271
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 272
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==35 or _la==36):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 273
                    self.expr_without_str_concat(7) 
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expr_sempred
        self._predicates[16] = self.expr_without_str_concat_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

    def expr_without_str_concat_sempred(self, localctx:Expr_without_str_concatContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




