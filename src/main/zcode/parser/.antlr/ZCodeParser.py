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
        4,1,46,231,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,3,1,44,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,3,
        1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,5,6,74,8,6,10,6,12,6,77,9,6,1,6,1,6,3,6,81,8,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,94,8,8,10,8,12,8,97,9,8,1,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,107,8,9,1,10,1,10,1,10,1,10,3,10,113,
        8,10,1,10,1,10,1,10,1,10,3,10,119,8,10,5,10,121,8,10,10,10,12,10,
        124,9,10,3,10,126,8,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,134,8,
        11,10,11,12,11,137,9,11,3,11,139,8,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,
        13,159,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,5,14,176,8,14,10,14,12,14,179,9,14,3,14,181,
        8,14,1,14,1,14,1,14,1,14,3,14,187,8,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,
        206,8,14,10,14,12,14,209,9,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        5,14,218,8,14,10,14,12,14,221,9,14,3,14,223,8,14,1,14,5,14,226,8,
        14,10,14,12,14,229,9,14,1,14,1,75,1,28,15,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,0,4,1,0,23,25,2,0,21,21,26,26,1,0,27,33,1,0,35,
        36,255,0,33,1,0,0,0,2,43,1,0,0,0,4,53,1,0,0,0,6,55,1,0,0,0,8,57,
        1,0,0,0,10,59,1,0,0,0,12,62,1,0,0,0,14,82,1,0,0,0,16,90,1,0,0,0,
        18,101,1,0,0,0,20,108,1,0,0,0,22,129,1,0,0,0,24,142,1,0,0,0,26,158,
        1,0,0,0,28,186,1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,35,1,0,0,0,
        33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,5,
        0,0,1,37,1,1,0,0,0,38,39,3,4,2,0,39,40,5,45,0,0,40,44,1,0,0,0,41,
        44,5,43,0,0,42,44,5,45,0,0,43,38,1,0,0,0,43,41,1,0,0,0,43,42,1,0,
        0,0,44,3,1,0,0,0,45,54,3,28,14,0,46,54,3,26,13,0,47,54,3,24,12,0,
        48,54,3,16,8,0,49,54,3,18,9,0,50,54,3,6,3,0,51,54,3,8,4,0,52,54,
        3,10,5,0,53,45,1,0,0,0,53,46,1,0,0,0,53,47,1,0,0,0,53,48,1,0,0,0,
        53,49,1,0,0,0,53,50,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,5,1,0,
        0,0,55,56,5,1,0,0,56,7,1,0,0,0,57,58,5,2,0,0,58,9,1,0,0,0,59,60,
        5,3,0,0,60,61,3,28,14,0,61,11,1,0,0,0,62,63,5,4,0,0,63,64,5,5,0,
        0,64,65,3,28,14,0,65,66,5,6,0,0,66,75,3,16,8,0,67,68,5,7,0,0,68,
        69,5,5,0,0,69,70,3,28,14,0,70,71,5,6,0,0,71,72,3,16,8,0,72,74,1,
        0,0,0,73,67,1,0,0,0,74,77,1,0,0,0,75,76,1,0,0,0,75,73,1,0,0,0,76,
        80,1,0,0,0,77,75,1,0,0,0,78,79,5,8,0,0,79,81,3,16,8,0,80,78,1,0,
        0,0,80,81,1,0,0,0,81,13,1,0,0,0,82,83,5,9,0,0,83,84,3,28,14,0,84,
        85,5,10,0,0,85,86,3,28,14,0,86,87,5,11,0,0,87,88,3,28,14,0,88,89,
        3,28,14,0,89,15,1,0,0,0,90,91,5,12,0,0,91,95,5,45,0,0,92,94,3,2,
        1,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,
        1,0,0,0,97,95,1,0,0,0,98,99,5,45,0,0,99,100,5,13,0,0,100,17,1,0,
        0,0,101,102,5,14,0,0,102,103,5,38,0,0,103,106,3,20,10,0,104,107,
        3,10,5,0,105,107,3,16,8,0,106,104,1,0,0,0,106,105,1,0,0,0,107,19,
        1,0,0,0,108,125,5,5,0,0,109,110,5,37,0,0,110,112,5,38,0,0,111,113,
        3,22,11,0,112,111,1,0,0,0,112,113,1,0,0,0,113,122,1,0,0,0,114,115,
        5,15,0,0,115,116,5,37,0,0,116,118,5,38,0,0,117,119,3,22,11,0,118,
        117,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,114,1,0,0,0,121,
        124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,126,1,0,0,0,124,
        122,1,0,0,0,125,109,1,0,0,0,125,126,1,0,0,0,126,127,1,0,0,0,127,
        128,5,6,0,0,128,21,1,0,0,0,129,138,5,16,0,0,130,135,5,39,0,0,131,
        132,5,15,0,0,132,134,5,39,0,0,133,131,1,0,0,0,134,137,1,0,0,0,135,
        133,1,0,0,0,135,136,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,138,
        130,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,141,5,17,0,0,141,
        23,1,0,0,0,142,143,3,28,14,0,143,144,5,18,0,0,144,145,3,28,14,0,
        145,25,1,0,0,0,146,147,5,37,0,0,147,148,3,28,14,0,148,149,5,18,0,
        0,149,150,3,28,14,0,150,159,1,0,0,0,151,152,5,19,0,0,152,153,3,28,
        14,0,153,154,5,18,0,0,154,155,3,28,14,0,155,159,1,0,0,0,156,157,
        5,20,0,0,157,159,3,28,14,0,158,146,1,0,0,0,158,151,1,0,0,0,158,156,
        1,0,0,0,159,27,1,0,0,0,160,161,6,14,-1,0,161,162,5,5,0,0,162,163,
        3,28,14,0,163,164,5,6,0,0,164,187,1,0,0,0,165,166,5,21,0,0,166,187,
        3,28,14,11,167,168,5,22,0,0,168,187,3,28,14,10,169,170,5,34,0,0,
        170,187,3,28,14,6,171,180,5,16,0,0,172,177,3,28,14,0,173,174,5,15,
        0,0,174,176,3,28,14,0,175,173,1,0,0,0,176,179,1,0,0,0,177,175,1,
        0,0,0,177,178,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,180,172,1,
        0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,187,5,17,0,0,183,187,5,
        39,0,0,184,187,5,42,0,0,185,187,5,38,0,0,186,160,1,0,0,0,186,165,
        1,0,0,0,186,167,1,0,0,0,186,169,1,0,0,0,186,171,1,0,0,0,186,183,
        1,0,0,0,186,184,1,0,0,0,186,185,1,0,0,0,187,227,1,0,0,0,188,189,
        10,9,0,0,189,190,7,0,0,0,190,226,3,28,14,10,191,192,10,8,0,0,192,
        193,7,1,0,0,193,226,3,28,14,9,194,195,10,7,0,0,195,196,7,2,0,0,196,
        226,3,28,14,8,197,198,10,5,0,0,198,199,7,3,0,0,199,226,3,28,14,6,
        200,201,10,13,0,0,201,202,5,16,0,0,202,207,3,28,14,0,203,204,5,15,
        0,0,204,206,3,28,14,0,205,203,1,0,0,0,206,209,1,0,0,0,207,205,1,
        0,0,0,207,208,1,0,0,0,208,210,1,0,0,0,209,207,1,0,0,0,210,211,5,
        17,0,0,211,226,1,0,0,0,212,213,10,12,0,0,213,222,5,5,0,0,214,219,
        3,28,14,0,215,216,5,15,0,0,216,218,3,28,14,0,217,215,1,0,0,0,218,
        221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,223,1,0,0,0,221,
        219,1,0,0,0,222,214,1,0,0,0,222,223,1,0,0,0,223,224,1,0,0,0,224,
        226,5,6,0,0,225,188,1,0,0,0,225,191,1,0,0,0,225,194,1,0,0,0,225,
        197,1,0,0,0,225,200,1,0,0,0,225,212,1,0,0,0,226,229,1,0,0,0,227,
        225,1,0,0,0,227,228,1,0,0,0,228,29,1,0,0,0,229,227,1,0,0,0,22,33,
        43,53,75,80,95,106,112,118,122,125,135,138,158,177,180,186,207,219,
        222,225,227
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

    ruleNames =  [ "program", "line", "stm", "r_break", "r_continue", "r_return", 
                   "r_if", "r_for", "block", "func", "args", "type_index", 
                   "ass", "decl", "expr" ]

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
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 49357772116014) != 0):
                self.state = 30
                self.line()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
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


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def COMMENT(self):
            return self.getToken(ZCodeParser.COMMENT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_line




    def line(self):

        localctx = ZCodeParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 5, 12, 14, 16, 19, 20, 21, 22, 34, 37, 38, 39, 42]:
                self.state = 38
                self.stm()
                self.state = 39
                self.match(ZCodeParser.NEWLINE)
                pass
            elif token in [43]:
                self.state = 41
                self.match(ZCodeParser.COMMENT)
                pass
            elif token in [45]:
                self.state = 42
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm




    def stm(self):

        localctx = ZCodeParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stm)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 51
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 52
                self.r_return()
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
            self.state = 55
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
            self.state = 57
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
            self.state = 59
            self.match(ZCodeParser.T__2)
            self.state = 60
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


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.BlockContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.BlockContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_if




    def r_if(self):

        localctx = ZCodeParser.R_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_r_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ZCodeParser.T__3)
            self.state = 63
            self.match(ZCodeParser.T__4)
            self.state = 64
            self.expr(0)
            self.state = 65
            self.match(ZCodeParser.T__5)
            self.state = 66
            self.block()
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 67
                    self.match(ZCodeParser.T__6)
                    self.state = 68
                    self.match(ZCodeParser.T__4)
                    self.state = 69
                    self.expr(0)
                    self.state = 70
                    self.match(ZCodeParser.T__5)
                    self.state = 71
                    self.block() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 78
                self.match(ZCodeParser.T__7)
                self.state = 79
                self.block()


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


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_for




    def r_for(self):

        localctx = ZCodeParser.R_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_r_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ZCodeParser.T__8)
            self.state = 83
            self.expr(0)
            self.state = 84
            self.match(ZCodeParser.T__9)
            self.state = 85
            self.expr(0)
            self.state = 86
            self.match(ZCodeParser.T__10)
            self.state = 87
            self.expr(0)
            self.state = 88
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
            self.state = 90
            self.match(ZCodeParser.T__11)
            self.state = 91
            self.match(ZCodeParser.NEWLINE)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 92
                    self.line() 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 98
            self.match(ZCodeParser.NEWLINE)
            self.state = 99
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
            self.state = 101
            self.match(ZCodeParser.T__13)
            self.state = 102
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 103
            self.args()
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 104
                self.r_return()
                pass
            elif token in [12]:
                self.state = 105
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
            self.state = 108
            self.match(ZCodeParser.T__4)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 109
                self.match(ZCodeParser.TYPE)
                self.state = 110
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 111
                    self.type_index()


                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 114
                    self.match(ZCodeParser.T__14)
                    self.state = 115
                    self.match(ZCodeParser.TYPE)
                    self.state = 116
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 118
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 117
                        self.type_index()


                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 127
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
            self.state = 129
            self.match(ZCodeParser.T__15)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 130
                self.match(ZCodeParser.NUMBER)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 131
                    self.match(ZCodeParser.T__14)
                    self.state = 132
                    self.match(ZCodeParser.NUMBER)
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 140
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
            self.state = 142
            self.expr(0)
            self.state = 143
            self.match(ZCodeParser.T__17)
            self.state = 144
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
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(ZCodeParser.TYPE)
                self.state = 147
                self.expr(0)
                self.state = 148
                self.match(ZCodeParser.T__17)
                self.state = 149
                self.expr(0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(ZCodeParser.T__18)
                self.state = 152
                self.expr(0)
                self.state = 153
                self.match(ZCodeParser.T__17)
                self.state = 154
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(ZCodeParser.T__19)
                self.state = 157
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
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.indexer = None # ExprContext
            self.param = None # ExprContext

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
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 161
                self.match(ZCodeParser.T__4)
                self.state = 162
                self.expr(0)
                self.state = 163
                self.match(ZCodeParser.T__5)
                pass
            elif token in [21]:
                self.state = 165
                self.match(ZCodeParser.T__20)
                self.state = 166
                self.expr(11)
                pass
            elif token in [22]:
                self.state = 167
                self.match(ZCodeParser.T__21)
                self.state = 168
                self.expr(10)
                pass
            elif token in [34]:
                self.state = 169
                self.match(ZCodeParser.T__33)
                self.state = 170
                self.expr(6)
                pass
            elif token in [16]:
                self.state = 171
                self.match(ZCodeParser.T__15)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5239866458144) != 0):
                    self.state = 172
                    self.expr(0)
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==15:
                        self.state = 173
                        self.match(ZCodeParser.T__14)
                        self.state = 174
                        self.expr(0)
                        self.state = 179
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 182
                self.match(ZCodeParser.T__16)
                pass
            elif token in [39]:
                self.state = 183
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [42]:
                self.state = 184
                self.match(ZCodeParser.STRING)
                pass
            elif token in [38]:
                self.state = 185
                self.match(ZCodeParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 225
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 188
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 189
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 190
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 192
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 193
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 195
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17045651456) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 196
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 197
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 198
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 199
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 200
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 201
                        self.match(ZCodeParser.T__15)
                        self.state = 202
                        localctx.indexer = self.expr(0)
                        self.state = 207
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 203
                            self.match(ZCodeParser.T__14)
                            self.state = 204
                            localctx.indexer = self.expr(0)
                            self.state = 209
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 210
                        self.match(ZCodeParser.T__16)
                        pass

                    elif la_ == 6:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 212
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 213
                        self.match(ZCodeParser.T__4)
                        self.state = 222
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5239866458144) != 0):
                            self.state = 214
                            localctx.param = self.expr(0)
                            self.state = 219
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 215
                                self.match(ZCodeParser.T__14)
                                self.state = 216
                                localctx.param = self.expr(0)
                                self.state = 221
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 224
                        self.match(ZCodeParser.T__5)
                        pass

             
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 12)
         




