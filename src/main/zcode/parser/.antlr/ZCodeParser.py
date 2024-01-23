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
        4,1,46,307,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,3,0,48,8,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,5,5,88,8,5,10,5,12,5,91,9,5,1,5,1,5,1,5,1,5,1,5,1,5,
        5,5,99,8,5,10,5,12,5,102,9,5,1,5,1,5,5,5,106,8,5,10,5,12,5,109,9,
        5,1,5,1,5,5,5,113,8,5,10,5,12,5,116,9,5,1,5,3,5,119,8,5,3,5,121,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,130,8,6,10,6,12,6,133,9,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,142,8,7,10,7,12,7,145,9,7,1,7,5,7,
        148,8,7,10,7,12,7,151,9,7,1,7,3,7,154,8,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,3,8,164,8,8,1,9,1,9,1,9,1,9,3,9,170,8,9,1,9,1,9,1,9,1,
        9,3,9,176,8,9,5,9,178,8,9,10,9,12,9,181,9,9,3,9,183,8,9,1,9,1,9,
        1,10,1,10,1,10,1,10,5,10,191,8,10,10,10,12,10,194,9,10,3,10,196,
        8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,3,12,216,8,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,232,8,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,245,
        8,13,10,13,12,13,248,9,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,
        257,8,13,10,13,12,13,260,9,13,3,13,262,8,13,1,13,5,13,265,8,13,10,
        13,12,13,268,9,13,1,14,1,14,1,14,1,14,1,14,3,14,275,8,14,1,15,1,
        15,1,15,1,15,1,15,5,15,282,8,15,10,15,12,15,285,9,15,3,15,287,8,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,297,8,15,1,15,1,
        15,1,15,5,15,302,8,15,10,15,12,15,305,9,15,1,15,1,107,2,26,30,16,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,4,1,0,27,33,1,0,23,
        25,2,0,21,21,26,26,1,0,35,36,343,0,47,1,0,0,0,2,61,1,0,0,0,4,63,
        1,0,0,0,6,65,1,0,0,0,8,67,1,0,0,0,10,120,1,0,0,0,12,122,1,0,0,0,
        14,136,1,0,0,0,16,158,1,0,0,0,18,165,1,0,0,0,20,186,1,0,0,0,22,199,
        1,0,0,0,24,215,1,0,0,0,26,231,1,0,0,0,28,274,1,0,0,0,30,296,1,0,
        0,0,32,37,3,2,1,0,33,34,5,45,0,0,34,36,3,2,1,0,35,33,1,0,0,0,36,
        39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,48,1,0,0,0,39,37,1,0,0,
        0,40,42,5,45,0,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,
        1,0,0,0,44,48,1,0,0,0,45,43,1,0,0,0,46,48,5,43,0,0,47,32,1,0,0,0,
        47,43,1,0,0,0,47,46,1,0,0,0,48,49,1,0,0,0,49,50,5,0,0,1,50,1,1,0,
        0,0,51,62,3,26,13,0,52,62,3,24,12,0,53,62,3,22,11,0,54,62,3,14,7,
        0,55,62,3,16,8,0,56,62,3,4,2,0,57,62,3,6,3,0,58,62,3,8,4,0,59,62,
        3,10,5,0,60,62,3,12,6,0,61,51,1,0,0,0,61,52,1,0,0,0,61,53,1,0,0,
        0,61,54,1,0,0,0,61,55,1,0,0,0,61,56,1,0,0,0,61,57,1,0,0,0,61,58,
        1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,3,1,0,0,0,63,64,5,1,0,0,64,
        5,1,0,0,0,65,66,5,2,0,0,66,7,1,0,0,0,67,68,5,3,0,0,68,69,3,26,13,
        0,69,9,1,0,0,0,70,71,5,4,0,0,71,72,5,5,0,0,72,73,3,26,13,0,73,77,
        5,6,0,0,74,76,5,45,0,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,
        77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,3,2,1,0,81,121,1,
        0,0,0,82,83,5,4,0,0,83,84,5,5,0,0,84,85,3,26,13,0,85,89,5,6,0,0,
        86,88,5,45,0,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,
        0,0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,107,3,2,1,0,93,94,5,7,0,0,94,
        95,5,5,0,0,95,96,3,26,13,0,96,100,5,6,0,0,97,99,5,45,0,0,98,97,1,
        0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,0,
        0,0,102,100,1,0,0,0,103,104,3,2,1,0,104,106,1,0,0,0,105,93,1,0,0,
        0,106,109,1,0,0,0,107,108,1,0,0,0,107,105,1,0,0,0,108,118,1,0,0,
        0,109,107,1,0,0,0,110,114,5,8,0,0,111,113,5,45,0,0,112,111,1,0,0,
        0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,
        0,116,114,1,0,0,0,117,119,3,2,1,0,118,110,1,0,0,0,118,119,1,0,0,
        0,119,121,1,0,0,0,120,70,1,0,0,0,120,82,1,0,0,0,121,11,1,0,0,0,122,
        123,5,9,0,0,123,124,3,26,13,0,124,125,5,10,0,0,125,126,3,26,13,0,
        126,127,5,11,0,0,127,131,3,26,13,0,128,130,5,45,0,0,129,128,1,0,
        0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,
        0,0,133,131,1,0,0,0,134,135,3,2,1,0,135,13,1,0,0,0,136,137,5,12,
        0,0,137,153,5,45,0,0,138,143,3,2,1,0,139,140,5,45,0,0,140,142,3,
        2,1,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,
        0,0,0,144,154,1,0,0,0,145,143,1,0,0,0,146,148,5,45,0,0,147,146,1,
        0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,154,1,
        0,0,0,151,149,1,0,0,0,152,154,5,43,0,0,153,138,1,0,0,0,153,149,1,
        0,0,0,153,152,1,0,0,0,154,155,1,0,0,0,155,156,5,45,0,0,156,157,5,
        13,0,0,157,15,1,0,0,0,158,159,5,14,0,0,159,160,5,38,0,0,160,163,
        3,18,9,0,161,164,3,8,4,0,162,164,3,14,7,0,163,161,1,0,0,0,163,162,
        1,0,0,0,164,17,1,0,0,0,165,182,5,5,0,0,166,167,5,37,0,0,167,169,
        5,38,0,0,168,170,3,20,10,0,169,168,1,0,0,0,169,170,1,0,0,0,170,179,
        1,0,0,0,171,172,5,15,0,0,172,173,5,37,0,0,173,175,5,38,0,0,174,176,
        3,20,10,0,175,174,1,0,0,0,175,176,1,0,0,0,176,178,1,0,0,0,177,171,
        1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,183,
        1,0,0,0,181,179,1,0,0,0,182,166,1,0,0,0,182,183,1,0,0,0,183,184,
        1,0,0,0,184,185,5,6,0,0,185,19,1,0,0,0,186,195,5,16,0,0,187,192,
        5,39,0,0,188,189,5,15,0,0,189,191,5,39,0,0,190,188,1,0,0,0,191,194,
        1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,196,1,0,0,0,194,192,
        1,0,0,0,195,187,1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,198,
        5,17,0,0,198,21,1,0,0,0,199,200,3,26,13,0,200,201,5,18,0,0,201,202,
        3,26,13,0,202,23,1,0,0,0,203,204,5,37,0,0,204,205,3,26,13,0,205,
        206,5,18,0,0,206,207,3,26,13,0,207,216,1,0,0,0,208,209,5,19,0,0,
        209,210,3,26,13,0,210,211,5,18,0,0,211,212,3,26,13,0,212,216,1,0,
        0,0,213,214,5,20,0,0,214,216,3,26,13,0,215,203,1,0,0,0,215,208,1,
        0,0,0,215,213,1,0,0,0,216,25,1,0,0,0,217,218,6,13,-1,0,218,219,5,
        5,0,0,219,220,3,26,13,0,220,221,5,6,0,0,221,232,1,0,0,0,222,223,
        5,21,0,0,223,232,3,26,13,6,224,225,5,22,0,0,225,232,3,26,13,5,226,
        227,3,28,14,0,227,228,7,0,0,0,228,229,3,28,14,0,229,232,1,0,0,0,
        230,232,3,28,14,0,231,217,1,0,0,0,231,222,1,0,0,0,231,224,1,0,0,
        0,231,226,1,0,0,0,231,230,1,0,0,0,232,266,1,0,0,0,233,234,10,4,0,
        0,234,235,7,1,0,0,235,265,3,26,13,5,236,237,10,3,0,0,237,238,7,2,
        0,0,238,265,3,26,13,4,239,240,10,8,0,0,240,241,5,16,0,0,241,246,
        3,26,13,0,242,243,5,15,0,0,243,245,3,26,13,0,244,242,1,0,0,0,245,
        248,1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,249,1,0,0,0,248,
        246,1,0,0,0,249,250,5,17,0,0,250,265,1,0,0,0,251,252,10,7,0,0,252,
        261,5,5,0,0,253,258,3,26,13,0,254,255,5,15,0,0,255,257,3,26,13,0,
        256,254,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,
        259,262,1,0,0,0,260,258,1,0,0,0,261,253,1,0,0,0,261,262,1,0,0,0,
        262,263,1,0,0,0,263,265,5,6,0,0,264,233,1,0,0,0,264,236,1,0,0,0,
        264,239,1,0,0,0,264,251,1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,0,
        266,267,1,0,0,0,267,27,1,0,0,0,268,266,1,0,0,0,269,270,3,30,15,0,
        270,271,5,34,0,0,271,272,3,30,15,0,272,275,1,0,0,0,273,275,3,30,
        15,0,274,269,1,0,0,0,274,273,1,0,0,0,275,29,1,0,0,0,276,277,6,15,
        -1,0,277,286,5,16,0,0,278,283,3,26,13,0,279,280,5,15,0,0,280,282,
        3,26,13,0,281,279,1,0,0,0,282,285,1,0,0,0,283,281,1,0,0,0,283,284,
        1,0,0,0,284,287,1,0,0,0,285,283,1,0,0,0,286,278,1,0,0,0,286,287,
        1,0,0,0,287,288,1,0,0,0,288,297,5,17,0,0,289,297,5,39,0,0,290,297,
        5,42,0,0,291,297,5,38,0,0,292,293,5,5,0,0,293,294,3,26,13,0,294,
        295,5,6,0,0,295,297,1,0,0,0,296,276,1,0,0,0,296,289,1,0,0,0,296,
        290,1,0,0,0,296,291,1,0,0,0,296,292,1,0,0,0,297,303,1,0,0,0,298,
        299,10,6,0,0,299,300,7,3,0,0,300,302,3,30,15,7,301,298,1,0,0,0,302,
        305,1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,31,1,0,0,0,305,303,
        1,0,0,0,34,37,43,47,61,77,89,100,107,114,118,120,131,143,149,153,
        163,169,175,179,182,192,195,215,231,246,258,261,264,266,274,283,
        286,296,303
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
    RULE_stm = 1
    RULE_r_break = 2
    RULE_r_continue = 3
    RULE_r_return = 4
    RULE_r_if = 5
    RULE_r_for = 6
    RULE_block = 7
    RULE_func = 8
    RULE_args = 9
    RULE_type_index = 10
    RULE_ass = 11
    RULE_decl = 12
    RULE_expr = 13
    RULE_expr_without_rel = 14
    RULE_expr_without_str_concat = 15

    ruleNames =  [ "program", "stm", "r_break", "r_continue", "r_return", 
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

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmContext,i)


        def COMMENT(self):
            return self.getToken(ZCodeParser.COMMENT, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 9, 12, 14, 16, 19, 20, 21, 22, 37, 38, 39, 42]:
                self.state = 32
                self.stm()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 33
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 34
                    self.stm()
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [-1, 45]:
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 40
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [43]:
                self.state = 46
                self.match(ZCodeParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 49
            self.match(ZCodeParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_stm)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 58
                self.r_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 59
                self.r_if()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 60
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
        self.enterRule(localctx, 4, self.RULE_r_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
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
        self.enterRule(localctx, 6, self.RULE_r_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
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
        self.enterRule(localctx, 8, self.RULE_r_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ZCodeParser.T__2)
            self.state = 68
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


        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_if




    def r_if(self):

        localctx = ZCodeParser.R_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_r_if)
        self._la = 0 # Token type
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(ZCodeParser.T__3)
                self.state = 71
                self.match(ZCodeParser.T__4)
                self.state = 72
                self.expr(0)
                self.state = 73
                self.match(ZCodeParser.T__5)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 74
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 80
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(ZCodeParser.T__3)
                self.state = 83
                self.match(ZCodeParser.T__4)
                self.state = 84
                self.expr(0)
                self.state = 85
                self.match(ZCodeParser.T__5)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 86
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 91
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 92
                self.stm()
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 93
                        self.match(ZCodeParser.T__6)
                        self.state = 94
                        self.match(ZCodeParser.T__4)
                        self.state = 95
                        self.expr(0)
                        self.state = 96
                        self.match(ZCodeParser.T__5)
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
                        self.stm() 
                    self.state = 109
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 118
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 110
                    self.match(ZCodeParser.T__7)
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==45:
                        self.state = 111
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 116
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 117
                    self.stm()


                pass


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


        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_for




    def r_for(self):

        localctx = ZCodeParser.R_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_r_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ZCodeParser.T__8)
            self.state = 123
            self.expr(0)
            self.state = 124
            self.match(ZCodeParser.T__9)
            self.state = 125
            self.expr(0)
            self.state = 126
            self.match(ZCodeParser.T__10)
            self.state = 127
            self.expr(0)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 128
                self.match(ZCodeParser.NEWLINE)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.stm()
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

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmContext,i)


        def COMMENT(self):
            return self.getToken(ZCodeParser.COMMENT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(ZCodeParser.T__11)
            self.state = 137
            self.match(ZCodeParser.NEWLINE)
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 9, 12, 14, 16, 19, 20, 21, 22, 37, 38, 39, 42]:
                self.state = 138
                self.stm()
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 139
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 140
                        self.stm() 
                    self.state = 145
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass
            elif token in [45]:
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 146
                        self.match(ZCodeParser.NEWLINE) 
                    self.state = 151
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass
            elif token in [43]:
                self.state = 152
                self.match(ZCodeParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 155
            self.match(ZCodeParser.NEWLINE)
            self.state = 156
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
        self.enterRule(localctx, 16, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ZCodeParser.T__13)
            self.state = 159
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 160
            self.args()
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 161
                self.r_return()
                pass
            elif token in [12]:
                self.state = 162
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
        self.enterRule(localctx, 18, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(ZCodeParser.T__4)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 166
                self.match(ZCodeParser.TYPE)
                self.state = 167
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 168
                    self.type_index()


                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 171
                    self.match(ZCodeParser.T__14)
                    self.state = 172
                    self.match(ZCodeParser.TYPE)
                    self.state = 173
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 174
                        self.type_index()


                    self.state = 181
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 184
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
        self.enterRule(localctx, 20, self.RULE_type_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(ZCodeParser.T__15)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 187
                self.match(ZCodeParser.NUMBER)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 188
                    self.match(ZCodeParser.T__14)
                    self.state = 189
                    self.match(ZCodeParser.NUMBER)
                    self.state = 194
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 197
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
        self.enterRule(localctx, 22, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.expr(0)
            self.state = 200
            self.match(ZCodeParser.T__17)
            self.state = 201
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
        self.enterRule(localctx, 24, self.RULE_decl)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(ZCodeParser.TYPE)
                self.state = 204
                self.expr(0)
                self.state = 205
                self.match(ZCodeParser.T__17)
                self.state = 206
                self.expr(0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(ZCodeParser.T__18)
                self.state = 209
                self.expr(0)
                self.state = 210
                self.match(ZCodeParser.T__17)
                self.state = 211
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(ZCodeParser.T__19)
                self.state = 214
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 218
                self.match(ZCodeParser.T__4)
                self.state = 219
                self.expr(0)
                self.state = 220
                self.match(ZCodeParser.T__5)
                pass

            elif la_ == 2:
                self.state = 222
                self.match(ZCodeParser.T__20)
                self.state = 223
                self.expr(6)
                pass

            elif la_ == 3:
                self.state = 224
                self.match(ZCodeParser.T__21)
                self.state = 225
                self.expr(5)
                pass

            elif la_ == 4:
                self.state = 226
                self.expr_without_rel()
                self.state = 227
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17045651456) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 228
                self.expr_without_rel()
                pass

            elif la_ == 5:
                self.state = 230
                self.expr_without_rel()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 264
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 233
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 234
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 235
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 236
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 237
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 238
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 239
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 240
                        self.match(ZCodeParser.T__15)
                        self.state = 241
                        localctx.indexer = self.expr(0)
                        self.state = 246
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 242
                            self.match(ZCodeParser.T__14)
                            self.state = 243
                            localctx.indexer = self.expr(0)
                            self.state = 248
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 249
                        self.match(ZCodeParser.T__16)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 251
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 252
                        self.match(ZCodeParser.T__4)
                        self.state = 261
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                            self.state = 253
                            localctx.param = self.expr(0)
                            self.state = 258
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 254
                                self.match(ZCodeParser.T__14)
                                self.state = 255
                                localctx.param = self.expr(0)
                                self.state = 260
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 263
                        self.match(ZCodeParser.T__5)
                        pass

             
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_expr_without_rel)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.expr_without_str_concat(0)
                self.state = 270
                self.match(ZCodeParser.T__33)
                self.state = 271
                self.expr_without_str_concat(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr_without_str_concat, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 277
                self.match(ZCodeParser.T__15)
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                    self.state = 278
                    self.expr(0)
                    self.state = 283
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==15:
                        self.state = 279
                        self.match(ZCodeParser.T__14)
                        self.state = 280
                        self.expr(0)
                        self.state = 285
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 288
                self.match(ZCodeParser.T__16)
                pass
            elif token in [39]:
                self.state = 289
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [42]:
                self.state = 290
                self.match(ZCodeParser.STRING)
                pass
            elif token in [38]:
                self.state = 291
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [5]:
                self.state = 292
                self.match(ZCodeParser.T__4)
                self.state = 293
                self.expr(0)
                self.state = 294
                self.match(ZCodeParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_without_str_concatContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_without_str_concat)
                    self.state = 298
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 299
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==35 or _la==36):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 300
                    self.expr_without_str_concat(7) 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        self._predicates[13] = self.expr_sempred
        self._predicates[15] = self.expr_without_str_concat_sempred
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
         




