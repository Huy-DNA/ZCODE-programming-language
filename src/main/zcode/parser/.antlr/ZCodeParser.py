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
        4,1,46,323,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        1,8,1,8,1,8,5,8,177,8,8,10,8,12,8,180,9,8,1,8,1,8,3,8,184,8,8,1,
        9,1,9,1,9,1,9,3,9,190,8,9,1,9,1,9,1,9,1,9,3,9,196,8,9,5,9,198,8,
        9,10,9,12,9,201,9,9,3,9,203,8,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,
        211,8,10,10,10,12,10,214,9,10,3,10,216,8,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,3,12,236,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,3,13,252,8,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,268,8,13,10,13,
        12,13,271,9,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,280,8,13,
        10,13,12,13,283,9,13,3,13,285,8,13,1,13,5,13,288,8,13,10,13,12,13,
        291,9,13,1,14,1,14,1,14,1,14,1,14,3,14,298,8,14,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,3,15,308,8,15,1,16,1,16,1,16,1,16,5,16,314,
        8,16,10,16,12,16,317,9,16,3,16,319,8,16,1,16,1,16,1,16,1,115,1,26,
        17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,4,1,0,27,33,1,
        0,23,25,2,0,21,21,26,26,1,0,34,35,361,0,49,1,0,0,0,2,63,1,0,0,0,
        4,65,1,0,0,0,6,67,1,0,0,0,8,69,1,0,0,0,10,134,1,0,0,0,12,136,1,0,
        0,0,14,150,1,0,0,0,16,172,1,0,0,0,18,185,1,0,0,0,20,206,1,0,0,0,
        22,219,1,0,0,0,24,235,1,0,0,0,26,251,1,0,0,0,28,297,1,0,0,0,30,307,
        1,0,0,0,32,309,1,0,0,0,34,39,3,2,1,0,35,36,5,45,0,0,36,38,3,2,1,
        0,37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,50,
        1,0,0,0,41,39,1,0,0,0,42,44,5,45,0,0,43,42,1,0,0,0,44,47,1,0,0,0,
        45,43,1,0,0,0,45,46,1,0,0,0,46,50,1,0,0,0,47,45,1,0,0,0,48,50,5,
        43,0,0,49,34,1,0,0,0,49,45,1,0,0,0,49,48,1,0,0,0,50,51,1,0,0,0,51,
        52,5,0,0,1,52,1,1,0,0,0,53,64,3,26,13,0,54,64,3,24,12,0,55,64,3,
        22,11,0,56,64,3,14,7,0,57,64,3,16,8,0,58,64,3,4,2,0,59,64,3,6,3,
        0,60,64,3,8,4,0,61,64,3,10,5,0,62,64,3,12,6,0,63,53,1,0,0,0,63,54,
        1,0,0,0,63,55,1,0,0,0,63,56,1,0,0,0,63,57,1,0,0,0,63,58,1,0,0,0,
        63,59,1,0,0,0,63,60,1,0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,64,3,1,0,
        0,0,65,66,5,1,0,0,66,5,1,0,0,0,67,68,5,2,0,0,68,7,1,0,0,0,69,70,
        5,3,0,0,70,71,3,26,13,0,71,9,1,0,0,0,72,73,5,4,0,0,73,74,5,5,0,0,
        74,75,3,26,13,0,75,79,5,6,0,0,76,78,5,45,0,0,77,76,1,0,0,0,78,81,
        1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,
        82,83,3,2,1,0,83,135,1,0,0,0,84,85,5,4,0,0,85,86,5,5,0,0,86,87,3,
        26,13,0,87,91,5,6,0,0,88,90,5,45,0,0,89,88,1,0,0,0,90,93,1,0,0,0,
        91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,1,0,0,0,94,115,3,
        2,1,0,95,97,5,45,0,0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,
        98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,102,5,7,0,0,102,
        103,5,5,0,0,103,104,3,26,13,0,104,108,5,6,0,0,105,107,5,45,0,0,106,
        105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,
        111,1,0,0,0,110,108,1,0,0,0,111,112,3,2,1,0,112,114,1,0,0,0,113,
        98,1,0,0,0,114,117,1,0,0,0,115,116,1,0,0,0,115,113,1,0,0,0,116,132,
        1,0,0,0,117,115,1,0,0,0,118,120,5,45,0,0,119,118,1,0,0,0,120,123,
        1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,
        1,0,0,0,124,128,5,8,0,0,125,127,5,45,0,0,126,125,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,128,
        1,0,0,0,131,133,3,2,1,0,132,121,1,0,0,0,132,133,1,0,0,0,133,135,
        1,0,0,0,134,72,1,0,0,0,134,84,1,0,0,0,135,11,1,0,0,0,136,137,5,9,
        0,0,137,138,3,26,13,0,138,139,5,10,0,0,139,140,3,26,13,0,140,141,
        5,11,0,0,141,145,3,26,13,0,142,144,5,45,0,0,143,142,1,0,0,0,144,
        147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,
        145,1,0,0,0,148,149,3,2,1,0,149,13,1,0,0,0,150,151,5,12,0,0,151,
        167,5,45,0,0,152,157,3,2,1,0,153,154,5,45,0,0,154,156,3,2,1,0,155,
        153,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,
        168,1,0,0,0,159,157,1,0,0,0,160,162,5,45,0,0,161,160,1,0,0,0,162,
        165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,168,1,0,0,0,165,
        163,1,0,0,0,166,168,5,43,0,0,167,152,1,0,0,0,167,163,1,0,0,0,167,
        166,1,0,0,0,168,169,1,0,0,0,169,170,5,45,0,0,170,171,5,13,0,0,171,
        15,1,0,0,0,172,173,5,14,0,0,173,174,5,38,0,0,174,178,3,18,9,0,175,
        177,5,45,0,0,176,175,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,
        179,1,0,0,0,179,183,1,0,0,0,180,178,1,0,0,0,181,184,3,8,4,0,182,
        184,3,14,7,0,183,181,1,0,0,0,183,182,1,0,0,0,184,17,1,0,0,0,185,
        202,5,5,0,0,186,187,5,37,0,0,187,189,5,38,0,0,188,190,3,20,10,0,
        189,188,1,0,0,0,189,190,1,0,0,0,190,199,1,0,0,0,191,192,5,15,0,0,
        192,193,5,37,0,0,193,195,5,38,0,0,194,196,3,20,10,0,195,194,1,0,
        0,0,195,196,1,0,0,0,196,198,1,0,0,0,197,191,1,0,0,0,198,201,1,0,
        0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,203,1,0,0,0,201,199,1,0,
        0,0,202,186,1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,205,5,6,
        0,0,205,19,1,0,0,0,206,215,5,16,0,0,207,212,5,39,0,0,208,209,5,15,
        0,0,209,211,5,39,0,0,210,208,1,0,0,0,211,214,1,0,0,0,212,210,1,0,
        0,0,212,213,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,215,207,1,0,
        0,0,215,216,1,0,0,0,216,217,1,0,0,0,217,218,5,17,0,0,218,21,1,0,
        0,0,219,220,3,26,13,0,220,221,5,18,0,0,221,222,3,26,13,0,222,23,
        1,0,0,0,223,224,5,37,0,0,224,225,3,26,13,0,225,226,5,18,0,0,226,
        227,3,26,13,0,227,236,1,0,0,0,228,229,5,19,0,0,229,230,3,26,13,0,
        230,231,5,18,0,0,231,232,3,26,13,0,232,236,1,0,0,0,233,234,5,20,
        0,0,234,236,3,26,13,0,235,223,1,0,0,0,235,228,1,0,0,0,235,233,1,
        0,0,0,236,25,1,0,0,0,237,238,6,13,-1,0,238,239,5,5,0,0,239,240,3,
        26,13,0,240,241,5,6,0,0,241,252,1,0,0,0,242,243,5,21,0,0,243,252,
        3,26,13,7,244,245,5,22,0,0,245,252,3,26,13,6,246,247,3,28,14,0,247,
        248,7,0,0,0,248,249,3,28,14,0,249,252,1,0,0,0,250,252,3,28,14,0,
        251,237,1,0,0,0,251,242,1,0,0,0,251,244,1,0,0,0,251,246,1,0,0,0,
        251,250,1,0,0,0,252,289,1,0,0,0,253,254,10,5,0,0,254,255,7,1,0,0,
        255,288,3,26,13,6,256,257,10,4,0,0,257,258,7,2,0,0,258,288,3,26,
        13,5,259,260,10,1,0,0,260,261,7,3,0,0,261,288,3,26,13,2,262,263,
        10,9,0,0,263,264,5,16,0,0,264,269,3,26,13,0,265,266,5,15,0,0,266,
        268,3,26,13,0,267,265,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,
        270,1,0,0,0,270,272,1,0,0,0,271,269,1,0,0,0,272,273,5,17,0,0,273,
        288,1,0,0,0,274,275,10,8,0,0,275,284,5,5,0,0,276,281,3,26,13,0,277,
        278,5,15,0,0,278,280,3,26,13,0,279,277,1,0,0,0,280,283,1,0,0,0,281,
        279,1,0,0,0,281,282,1,0,0,0,282,285,1,0,0,0,283,281,1,0,0,0,284,
        276,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,288,5,6,0,0,287,
        253,1,0,0,0,287,256,1,0,0,0,287,259,1,0,0,0,287,262,1,0,0,0,287,
        274,1,0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,
        27,1,0,0,0,291,289,1,0,0,0,292,293,3,30,15,0,293,294,5,36,0,0,294,
        295,3,30,15,0,295,298,1,0,0,0,296,298,3,30,15,0,297,292,1,0,0,0,
        297,296,1,0,0,0,298,29,1,0,0,0,299,308,3,32,16,0,300,308,5,39,0,
        0,301,308,5,42,0,0,302,308,5,38,0,0,303,304,5,5,0,0,304,305,3,26,
        13,0,305,306,5,6,0,0,306,308,1,0,0,0,307,299,1,0,0,0,307,300,1,0,
        0,0,307,301,1,0,0,0,307,302,1,0,0,0,307,303,1,0,0,0,308,31,1,0,0,
        0,309,318,5,16,0,0,310,315,3,26,13,0,311,312,5,15,0,0,312,314,3,
        26,13,0,313,311,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,315,316,
        1,0,0,0,316,319,1,0,0,0,317,315,1,0,0,0,318,310,1,0,0,0,318,319,
        1,0,0,0,319,320,1,0,0,0,320,321,5,17,0,0,321,33,1,0,0,0,36,39,45,
        49,63,79,91,98,108,115,121,128,132,134,145,157,163,167,178,183,189,
        195,199,202,212,215,235,251,269,281,284,287,289,297,307,315,318
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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func




    def func(self):

        localctx = ZCodeParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ZCodeParser.T__13)
            self.state = 173
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 174
            self.args()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 175
                self.match(ZCodeParser.NEWLINE)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 181
                self.r_return()
                pass
            elif token in [12]:
                self.state = 182
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
            self.state = 185
            self.match(ZCodeParser.T__4)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
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


                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 191
                    self.match(ZCodeParser.T__14)
                    self.state = 192
                    self.match(ZCodeParser.TYPE)
                    self.state = 193
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 195
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 194
                        self.type_index()


                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 204
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
            self.state = 206
            self.match(ZCodeParser.T__15)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 207
                self.match(ZCodeParser.NUMBER)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 208
                    self.match(ZCodeParser.T__14)
                    self.state = 209
                    self.match(ZCodeParser.NUMBER)
                    self.state = 214
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 217
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
            self.state = 219
            self.expr(0)
            self.state = 220
            self.match(ZCodeParser.T__17)
            self.state = 221
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
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(ZCodeParser.TYPE)
                self.state = 224
                self.expr(0)
                self.state = 225
                self.match(ZCodeParser.T__17)
                self.state = 226
                self.expr(0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(ZCodeParser.T__18)
                self.state = 229
                self.expr(0)
                self.state = 230
                self.match(ZCodeParser.T__17)
                self.state = 231
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.match(ZCodeParser.T__19)
                self.state = 234
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
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 238
                self.match(ZCodeParser.T__4)
                self.state = 239
                self.expr(0)
                self.state = 240
                self.match(ZCodeParser.T__5)
                pass

            elif la_ == 2:
                self.state = 242
                self.match(ZCodeParser.T__20)
                self.state = 243
                self.expr(7)
                pass

            elif la_ == 3:
                self.state = 244
                self.match(ZCodeParser.T__21)
                self.state = 245
                self.expr(6)
                pass

            elif la_ == 4:
                self.state = 246
                self.expr_without_rel()
                self.state = 247
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17045651456) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 248
                self.expr_without_rel()
                pass

            elif la_ == 5:
                self.state = 250
                self.expr_without_rel()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 287
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 253
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 254
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 255
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 256
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 257
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 258
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 259
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 260
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==34 or _la==35):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 261
                        self.expr(2)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 262
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 263
                        self.match(ZCodeParser.T__15)
                        self.state = 264
                        localctx.indexer = self.expr(0)
                        self.state = 269
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 265
                            self.match(ZCodeParser.T__14)
                            self.state = 266
                            localctx.indexer = self.expr(0)
                            self.state = 271
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 272
                        self.match(ZCodeParser.T__16)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 274
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 275
                        self.match(ZCodeParser.T__4)
                        self.state = 284
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                            self.state = 276
                            localctx.param = self.expr(0)
                            self.state = 281
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 277
                                self.match(ZCodeParser.T__14)
                                self.state = 278
                                localctx.param = self.expr(0)
                                self.state = 283
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 286
                        self.match(ZCodeParser.T__5)
                        pass

             
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.expr_without_str_concat()
                self.state = 293
                self.match(ZCodeParser.T__35)
                self.state = 294
                self.expr_without_str_concat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
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
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.r_list()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 301
                self.match(ZCodeParser.STRING)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 4)
                self.state = 302
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 303
                self.match(ZCodeParser.T__4)
                self.state = 304
                self.expr(0)
                self.state = 305
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
            self.state = 309
            self.match(ZCodeParser.T__15)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                self.state = 310
                self.expr(0)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 311
                    self.match(ZCodeParser.T__14)
                    self.state = 312
                    self.expr(0)
                    self.state = 317
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 320
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
         




