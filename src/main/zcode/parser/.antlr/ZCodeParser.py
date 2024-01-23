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
        4,1,48,316,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,3,0,38,8,0,1,0,1,0,3,
        0,42,8,0,1,0,5,0,45,8,0,10,0,12,0,48,9,0,3,0,50,8,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,65,8,1,1,2,1,2,1,2,1,
        3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,5,6,80,8,6,10,6,12,6,83,9,
        6,1,6,1,6,1,6,1,6,1,6,5,6,90,8,6,10,6,12,6,93,9,6,1,6,1,6,5,6,97,
        8,6,10,6,12,6,100,9,6,1,6,1,6,1,6,5,6,105,8,6,10,6,12,6,108,9,6,
        1,6,1,6,5,6,112,8,6,10,6,12,6,115,9,6,1,6,5,6,118,8,6,10,6,12,6,
        121,9,6,1,6,1,6,5,6,125,8,6,10,6,12,6,128,9,6,1,6,3,6,131,8,6,3,
        6,133,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,142,8,7,10,7,12,7,145,
        9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,154,8,8,10,8,12,8,157,9,8,3,
        8,159,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,168,8,9,10,9,12,9,171,
        9,9,1,9,1,9,3,9,175,8,9,3,9,177,8,9,1,10,1,10,1,10,1,10,3,10,183,
        8,10,1,10,1,10,1,10,1,10,3,10,189,8,10,5,10,191,8,10,10,10,12,10,
        194,9,10,3,10,196,8,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,204,8,
        11,10,11,12,11,207,9,11,3,11,209,8,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,
        13,229,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,3,14,245,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,261,8,14,10,14,12,14,
        264,9,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,273,8,14,10,14,
        12,14,276,9,14,3,14,278,8,14,1,14,5,14,281,8,14,10,14,12,14,284,
        9,14,1,15,1,15,1,15,1,15,1,15,3,15,291,8,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,301,8,16,1,17,1,17,1,17,1,17,5,17,307,8,
        17,10,17,12,17,310,9,17,3,17,312,8,17,1,17,1,17,1,17,1,113,1,28,
        18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,4,1,0,28,34,
        1,0,24,26,2,0,22,22,27,27,1,0,35,36,353,0,37,1,0,0,0,2,64,1,0,0,
        0,4,66,1,0,0,0,6,69,1,0,0,0,8,71,1,0,0,0,10,73,1,0,0,0,12,132,1,
        0,0,0,14,134,1,0,0,0,16,148,1,0,0,0,18,163,1,0,0,0,20,178,1,0,0,
        0,22,199,1,0,0,0,24,212,1,0,0,0,26,228,1,0,0,0,28,244,1,0,0,0,30,
        290,1,0,0,0,32,300,1,0,0,0,34,302,1,0,0,0,36,38,5,44,0,0,37,36,1,
        0,0,0,37,38,1,0,0,0,38,49,1,0,0,0,39,46,3,2,1,0,40,42,5,44,0,0,41,
        40,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,45,3,2,1,0,44,41,1,0,0,
        0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,50,1,0,0,0,48,46,
        1,0,0,0,49,39,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,52,5,0,0,1,
        52,1,1,0,0,0,53,65,3,28,14,0,54,65,3,26,13,0,55,65,3,24,12,0,56,
        65,3,16,8,0,57,65,3,18,9,0,58,65,3,6,3,0,59,65,3,8,4,0,60,65,3,10,
        5,0,61,65,3,12,6,0,62,65,3,14,7,0,63,65,3,4,2,0,64,53,1,0,0,0,64,
        54,1,0,0,0,64,55,1,0,0,0,64,56,1,0,0,0,64,57,1,0,0,0,64,58,1,0,0,
        0,64,59,1,0,0,0,64,60,1,0,0,0,64,61,1,0,0,0,64,62,1,0,0,0,64,63,
        1,0,0,0,65,3,1,0,0,0,66,67,5,1,0,0,67,68,3,28,14,0,68,5,1,0,0,0,
        69,70,5,2,0,0,70,7,1,0,0,0,71,72,5,3,0,0,72,9,1,0,0,0,73,74,5,4,
        0,0,74,75,3,28,14,0,75,11,1,0,0,0,76,77,5,5,0,0,77,81,3,28,14,0,
        78,80,5,44,0,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,
        0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,3,2,1,0,85,133,1,0,0,0,86,
        87,5,5,0,0,87,91,3,28,14,0,88,90,5,44,0,0,89,88,1,0,0,0,90,93,1,
        0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,1,0,0,0,94,
        113,3,2,1,0,95,97,5,44,0,0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,1,
        0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,102,5,6,0,
        0,102,106,3,28,14,0,103,105,5,44,0,0,104,103,1,0,0,0,105,108,1,0,
        0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,106,1,0,
        0,0,109,110,3,2,1,0,110,112,1,0,0,0,111,98,1,0,0,0,112,115,1,0,0,
        0,113,114,1,0,0,0,113,111,1,0,0,0,114,130,1,0,0,0,115,113,1,0,0,
        0,116,118,5,44,0,0,117,116,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,
        0,119,120,1,0,0,0,120,122,1,0,0,0,121,119,1,0,0,0,122,126,5,7,0,
        0,123,125,5,44,0,0,124,123,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,
        0,126,127,1,0,0,0,127,129,1,0,0,0,128,126,1,0,0,0,129,131,3,2,1,
        0,130,119,1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,76,1,0,0,0,
        132,86,1,0,0,0,133,13,1,0,0,0,134,135,5,8,0,0,135,136,3,28,14,0,
        136,137,5,9,0,0,137,138,3,28,14,0,138,139,5,10,0,0,139,143,3,28,
        14,0,140,142,5,44,0,0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,1,
        0,0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,147,3,
        2,1,0,147,15,1,0,0,0,148,149,5,11,0,0,149,158,5,44,0,0,150,155,3,
        2,1,0,151,152,5,44,0,0,152,154,3,2,1,0,153,151,1,0,0,0,154,157,1,
        0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,159,1,0,0,0,157,155,1,
        0,0,0,158,150,1,0,0,0,158,159,1,0,0,0,159,160,1,0,0,0,160,161,5,
        44,0,0,161,162,5,12,0,0,162,17,1,0,0,0,163,164,5,13,0,0,164,165,
        5,39,0,0,165,176,3,20,10,0,166,168,5,44,0,0,167,166,1,0,0,0,168,
        171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,174,1,0,0,0,171,
        169,1,0,0,0,172,175,3,10,5,0,173,175,3,16,8,0,174,172,1,0,0,0,174,
        173,1,0,0,0,175,177,1,0,0,0,176,169,1,0,0,0,176,177,1,0,0,0,177,
        19,1,0,0,0,178,195,5,14,0,0,179,180,5,38,0,0,180,182,5,39,0,0,181,
        183,3,22,11,0,182,181,1,0,0,0,182,183,1,0,0,0,183,192,1,0,0,0,184,
        185,5,15,0,0,185,186,5,38,0,0,186,188,5,39,0,0,187,189,3,22,11,0,
        188,187,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,184,1,0,0,0,
        191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,196,1,0,0,0,
        194,192,1,0,0,0,195,179,1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,
        197,198,5,16,0,0,198,21,1,0,0,0,199,208,5,17,0,0,200,205,5,40,0,
        0,201,202,5,15,0,0,202,204,5,40,0,0,203,201,1,0,0,0,204,207,1,0,
        0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,209,1,0,0,0,207,205,1,0,
        0,0,208,200,1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,211,5,18,
        0,0,211,23,1,0,0,0,212,213,3,28,14,0,213,214,5,19,0,0,214,215,3,
        28,14,0,215,25,1,0,0,0,216,217,5,38,0,0,217,218,3,28,14,0,218,219,
        5,19,0,0,219,220,3,28,14,0,220,229,1,0,0,0,221,222,5,20,0,0,222,
        223,3,28,14,0,223,224,5,19,0,0,224,225,3,28,14,0,225,229,1,0,0,0,
        226,227,5,21,0,0,227,229,3,28,14,0,228,216,1,0,0,0,228,221,1,0,0,
        0,228,226,1,0,0,0,229,27,1,0,0,0,230,231,6,14,-1,0,231,232,5,14,
        0,0,232,233,3,28,14,0,233,234,5,16,0,0,234,245,1,0,0,0,235,236,5,
        22,0,0,236,245,3,28,14,7,237,238,5,23,0,0,238,245,3,28,14,6,239,
        240,3,30,15,0,240,241,7,0,0,0,241,242,3,30,15,0,242,245,1,0,0,0,
        243,245,3,30,15,0,244,230,1,0,0,0,244,235,1,0,0,0,244,237,1,0,0,
        0,244,239,1,0,0,0,244,243,1,0,0,0,245,282,1,0,0,0,246,247,10,5,0,
        0,247,248,7,1,0,0,248,281,3,28,14,6,249,250,10,4,0,0,250,251,7,2,
        0,0,251,281,3,28,14,5,252,253,10,1,0,0,253,254,7,3,0,0,254,281,3,
        28,14,2,255,256,10,9,0,0,256,257,5,17,0,0,257,262,3,28,14,0,258,
        259,5,15,0,0,259,261,3,28,14,0,260,258,1,0,0,0,261,264,1,0,0,0,262,
        260,1,0,0,0,262,263,1,0,0,0,263,265,1,0,0,0,264,262,1,0,0,0,265,
        266,5,18,0,0,266,281,1,0,0,0,267,268,10,8,0,0,268,277,5,14,0,0,269,
        274,3,28,14,0,270,271,5,15,0,0,271,273,3,28,14,0,272,270,1,0,0,0,
        273,276,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,278,1,0,0,0,
        276,274,1,0,0,0,277,269,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,
        279,281,5,16,0,0,280,246,1,0,0,0,280,249,1,0,0,0,280,252,1,0,0,0,
        280,255,1,0,0,0,280,267,1,0,0,0,281,284,1,0,0,0,282,280,1,0,0,0,
        282,283,1,0,0,0,283,29,1,0,0,0,284,282,1,0,0,0,285,286,3,32,16,0,
        286,287,5,37,0,0,287,288,3,32,16,0,288,291,1,0,0,0,289,291,3,32,
        16,0,290,285,1,0,0,0,290,289,1,0,0,0,291,31,1,0,0,0,292,301,3,34,
        17,0,293,301,5,40,0,0,294,301,5,43,0,0,295,301,5,39,0,0,296,297,
        5,14,0,0,297,298,3,28,14,0,298,299,5,16,0,0,299,301,1,0,0,0,300,
        292,1,0,0,0,300,293,1,0,0,0,300,294,1,0,0,0,300,295,1,0,0,0,300,
        296,1,0,0,0,301,33,1,0,0,0,302,311,5,17,0,0,303,308,3,28,14,0,304,
        305,5,15,0,0,305,307,3,28,14,0,306,304,1,0,0,0,307,310,1,0,0,0,308,
        306,1,0,0,0,308,309,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,311,
        303,1,0,0,0,311,312,1,0,0,0,312,313,1,0,0,0,313,314,5,18,0,0,314,
        35,1,0,0,0,37,37,41,46,49,64,81,91,98,106,113,119,126,130,132,143,
        155,158,169,174,176,182,188,192,195,205,208,228,244,262,274,277,
        280,282,290,300,308,311
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
            _la = self._input.LA(1)
            if _la==44:
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
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28312440301886) != 0):
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
                    _la = self._input.LA(1)



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


        def print_(self):
            return self.getTypedRuleContext(ZCodeParser.PrintContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm




    def stm(self):

        localctx = ZCodeParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stm)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
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

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 63
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
            self.state = 66
            self.match(ZCodeParser.T__0)
            self.state = 67
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
            self.state = 69
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
            self.state = 71
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
            self.state = 73
            self.match(ZCodeParser.T__3)
            self.state = 74
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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(ZCodeParser.T__4)
                self.state = 77
                self.expr(0)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 78
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 84
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(ZCodeParser.T__4)
                self.state = 87
                self.expr(0)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 88
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 94
                self.stm()
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 98
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==44:
                            self.state = 95
                            self.match(ZCodeParser.NULL_LINES)
                            self.state = 100
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 101
                        self.match(ZCodeParser.T__5)
                        self.state = 102
                        self.expr(0)
                        self.state = 106
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==44:
                            self.state = 103
                            self.match(ZCodeParser.NULL_LINES)
                            self.state = 108
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 109
                        self.stm() 
                    self.state = 115
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 130
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==44:
                        self.state = 116
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 121
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 122
                    self.match(ZCodeParser.T__6)
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==44:
                        self.state = 123
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 128
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 129
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
            self.state = 134
            self.match(ZCodeParser.T__7)
            self.state = 135
            self.expr(0)
            self.state = 136
            self.match(ZCodeParser.T__8)
            self.state = 137
            self.expr(0)
            self.state = 138
            self.match(ZCodeParser.T__9)
            self.state = 139
            self.expr(0)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 140
                self.match(ZCodeParser.NULL_LINES)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
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
            self.state = 148
            self.match(ZCodeParser.T__10)
            self.state = 149
            self.match(ZCodeParser.NULL_LINES)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10720254257470) != 0):
                self.state = 150
                self.stm()
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 151
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 152
                        self.stm() 
                    self.state = 157
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)



            self.state = 160
            self.match(ZCodeParser.NULL_LINES)
            self.state = 161
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
            self.state = 163
            self.match(ZCodeParser.T__12)
            self.state = 164
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 165
            self.args()
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 166
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 171
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 174
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 172
                    self.r_return()
                    pass
                elif token in [11]:
                    self.state = 173
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
            self.state = 178
            self.match(ZCodeParser.T__13)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 179
                self.match(ZCodeParser.TYPE)
                self.state = 180
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 181
                    self.type_index()


                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 184
                    self.match(ZCodeParser.T__14)
                    self.state = 185
                    self.match(ZCodeParser.TYPE)
                    self.state = 186
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 188
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==17:
                        self.state = 187
                        self.type_index()


                    self.state = 194
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 197
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
            self.state = 199
            self.match(ZCodeParser.T__16)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 200
                self.match(ZCodeParser.NUMBER)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 201
                    self.match(ZCodeParser.T__14)
                    self.state = 202
                    self.match(ZCodeParser.NUMBER)
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 210
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
            self.state = 212
            self.expr(0)
            self.state = 213
            self.match(ZCodeParser.T__18)
            self.state = 214
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
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(ZCodeParser.TYPE)
                self.state = 217
                self.expr(0)
                self.state = 218
                self.match(ZCodeParser.T__18)
                self.state = 219
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(ZCodeParser.T__19)
                self.state = 222
                self.expr(0)
                self.state = 223
                self.match(ZCodeParser.T__18)
                self.state = 224
                self.expr(0)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.match(ZCodeParser.T__20)
                self.state = 227
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
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 231
                self.match(ZCodeParser.T__13)
                self.state = 232
                self.expr(0)
                self.state = 233
                self.match(ZCodeParser.T__15)
                pass

            elif la_ == 2:
                self.state = 235
                self.match(ZCodeParser.T__21)
                self.state = 236
                self.expr(7)
                pass

            elif la_ == 3:
                self.state = 237
                self.match(ZCodeParser.T__22)
                self.state = 238
                self.expr(6)
                pass

            elif la_ == 4:
                self.state = 239
                self.concat_expr()
                self.state = 240
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34091302912) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 241
                self.concat_expr()
                pass

            elif la_ == 5:
                self.state = 243
                self.concat_expr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 280
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 246
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 247
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 248
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 249
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 250
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 251
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 252
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 253
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 254
                        self.expr(2)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 255
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 256
                        self.match(ZCodeParser.T__16)
                        self.state = 257
                        localctx.indexer = self.expr(0)
                        self.state = 262
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 258
                            self.match(ZCodeParser.T__14)
                            self.state = 259
                            localctx.indexer = self.expr(0)
                            self.state = 264
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 265
                        self.match(ZCodeParser.T__17)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 267
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 268
                        self.match(ZCodeParser.T__13)
                        self.state = 277
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445373194240) != 0):
                            self.state = 269
                            localctx.param = self.expr(0)
                            self.state = 274
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 270
                                self.match(ZCodeParser.T__14)
                                self.state = 271
                                localctx.param = self.expr(0)
                                self.state = 276
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 279
                        self.match(ZCodeParser.T__15)
                        pass

             
                self.state = 284
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
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.operand()
                self.state = 286
                self.match(ZCodeParser.T__36)
                self.state = 287
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
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
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.r_list()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.match(ZCodeParser.STRING)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 295
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 296
                self.match(ZCodeParser.T__13)
                self.state = 297
                self.expr(0)
                self.state = 298
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
            self.state = 302
            self.match(ZCodeParser.T__16)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445373194240) != 0):
                self.state = 303
                self.expr(0)
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 304
                    self.match(ZCodeParser.T__14)
                    self.state = 305
                    self.expr(0)
                    self.state = 310
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 313
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
         




