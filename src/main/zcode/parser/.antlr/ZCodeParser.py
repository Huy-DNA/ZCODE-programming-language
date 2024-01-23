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
        4,1,47,331,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,5,0,40,8,0,10,
        0,12,0,43,9,0,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,3,0,52,8,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,2,1,
        2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,5,6,84,8,6,
        10,6,12,6,87,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,96,8,6,10,6,12,
        6,99,9,6,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,1,6,1,6,1,6,1,6,1,
        6,5,6,113,8,6,10,6,12,6,116,9,6,1,6,1,6,5,6,120,8,6,10,6,12,6,123,
        9,6,1,6,5,6,126,8,6,10,6,12,6,129,9,6,1,6,1,6,5,6,133,8,6,10,6,12,
        6,136,9,6,1,6,3,6,139,8,6,3,6,141,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,5,7,150,8,7,10,7,12,7,153,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,
        162,8,8,10,8,12,8,165,9,8,1,8,5,8,168,8,8,10,8,12,8,171,9,8,1,8,
        3,8,174,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,183,8,9,10,9,12,9,186,
        9,9,1,9,1,9,3,9,190,8,9,3,9,192,8,9,1,10,1,10,1,10,1,10,3,10,198,
        8,10,1,10,1,10,1,10,1,10,3,10,204,8,10,5,10,206,8,10,10,10,12,10,
        209,9,10,3,10,211,8,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,219,8,
        11,10,11,12,11,222,9,11,3,11,224,8,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,
        13,244,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,3,14,260,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,276,8,14,10,14,12,14,
        279,9,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,288,8,14,10,14,
        12,14,291,9,14,3,14,293,8,14,1,14,5,14,296,8,14,10,14,12,14,299,
        9,14,1,15,1,15,1,15,1,15,1,15,3,15,306,8,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,316,8,16,1,17,1,17,1,17,1,17,5,17,322,8,
        17,10,17,12,17,325,9,17,3,17,327,8,17,1,17,1,17,1,17,1,121,1,28,
        18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,4,1,0,28,34,
        1,0,24,26,2,0,22,22,27,27,1,0,35,36,370,0,51,1,0,0,0,2,66,1,0,0,
        0,4,68,1,0,0,0,6,71,1,0,0,0,8,73,1,0,0,0,10,75,1,0,0,0,12,140,1,
        0,0,0,14,142,1,0,0,0,16,156,1,0,0,0,18,178,1,0,0,0,20,193,1,0,0,
        0,22,214,1,0,0,0,24,227,1,0,0,0,26,243,1,0,0,0,28,259,1,0,0,0,30,
        305,1,0,0,0,32,315,1,0,0,0,34,317,1,0,0,0,36,41,3,2,1,0,37,38,5,
        46,0,0,38,40,3,2,1,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,
        42,1,0,0,0,42,52,1,0,0,0,43,41,1,0,0,0,44,46,5,46,0,0,45,44,1,0,
        0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,52,1,0,0,0,49,47,
        1,0,0,0,50,52,5,44,0,0,51,36,1,0,0,0,51,47,1,0,0,0,51,50,1,0,0,0,
        52,53,1,0,0,0,53,54,5,0,0,1,54,1,1,0,0,0,55,67,3,28,14,0,56,67,3,
        26,13,0,57,67,3,24,12,0,58,67,3,16,8,0,59,67,3,18,9,0,60,67,3,6,
        3,0,61,67,3,8,4,0,62,67,3,10,5,0,63,67,3,12,6,0,64,67,3,14,7,0,65,
        67,3,4,2,0,66,55,1,0,0,0,66,56,1,0,0,0,66,57,1,0,0,0,66,58,1,0,0,
        0,66,59,1,0,0,0,66,60,1,0,0,0,66,61,1,0,0,0,66,62,1,0,0,0,66,63,
        1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,3,1,0,0,0,68,69,5,1,0,0,69,
        70,3,28,14,0,70,5,1,0,0,0,71,72,5,2,0,0,72,7,1,0,0,0,73,74,5,3,0,
        0,74,9,1,0,0,0,75,76,5,4,0,0,76,77,3,28,14,0,77,11,1,0,0,0,78,79,
        5,5,0,0,79,80,5,6,0,0,80,81,3,28,14,0,81,85,5,7,0,0,82,84,5,46,0,
        0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,
        1,0,0,0,87,85,1,0,0,0,88,89,3,2,1,0,89,141,1,0,0,0,90,91,5,5,0,0,
        91,92,5,6,0,0,92,93,3,28,14,0,93,97,5,7,0,0,94,96,5,46,0,0,95,94,
        1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,
        99,97,1,0,0,0,100,121,3,2,1,0,101,103,5,46,0,0,102,101,1,0,0,0,103,
        106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,
        104,1,0,0,0,107,108,5,8,0,0,108,109,5,6,0,0,109,110,3,28,14,0,110,
        114,5,7,0,0,111,113,5,46,0,0,112,111,1,0,0,0,113,116,1,0,0,0,114,
        112,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,114,1,0,0,0,117,
        118,3,2,1,0,118,120,1,0,0,0,119,104,1,0,0,0,120,123,1,0,0,0,121,
        122,1,0,0,0,121,119,1,0,0,0,122,138,1,0,0,0,123,121,1,0,0,0,124,
        126,5,46,0,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,
        128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,134,5,9,0,0,131,
        133,5,46,0,0,132,131,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,
        135,1,0,0,0,135,137,1,0,0,0,136,134,1,0,0,0,137,139,3,2,1,0,138,
        127,1,0,0,0,138,139,1,0,0,0,139,141,1,0,0,0,140,78,1,0,0,0,140,90,
        1,0,0,0,141,13,1,0,0,0,142,143,5,10,0,0,143,144,3,28,14,0,144,145,
        5,11,0,0,145,146,3,28,14,0,146,147,5,12,0,0,147,151,3,28,14,0,148,
        150,5,46,0,0,149,148,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,
        152,1,0,0,0,152,154,1,0,0,0,153,151,1,0,0,0,154,155,3,2,1,0,155,
        15,1,0,0,0,156,157,5,13,0,0,157,173,5,46,0,0,158,163,3,2,1,0,159,
        160,5,46,0,0,160,162,3,2,1,0,161,159,1,0,0,0,162,165,1,0,0,0,163,
        161,1,0,0,0,163,164,1,0,0,0,164,174,1,0,0,0,165,163,1,0,0,0,166,
        168,5,46,0,0,167,166,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,
        170,1,0,0,0,170,174,1,0,0,0,171,169,1,0,0,0,172,174,5,44,0,0,173,
        158,1,0,0,0,173,169,1,0,0,0,173,172,1,0,0,0,174,175,1,0,0,0,175,
        176,5,46,0,0,176,177,5,14,0,0,177,17,1,0,0,0,178,179,5,15,0,0,179,
        180,5,39,0,0,180,191,3,20,10,0,181,183,5,46,0,0,182,181,1,0,0,0,
        183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,189,1,0,0,0,
        186,184,1,0,0,0,187,190,3,10,5,0,188,190,3,16,8,0,189,187,1,0,0,
        0,189,188,1,0,0,0,190,192,1,0,0,0,191,184,1,0,0,0,191,192,1,0,0,
        0,192,19,1,0,0,0,193,210,5,6,0,0,194,195,5,38,0,0,195,197,5,39,0,
        0,196,198,3,22,11,0,197,196,1,0,0,0,197,198,1,0,0,0,198,207,1,0,
        0,0,199,200,5,16,0,0,200,201,5,38,0,0,201,203,5,39,0,0,202,204,3,
        22,11,0,203,202,1,0,0,0,203,204,1,0,0,0,204,206,1,0,0,0,205,199,
        1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,211,
        1,0,0,0,209,207,1,0,0,0,210,194,1,0,0,0,210,211,1,0,0,0,211,212,
        1,0,0,0,212,213,5,7,0,0,213,21,1,0,0,0,214,223,5,17,0,0,215,220,
        5,40,0,0,216,217,5,16,0,0,217,219,5,40,0,0,218,216,1,0,0,0,219,222,
        1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,224,1,0,0,0,222,220,
        1,0,0,0,223,215,1,0,0,0,223,224,1,0,0,0,224,225,1,0,0,0,225,226,
        5,18,0,0,226,23,1,0,0,0,227,228,3,28,14,0,228,229,5,19,0,0,229,230,
        3,28,14,0,230,25,1,0,0,0,231,232,5,38,0,0,232,233,3,28,14,0,233,
        234,5,19,0,0,234,235,3,28,14,0,235,244,1,0,0,0,236,237,5,20,0,0,
        237,238,3,28,14,0,238,239,5,19,0,0,239,240,3,28,14,0,240,244,1,0,
        0,0,241,242,5,21,0,0,242,244,3,28,14,0,243,231,1,0,0,0,243,236,1,
        0,0,0,243,241,1,0,0,0,244,27,1,0,0,0,245,246,6,14,-1,0,246,247,5,
        6,0,0,247,248,3,28,14,0,248,249,5,7,0,0,249,260,1,0,0,0,250,251,
        5,22,0,0,251,260,3,28,14,7,252,253,5,23,0,0,253,260,3,28,14,6,254,
        255,3,30,15,0,255,256,7,0,0,0,256,257,3,30,15,0,257,260,1,0,0,0,
        258,260,3,30,15,0,259,245,1,0,0,0,259,250,1,0,0,0,259,252,1,0,0,
        0,259,254,1,0,0,0,259,258,1,0,0,0,260,297,1,0,0,0,261,262,10,5,0,
        0,262,263,7,1,0,0,263,296,3,28,14,6,264,265,10,4,0,0,265,266,7,2,
        0,0,266,296,3,28,14,5,267,268,10,1,0,0,268,269,7,3,0,0,269,296,3,
        28,14,2,270,271,10,9,0,0,271,272,5,17,0,0,272,277,3,28,14,0,273,
        274,5,16,0,0,274,276,3,28,14,0,275,273,1,0,0,0,276,279,1,0,0,0,277,
        275,1,0,0,0,277,278,1,0,0,0,278,280,1,0,0,0,279,277,1,0,0,0,280,
        281,5,18,0,0,281,296,1,0,0,0,282,283,10,8,0,0,283,292,5,6,0,0,284,
        289,3,28,14,0,285,286,5,16,0,0,286,288,3,28,14,0,287,285,1,0,0,0,
        288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,293,1,0,0,0,
        291,289,1,0,0,0,292,284,1,0,0,0,292,293,1,0,0,0,293,294,1,0,0,0,
        294,296,5,7,0,0,295,261,1,0,0,0,295,264,1,0,0,0,295,267,1,0,0,0,
        295,270,1,0,0,0,295,282,1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,
        297,298,1,0,0,0,298,29,1,0,0,0,299,297,1,0,0,0,300,301,3,32,16,0,
        301,302,5,37,0,0,302,303,3,32,16,0,303,306,1,0,0,0,304,306,3,32,
        16,0,305,300,1,0,0,0,305,304,1,0,0,0,306,31,1,0,0,0,307,316,3,34,
        17,0,308,316,5,40,0,0,309,316,5,43,0,0,310,316,5,39,0,0,311,312,
        5,6,0,0,312,313,3,28,14,0,313,314,5,7,0,0,314,316,1,0,0,0,315,307,
        1,0,0,0,315,308,1,0,0,0,315,309,1,0,0,0,315,310,1,0,0,0,315,311,
        1,0,0,0,316,33,1,0,0,0,317,326,5,17,0,0,318,323,3,28,14,0,319,320,
        5,16,0,0,320,322,3,28,14,0,321,319,1,0,0,0,322,325,1,0,0,0,323,321,
        1,0,0,0,323,324,1,0,0,0,324,327,1,0,0,0,325,323,1,0,0,0,326,318,
        1,0,0,0,326,327,1,0,0,0,327,328,1,0,0,0,328,329,5,18,0,0,329,35,
        1,0,0,0,37,41,47,51,66,85,97,104,114,121,127,134,138,140,151,163,
        169,173,184,189,191,197,203,207,210,220,223,243,259,277,289,292,
        295,297,305,315,323,326
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'break'", "'continue'", "'return'", 
                     "'if'", "'('", "')'", "'elif'", "'else'", "'for'", 
                     "'until'", "'by'", "'begin'", "'end'", "'func'", "','", 
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
    RULE_expr_without_rel = 15
    RULE_expr_without_str_concat = 16
    RULE_r_list = 17

    ruleNames =  [ "program", "stm", "print", "r_break", "r_continue", "r_return", 
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
            if token in [1, 2, 3, 4, 5, 6, 10, 13, 15, 17, 20, 21, 22, 23, 38, 39, 40, 43]:
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
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(ZCodeParser.T__4)
                self.state = 79
                self.match(ZCodeParser.T__5)
                self.state = 80
                self.expr(0)
                self.state = 81
                self.match(ZCodeParser.T__6)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 82
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 88
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(ZCodeParser.T__4)
                self.state = 91
                self.match(ZCodeParser.T__5)
                self.state = 92
                self.expr(0)
                self.state = 93
                self.match(ZCodeParser.T__6)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 94
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 100
                self.stm()
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 104
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==46:
                            self.state = 101
                            self.match(ZCodeParser.NEWLINE)
                            self.state = 106
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 107
                        self.match(ZCodeParser.T__7)
                        self.state = 108
                        self.match(ZCodeParser.T__5)
                        self.state = 109
                        self.expr(0)
                        self.state = 110
                        self.match(ZCodeParser.T__6)
                        self.state = 114
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==46:
                            self.state = 111
                            self.match(ZCodeParser.NEWLINE)
                            self.state = 116
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 117
                        self.stm() 
                    self.state = 123
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 138
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==46:
                        self.state = 124
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 129
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 130
                    self.match(ZCodeParser.T__8)
                    self.state = 134
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==46:
                        self.state = 131
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 136
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 137
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
            self.state = 142
            self.match(ZCodeParser.T__9)
            self.state = 143
            self.expr(0)
            self.state = 144
            self.match(ZCodeParser.T__10)
            self.state = 145
            self.expr(0)
            self.state = 146
            self.match(ZCodeParser.T__11)
            self.state = 147
            self.expr(0)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 148
                self.match(ZCodeParser.NEWLINE)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
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
            self.state = 156
            self.match(ZCodeParser.T__12)
            self.state = 157
            self.match(ZCodeParser.NEWLINE)
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 10, 13, 15, 17, 20, 21, 22, 23, 38, 39, 40, 43]:
                self.state = 158
                self.stm()
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 159
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 160
                        self.stm() 
                    self.state = 165
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass
            elif token in [46]:
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 166
                        self.match(ZCodeParser.NEWLINE) 
                    self.state = 171
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass
            elif token in [44]:
                self.state = 172
                self.match(ZCodeParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 175
            self.match(ZCodeParser.NEWLINE)
            self.state = 176
            self.match(ZCodeParser.T__13)
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
            self.state = 178
            self.match(ZCodeParser.T__14)
            self.state = 179
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 180
            self.args()
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 181
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 189
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 187
                    self.r_return()
                    pass
                elif token in [13]:
                    self.state = 188
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
            self.state = 193
            self.match(ZCodeParser.T__5)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
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


                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 199
                    self.match(ZCodeParser.T__15)
                    self.state = 200
                    self.match(ZCodeParser.TYPE)
                    self.state = 201
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 203
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==17:
                        self.state = 202
                        self.type_index()


                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 212
            self.match(ZCodeParser.T__6)
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
            self.state = 214
            self.match(ZCodeParser.T__16)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 215
                self.match(ZCodeParser.NUMBER)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 216
                    self.match(ZCodeParser.T__15)
                    self.state = 217
                    self.match(ZCodeParser.NUMBER)
                    self.state = 222
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 225
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
            self.state = 227
            self.expr(0)
            self.state = 228
            self.match(ZCodeParser.T__18)
            self.state = 229
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
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(ZCodeParser.TYPE)
                self.state = 232
                self.expr(0)
                self.state = 233
                self.match(ZCodeParser.T__18)
                self.state = 234
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(ZCodeParser.T__19)
                self.state = 237
                self.expr(0)
                self.state = 238
                self.match(ZCodeParser.T__18)
                self.state = 239
                self.expr(0)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.match(ZCodeParser.T__20)
                self.state = 242
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
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 246
                self.match(ZCodeParser.T__5)
                self.state = 247
                self.expr(0)
                self.state = 248
                self.match(ZCodeParser.T__6)
                pass

            elif la_ == 2:
                self.state = 250
                self.match(ZCodeParser.T__21)
                self.state = 251
                self.expr(7)
                pass

            elif la_ == 3:
                self.state = 252
                self.match(ZCodeParser.T__22)
                self.state = 253
                self.expr(6)
                pass

            elif la_ == 4:
                self.state = 254
                self.expr_without_rel()
                self.state = 255
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34091302912) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 256
                self.expr_without_rel()
                pass

            elif la_ == 5:
                self.state = 258
                self.expr_without_rel()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 295
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 261
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 262
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 263
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 264
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 265
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 266
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 267
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 268
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 269
                        self.expr(2)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 270
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 271
                        self.match(ZCodeParser.T__16)
                        self.state = 272
                        localctx.indexer = self.expr(0)
                        self.state = 277
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==16:
                            self.state = 273
                            self.match(ZCodeParser.T__15)
                            self.state = 274
                            localctx.indexer = self.expr(0)
                            self.state = 279
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 280
                        self.match(ZCodeParser.T__17)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 282
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 283
                        self.match(ZCodeParser.T__5)
                        self.state = 292
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445373177920) != 0):
                            self.state = 284
                            localctx.param = self.expr(0)
                            self.state = 289
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==16:
                                self.state = 285
                                self.match(ZCodeParser.T__15)
                                self.state = 286
                                localctx.param = self.expr(0)
                                self.state = 291
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 294
                        self.match(ZCodeParser.T__6)
                        pass

             
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.expr_without_str_concat()
                self.state = 301
                self.match(ZCodeParser.T__36)
                self.state = 302
                self.expr_without_str_concat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
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
        self.enterRule(localctx, 32, self.RULE_expr_without_str_concat)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.r_list()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.match(ZCodeParser.STRING)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 310
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 311
                self.match(ZCodeParser.T__5)
                self.state = 312
                self.expr(0)
                self.state = 313
                self.match(ZCodeParser.T__6)
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
            self.state = 317
            self.match(ZCodeParser.T__16)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445373177920) != 0):
                self.state = 318
                self.expr(0)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 319
                    self.match(ZCodeParser.T__15)
                    self.state = 320
                    self.expr(0)
                    self.state = 325
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 328
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
         




