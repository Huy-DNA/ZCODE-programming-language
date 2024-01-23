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
        4,1,47,325,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,5,0,40,8,0,10,
        0,12,0,43,9,0,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,3,0,52,8,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,2,1,
        2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,5,6,82,8,6,10,6,12,
        6,85,9,6,1,6,1,6,1,6,1,6,1,6,5,6,92,8,6,10,6,12,6,95,9,6,1,6,1,6,
        5,6,99,8,6,10,6,12,6,102,9,6,1,6,1,6,1,6,5,6,107,8,6,10,6,12,6,110,
        9,6,1,6,1,6,5,6,114,8,6,10,6,12,6,117,9,6,1,6,5,6,120,8,6,10,6,12,
        6,123,9,6,1,6,1,6,5,6,127,8,6,10,6,12,6,130,9,6,1,6,3,6,133,8,6,
        3,6,135,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,144,8,7,10,7,12,7,147,
        9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,156,8,8,10,8,12,8,159,9,8,1,
        8,5,8,162,8,8,10,8,12,8,165,9,8,1,8,3,8,168,8,8,1,8,1,8,1,8,1,9,
        1,9,1,9,1,9,5,9,177,8,9,10,9,12,9,180,9,9,1,9,1,9,3,9,184,8,9,3,
        9,186,8,9,1,10,1,10,1,10,1,10,3,10,192,8,10,1,10,1,10,1,10,1,10,
        3,10,198,8,10,5,10,200,8,10,10,10,12,10,203,9,10,3,10,205,8,10,1,
        10,1,10,1,11,1,11,1,11,1,11,5,11,213,8,11,10,11,12,11,216,9,11,3,
        11,218,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,238,8,13,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,254,
        8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,5,14,270,8,14,10,14,12,14,273,9,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,5,14,282,8,14,10,14,12,14,285,9,14,3,14,287,8,14,
        1,14,5,14,290,8,14,10,14,12,14,293,9,14,1,15,1,15,1,15,1,15,1,15,
        3,15,300,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,310,8,
        16,1,17,1,17,1,17,1,17,5,17,316,8,17,10,17,12,17,319,9,17,3,17,321,
        8,17,1,17,1,17,1,17,1,115,1,28,18,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,0,4,1,0,28,34,1,0,24,26,2,0,22,22,27,27,1,0,35,
        36,364,0,51,1,0,0,0,2,66,1,0,0,0,4,68,1,0,0,0,6,71,1,0,0,0,8,73,
        1,0,0,0,10,75,1,0,0,0,12,134,1,0,0,0,14,136,1,0,0,0,16,150,1,0,0,
        0,18,172,1,0,0,0,20,187,1,0,0,0,22,208,1,0,0,0,24,221,1,0,0,0,26,
        237,1,0,0,0,28,253,1,0,0,0,30,299,1,0,0,0,32,309,1,0,0,0,34,311,
        1,0,0,0,36,41,3,2,1,0,37,38,5,46,0,0,38,40,3,2,1,0,39,37,1,0,0,0,
        40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,52,1,0,0,0,43,41,1,
        0,0,0,44,46,5,46,0,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,
        48,1,0,0,0,48,52,1,0,0,0,49,47,1,0,0,0,50,52,5,44,0,0,51,36,1,0,
        0,0,51,47,1,0,0,0,51,50,1,0,0,0,52,53,1,0,0,0,53,54,5,0,0,1,54,1,
        1,0,0,0,55,67,3,28,14,0,56,67,3,26,13,0,57,67,3,24,12,0,58,67,3,
        16,8,0,59,67,3,18,9,0,60,67,3,6,3,0,61,67,3,8,4,0,62,67,3,10,5,0,
        63,67,3,12,6,0,64,67,3,14,7,0,65,67,3,4,2,0,66,55,1,0,0,0,66,56,
        1,0,0,0,66,57,1,0,0,0,66,58,1,0,0,0,66,59,1,0,0,0,66,60,1,0,0,0,
        66,61,1,0,0,0,66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,
        0,0,0,67,3,1,0,0,0,68,69,5,1,0,0,69,70,3,28,14,0,70,5,1,0,0,0,71,
        72,5,2,0,0,72,7,1,0,0,0,73,74,5,3,0,0,74,9,1,0,0,0,75,76,5,4,0,0,
        76,77,3,28,14,0,77,11,1,0,0,0,78,79,5,5,0,0,79,83,3,28,14,0,80,82,
        5,46,0,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,
        84,86,1,0,0,0,85,83,1,0,0,0,86,87,3,2,1,0,87,135,1,0,0,0,88,89,5,
        5,0,0,89,93,3,28,14,0,90,92,5,46,0,0,91,90,1,0,0,0,92,95,1,0,0,0,
        93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,115,3,
        2,1,0,97,99,5,46,0,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,
        100,101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,5,6,0,0,
        104,108,3,28,14,0,105,107,5,46,0,0,106,105,1,0,0,0,107,110,1,0,0,
        0,108,106,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,
        0,111,112,3,2,1,0,112,114,1,0,0,0,113,100,1,0,0,0,114,117,1,0,0,
        0,115,116,1,0,0,0,115,113,1,0,0,0,116,132,1,0,0,0,117,115,1,0,0,
        0,118,120,5,46,0,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,
        0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,128,5,7,0,
        0,125,127,5,46,0,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,
        0,128,129,1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,133,3,2,1,
        0,132,121,1,0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,78,1,0,0,0,
        134,88,1,0,0,0,135,13,1,0,0,0,136,137,5,8,0,0,137,138,3,28,14,0,
        138,139,5,9,0,0,139,140,3,28,14,0,140,141,5,10,0,0,141,145,3,28,
        14,0,142,144,5,46,0,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,1,
        0,0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,149,3,
        2,1,0,149,15,1,0,0,0,150,151,5,11,0,0,151,167,5,46,0,0,152,157,3,
        2,1,0,153,154,5,46,0,0,154,156,3,2,1,0,155,153,1,0,0,0,156,159,1,
        0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,168,1,0,0,0,159,157,1,
        0,0,0,160,162,5,46,0,0,161,160,1,0,0,0,162,165,1,0,0,0,163,161,1,
        0,0,0,163,164,1,0,0,0,164,168,1,0,0,0,165,163,1,0,0,0,166,168,5,
        44,0,0,167,152,1,0,0,0,167,163,1,0,0,0,167,166,1,0,0,0,168,169,1,
        0,0,0,169,170,5,46,0,0,170,171,5,12,0,0,171,17,1,0,0,0,172,173,5,
        13,0,0,173,174,5,39,0,0,174,185,3,20,10,0,175,177,5,46,0,0,176,175,
        1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,183,
        1,0,0,0,180,178,1,0,0,0,181,184,3,10,5,0,182,184,3,16,8,0,183,181,
        1,0,0,0,183,182,1,0,0,0,184,186,1,0,0,0,185,178,1,0,0,0,185,186,
        1,0,0,0,186,19,1,0,0,0,187,204,5,14,0,0,188,189,5,38,0,0,189,191,
        5,39,0,0,190,192,3,22,11,0,191,190,1,0,0,0,191,192,1,0,0,0,192,201,
        1,0,0,0,193,194,5,15,0,0,194,195,5,38,0,0,195,197,5,39,0,0,196,198,
        3,22,11,0,197,196,1,0,0,0,197,198,1,0,0,0,198,200,1,0,0,0,199,193,
        1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,205,
        1,0,0,0,203,201,1,0,0,0,204,188,1,0,0,0,204,205,1,0,0,0,205,206,
        1,0,0,0,206,207,5,16,0,0,207,21,1,0,0,0,208,217,5,17,0,0,209,214,
        5,40,0,0,210,211,5,15,0,0,211,213,5,40,0,0,212,210,1,0,0,0,213,216,
        1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,218,1,0,0,0,216,214,
        1,0,0,0,217,209,1,0,0,0,217,218,1,0,0,0,218,219,1,0,0,0,219,220,
        5,18,0,0,220,23,1,0,0,0,221,222,3,28,14,0,222,223,5,19,0,0,223,224,
        3,28,14,0,224,25,1,0,0,0,225,226,5,38,0,0,226,227,3,28,14,0,227,
        228,5,19,0,0,228,229,3,28,14,0,229,238,1,0,0,0,230,231,5,20,0,0,
        231,232,3,28,14,0,232,233,5,19,0,0,233,234,3,28,14,0,234,238,1,0,
        0,0,235,236,5,21,0,0,236,238,3,28,14,0,237,225,1,0,0,0,237,230,1,
        0,0,0,237,235,1,0,0,0,238,27,1,0,0,0,239,240,6,14,-1,0,240,241,5,
        14,0,0,241,242,3,28,14,0,242,243,5,16,0,0,243,254,1,0,0,0,244,245,
        5,22,0,0,245,254,3,28,14,7,246,247,5,23,0,0,247,254,3,28,14,6,248,
        249,3,30,15,0,249,250,7,0,0,0,250,251,3,30,15,0,251,254,1,0,0,0,
        252,254,3,30,15,0,253,239,1,0,0,0,253,244,1,0,0,0,253,246,1,0,0,
        0,253,248,1,0,0,0,253,252,1,0,0,0,254,291,1,0,0,0,255,256,10,5,0,
        0,256,257,7,1,0,0,257,290,3,28,14,6,258,259,10,4,0,0,259,260,7,2,
        0,0,260,290,3,28,14,5,261,262,10,1,0,0,262,263,7,3,0,0,263,290,3,
        28,14,2,264,265,10,9,0,0,265,266,5,17,0,0,266,271,3,28,14,0,267,
        268,5,15,0,0,268,270,3,28,14,0,269,267,1,0,0,0,270,273,1,0,0,0,271,
        269,1,0,0,0,271,272,1,0,0,0,272,274,1,0,0,0,273,271,1,0,0,0,274,
        275,5,18,0,0,275,290,1,0,0,0,276,277,10,8,0,0,277,286,5,14,0,0,278,
        283,3,28,14,0,279,280,5,15,0,0,280,282,3,28,14,0,281,279,1,0,0,0,
        282,285,1,0,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,287,1,0,0,0,
        285,283,1,0,0,0,286,278,1,0,0,0,286,287,1,0,0,0,287,288,1,0,0,0,
        288,290,5,16,0,0,289,255,1,0,0,0,289,258,1,0,0,0,289,261,1,0,0,0,
        289,264,1,0,0,0,289,276,1,0,0,0,290,293,1,0,0,0,291,289,1,0,0,0,
        291,292,1,0,0,0,292,29,1,0,0,0,293,291,1,0,0,0,294,295,3,32,16,0,
        295,296,5,37,0,0,296,297,3,32,16,0,297,300,1,0,0,0,298,300,3,32,
        16,0,299,294,1,0,0,0,299,298,1,0,0,0,300,31,1,0,0,0,301,310,3,34,
        17,0,302,310,5,40,0,0,303,310,5,43,0,0,304,310,5,39,0,0,305,306,
        5,14,0,0,306,307,3,28,14,0,307,308,5,16,0,0,308,310,1,0,0,0,309,
        301,1,0,0,0,309,302,1,0,0,0,309,303,1,0,0,0,309,304,1,0,0,0,309,
        305,1,0,0,0,310,33,1,0,0,0,311,320,5,17,0,0,312,317,3,28,14,0,313,
        314,5,15,0,0,314,316,3,28,14,0,315,313,1,0,0,0,316,319,1,0,0,0,317,
        315,1,0,0,0,317,318,1,0,0,0,318,321,1,0,0,0,319,317,1,0,0,0,320,
        312,1,0,0,0,320,321,1,0,0,0,321,322,1,0,0,0,322,323,5,18,0,0,323,
        35,1,0,0,0,37,41,47,51,66,83,93,100,108,115,121,128,132,134,145,
        157,163,167,178,183,185,191,197,201,204,214,217,237,253,271,283,
        286,289,291,299,309,317,320
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'break'", "'continue'", "'return'", 
                     "'if'", "'elif'", "'else'", "'for'", "'until'", "'by'", 
                     "'begin'", "'end'", "'func'", "'('", "','", "')'", 
                     "'['", "']'", "'<-'", "'var'", "'dynamic'", "'-'", 
                     "'not'", "'*'", "'/'", "'%'", "'+'", "'='", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'and'", "'or'", 
                     "'...'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "TYPE", "IDENTIFIER", "NUMBER", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRING", "COMMENT", 
                      "WS", "NEWLINE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_stm = 1
    RULE_print = 2
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
    RULE_concat_expr = 15
    RULE_operand = 16
    RULE_r_list = 17

    ruleNames =  [ "program", "stm", "print", "r_break", "r_continue", "r_return", 
                   "r_if", "r_for", "block", "func", "args", "type_index", 
                   "ass", "decl", "expr", "concat_expr", "operand", "r_list" ]

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
    T__36=37
    TYPE=38
    IDENTIFIER=39
    NUMBER=40
    ILLEGAL_ESCAPE=41
    UNCLOSE_STRING=42
    STRING=43
    COMMENT=44
    WS=45
    NEWLINE=46
    ERROR_CHAR=47

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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 8, 11, 13, 14, 17, 20, 21, 22, 23, 38, 39, 40, 43]:
                self.state = 36
                self.stm()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 37
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 38
                    self.stm()
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [-1, 46]:
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 44
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [44]:
                self.state = 50
                self.match(ZCodeParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 53
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


        def print_(self):
            return self.getTypedRuleContext(ZCodeParser.PrintContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm




    def stm(self):

        localctx = ZCodeParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stm)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 61
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 62
                self.r_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 63
                self.r_if()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 64
                self.r_for()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 65
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_print




    def print_(self):

        localctx = ZCodeParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ZCodeParser.T__0)
            self.state = 69
            self.expr(0)
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
            self.state = 71
            self.match(ZCodeParser.T__1)
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
            self.state = 73
            self.match(ZCodeParser.T__2)
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
            self.state = 75
            self.match(ZCodeParser.T__3)
            self.state = 76
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
        self.enterRule(localctx, 12, self.RULE_r_if)
        self._la = 0 # Token type
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(ZCodeParser.T__4)
                self.state = 79
                self.expr(0)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 80
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(ZCodeParser.T__4)
                self.state = 89
                self.expr(0)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 90
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 96
                self.stm()
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 100
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==46:
                            self.state = 97
                            self.match(ZCodeParser.NEWLINE)
                            self.state = 102
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 103
                        self.match(ZCodeParser.T__5)
                        self.state = 104
                        self.expr(0)
                        self.state = 108
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==46:
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
                    while _la==46:
                        self.state = 118
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 123
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 124
                    self.match(ZCodeParser.T__6)
                    self.state = 128
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==46:
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
        self.enterRule(localctx, 14, self.RULE_r_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(ZCodeParser.T__7)
            self.state = 137
            self.expr(0)
            self.state = 138
            self.match(ZCodeParser.T__8)
            self.state = 139
            self.expr(0)
            self.state = 140
            self.match(ZCodeParser.T__9)
            self.state = 141
            self.expr(0)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
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
        self.enterRule(localctx, 16, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ZCodeParser.T__10)
            self.state = 151
            self.match(ZCodeParser.NEWLINE)
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 8, 11, 13, 14, 17, 20, 21, 22, 23, 38, 39, 40, 43]:
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
            elif token in [46]:
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
            elif token in [44]:
                self.state = 166
                self.match(ZCodeParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 169
            self.match(ZCodeParser.NEWLINE)
            self.state = 170
            self.match(ZCodeParser.T__11)
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
        self.enterRule(localctx, 18, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ZCodeParser.T__12)
            self.state = 173
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 174
            self.args()
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 175
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 180
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 183
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 181
                    self.r_return()
                    pass
                elif token in [11]:
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
        self.enterRule(localctx, 20, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(ZCodeParser.T__13)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 188
                self.match(ZCodeParser.TYPE)
                self.state = 189
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 190
                    self.type_index()


                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 193
                    self.match(ZCodeParser.T__14)
                    self.state = 194
                    self.match(ZCodeParser.TYPE)
                    self.state = 195
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 197
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==17:
                        self.state = 196
                        self.type_index()


                    self.state = 203
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 206
            self.match(ZCodeParser.T__15)
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
            self.state = 208
            self.match(ZCodeParser.T__16)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 209
                self.match(ZCodeParser.NUMBER)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 210
                    self.match(ZCodeParser.T__14)
                    self.state = 211
                    self.match(ZCodeParser.NUMBER)
                    self.state = 216
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 219
            self.match(ZCodeParser.T__17)
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
            self.state = 221
            self.expr(0)
            self.state = 222
            self.match(ZCodeParser.T__18)
            self.state = 223
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
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(ZCodeParser.TYPE)
                self.state = 226
                self.expr(0)
                self.state = 227
                self.match(ZCodeParser.T__18)
                self.state = 228
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(ZCodeParser.T__19)
                self.state = 231
                self.expr(0)
                self.state = 232
                self.match(ZCodeParser.T__18)
                self.state = 233
                self.expr(0)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.match(ZCodeParser.T__20)
                self.state = 236
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


        def concat_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Concat_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Concat_exprContext,i)


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
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 240
                self.match(ZCodeParser.T__13)
                self.state = 241
                self.expr(0)
                self.state = 242
                self.match(ZCodeParser.T__15)
                pass

            elif la_ == 2:
                self.state = 244
                self.match(ZCodeParser.T__21)
                self.state = 245
                self.expr(7)
                pass

            elif la_ == 3:
                self.state = 246
                self.match(ZCodeParser.T__22)
                self.state = 247
                self.expr(6)
                pass

            elif la_ == 4:
                self.state = 248
                self.concat_expr()
                self.state = 249
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34091302912) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 250
                self.concat_expr()
                pass

            elif la_ == 5:
                self.state = 252
                self.concat_expr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 289
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 255
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 256
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 257
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 258
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 259
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 260
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 261
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 262
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 263
                        self.expr(2)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 264
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 265
                        self.match(ZCodeParser.T__16)
                        self.state = 266
                        localctx.indexer = self.expr(0)
                        self.state = 271
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 267
                            self.match(ZCodeParser.T__14)
                            self.state = 268
                            localctx.indexer = self.expr(0)
                            self.state = 273
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 274
                        self.match(ZCodeParser.T__17)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 276
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 277
                        self.match(ZCodeParser.T__13)
                        self.state = 286
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445373194240) != 0):
                            self.state = 278
                            localctx.param = self.expr(0)
                            self.state = 283
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 279
                                self.match(ZCodeParser.T__14)
                                self.state = 280
                                localctx.param = self.expr(0)
                                self.state = 285
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 288
                        self.match(ZCodeParser.T__15)
                        pass

             
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Concat_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.OperandContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.OperandContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_concat_expr




    def concat_expr(self):

        localctx = ZCodeParser.Concat_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_concat_expr)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.operand()
                self.state = 295
                self.match(ZCodeParser.T__36)
                self.state = 296
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
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
            return ZCodeParser.RULE_operand




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_operand)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.r_list()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(ZCodeParser.STRING)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 304
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 305
                self.match(ZCodeParser.T__13)
                self.state = 306
                self.expr(0)
                self.state = 307
                self.match(ZCodeParser.T__15)
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
        self.enterRule(localctx, 34, self.RULE_r_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(ZCodeParser.T__16)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445373194240) != 0):
                self.state = 312
                self.expr(0)
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 313
                    self.match(ZCodeParser.T__14)
                    self.state = 314
                    self.expr(0)
                    self.state = 319
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 322
            self.match(ZCodeParser.T__17)
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
        self._predicates[14] = self.expr_sempred
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
         




