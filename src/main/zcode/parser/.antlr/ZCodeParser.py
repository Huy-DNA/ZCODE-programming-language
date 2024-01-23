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
        4,1,46,317,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,5,0,38,8,0,10,0,12,0,41,
        9,0,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,3,0,50,8,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,64,8,1,1,2,1,2,1,3,1,3,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,5,5,90,8,5,10,5,12,5,93,9,5,1,5,1,5,5,5,97,8,
        5,10,5,12,5,100,9,5,1,5,1,5,1,5,1,5,1,5,5,5,107,8,5,10,5,12,5,110,
        9,5,1,5,1,5,5,5,114,8,5,10,5,12,5,117,9,5,1,5,5,5,120,8,5,10,5,12,
        5,123,9,5,1,5,1,5,5,5,127,8,5,10,5,12,5,130,9,5,1,5,3,5,133,8,5,
        3,5,135,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,144,8,6,10,6,12,6,147,
        9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,156,8,7,10,7,12,7,159,9,7,1,
        7,5,7,162,8,7,10,7,12,7,165,9,7,1,7,3,7,168,8,7,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,3,8,178,8,8,1,9,1,9,1,9,1,9,3,9,184,8,9,1,9,1,9,
        1,9,1,9,3,9,190,8,9,5,9,192,8,9,10,9,12,9,195,9,9,3,9,197,8,9,1,
        9,1,9,1,10,1,10,1,10,1,10,5,10,205,8,10,10,10,12,10,208,9,10,3,10,
        210,8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,230,8,12,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,246,
        8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,262,8,13,10,13,12,13,265,9,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,5,13,274,8,13,10,13,12,13,277,9,13,3,13,279,8,13,
        1,13,5,13,282,8,13,10,13,12,13,285,9,13,1,14,1,14,1,14,1,14,1,14,
        3,14,292,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,302,8,
        15,1,16,1,16,1,16,1,16,5,16,308,8,16,10,16,12,16,311,9,16,3,16,313,
        8,16,1,16,1,16,1,16,1,115,1,26,17,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,0,4,1,0,27,33,1,0,23,25,2,0,21,21,26,26,1,0,34,35,
        354,0,49,1,0,0,0,2,63,1,0,0,0,4,65,1,0,0,0,6,67,1,0,0,0,8,69,1,0,
        0,0,10,134,1,0,0,0,12,136,1,0,0,0,14,150,1,0,0,0,16,172,1,0,0,0,
        18,179,1,0,0,0,20,200,1,0,0,0,22,213,1,0,0,0,24,229,1,0,0,0,26,245,
        1,0,0,0,28,291,1,0,0,0,30,301,1,0,0,0,32,303,1,0,0,0,34,39,3,2,1,
        0,35,36,5,45,0,0,36,38,3,2,1,0,37,35,1,0,0,0,38,41,1,0,0,0,39,37,
        1,0,0,0,39,40,1,0,0,0,40,50,1,0,0,0,41,39,1,0,0,0,42,44,5,45,0,0,
        43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,50,1,
        0,0,0,47,45,1,0,0,0,48,50,5,43,0,0,49,34,1,0,0,0,49,45,1,0,0,0,49,
        48,1,0,0,0,50,51,1,0,0,0,51,52,5,0,0,1,52,1,1,0,0,0,53,64,3,26,13,
        0,54,64,3,24,12,0,55,64,3,22,11,0,56,64,3,14,7,0,57,64,3,16,8,0,
        58,64,3,4,2,0,59,64,3,6,3,0,60,64,3,8,4,0,61,64,3,10,5,0,62,64,3,
        12,6,0,63,53,1,0,0,0,63,54,1,0,0,0,63,55,1,0,0,0,63,56,1,0,0,0,63,
        57,1,0,0,0,63,58,1,0,0,0,63,59,1,0,0,0,63,60,1,0,0,0,63,61,1,0,0,
        0,63,62,1,0,0,0,64,3,1,0,0,0,65,66,5,1,0,0,66,5,1,0,0,0,67,68,5,
        2,0,0,68,7,1,0,0,0,69,70,5,3,0,0,70,71,3,26,13,0,71,9,1,0,0,0,72,
        73,5,4,0,0,73,74,5,5,0,0,74,75,3,26,13,0,75,79,5,6,0,0,76,78,5,45,
        0,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,
        1,0,0,0,81,79,1,0,0,0,82,83,3,2,1,0,83,135,1,0,0,0,84,85,5,4,0,0,
        85,86,5,5,0,0,86,87,3,26,13,0,87,91,5,6,0,0,88,90,5,45,0,0,89,88,
        1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,
        93,91,1,0,0,0,94,115,3,2,1,0,95,97,5,45,0,0,96,95,1,0,0,0,97,100,
        1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,
        0,101,102,5,7,0,0,102,103,5,5,0,0,103,104,3,26,13,0,104,108,5,6,
        0,0,105,107,5,45,0,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,
        0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,112,3,2,
        1,0,112,114,1,0,0,0,113,98,1,0,0,0,114,117,1,0,0,0,115,116,1,0,0,
        0,115,113,1,0,0,0,116,132,1,0,0,0,117,115,1,0,0,0,118,120,5,45,0,
        0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,
        0,122,124,1,0,0,0,123,121,1,0,0,0,124,128,5,8,0,0,125,127,5,45,0,
        0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,
        0,129,131,1,0,0,0,130,128,1,0,0,0,131,133,3,2,1,0,132,121,1,0,0,
        0,132,133,1,0,0,0,133,135,1,0,0,0,134,72,1,0,0,0,134,84,1,0,0,0,
        135,11,1,0,0,0,136,137,5,9,0,0,137,138,3,26,13,0,138,139,5,10,0,
        0,139,140,3,26,13,0,140,141,5,11,0,0,141,145,3,26,13,0,142,144,5,
        45,0,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,
        0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,149,3,2,1,0,149,13,1,0,
        0,0,150,151,5,12,0,0,151,167,5,45,0,0,152,157,3,2,1,0,153,154,5,
        45,0,0,154,156,3,2,1,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,1,
        0,0,0,157,158,1,0,0,0,158,168,1,0,0,0,159,157,1,0,0,0,160,162,5,
        45,0,0,161,160,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,
        0,0,0,164,168,1,0,0,0,165,163,1,0,0,0,166,168,5,43,0,0,167,152,1,
        0,0,0,167,163,1,0,0,0,167,166,1,0,0,0,168,169,1,0,0,0,169,170,5,
        45,0,0,170,171,5,13,0,0,171,15,1,0,0,0,172,173,5,14,0,0,173,174,
        5,38,0,0,174,177,3,18,9,0,175,178,3,8,4,0,176,178,3,14,7,0,177,175,
        1,0,0,0,177,176,1,0,0,0,178,17,1,0,0,0,179,196,5,5,0,0,180,181,5,
        37,0,0,181,183,5,38,0,0,182,184,3,20,10,0,183,182,1,0,0,0,183,184,
        1,0,0,0,184,193,1,0,0,0,185,186,5,15,0,0,186,187,5,37,0,0,187,189,
        5,38,0,0,188,190,3,20,10,0,189,188,1,0,0,0,189,190,1,0,0,0,190,192,
        1,0,0,0,191,185,1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,
        1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,196,180,1,0,0,0,196,197,
        1,0,0,0,197,198,1,0,0,0,198,199,5,6,0,0,199,19,1,0,0,0,200,209,5,
        16,0,0,201,206,5,39,0,0,202,203,5,15,0,0,203,205,5,39,0,0,204,202,
        1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,210,
        1,0,0,0,208,206,1,0,0,0,209,201,1,0,0,0,209,210,1,0,0,0,210,211,
        1,0,0,0,211,212,5,17,0,0,212,21,1,0,0,0,213,214,3,26,13,0,214,215,
        5,18,0,0,215,216,3,26,13,0,216,23,1,0,0,0,217,218,5,37,0,0,218,219,
        3,26,13,0,219,220,5,18,0,0,220,221,3,26,13,0,221,230,1,0,0,0,222,
        223,5,19,0,0,223,224,3,26,13,0,224,225,5,18,0,0,225,226,3,26,13,
        0,226,230,1,0,0,0,227,228,5,20,0,0,228,230,3,26,13,0,229,217,1,0,
        0,0,229,222,1,0,0,0,229,227,1,0,0,0,230,25,1,0,0,0,231,232,6,13,
        -1,0,232,233,5,5,0,0,233,234,3,26,13,0,234,235,5,6,0,0,235,246,1,
        0,0,0,236,237,5,21,0,0,237,246,3,26,13,7,238,239,5,22,0,0,239,246,
        3,26,13,6,240,241,3,28,14,0,241,242,7,0,0,0,242,243,3,28,14,0,243,
        246,1,0,0,0,244,246,3,28,14,0,245,231,1,0,0,0,245,236,1,0,0,0,245,
        238,1,0,0,0,245,240,1,0,0,0,245,244,1,0,0,0,246,283,1,0,0,0,247,
        248,10,5,0,0,248,249,7,1,0,0,249,282,3,26,13,6,250,251,10,4,0,0,
        251,252,7,2,0,0,252,282,3,26,13,5,253,254,10,1,0,0,254,255,7,3,0,
        0,255,282,3,26,13,2,256,257,10,9,0,0,257,258,5,16,0,0,258,263,3,
        26,13,0,259,260,5,15,0,0,260,262,3,26,13,0,261,259,1,0,0,0,262,265,
        1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,266,1,0,0,0,265,263,
        1,0,0,0,266,267,5,17,0,0,267,282,1,0,0,0,268,269,10,8,0,0,269,278,
        5,5,0,0,270,275,3,26,13,0,271,272,5,15,0,0,272,274,3,26,13,0,273,
        271,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,
        279,1,0,0,0,277,275,1,0,0,0,278,270,1,0,0,0,278,279,1,0,0,0,279,
        280,1,0,0,0,280,282,5,6,0,0,281,247,1,0,0,0,281,250,1,0,0,0,281,
        253,1,0,0,0,281,256,1,0,0,0,281,268,1,0,0,0,282,285,1,0,0,0,283,
        281,1,0,0,0,283,284,1,0,0,0,284,27,1,0,0,0,285,283,1,0,0,0,286,287,
        3,30,15,0,287,288,5,36,0,0,288,289,3,30,15,0,289,292,1,0,0,0,290,
        292,3,30,15,0,291,286,1,0,0,0,291,290,1,0,0,0,292,29,1,0,0,0,293,
        302,3,32,16,0,294,302,5,39,0,0,295,302,5,42,0,0,296,302,5,38,0,0,
        297,298,5,5,0,0,298,299,3,26,13,0,299,300,5,6,0,0,300,302,1,0,0,
        0,301,293,1,0,0,0,301,294,1,0,0,0,301,295,1,0,0,0,301,296,1,0,0,
        0,301,297,1,0,0,0,302,31,1,0,0,0,303,312,5,16,0,0,304,309,3,26,13,
        0,305,306,5,15,0,0,306,308,3,26,13,0,307,305,1,0,0,0,308,311,1,0,
        0,0,309,307,1,0,0,0,309,310,1,0,0,0,310,313,1,0,0,0,311,309,1,0,
        0,0,312,304,1,0,0,0,312,313,1,0,0,0,313,314,1,0,0,0,314,315,5,17,
        0,0,315,33,1,0,0,0,35,39,45,49,63,79,91,98,108,115,121,128,132,134,
        145,157,163,167,177,183,189,193,196,206,209,229,245,263,275,278,
        281,283,291,301,309,312
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
                     "'<'", "'>'", "'<='", "'>='", "'and'", "'or'", "'...'" ]

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
    RULE_r_list = 16

    ruleNames =  [ "program", "stm", "r_break", "r_continue", "r_return", 
                   "r_if", "r_for", "block", "func", "args", "type_index", 
                   "ass", "decl", "expr", "expr_without_rel", "expr_without_str_concat", 
                   "r_list" ]

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
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 9, 12, 14, 16, 19, 20, 21, 22, 37, 38, 39, 42]:
                self.state = 34
                self.stm()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 35
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 36
                    self.stm()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [-1, 45]:
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 42
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [43]:
                self.state = 48
                self.match(ZCodeParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 51
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
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 59
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 60
                self.r_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 61
                self.r_if()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 62
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
            self.state = 65
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
            self.state = 67
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
            self.state = 69
            self.match(ZCodeParser.T__2)
            self.state = 70
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
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(ZCodeParser.T__3)
                self.state = 73
                self.match(ZCodeParser.T__4)
                self.state = 74
                self.expr(0)
                self.state = 75
                self.match(ZCodeParser.T__5)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 76
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 82
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(ZCodeParser.T__3)
                self.state = 85
                self.match(ZCodeParser.T__4)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(ZCodeParser.T__5)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 88
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 94
                self.stm()
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 98
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==45:
                            self.state = 95
                            self.match(ZCodeParser.NEWLINE)
                            self.state = 100
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 101
                        self.match(ZCodeParser.T__6)
                        self.state = 102
                        self.match(ZCodeParser.T__4)
                        self.state = 103
                        self.expr(0)
                        self.state = 104
                        self.match(ZCodeParser.T__5)
                        self.state = 108
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==45:
                            self.state = 105
                            self.match(ZCodeParser.NEWLINE)
                            self.state = 110
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 111
                        self.stm() 
                    self.state = 117
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 132
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==45:
                        self.state = 118
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 123
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 124
                    self.match(ZCodeParser.T__7)
                    self.state = 128
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==45:
                        self.state = 125
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 130
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 131
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
            self.state = 136
            self.match(ZCodeParser.T__8)
            self.state = 137
            self.expr(0)
            self.state = 138
            self.match(ZCodeParser.T__9)
            self.state = 139
            self.expr(0)
            self.state = 140
            self.match(ZCodeParser.T__10)
            self.state = 141
            self.expr(0)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 142
                self.match(ZCodeParser.NEWLINE)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
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
            self.state = 150
            self.match(ZCodeParser.T__11)
            self.state = 151
            self.match(ZCodeParser.NEWLINE)
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 9, 12, 14, 16, 19, 20, 21, 22, 37, 38, 39, 42]:
                self.state = 152
                self.stm()
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 153
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 154
                        self.stm() 
                    self.state = 159
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass
            elif token in [45]:
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 160
                        self.match(ZCodeParser.NEWLINE) 
                    self.state = 165
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass
            elif token in [43]:
                self.state = 166
                self.match(ZCodeParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 169
            self.match(ZCodeParser.NEWLINE)
            self.state = 170
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
            self.state = 172
            self.match(ZCodeParser.T__13)
            self.state = 173
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 174
            self.args()
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 175
                self.r_return()
                pass
            elif token in [12]:
                self.state = 176
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
            self.state = 179
            self.match(ZCodeParser.T__4)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 180
                self.match(ZCodeParser.TYPE)
                self.state = 181
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 182
                    self.type_index()


                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 185
                    self.match(ZCodeParser.T__14)
                    self.state = 186
                    self.match(ZCodeParser.TYPE)
                    self.state = 187
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 189
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 188
                        self.type_index()


                    self.state = 195
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 198
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
            self.state = 200
            self.match(ZCodeParser.T__15)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 201
                self.match(ZCodeParser.NUMBER)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 202
                    self.match(ZCodeParser.T__14)
                    self.state = 203
                    self.match(ZCodeParser.NUMBER)
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 211
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
            self.state = 213
            self.expr(0)
            self.state = 214
            self.match(ZCodeParser.T__17)
            self.state = 215
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
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(ZCodeParser.TYPE)
                self.state = 218
                self.expr(0)
                self.state = 219
                self.match(ZCodeParser.T__17)
                self.state = 220
                self.expr(0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(ZCodeParser.T__18)
                self.state = 223
                self.expr(0)
                self.state = 224
                self.match(ZCodeParser.T__17)
                self.state = 225
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(ZCodeParser.T__19)
                self.state = 228
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
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 232
                self.match(ZCodeParser.T__4)
                self.state = 233
                self.expr(0)
                self.state = 234
                self.match(ZCodeParser.T__5)
                pass

            elif la_ == 2:
                self.state = 236
                self.match(ZCodeParser.T__20)
                self.state = 237
                self.expr(7)
                pass

            elif la_ == 3:
                self.state = 238
                self.match(ZCodeParser.T__21)
                self.state = 239
                self.expr(6)
                pass

            elif la_ == 4:
                self.state = 240
                self.expr_without_rel()
                self.state = 241
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17045651456) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.expr_without_rel()
                pass

            elif la_ == 5:
                self.state = 244
                self.expr_without_rel()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 281
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 247
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 248
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 249
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 250
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 251
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 252
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 253
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 254
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==34 or _la==35):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 255
                        self.expr(2)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 256
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 257
                        self.match(ZCodeParser.T__15)
                        self.state = 258
                        localctx.indexer = self.expr(0)
                        self.state = 263
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 259
                            self.match(ZCodeParser.T__14)
                            self.state = 260
                            localctx.indexer = self.expr(0)
                            self.state = 265
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 266
                        self.match(ZCodeParser.T__16)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 268
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 269
                        self.match(ZCodeParser.T__4)
                        self.state = 278
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                            self.state = 270
                            localctx.param = self.expr(0)
                            self.state = 275
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 271
                                self.match(ZCodeParser.T__14)
                                self.state = 272
                                localctx.param = self.expr(0)
                                self.state = 277
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 280
                        self.match(ZCodeParser.T__5)
                        pass

             
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.expr_without_str_concat()
                self.state = 287
                self.match(ZCodeParser.T__35)
                self.state = 288
                self.expr_without_str_concat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.expr_without_str_concat()
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

        def r_list(self):
            return self.getTypedRuleContext(ZCodeParser.R_listContext,0)


        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_without_str_concat




    def expr_without_str_concat(self):

        localctx = ZCodeParser.Expr_without_str_concatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_without_str_concat)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.r_list()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.match(ZCodeParser.STRING)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 4)
                self.state = 296
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 297
                self.match(ZCodeParser.T__4)
                self.state = 298
                self.expr(0)
                self.state = 299
                self.match(ZCodeParser.T__5)
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


    class R_listContext(ParserRuleContext):
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
            return ZCodeParser.RULE_r_list




    def r_list(self):

        localctx = ZCodeParser.R_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_r_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.T__15)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                self.state = 304
                self.expr(0)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 305
                    self.match(ZCodeParser.T__14)
                    self.state = 306
                    self.expr(0)
                    self.state = 311
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 314
            self.match(ZCodeParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         




