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
        4,1,46,319,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,3,0,48,8,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,5,5,88,8,5,10,5,12,5,91,9,5,1,5,1,5,5,5,95,8,5,10,5,
        12,5,98,9,5,1,5,1,5,1,5,1,5,1,5,5,5,105,8,5,10,5,12,5,108,9,5,1,
        5,1,5,5,5,112,8,5,10,5,12,5,115,9,5,1,5,5,5,118,8,5,10,5,12,5,121,
        9,5,1,5,1,5,5,5,125,8,5,10,5,12,5,128,9,5,1,5,3,5,131,8,5,3,5,133,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,142,8,6,10,6,12,6,145,9,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,154,8,7,10,7,12,7,157,9,7,1,7,5,7,
        160,8,7,10,7,12,7,163,9,7,1,7,3,7,166,8,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,3,8,176,8,8,1,9,1,9,1,9,1,9,3,9,182,8,9,1,9,1,9,1,9,1,
        9,3,9,188,8,9,5,9,190,8,9,10,9,12,9,193,9,9,3,9,195,8,9,1,9,1,9,
        1,10,1,10,1,10,1,10,5,10,203,8,10,10,10,12,10,206,9,10,3,10,208,
        8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,3,12,228,8,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,244,8,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,257,
        8,13,10,13,12,13,260,9,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,
        269,8,13,10,13,12,13,272,9,13,3,13,274,8,13,1,13,5,13,277,8,13,10,
        13,12,13,280,9,13,1,14,1,14,1,14,1,14,1,14,3,14,287,8,14,1,15,1,
        15,1,15,1,15,1,15,5,15,294,8,15,10,15,12,15,297,9,15,3,15,299,8,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,309,8,15,1,15,1,
        15,1,15,5,15,314,8,15,10,15,12,15,317,9,15,1,15,1,113,2,26,30,16,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,4,1,0,27,33,1,0,23,
        25,2,0,21,21,26,26,1,0,35,36,357,0,47,1,0,0,0,2,61,1,0,0,0,4,63,
        1,0,0,0,6,65,1,0,0,0,8,67,1,0,0,0,10,132,1,0,0,0,12,134,1,0,0,0,
        14,148,1,0,0,0,16,170,1,0,0,0,18,177,1,0,0,0,20,198,1,0,0,0,22,211,
        1,0,0,0,24,227,1,0,0,0,26,243,1,0,0,0,28,286,1,0,0,0,30,308,1,0,
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
        77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,3,2,1,0,81,133,1,
        0,0,0,82,83,5,4,0,0,83,84,5,5,0,0,84,85,3,26,13,0,85,89,5,6,0,0,
        86,88,5,45,0,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,
        0,0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,113,3,2,1,0,93,95,5,45,0,0,
        94,93,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,
        0,0,0,98,96,1,0,0,0,99,100,5,7,0,0,100,101,5,5,0,0,101,102,3,26,
        13,0,102,106,5,6,0,0,103,105,5,45,0,0,104,103,1,0,0,0,105,108,1,
        0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,106,1,
        0,0,0,109,110,3,2,1,0,110,112,1,0,0,0,111,96,1,0,0,0,112,115,1,0,
        0,0,113,114,1,0,0,0,113,111,1,0,0,0,114,130,1,0,0,0,115,113,1,0,
        0,0,116,118,5,45,0,0,117,116,1,0,0,0,118,121,1,0,0,0,119,117,1,0,
        0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,119,1,0,0,0,122,126,5,8,
        0,0,123,125,5,45,0,0,124,123,1,0,0,0,125,128,1,0,0,0,126,124,1,0,
        0,0,126,127,1,0,0,0,127,129,1,0,0,0,128,126,1,0,0,0,129,131,3,2,
        1,0,130,119,1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,70,1,0,0,
        0,132,82,1,0,0,0,133,11,1,0,0,0,134,135,5,9,0,0,135,136,3,26,13,
        0,136,137,5,10,0,0,137,138,3,26,13,0,138,139,5,11,0,0,139,143,3,
        26,13,0,140,142,5,45,0,0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,
        1,0,0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,147,
        3,2,1,0,147,13,1,0,0,0,148,149,5,12,0,0,149,165,5,45,0,0,150,155,
        3,2,1,0,151,152,5,45,0,0,152,154,3,2,1,0,153,151,1,0,0,0,154,157,
        1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,166,1,0,0,0,157,155,
        1,0,0,0,158,160,5,45,0,0,159,158,1,0,0,0,160,163,1,0,0,0,161,159,
        1,0,0,0,161,162,1,0,0,0,162,166,1,0,0,0,163,161,1,0,0,0,164,166,
        5,43,0,0,165,150,1,0,0,0,165,161,1,0,0,0,165,164,1,0,0,0,166,167,
        1,0,0,0,167,168,5,45,0,0,168,169,5,13,0,0,169,15,1,0,0,0,170,171,
        5,14,0,0,171,172,5,38,0,0,172,175,3,18,9,0,173,176,3,8,4,0,174,176,
        3,14,7,0,175,173,1,0,0,0,175,174,1,0,0,0,176,17,1,0,0,0,177,194,
        5,5,0,0,178,179,5,37,0,0,179,181,5,38,0,0,180,182,3,20,10,0,181,
        180,1,0,0,0,181,182,1,0,0,0,182,191,1,0,0,0,183,184,5,15,0,0,184,
        185,5,37,0,0,185,187,5,38,0,0,186,188,3,20,10,0,187,186,1,0,0,0,
        187,188,1,0,0,0,188,190,1,0,0,0,189,183,1,0,0,0,190,193,1,0,0,0,
        191,189,1,0,0,0,191,192,1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,
        194,178,1,0,0,0,194,195,1,0,0,0,195,196,1,0,0,0,196,197,5,6,0,0,
        197,19,1,0,0,0,198,207,5,16,0,0,199,204,5,39,0,0,200,201,5,15,0,
        0,201,203,5,39,0,0,202,200,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,
        0,204,205,1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,207,199,1,0,0,
        0,207,208,1,0,0,0,208,209,1,0,0,0,209,210,5,17,0,0,210,21,1,0,0,
        0,211,212,3,26,13,0,212,213,5,18,0,0,213,214,3,26,13,0,214,23,1,
        0,0,0,215,216,5,37,0,0,216,217,3,26,13,0,217,218,5,18,0,0,218,219,
        3,26,13,0,219,228,1,0,0,0,220,221,5,19,0,0,221,222,3,26,13,0,222,
        223,5,18,0,0,223,224,3,26,13,0,224,228,1,0,0,0,225,226,5,20,0,0,
        226,228,3,26,13,0,227,215,1,0,0,0,227,220,1,0,0,0,227,225,1,0,0,
        0,228,25,1,0,0,0,229,230,6,13,-1,0,230,231,5,5,0,0,231,232,3,26,
        13,0,232,233,5,6,0,0,233,244,1,0,0,0,234,235,5,21,0,0,235,244,3,
        26,13,6,236,237,5,22,0,0,237,244,3,26,13,5,238,239,3,28,14,0,239,
        240,7,0,0,0,240,241,3,28,14,0,241,244,1,0,0,0,242,244,3,28,14,0,
        243,229,1,0,0,0,243,234,1,0,0,0,243,236,1,0,0,0,243,238,1,0,0,0,
        243,242,1,0,0,0,244,278,1,0,0,0,245,246,10,4,0,0,246,247,7,1,0,0,
        247,277,3,26,13,5,248,249,10,3,0,0,249,250,7,2,0,0,250,277,3,26,
        13,4,251,252,10,8,0,0,252,253,5,16,0,0,253,258,3,26,13,0,254,255,
        5,15,0,0,255,257,3,26,13,0,256,254,1,0,0,0,257,260,1,0,0,0,258,256,
        1,0,0,0,258,259,1,0,0,0,259,261,1,0,0,0,260,258,1,0,0,0,261,262,
        5,17,0,0,262,277,1,0,0,0,263,264,10,7,0,0,264,273,5,5,0,0,265,270,
        3,26,13,0,266,267,5,15,0,0,267,269,3,26,13,0,268,266,1,0,0,0,269,
        272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,274,1,0,0,0,272,
        270,1,0,0,0,273,265,1,0,0,0,273,274,1,0,0,0,274,275,1,0,0,0,275,
        277,5,6,0,0,276,245,1,0,0,0,276,248,1,0,0,0,276,251,1,0,0,0,276,
        263,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,279,
        27,1,0,0,0,280,278,1,0,0,0,281,282,3,30,15,0,282,283,5,34,0,0,283,
        284,3,30,15,0,284,287,1,0,0,0,285,287,3,30,15,0,286,281,1,0,0,0,
        286,285,1,0,0,0,287,29,1,0,0,0,288,289,6,15,-1,0,289,298,5,16,0,
        0,290,295,3,26,13,0,291,292,5,15,0,0,292,294,3,26,13,0,293,291,1,
        0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,299,1,
        0,0,0,297,295,1,0,0,0,298,290,1,0,0,0,298,299,1,0,0,0,299,300,1,
        0,0,0,300,309,5,17,0,0,301,309,5,39,0,0,302,309,5,42,0,0,303,309,
        5,38,0,0,304,305,5,5,0,0,305,306,3,26,13,0,306,307,5,6,0,0,307,309,
        1,0,0,0,308,288,1,0,0,0,308,301,1,0,0,0,308,302,1,0,0,0,308,303,
        1,0,0,0,308,304,1,0,0,0,309,315,1,0,0,0,310,311,10,6,0,0,311,312,
        7,3,0,0,312,314,3,30,15,7,313,310,1,0,0,0,314,317,1,0,0,0,315,313,
        1,0,0,0,315,316,1,0,0,0,316,31,1,0,0,0,317,315,1,0,0,0,36,37,43,
        47,61,77,89,96,106,113,119,126,130,132,143,155,161,165,175,181,187,
        191,194,204,207,227,243,258,270,273,276,278,286,295,298,308,315
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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
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
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 96
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==45:
                            self.state = 93
                            self.match(ZCodeParser.NEWLINE)
                            self.state = 98
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 99
                        self.match(ZCodeParser.T__6)
                        self.state = 100
                        self.match(ZCodeParser.T__4)
                        self.state = 101
                        self.expr(0)
                        self.state = 102
                        self.match(ZCodeParser.T__5)
                        self.state = 106
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==45:
                            self.state = 103
                            self.match(ZCodeParser.NEWLINE)
                            self.state = 108
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 109
                        self.stm() 
                    self.state = 115
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 130
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==45:
                        self.state = 116
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 121
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 122
                    self.match(ZCodeParser.T__7)
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==45:
                        self.state = 123
                        self.match(ZCodeParser.NEWLINE)
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
            self.state = 134
            self.match(ZCodeParser.T__8)
            self.state = 135
            self.expr(0)
            self.state = 136
            self.match(ZCodeParser.T__9)
            self.state = 137
            self.expr(0)
            self.state = 138
            self.match(ZCodeParser.T__10)
            self.state = 139
            self.expr(0)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 140
                self.match(ZCodeParser.NEWLINE)
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
            self.state = 148
            self.match(ZCodeParser.T__11)
            self.state = 149
            self.match(ZCodeParser.NEWLINE)
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 9, 12, 14, 16, 19, 20, 21, 22, 37, 38, 39, 42]:
                self.state = 150
                self.stm()
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 151
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 152
                        self.stm() 
                    self.state = 157
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass
            elif token in [45]:
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 158
                        self.match(ZCodeParser.NEWLINE) 
                    self.state = 163
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass
            elif token in [43]:
                self.state = 164
                self.match(ZCodeParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 167
            self.match(ZCodeParser.NEWLINE)
            self.state = 168
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
            self.state = 170
            self.match(ZCodeParser.T__13)
            self.state = 171
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 172
            self.args()
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 173
                self.r_return()
                pass
            elif token in [12]:
                self.state = 174
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
            self.state = 177
            self.match(ZCodeParser.T__4)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 178
                self.match(ZCodeParser.TYPE)
                self.state = 179
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 180
                    self.type_index()


                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 183
                    self.match(ZCodeParser.T__14)
                    self.state = 184
                    self.match(ZCodeParser.TYPE)
                    self.state = 185
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 187
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 186
                        self.type_index()


                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 196
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
            self.state = 198
            self.match(ZCodeParser.T__15)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 199
                self.match(ZCodeParser.NUMBER)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 200
                    self.match(ZCodeParser.T__14)
                    self.state = 201
                    self.match(ZCodeParser.NUMBER)
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 209
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
            self.state = 211
            self.expr(0)
            self.state = 212
            self.match(ZCodeParser.T__17)
            self.state = 213
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
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(ZCodeParser.TYPE)
                self.state = 216
                self.expr(0)
                self.state = 217
                self.match(ZCodeParser.T__17)
                self.state = 218
                self.expr(0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(ZCodeParser.T__18)
                self.state = 221
                self.expr(0)
                self.state = 222
                self.match(ZCodeParser.T__17)
                self.state = 223
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.match(ZCodeParser.T__19)
                self.state = 226
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
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 230
                self.match(ZCodeParser.T__4)
                self.state = 231
                self.expr(0)
                self.state = 232
                self.match(ZCodeParser.T__5)
                pass

            elif la_ == 2:
                self.state = 234
                self.match(ZCodeParser.T__20)
                self.state = 235
                self.expr(6)
                pass

            elif la_ == 3:
                self.state = 236
                self.match(ZCodeParser.T__21)
                self.state = 237
                self.expr(5)
                pass

            elif la_ == 4:
                self.state = 238
                self.expr_without_rel()
                self.state = 239
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17045651456) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 240
                self.expr_without_rel()
                pass

            elif la_ == 5:
                self.state = 242
                self.expr_without_rel()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 276
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 245
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 246
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 247
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 249
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 250
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 251
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 252
                        self.match(ZCodeParser.T__15)
                        self.state = 253
                        localctx.indexer = self.expr(0)
                        self.state = 258
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 254
                            self.match(ZCodeParser.T__14)
                            self.state = 255
                            localctx.indexer = self.expr(0)
                            self.state = 260
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 261
                        self.match(ZCodeParser.T__16)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 263
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 264
                        self.match(ZCodeParser.T__4)
                        self.state = 273
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                            self.state = 265
                            localctx.param = self.expr(0)
                            self.state = 270
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 266
                                self.match(ZCodeParser.T__14)
                                self.state = 267
                                localctx.param = self.expr(0)
                                self.state = 272
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 275
                        self.match(ZCodeParser.T__5)
                        pass

             
                self.state = 280
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
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.expr_without_str_concat(0)
                self.state = 282
                self.match(ZCodeParser.T__33)
                self.state = 283
                self.expr_without_str_concat(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
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
            self.state = 308
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 289
                self.match(ZCodeParser.T__15)
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                    self.state = 290
                    self.expr(0)
                    self.state = 295
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==15:
                        self.state = 291
                        self.match(ZCodeParser.T__14)
                        self.state = 292
                        self.expr(0)
                        self.state = 297
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 300
                self.match(ZCodeParser.T__16)
                pass
            elif token in [39]:
                self.state = 301
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [42]:
                self.state = 302
                self.match(ZCodeParser.STRING)
                pass
            elif token in [38]:
                self.state = 303
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [5]:
                self.state = 304
                self.match(ZCodeParser.T__4)
                self.state = 305
                self.expr(0)
                self.state = 306
                self.match(ZCodeParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_without_str_concatContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_without_str_concat)
                    self.state = 310
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 311
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==35 or _la==36):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 312
                    self.expr_without_str_concat(7) 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
         




