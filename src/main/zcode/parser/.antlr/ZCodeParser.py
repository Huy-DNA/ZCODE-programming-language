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
        4,1,48,318,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,3,0,46,8,0,1,0,1,0,1,0,5,0,51,8,0,10,0,12,0,54,
        9,0,3,0,56,8,0,1,0,3,0,59,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        5,6,101,8,6,10,6,12,6,104,9,6,1,6,1,6,1,6,1,6,3,6,110,8,6,3,6,112,
        8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,
        128,8,8,10,8,12,8,131,9,8,3,8,133,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,3,9,144,8,9,3,9,146,8,9,1,10,1,10,1,10,1,10,3,10,152,8,
        10,1,10,1,10,1,10,1,10,3,10,158,8,10,5,10,160,8,10,10,10,12,10,163,
        9,10,3,10,165,8,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,173,8,11,10,
        11,12,11,176,9,11,3,11,178,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,198,
        8,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,206,8,14,10,14,12,14,209,
        9,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,217,8,15,10,15,12,15,220,
        9,15,1,16,1,16,1,16,1,16,1,16,3,16,227,8,16,1,17,1,17,1,17,1,17,
        1,17,1,17,5,17,235,8,17,10,17,12,17,238,9,17,1,18,1,18,1,18,1,18,
        1,18,3,18,245,8,18,1,19,1,19,1,19,1,19,1,19,3,19,252,8,19,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,5,20,261,8,20,10,20,12,20,264,9,20,1,
        20,1,20,1,20,1,20,1,20,1,20,5,20,272,8,20,10,20,12,20,275,9,20,3,
        20,277,8,20,1,20,5,20,280,8,20,10,20,12,20,283,9,20,1,21,1,21,1,
        21,1,21,5,21,289,8,21,10,21,12,21,292,9,21,3,21,294,8,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,304,8,21,10,21,12,21,307,9,
        21,3,21,309,8,21,1,21,1,21,1,21,1,21,1,21,3,21,316,8,21,1,21,1,102,
        4,28,30,34,40,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,0,4,2,0,8,9,36,36,1,0,6,7,2,0,14,19,27,27,1,0,10,11,
        345,0,45,1,0,0,0,2,73,1,0,0,0,4,75,1,0,0,0,6,78,1,0,0,0,8,80,1,0,
        0,0,10,82,1,0,0,0,12,111,1,0,0,0,14,113,1,0,0,0,16,122,1,0,0,0,18,
        137,1,0,0,0,20,147,1,0,0,0,22,168,1,0,0,0,24,181,1,0,0,0,26,197,
        1,0,0,0,28,199,1,0,0,0,30,210,1,0,0,0,32,226,1,0,0,0,34,228,1,0,
        0,0,36,244,1,0,0,0,38,251,1,0,0,0,40,253,1,0,0,0,42,315,1,0,0,0,
        44,46,5,44,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,55,1,0,0,0,47,52,3,
        2,1,0,48,49,5,44,0,0,49,51,3,2,1,0,50,48,1,0,0,0,51,54,1,0,0,0,52,
        50,1,0,0,0,52,53,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,55,47,1,0,0,
        0,55,56,1,0,0,0,56,58,1,0,0,0,57,59,5,44,0,0,58,57,1,0,0,0,58,59,
        1,0,0,0,59,60,1,0,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,74,3,28,14,0,
        63,74,3,26,13,0,64,74,3,24,12,0,65,74,3,16,8,0,66,74,3,18,9,0,67,
        74,3,6,3,0,68,74,3,8,4,0,69,74,3,10,5,0,70,74,3,12,6,0,71,74,3,14,
        7,0,72,74,3,4,2,0,73,62,1,0,0,0,73,63,1,0,0,0,73,64,1,0,0,0,73,65,
        1,0,0,0,73,66,1,0,0,0,73,67,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,
        73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,3,1,0,0,0,75,76,5,31,
        0,0,76,77,3,28,14,0,77,5,1,0,0,0,78,79,5,32,0,0,79,7,1,0,0,0,80,
        81,5,33,0,0,81,9,1,0,0,0,82,83,5,34,0,0,83,84,3,28,14,0,84,11,1,
        0,0,0,85,86,5,2,0,0,86,87,3,28,14,0,87,88,5,44,0,0,88,89,3,2,1,0,
        89,112,1,0,0,0,90,91,5,2,0,0,91,92,3,28,14,0,92,93,5,44,0,0,93,102,
        3,2,1,0,94,95,5,44,0,0,95,96,5,3,0,0,96,97,3,28,14,0,97,98,5,44,
        0,0,98,99,3,2,1,0,99,101,1,0,0,0,100,94,1,0,0,0,101,104,1,0,0,0,
        102,103,1,0,0,0,102,100,1,0,0,0,103,109,1,0,0,0,104,102,1,0,0,0,
        105,106,5,44,0,0,106,107,5,4,0,0,107,108,5,44,0,0,108,110,3,2,1,
        0,109,105,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,85,1,0,0,0,
        111,90,1,0,0,0,112,13,1,0,0,0,113,114,5,5,0,0,114,115,3,28,14,0,
        115,116,5,37,0,0,116,117,3,28,14,0,117,118,5,38,0,0,118,119,3,28,
        14,0,119,120,5,44,0,0,120,121,3,2,1,0,121,15,1,0,0,0,122,123,5,24,
        0,0,123,132,5,44,0,0,124,129,3,2,1,0,125,126,5,44,0,0,126,128,3,
        2,1,0,127,125,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,
        0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,132,124,1,0,0,0,132,133,1,
        0,0,0,133,134,1,0,0,0,134,135,5,44,0,0,135,136,5,25,0,0,136,17,1,
        0,0,0,137,138,5,35,0,0,138,139,5,39,0,0,139,145,3,20,10,0,140,143,
        5,44,0,0,141,144,3,10,5,0,142,144,3,16,8,0,143,141,1,0,0,0,143,142,
        1,0,0,0,144,146,1,0,0,0,145,140,1,0,0,0,145,146,1,0,0,0,146,19,1,
        0,0,0,147,164,5,20,0,0,148,149,5,1,0,0,149,151,5,39,0,0,150,152,
        3,22,11,0,151,150,1,0,0,0,151,152,1,0,0,0,152,161,1,0,0,0,153,154,
        5,30,0,0,154,155,5,1,0,0,155,157,5,39,0,0,156,158,3,22,11,0,157,
        156,1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,153,1,0,0,0,160,
        163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,165,1,0,0,0,163,
        161,1,0,0,0,164,148,1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,
        167,5,21,0,0,167,21,1,0,0,0,168,177,5,22,0,0,169,174,5,40,0,0,170,
        171,5,30,0,0,171,173,5,40,0,0,172,170,1,0,0,0,173,176,1,0,0,0,174,
        172,1,0,0,0,174,175,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,177,
        169,1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,180,5,23,0,0,180,
        23,1,0,0,0,181,182,3,28,14,0,182,183,5,13,0,0,183,184,3,28,14,0,
        184,25,1,0,0,0,185,186,5,1,0,0,186,187,3,28,14,0,187,188,5,13,0,
        0,188,189,3,28,14,0,189,198,1,0,0,0,190,191,5,28,0,0,191,192,3,28,
        14,0,192,193,5,13,0,0,193,194,3,28,14,0,194,198,1,0,0,0,195,196,
        5,29,0,0,196,198,3,28,14,0,197,185,1,0,0,0,197,190,1,0,0,0,197,195,
        1,0,0,0,198,27,1,0,0,0,199,200,6,14,-1,0,200,201,3,30,15,0,201,207,
        1,0,0,0,202,203,10,2,0,0,203,204,7,0,0,0,204,206,3,30,15,0,205,202,
        1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,29,1,
        0,0,0,209,207,1,0,0,0,210,211,6,15,-1,0,211,212,3,32,16,0,212,218,
        1,0,0,0,213,214,10,2,0,0,214,215,7,1,0,0,215,217,3,32,16,0,216,213,
        1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,31,1,
        0,0,0,220,218,1,0,0,0,221,222,3,34,17,0,222,223,7,2,0,0,223,224,
        3,34,17,0,224,227,1,0,0,0,225,227,3,34,17,0,226,221,1,0,0,0,226,
        225,1,0,0,0,227,33,1,0,0,0,228,229,6,17,-1,0,229,230,3,36,18,0,230,
        236,1,0,0,0,231,232,10,2,0,0,232,233,7,3,0,0,233,235,3,36,18,0,234,
        231,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,
        35,1,0,0,0,238,236,1,0,0,0,239,240,3,38,19,0,240,241,5,12,0,0,241,
        242,3,38,19,0,242,245,1,0,0,0,243,245,3,38,19,0,244,239,1,0,0,0,
        244,243,1,0,0,0,245,37,1,0,0,0,246,247,5,6,0,0,247,252,3,38,19,0,
        248,249,5,26,0,0,249,252,3,38,19,0,250,252,3,40,20,0,251,246,1,0,
        0,0,251,248,1,0,0,0,251,250,1,0,0,0,252,39,1,0,0,0,253,254,6,20,
        -1,0,254,255,3,42,21,0,255,281,1,0,0,0,256,257,10,3,0,0,257,258,
        5,22,0,0,258,262,3,28,14,0,259,261,3,28,14,0,260,259,1,0,0,0,261,
        264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,265,1,0,0,0,264,
        262,1,0,0,0,265,266,5,23,0,0,266,280,1,0,0,0,267,268,10,2,0,0,268,
        276,5,20,0,0,269,273,3,28,14,0,270,272,3,28,14,0,271,270,1,0,0,0,
        272,275,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,277,1,0,0,0,
        275,273,1,0,0,0,276,269,1,0,0,0,276,277,1,0,0,0,277,278,1,0,0,0,
        278,280,5,21,0,0,279,256,1,0,0,0,279,267,1,0,0,0,280,283,1,0,0,0,
        281,279,1,0,0,0,281,282,1,0,0,0,282,41,1,0,0,0,283,281,1,0,0,0,284,
        293,5,22,0,0,285,286,3,28,14,0,286,290,5,30,0,0,287,289,3,28,14,
        0,288,287,1,0,0,0,289,292,1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,
        0,291,294,1,0,0,0,292,290,1,0,0,0,293,285,1,0,0,0,293,294,1,0,0,
        0,294,295,1,0,0,0,295,316,5,23,0,0,296,316,5,40,0,0,297,316,5,43,
        0,0,298,316,5,39,0,0,299,308,5,22,0,0,300,305,3,28,14,0,301,302,
        5,30,0,0,302,304,3,28,14,0,303,301,1,0,0,0,304,307,1,0,0,0,305,303,
        1,0,0,0,305,306,1,0,0,0,306,309,1,0,0,0,307,305,1,0,0,0,308,300,
        1,0,0,0,308,309,1,0,0,0,309,310,1,0,0,0,310,316,5,23,0,0,311,312,
        5,20,0,0,312,313,3,28,14,0,313,314,5,21,0,0,314,316,1,0,0,0,315,
        284,1,0,0,0,315,296,1,0,0,0,315,297,1,0,0,0,315,298,1,0,0,0,315,
        299,1,0,0,0,315,311,1,0,0,0,316,43,1,0,0,0,35,45,52,55,58,73,102,
        109,111,129,132,143,145,151,157,161,164,174,177,197,207,218,226,
        236,244,251,262,273,276,279,281,290,293,305,308,315
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'if'", "'elif'", "'else'", 
                     "'for'", "'-'", "'+'", "'*'", "'/'", "'and'", "'or'", 
                     "'...'", "'<-'", "'='", "'=='", "'>='", "'>'", "'<='", 
                     "'<'", "'('", "')'", "'['", "']'", "'begin'", "'end'", 
                     "'not'", "'!='", "'var'", "'dynamic'", "','", "'print'", 
                     "'break'", "'continue'", "'return'", "'func'", "'%'", 
                     "'until'", "'by'" ]

    symbolicNames = [ "<INVALID>", "TYPE", "IF", "ELIF", "ELSE", "FOR", 
                      "SUB", "ADD", "MUL", "DIV", "AND", "OR", "CONCAT", 
                      "ASSIGN", "EQ", "DEQ", "GE", "GT", "LE", "LT", "LP", 
                      "RP", "LB", "RB", "BEGIN", "END", "NOT", "NEQ", "VAR", 
                      "DYN", "COMMA", "PRINT", "BREAK", "CONTINUE", "RETURN", 
                      "FUNC", "MOD", "UNTIL", "BY", "IDENTIFIER", "NUMBER", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRING", "NULL_LINES", 
                      "COMMENT", "WS", "NEWLINE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_stm = 1
    RULE_r_print = 2
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
    RULE_expr1 = 15
    RULE_expr2 = 16
    RULE_expr3 = 17
    RULE_expr4 = 18
    RULE_expr5 = 19
    RULE_expr6 = 20
    RULE_term = 21

    ruleNames =  [ "program", "stm", "r_print", "r_break", "r_continue", 
                   "r_return", "r_if", "r_for", "block", "func", "args", 
                   "type_index", "ass", "decl", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "term" ]

    EOF = Token.EOF
    TYPE=1
    IF=2
    ELIF=3
    ELSE=4
    FOR=5
    SUB=6
    ADD=7
    MUL=8
    DIV=9
    AND=10
    OR=11
    CONCAT=12
    ASSIGN=13
    EQ=14
    DEQ=15
    GE=16
    GT=17
    LE=18
    LT=19
    LP=20
    RP=21
    LB=22
    RB=23
    BEGIN=24
    END=25
    NOT=26
    NEQ=27
    VAR=28
    DYN=29
    COMMA=30
    PRINT=31
    BREAK=32
    CONTINUE=33
    RETURN=34
    FUNC=35
    MOD=36
    UNTIL=37
    BY=38
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
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 44
                self.match(ZCodeParser.NULL_LINES)


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10512826892390) != 0):
                self.state = 47
                self.stm()
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 48
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 49
                        self.stm() 
                    self.state = 54
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)



            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 57
                self.match(ZCodeParser.NULL_LINES)


            self.state = 60
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


        def r_print(self):
            return self.getTypedRuleContext(ZCodeParser.R_printContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm




    def stm(self):

        localctx = ZCodeParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stm)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                self.r_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 70
                self.r_if()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 71
                self.r_for()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 72
                self.r_print()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ZCodeParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_print




    def r_print(self):

        localctx = ZCodeParser.R_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_r_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ZCodeParser.PRINT)
            self.state = 76
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

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_break




    def r_break(self):

        localctx = ZCodeParser.R_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_r_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ZCodeParser.BREAK)
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

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_continue




    def r_continue(self):

        localctx = ZCodeParser.R_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_r_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ZCodeParser.CONTINUE)
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

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_return




    def r_return(self):

        localctx = ZCodeParser.R_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_r_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ZCodeParser.RETURN)
            self.state = 83
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

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


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


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.ELIF)
            else:
                return self.getToken(ZCodeParser.ELIF, i)

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_if




    def r_if(self):

        localctx = ZCodeParser.R_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_r_if)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(ZCodeParser.IF)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(ZCodeParser.NULL_LINES)
                self.state = 88
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(ZCodeParser.IF)
                self.state = 91
                self.expr(0)
                self.state = 92
                self.match(ZCodeParser.NULL_LINES)
                self.state = 93
                self.stm()
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 94
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 95
                        self.match(ZCodeParser.ELIF)
                        self.state = 96
                        self.expr(0)
                        self.state = 97
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 98
                        self.stm() 
                    self.state = 104
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 109
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 105
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 106
                    self.match(ZCodeParser.ELSE)
                    self.state = 107
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 108
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

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def NULL_LINES(self):
            return self.getToken(ZCodeParser.NULL_LINES, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_for




    def r_for(self):

        localctx = ZCodeParser.R_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_r_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ZCodeParser.FOR)
            self.state = 114
            self.expr(0)
            self.state = 115
            self.match(ZCodeParser.UNTIL)
            self.state = 116
            self.expr(0)
            self.state = 117
            self.match(ZCodeParser.BY)
            self.state = 118
            self.expr(0)
            self.state = 119
            self.match(ZCodeParser.NULL_LINES)
            self.state = 120
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

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

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
            self.state = 122
            self.match(ZCodeParser.BEGIN)
            self.state = 123
            self.match(ZCodeParser.NULL_LINES)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10512826892390) != 0):
                self.state = 124
                self.stm()
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 125
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 126
                        self.stm() 
                    self.state = 131
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)



            self.state = 134
            self.match(ZCodeParser.NULL_LINES)
            self.state = 135
            self.match(ZCodeParser.END)
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

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def args(self):
            return self.getTypedRuleContext(ZCodeParser.ArgsContext,0)


        def NULL_LINES(self):
            return self.getToken(ZCodeParser.NULL_LINES, 0)

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
            self.state = 137
            self.match(ZCodeParser.FUNC)
            self.state = 138
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 139
            self.args()
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 140
                self.match(ZCodeParser.NULL_LINES)
                self.state = 143
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34]:
                    self.state = 141
                    self.r_return()
                    pass
                elif token in [24]:
                    self.state = 142
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

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_args




    def args(self):

        localctx = ZCodeParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(ZCodeParser.LP)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 148
                self.match(ZCodeParser.TYPE)
                self.state = 149
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 150
                    self.type_index()


                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 153
                    self.match(ZCodeParser.COMMA)
                    self.state = 154
                    self.match(ZCodeParser.TYPE)
                    self.state = 155
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 157
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==22:
                        self.state = 156
                        self.type_index()


                    self.state = 163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 166
            self.match(ZCodeParser.RP)
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

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NUMBER)
            else:
                return self.getToken(ZCodeParser.NUMBER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type_index




    def type_index(self):

        localctx = ZCodeParser.Type_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ZCodeParser.LB)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 169
                self.match(ZCodeParser.NUMBER)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 170
                    self.match(ZCodeParser.COMMA)
                    self.state = 171
                    self.match(ZCodeParser.NUMBER)
                    self.state = 176
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 179
            self.match(ZCodeParser.RB)
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


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ass




    def ass(self):

        localctx = ZCodeParser.AssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.expr(0)
            self.state = 182
            self.match(ZCodeParser.ASSIGN)
            self.state = 183
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


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def DYN(self):
            return self.getToken(ZCodeParser.DYN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_decl




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_decl)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(ZCodeParser.TYPE)
                self.state = 186
                self.expr(0)
                self.state = 187
                self.match(ZCodeParser.ASSIGN)
                self.state = 188
                self.expr(0)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(ZCodeParser.VAR)
                self.state = 191
                self.expr(0)
                self.state = 192
                self.match(ZCodeParser.ASSIGN)
                self.state = 193
                self.expr(0)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.match(ZCodeParser.DYN)
                self.state = 196
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
            self.op = None # Token

        def expr1(self):
            return self.getTypedRuleContext(ZCodeParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

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
            self.state = 200
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 202
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 203
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 68719477504) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 204
                    self.expr1(0) 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(ZCodeParser.Expr1Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.expr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 213
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 214
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==6 or _la==7):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 215
                    self.expr2() 
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr3Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr3Context,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def DEQ(self):
            return self.getToken(ZCodeParser.DEQ, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LE(self):
            return self.getToken(ZCodeParser.LE, 0)

        def GE(self):
            return self.getToken(ZCodeParser.GE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2




    def expr2(self):

        localctx = ZCodeParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.expr3(0)
                self.state = 222
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135249920) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.expr3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.expr3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 231
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 232
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 233
                    self.expr4() 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr5Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr5Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4




    def expr4(self):

        localctx = ZCodeParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr4)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.expr5()
                self.state = 240
                self.match(ZCodeParser.CONCAT)
                self.state = 241
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.expr5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr5)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(ZCodeParser.SUB)
                self.state = 247
                self.expr5()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(ZCodeParser.NOT)
                self.state = 249
                self.expr5()
                pass
            elif token in [20, 22, 39, 40, 43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                self.expr6(0)
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.array = None # Expr6Context
            self.callee = None # Expr6Context
            self.indexer = None # ExprContext
            self.COMMAindexer = None # ExprContext
            self.param = None # ExprContext
            self.COMMAparam = None # ExprContext

        def term(self):
            return self.getTypedRuleContext(ZCodeParser.TermContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 279
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 256
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 257
                        self.match(ZCodeParser.LB)
                        self.state = 258
                        localctx.indexer = self.expr(0)
                        self.state = 262
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                            self.state = 259
                            localctx.COMMAindexer = self.expr(0)
                            self.state = 264
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 265
                        self.match(ZCodeParser.RB)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 267
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 268
                        self.match(ZCodeParser.LP)
                        self.state = 276
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                            self.state = 269
                            localctx.param = self.expr(0)
                            self.state = 273
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                                self.state = 270
                                localctx.COMMAparam = self.expr(0)
                                self.state = 275
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 278
                        self.match(ZCodeParser.RP)
                        pass

             
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_term




    def term(self):

        localctx = ZCodeParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(ZCodeParser.LB)
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                    self.state = 285
                    self.expr(0)
                    self.state = 286
                    self.match(ZCodeParser.COMMA)
                    self.state = 290
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                        self.state = 287
                        self.expr(0)
                        self.state = 292
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 295
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 297
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 298
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 299
                self.match(ZCodeParser.LB)
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                    self.state = 300
                    self.expr(0)
                    self.state = 305
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==30:
                        self.state = 301
                        self.match(ZCodeParser.COMMA)
                        self.state = 302
                        self.expr(0)
                        self.state = 307
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 310
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 311
                self.match(ZCodeParser.LP)
                self.state = 312
                self.expr(0)
                self.state = 313
                self.match(ZCodeParser.RP)
                pass


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
        self._predicates[15] = self.expr1_sempred
        self._predicates[17] = self.expr3_sempred
        self._predicates[20] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




