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
        4,1,48,319,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,3,0,38,8,0,1,0,1,0,3,
        0,42,8,0,1,0,5,0,45,8,0,10,0,12,0,48,9,0,3,0,50,8,0,1,0,3,0,53,8,
        0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,68,8,1,
        1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,5,6,83,8,6,10,
        6,12,6,86,9,6,1,6,1,6,1,6,1,6,1,6,5,6,93,8,6,10,6,12,6,96,9,6,1,
        6,1,6,5,6,100,8,6,10,6,12,6,103,9,6,1,6,1,6,1,6,5,6,108,8,6,10,6,
        12,6,111,9,6,1,6,1,6,5,6,115,8,6,10,6,12,6,118,9,6,1,6,5,6,121,8,
        6,10,6,12,6,124,9,6,1,6,1,6,5,6,128,8,6,10,6,12,6,131,9,6,1,6,3,
        6,134,8,6,3,6,136,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,145,8,7,10,
        7,12,7,148,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,157,8,8,10,8,12,8,
        160,9,8,3,8,162,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,171,8,9,10,9,
        12,9,174,9,9,1,9,1,9,3,9,178,8,9,3,9,180,8,9,1,10,1,10,1,10,1,10,
        3,10,186,8,10,1,10,1,10,1,10,1,10,3,10,192,8,10,5,10,194,8,10,10,
        10,12,10,197,9,10,3,10,199,8,10,1,10,1,10,1,11,1,11,1,11,1,11,5,
        11,207,8,11,10,11,12,11,210,9,11,3,11,212,8,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,232,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,3,14,248,8,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,264,8,14,10,
        14,12,14,267,9,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,276,8,
        14,10,14,12,14,279,9,14,3,14,281,8,14,1,14,5,14,284,8,14,10,14,12,
        14,287,9,14,1,15,1,15,1,15,1,15,1,15,3,15,294,8,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,3,16,304,8,16,1,17,1,17,1,17,1,17,5,17,
        310,8,17,10,17,12,17,313,9,17,3,17,315,8,17,1,17,1,17,1,17,1,116,
        1,28,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,4,1,0,
        28,34,1,0,24,26,2,0,22,22,27,27,1,0,35,36,357,0,37,1,0,0,0,2,67,
        1,0,0,0,4,69,1,0,0,0,6,72,1,0,0,0,8,74,1,0,0,0,10,76,1,0,0,0,12,
        135,1,0,0,0,14,137,1,0,0,0,16,151,1,0,0,0,18,166,1,0,0,0,20,181,
        1,0,0,0,22,202,1,0,0,0,24,215,1,0,0,0,26,231,1,0,0,0,28,247,1,0,
        0,0,30,293,1,0,0,0,32,303,1,0,0,0,34,305,1,0,0,0,36,38,5,44,0,0,
        37,36,1,0,0,0,37,38,1,0,0,0,38,49,1,0,0,0,39,46,3,2,1,0,40,42,5,
        44,0,0,41,40,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,45,3,2,1,0,44,
        41,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,50,1,0,0,
        0,48,46,1,0,0,0,49,39,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,53,
        5,44,0,0,52,51,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,0,0,1,
        55,1,1,0,0,0,56,68,3,28,14,0,57,68,3,26,13,0,58,68,3,24,12,0,59,
        68,3,16,8,0,60,68,3,18,9,0,61,68,3,6,3,0,62,68,3,8,4,0,63,68,3,10,
        5,0,64,68,3,12,6,0,65,68,3,14,7,0,66,68,3,4,2,0,67,56,1,0,0,0,67,
        57,1,0,0,0,67,58,1,0,0,0,67,59,1,0,0,0,67,60,1,0,0,0,67,61,1,0,0,
        0,67,62,1,0,0,0,67,63,1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,
        1,0,0,0,68,3,1,0,0,0,69,70,5,1,0,0,70,71,3,28,14,0,71,5,1,0,0,0,
        72,73,5,2,0,0,73,7,1,0,0,0,74,75,5,3,0,0,75,9,1,0,0,0,76,77,5,4,
        0,0,77,78,3,28,14,0,78,11,1,0,0,0,79,80,5,5,0,0,80,84,3,28,14,0,
        81,83,5,44,0,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,
        0,0,0,85,87,1,0,0,0,86,84,1,0,0,0,87,88,3,2,1,0,88,136,1,0,0,0,89,
        90,5,5,0,0,90,94,3,28,14,0,91,93,5,44,0,0,92,91,1,0,0,0,93,96,1,
        0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,
        116,3,2,1,0,98,100,5,44,0,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,
        1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,101,1,0,0,0,104,105,
        5,6,0,0,105,109,3,28,14,0,106,108,5,44,0,0,107,106,1,0,0,0,108,111,
        1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,109,
        1,0,0,0,112,113,3,2,1,0,113,115,1,0,0,0,114,101,1,0,0,0,115,118,
        1,0,0,0,116,117,1,0,0,0,116,114,1,0,0,0,117,133,1,0,0,0,118,116,
        1,0,0,0,119,121,5,44,0,0,120,119,1,0,0,0,121,124,1,0,0,0,122,120,
        1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,122,1,0,0,0,125,129,
        5,7,0,0,126,128,5,44,0,0,127,126,1,0,0,0,128,131,1,0,0,0,129,127,
        1,0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,129,1,0,0,0,132,134,
        3,2,1,0,133,122,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,79,1,
        0,0,0,135,89,1,0,0,0,136,13,1,0,0,0,137,138,5,8,0,0,138,139,3,28,
        14,0,139,140,5,9,0,0,140,141,3,28,14,0,141,142,5,10,0,0,142,146,
        3,28,14,0,143,145,5,44,0,0,144,143,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,146,1,0,0,0,149,150,
        3,2,1,0,150,15,1,0,0,0,151,152,5,11,0,0,152,161,5,44,0,0,153,158,
        3,2,1,0,154,155,5,44,0,0,155,157,3,2,1,0,156,154,1,0,0,0,157,160,
        1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,162,1,0,0,0,160,158,
        1,0,0,0,161,153,1,0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,164,
        5,44,0,0,164,165,5,12,0,0,165,17,1,0,0,0,166,167,5,13,0,0,167,168,
        5,39,0,0,168,179,3,20,10,0,169,171,5,44,0,0,170,169,1,0,0,0,171,
        174,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,177,1,0,0,0,174,
        172,1,0,0,0,175,178,3,10,5,0,176,178,3,16,8,0,177,175,1,0,0,0,177,
        176,1,0,0,0,178,180,1,0,0,0,179,172,1,0,0,0,179,180,1,0,0,0,180,
        19,1,0,0,0,181,198,5,14,0,0,182,183,5,38,0,0,183,185,5,39,0,0,184,
        186,3,22,11,0,185,184,1,0,0,0,185,186,1,0,0,0,186,195,1,0,0,0,187,
        188,5,15,0,0,188,189,5,38,0,0,189,191,5,39,0,0,190,192,3,22,11,0,
        191,190,1,0,0,0,191,192,1,0,0,0,192,194,1,0,0,0,193,187,1,0,0,0,
        194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,199,1,0,0,0,
        197,195,1,0,0,0,198,182,1,0,0,0,198,199,1,0,0,0,199,200,1,0,0,0,
        200,201,5,16,0,0,201,21,1,0,0,0,202,211,5,17,0,0,203,208,5,40,0,
        0,204,205,5,15,0,0,205,207,5,40,0,0,206,204,1,0,0,0,207,210,1,0,
        0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,212,1,0,0,0,210,208,1,0,
        0,0,211,203,1,0,0,0,211,212,1,0,0,0,212,213,1,0,0,0,213,214,5,18,
        0,0,214,23,1,0,0,0,215,216,3,28,14,0,216,217,5,19,0,0,217,218,3,
        28,14,0,218,25,1,0,0,0,219,220,5,38,0,0,220,221,3,28,14,0,221,222,
        5,19,0,0,222,223,3,28,14,0,223,232,1,0,0,0,224,225,5,20,0,0,225,
        226,3,28,14,0,226,227,5,19,0,0,227,228,3,28,14,0,228,232,1,0,0,0,
        229,230,5,21,0,0,230,232,3,28,14,0,231,219,1,0,0,0,231,224,1,0,0,
        0,231,229,1,0,0,0,232,27,1,0,0,0,233,234,6,14,-1,0,234,235,5,14,
        0,0,235,236,3,28,14,0,236,237,5,16,0,0,237,248,1,0,0,0,238,239,5,
        22,0,0,239,248,3,28,14,7,240,241,5,23,0,0,241,248,3,28,14,6,242,
        243,3,30,15,0,243,244,7,0,0,0,244,245,3,30,15,0,245,248,1,0,0,0,
        246,248,3,30,15,0,247,233,1,0,0,0,247,238,1,0,0,0,247,240,1,0,0,
        0,247,242,1,0,0,0,247,246,1,0,0,0,248,285,1,0,0,0,249,250,10,5,0,
        0,250,251,7,1,0,0,251,284,3,28,14,6,252,253,10,4,0,0,253,254,7,2,
        0,0,254,284,3,28,14,5,255,256,10,1,0,0,256,257,7,3,0,0,257,284,3,
        28,14,2,258,259,10,9,0,0,259,260,5,17,0,0,260,265,3,28,14,0,261,
        262,5,15,0,0,262,264,3,28,14,0,263,261,1,0,0,0,264,267,1,0,0,0,265,
        263,1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,265,1,0,0,0,268,
        269,5,18,0,0,269,284,1,0,0,0,270,271,10,8,0,0,271,280,5,14,0,0,272,
        277,3,28,14,0,273,274,5,15,0,0,274,276,3,28,14,0,275,273,1,0,0,0,
        276,279,1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,281,1,0,0,0,
        279,277,1,0,0,0,280,272,1,0,0,0,280,281,1,0,0,0,281,282,1,0,0,0,
        282,284,5,16,0,0,283,249,1,0,0,0,283,252,1,0,0,0,283,255,1,0,0,0,
        283,258,1,0,0,0,283,270,1,0,0,0,284,287,1,0,0,0,285,283,1,0,0,0,
        285,286,1,0,0,0,286,29,1,0,0,0,287,285,1,0,0,0,288,289,3,32,16,0,
        289,290,5,37,0,0,290,291,3,32,16,0,291,294,1,0,0,0,292,294,3,32,
        16,0,293,288,1,0,0,0,293,292,1,0,0,0,294,31,1,0,0,0,295,304,3,34,
        17,0,296,304,5,40,0,0,297,304,5,43,0,0,298,304,5,39,0,0,299,300,
        5,14,0,0,300,301,3,28,14,0,301,302,5,16,0,0,302,304,1,0,0,0,303,
        295,1,0,0,0,303,296,1,0,0,0,303,297,1,0,0,0,303,298,1,0,0,0,303,
        299,1,0,0,0,304,33,1,0,0,0,305,314,5,17,0,0,306,311,3,28,14,0,307,
        308,5,15,0,0,308,310,3,28,14,0,309,307,1,0,0,0,310,313,1,0,0,0,311,
        309,1,0,0,0,311,312,1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,314,
        306,1,0,0,0,314,315,1,0,0,0,315,316,1,0,0,0,316,317,5,18,0,0,317,
        35,1,0,0,0,38,37,41,46,49,52,67,84,94,101,109,116,122,129,133,135,
        146,158,161,172,177,179,185,191,195,198,208,211,231,247,265,277,
        280,283,285,293,303,311,314
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
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRING", "NULL_LINES", 
                      "COMMENT", "WS", "NEWLINE", "ERROR_CHAR" ]

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
    NULL_LINES=44
    COMMENT=45
    WS=46
    NEWLINE=47
    ERROR_CHAR=48

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

        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmContext,i)


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
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 36
                self.match(ZCodeParser.NULL_LINES)


            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10720254257470) != 0):
                self.state = 39
                self.stm()
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 41
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==44:
                            self.state = 40
                            self.match(ZCodeParser.NULL_LINES)


                        self.state = 43
                        self.stm() 
                    self.state = 48
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)



            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 51
                self.match(ZCodeParser.NULL_LINES)


            self.state = 54
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
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 63
                self.r_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 64
                self.r_if()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 65
                self.r_for()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 66
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
            self.state = 69
            self.match(ZCodeParser.T__0)
            self.state = 70
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
            self.state = 72
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
            self.state = 74
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
            self.state = 76
            self.match(ZCodeParser.T__3)
            self.state = 77
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


        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_if




    def r_if(self):

        localctx = ZCodeParser.R_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_r_if)
        self._la = 0 # Token type
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(ZCodeParser.T__4)
                self.state = 80
                self.expr(0)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 81
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(ZCodeParser.T__4)
                self.state = 90
                self.expr(0)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 91
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 97
                self.stm()
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 101
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==44:
                            self.state = 98
                            self.match(ZCodeParser.NULL_LINES)
                            self.state = 103
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 104
                        self.match(ZCodeParser.T__5)
                        self.state = 105
                        self.expr(0)
                        self.state = 109
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==44:
                            self.state = 106
                            self.match(ZCodeParser.NULL_LINES)
                            self.state = 111
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 112
                        self.stm() 
                    self.state = 118
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                self.state = 133
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==44:
                        self.state = 119
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 124
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 125
                    self.match(ZCodeParser.T__6)
                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==44:
                        self.state = 126
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 131
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 132
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


        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_for




    def r_for(self):

        localctx = ZCodeParser.R_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_r_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ZCodeParser.T__7)
            self.state = 138
            self.expr(0)
            self.state = 139
            self.match(ZCodeParser.T__8)
            self.state = 140
            self.expr(0)
            self.state = 141
            self.match(ZCodeParser.T__9)
            self.state = 142
            self.expr(0)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 143
                self.match(ZCodeParser.NULL_LINES)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
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

        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ZCodeParser.T__10)
            self.state = 152
            self.match(ZCodeParser.NULL_LINES)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10720254257470) != 0):
                self.state = 153
                self.stm()
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 154
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 155
                        self.stm() 
                    self.state = 160
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)



            self.state = 163
            self.match(ZCodeParser.NULL_LINES)
            self.state = 164
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


        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func




    def func(self):

        localctx = ZCodeParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(ZCodeParser.T__12)
            self.state = 167
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 168
            self.args()
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 169
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 174
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 177
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 175
                    self.r_return()
                    pass
                elif token in [11]:
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
        self.enterRule(localctx, 20, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(ZCodeParser.T__13)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 182
                self.match(ZCodeParser.TYPE)
                self.state = 183
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 184
                    self.type_index()


                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 187
                    self.match(ZCodeParser.T__14)
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


                    self.state = 197
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 200
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
            self.state = 202
            self.match(ZCodeParser.T__16)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 203
                self.match(ZCodeParser.NUMBER)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 204
                    self.match(ZCodeParser.T__14)
                    self.state = 205
                    self.match(ZCodeParser.NUMBER)
                    self.state = 210
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 213
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
            self.state = 215
            self.expr(0)
            self.state = 216
            self.match(ZCodeParser.T__18)
            self.state = 217
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
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(ZCodeParser.TYPE)
                self.state = 220
                self.expr(0)
                self.state = 221
                self.match(ZCodeParser.T__18)
                self.state = 222
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(ZCodeParser.T__19)
                self.state = 225
                self.expr(0)
                self.state = 226
                self.match(ZCodeParser.T__18)
                self.state = 227
                self.expr(0)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 229
                self.match(ZCodeParser.T__20)
                self.state = 230
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
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 234
                self.match(ZCodeParser.T__13)
                self.state = 235
                self.expr(0)
                self.state = 236
                self.match(ZCodeParser.T__15)
                pass

            elif la_ == 2:
                self.state = 238
                self.match(ZCodeParser.T__21)
                self.state = 239
                self.expr(7)
                pass

            elif la_ == 3:
                self.state = 240
                self.match(ZCodeParser.T__22)
                self.state = 241
                self.expr(6)
                pass

            elif la_ == 4:
                self.state = 242
                self.concat_expr()
                self.state = 243
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34091302912) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 244
                self.concat_expr()
                pass

            elif la_ == 5:
                self.state = 246
                self.concat_expr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 283
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 249
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 250
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 251
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 252
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 253
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 254
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 255
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 256
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 257
                        self.expr(2)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 258
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 259
                        self.match(ZCodeParser.T__16)
                        self.state = 260
                        localctx.indexer = self.expr(0)
                        self.state = 265
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 261
                            self.match(ZCodeParser.T__14)
                            self.state = 262
                            localctx.indexer = self.expr(0)
                            self.state = 267
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 268
                        self.match(ZCodeParser.T__17)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 270
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 271
                        self.match(ZCodeParser.T__13)
                        self.state = 280
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445373194240) != 0):
                            self.state = 272
                            localctx.param = self.expr(0)
                            self.state = 277
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 273
                                self.match(ZCodeParser.T__14)
                                self.state = 274
                                localctx.param = self.expr(0)
                                self.state = 279
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 282
                        self.match(ZCodeParser.T__15)
                        pass

             
                self.state = 287
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.operand()
                self.state = 289
                self.match(ZCodeParser.T__36)
                self.state = 290
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
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
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.r_list()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 297
                self.match(ZCodeParser.STRING)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 298
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 299
                self.match(ZCodeParser.T__13)
                self.state = 300
                self.expr(0)
                self.state = 301
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
            self.state = 305
            self.match(ZCodeParser.T__16)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445373194240) != 0):
                self.state = 306
                self.expr(0)
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 307
                    self.match(ZCodeParser.T__14)
                    self.state = 308
                    self.expr(0)
                    self.state = 313
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 316
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
         




