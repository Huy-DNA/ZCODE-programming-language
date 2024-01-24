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
        4,1,48,343,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,1,1,1,1,3,1,62,8,1,1,1,1,1,1,1,3,1,67,8,1,
        1,1,3,1,70,8,1,1,2,1,2,1,2,1,2,1,2,3,2,77,8,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,90,8,3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        114,8,8,1,9,1,9,3,9,118,8,9,1,10,1,10,1,10,1,10,3,10,124,8,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,137,8,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,14,5,14,153,8,14,10,14,12,14,156,9,14,3,14,158,8,14,1,14,1,
        14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,3,15,169,8,15,3,15,171,8,15,
        1,16,1,16,1,16,1,16,3,16,177,8,16,1,16,1,16,1,16,1,16,3,16,183,8,
        16,5,16,185,8,16,10,16,12,16,188,9,16,3,16,190,8,16,1,16,1,16,1,
        17,1,17,1,17,1,17,5,17,198,8,17,10,17,12,17,201,9,17,3,17,203,8,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,3,19,223,8,19,1,20,1,20,1,20,1,20,1,
        20,1,20,5,20,231,8,20,10,20,12,20,234,9,20,1,21,1,21,1,21,1,21,1,
        21,1,21,5,21,242,8,21,10,21,12,21,245,9,21,1,22,1,22,1,22,1,22,1,
        22,3,22,252,8,22,1,23,1,23,1,23,1,23,1,23,1,23,5,23,260,8,23,10,
        23,12,23,263,9,23,1,24,1,24,1,24,1,24,1,24,3,24,270,8,24,1,25,1,
        25,1,25,1,25,1,25,3,25,277,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,5,26,286,8,26,10,26,12,26,289,9,26,1,26,1,26,1,26,1,26,1,26,1,
        26,5,26,297,8,26,10,26,12,26,300,9,26,3,26,302,8,26,1,26,5,26,305,
        8,26,10,26,12,26,308,9,26,1,27,1,27,1,27,1,27,5,27,314,8,27,10,27,
        12,27,317,9,27,3,27,319,8,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,5,27,329,8,27,10,27,12,27,332,9,27,3,27,334,8,27,1,27,1,27,
        1,27,1,27,1,27,3,27,341,8,27,1,27,0,4,40,42,46,52,28,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        0,4,2,0,8,9,36,36,1,0,6,7,2,0,14,19,27,27,1,0,10,11,365,0,56,1,0,
        0,0,2,69,1,0,0,0,4,76,1,0,0,0,6,89,1,0,0,0,8,91,1,0,0,0,10,94,1,
        0,0,0,12,96,1,0,0,0,14,98,1,0,0,0,16,113,1,0,0,0,18,117,1,0,0,0,
        20,123,1,0,0,0,22,125,1,0,0,0,24,136,1,0,0,0,26,138,1,0,0,0,28,147,
        1,0,0,0,30,162,1,0,0,0,32,172,1,0,0,0,34,193,1,0,0,0,36,206,1,0,
        0,0,38,222,1,0,0,0,40,224,1,0,0,0,42,235,1,0,0,0,44,251,1,0,0,0,
        46,253,1,0,0,0,48,269,1,0,0,0,50,276,1,0,0,0,52,278,1,0,0,0,54,340,
        1,0,0,0,56,57,3,2,1,0,57,58,5,0,0,1,58,1,1,0,0,0,59,62,5,44,0,0,
        60,62,1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,63,1,0,0,0,63,66,3,
        4,2,0,64,67,5,44,0,0,65,67,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,
        70,1,0,0,0,68,70,1,0,0,0,69,61,1,0,0,0,69,68,1,0,0,0,70,3,1,0,0,
        0,71,77,3,6,3,0,72,73,3,6,3,0,73,74,5,44,0,0,74,75,3,4,2,0,75,77,
        1,0,0,0,76,71,1,0,0,0,76,72,1,0,0,0,77,5,1,0,0,0,78,90,3,40,20,0,
        79,90,3,38,19,0,80,90,3,36,18,0,81,90,3,28,14,0,82,90,3,30,15,0,
        83,90,3,10,5,0,84,90,3,12,6,0,85,90,3,14,7,0,86,90,3,16,8,0,87,90,
        3,26,13,0,88,90,3,8,4,0,89,78,1,0,0,0,89,79,1,0,0,0,89,80,1,0,0,
        0,89,81,1,0,0,0,89,82,1,0,0,0,89,83,1,0,0,0,89,84,1,0,0,0,89,85,
        1,0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,7,1,0,0,0,91,
        92,5,31,0,0,92,93,3,40,20,0,93,9,1,0,0,0,94,95,5,32,0,0,95,11,1,
        0,0,0,96,97,5,33,0,0,97,13,1,0,0,0,98,99,5,34,0,0,99,100,3,40,20,
        0,100,15,1,0,0,0,101,102,5,2,0,0,102,103,3,40,20,0,103,104,5,44,
        0,0,104,105,3,6,3,0,105,114,1,0,0,0,106,107,5,2,0,0,107,108,3,40,
        20,0,108,109,5,44,0,0,109,110,3,6,3,0,110,111,3,18,9,0,111,112,3,
        24,12,0,112,114,1,0,0,0,113,101,1,0,0,0,113,106,1,0,0,0,114,17,1,
        0,0,0,115,118,3,20,10,0,116,118,1,0,0,0,117,115,1,0,0,0,117,116,
        1,0,0,0,118,19,1,0,0,0,119,124,3,22,11,0,120,121,3,22,11,0,121,122,
        3,20,10,0,122,124,1,0,0,0,123,119,1,0,0,0,123,120,1,0,0,0,124,21,
        1,0,0,0,125,126,5,44,0,0,126,127,5,3,0,0,127,128,3,40,20,0,128,129,
        5,44,0,0,129,130,3,6,3,0,130,23,1,0,0,0,131,132,5,44,0,0,132,133,
        5,4,0,0,133,134,5,44,0,0,134,137,3,6,3,0,135,137,1,0,0,0,136,131,
        1,0,0,0,136,135,1,0,0,0,137,25,1,0,0,0,138,139,5,5,0,0,139,140,3,
        40,20,0,140,141,5,37,0,0,141,142,3,40,20,0,142,143,5,38,0,0,143,
        144,3,40,20,0,144,145,5,44,0,0,145,146,3,6,3,0,146,27,1,0,0,0,147,
        148,5,24,0,0,148,157,5,44,0,0,149,154,3,6,3,0,150,151,5,44,0,0,151,
        153,3,6,3,0,152,150,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,
        155,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,157,149,1,0,0,0,157,
        158,1,0,0,0,158,159,1,0,0,0,159,160,5,44,0,0,160,161,5,25,0,0,161,
        29,1,0,0,0,162,163,5,35,0,0,163,164,5,39,0,0,164,170,3,32,16,0,165,
        168,5,44,0,0,166,169,3,14,7,0,167,169,3,28,14,0,168,166,1,0,0,0,
        168,167,1,0,0,0,169,171,1,0,0,0,170,165,1,0,0,0,170,171,1,0,0,0,
        171,31,1,0,0,0,172,189,5,20,0,0,173,174,5,1,0,0,174,176,5,39,0,0,
        175,177,3,34,17,0,176,175,1,0,0,0,176,177,1,0,0,0,177,186,1,0,0,
        0,178,179,5,30,0,0,179,180,5,1,0,0,180,182,5,39,0,0,181,183,3,34,
        17,0,182,181,1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,178,1,0,
        0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,190,1,0,
        0,0,188,186,1,0,0,0,189,173,1,0,0,0,189,190,1,0,0,0,190,191,1,0,
        0,0,191,192,5,21,0,0,192,33,1,0,0,0,193,202,5,22,0,0,194,199,5,40,
        0,0,195,196,5,30,0,0,196,198,5,40,0,0,197,195,1,0,0,0,198,201,1,
        0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,203,1,0,0,0,201,199,1,
        0,0,0,202,194,1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,205,5,
        23,0,0,205,35,1,0,0,0,206,207,3,40,20,0,207,208,5,13,0,0,208,209,
        3,40,20,0,209,37,1,0,0,0,210,211,5,1,0,0,211,212,3,40,20,0,212,213,
        5,13,0,0,213,214,3,40,20,0,214,223,1,0,0,0,215,216,5,28,0,0,216,
        217,3,40,20,0,217,218,5,13,0,0,218,219,3,40,20,0,219,223,1,0,0,0,
        220,221,5,29,0,0,221,223,3,40,20,0,222,210,1,0,0,0,222,215,1,0,0,
        0,222,220,1,0,0,0,223,39,1,0,0,0,224,225,6,20,-1,0,225,226,3,42,
        21,0,226,232,1,0,0,0,227,228,10,2,0,0,228,229,7,0,0,0,229,231,3,
        42,21,0,230,227,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,
        1,0,0,0,233,41,1,0,0,0,234,232,1,0,0,0,235,236,6,21,-1,0,236,237,
        3,44,22,0,237,243,1,0,0,0,238,239,10,2,0,0,239,240,7,1,0,0,240,242,
        3,44,22,0,241,238,1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,244,
        1,0,0,0,244,43,1,0,0,0,245,243,1,0,0,0,246,247,3,46,23,0,247,248,
        7,2,0,0,248,249,3,46,23,0,249,252,1,0,0,0,250,252,3,46,23,0,251,
        246,1,0,0,0,251,250,1,0,0,0,252,45,1,0,0,0,253,254,6,23,-1,0,254,
        255,3,48,24,0,255,261,1,0,0,0,256,257,10,2,0,0,257,258,7,3,0,0,258,
        260,3,48,24,0,259,256,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,
        262,1,0,0,0,262,47,1,0,0,0,263,261,1,0,0,0,264,265,3,50,25,0,265,
        266,5,12,0,0,266,267,3,50,25,0,267,270,1,0,0,0,268,270,3,50,25,0,
        269,264,1,0,0,0,269,268,1,0,0,0,270,49,1,0,0,0,271,272,5,6,0,0,272,
        277,3,50,25,0,273,274,5,26,0,0,274,277,3,50,25,0,275,277,3,52,26,
        0,276,271,1,0,0,0,276,273,1,0,0,0,276,275,1,0,0,0,277,51,1,0,0,0,
        278,279,6,26,-1,0,279,280,3,54,27,0,280,306,1,0,0,0,281,282,10,3,
        0,0,282,283,5,22,0,0,283,287,3,40,20,0,284,286,3,40,20,0,285,284,
        1,0,0,0,286,289,1,0,0,0,287,285,1,0,0,0,287,288,1,0,0,0,288,290,
        1,0,0,0,289,287,1,0,0,0,290,291,5,23,0,0,291,305,1,0,0,0,292,293,
        10,2,0,0,293,301,5,20,0,0,294,298,3,40,20,0,295,297,3,40,20,0,296,
        295,1,0,0,0,297,300,1,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,
        302,1,0,0,0,300,298,1,0,0,0,301,294,1,0,0,0,301,302,1,0,0,0,302,
        303,1,0,0,0,303,305,5,21,0,0,304,281,1,0,0,0,304,292,1,0,0,0,305,
        308,1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,53,1,0,0,0,308,306,
        1,0,0,0,309,318,5,22,0,0,310,311,3,40,20,0,311,315,5,30,0,0,312,
        314,3,40,20,0,313,312,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,315,
        316,1,0,0,0,316,319,1,0,0,0,317,315,1,0,0,0,318,310,1,0,0,0,318,
        319,1,0,0,0,319,320,1,0,0,0,320,341,5,23,0,0,321,341,5,40,0,0,322,
        341,5,43,0,0,323,341,5,39,0,0,324,333,5,22,0,0,325,330,3,40,20,0,
        326,327,5,30,0,0,327,329,3,40,20,0,328,326,1,0,0,0,329,332,1,0,0,
        0,330,328,1,0,0,0,330,331,1,0,0,0,331,334,1,0,0,0,332,330,1,0,0,
        0,333,325,1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,341,5,23,0,
        0,336,337,5,20,0,0,337,338,3,40,20,0,338,339,5,21,0,0,339,341,1,
        0,0,0,340,309,1,0,0,0,340,321,1,0,0,0,340,322,1,0,0,0,340,323,1,
        0,0,0,340,324,1,0,0,0,340,336,1,0,0,0,341,55,1,0,0,0,36,61,66,69,
        76,89,113,117,123,136,154,157,168,170,176,182,186,189,199,202,222,
        232,243,251,261,269,276,287,298,301,304,306,315,318,330,333,340
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
    RULE_stms = 1
    RULE_stm_lists = 2
    RULE_stm = 3
    RULE_r_print = 4
    RULE_r_break = 5
    RULE_r_continue = 6
    RULE_r_return = 7
    RULE_r_if = 8
    RULE_r_elif_list = 9
    RULE_r_elifs = 10
    RULE_r_elif = 11
    RULE_r_else = 12
    RULE_r_for = 13
    RULE_block = 14
    RULE_func = 15
    RULE_args = 16
    RULE_type_index = 17
    RULE_ass = 18
    RULE_decl = 19
    RULE_expr = 20
    RULE_expr1 = 21
    RULE_expr2 = 22
    RULE_expr3 = 23
    RULE_expr4 = 24
    RULE_expr5 = 25
    RULE_expr6 = 26
    RULE_term = 27

    ruleNames =  [ "program", "stms", "stm_lists", "stm", "r_print", "r_break", 
                   "r_continue", "r_return", "r_if", "r_elif_list", "r_elifs", 
                   "r_elif", "r_else", "r_for", "block", "func", "args", 
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

        def stms(self):
            return self.getTypedRuleContext(ZCodeParser.StmsContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.stms()
            self.state = 57
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm_lists(self):
            return self.getTypedRuleContext(ZCodeParser.Stm_listsContext,0)


        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stms




    def stms(self):

        localctx = ZCodeParser.StmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stms)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [44]:
                    self.state = 59
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 43]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 63
                self.stm_lists()
                self.state = 66
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [44]:
                    self.state = 64
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [-1]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

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


    class Stm_listsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def NULL_LINES(self):
            return self.getToken(ZCodeParser.NULL_LINES, 0)

        def stm_lists(self):
            return self.getTypedRuleContext(ZCodeParser.Stm_listsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm_lists




    def stm_lists(self):

        localctx = ZCodeParser.Stm_listsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stm_lists)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.stm()
                self.state = 73
                self.match(ZCodeParser.NULL_LINES)
                self.state = 74
                self.stm_lists()
                pass


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
        self.enterRule(localctx, 6, self.RULE_stm)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 83
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 84
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 85
                self.r_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 86
                self.r_if()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 87
                self.r_for()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 88
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
        self.enterRule(localctx, 8, self.RULE_r_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ZCodeParser.PRINT)
            self.state = 92
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
        self.enterRule(localctx, 10, self.RULE_r_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
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
        self.enterRule(localctx, 12, self.RULE_r_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
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
        self.enterRule(localctx, 14, self.RULE_r_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(ZCodeParser.RETURN)
            self.state = 99
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

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def NULL_LINES(self):
            return self.getToken(ZCodeParser.NULL_LINES, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def r_elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.R_elif_listContext,0)


        def r_else(self):
            return self.getTypedRuleContext(ZCodeParser.R_elseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_if




    def r_if(self):

        localctx = ZCodeParser.R_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_r_if)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(ZCodeParser.IF)
                self.state = 102
                self.expr(0)
                self.state = 103
                self.match(ZCodeParser.NULL_LINES)
                self.state = 104
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(ZCodeParser.IF)
                self.state = 107
                self.expr(0)
                self.state = 108
                self.match(ZCodeParser.NULL_LINES)
                self.state = 109
                self.stm()
                self.state = 110
                self.r_elif_list()
                self.state = 111
                self.r_else()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r_elifs(self):
            return self.getTypedRuleContext(ZCodeParser.R_elifsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_elif_list




    def r_elif_list(self):

        localctx = ZCodeParser.R_elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_r_elif_list)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.r_elifs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_elifsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r_elif(self):
            return self.getTypedRuleContext(ZCodeParser.R_elifContext,0)


        def r_elifs(self):
            return self.getTypedRuleContext(ZCodeParser.R_elifsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_elifs




    def r_elifs(self):

        localctx = ZCodeParser.R_elifsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_r_elifs)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.r_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.r_elif()
                self.state = 121
                self.r_elifs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_elif




    def r_elif(self):

        localctx = ZCodeParser.R_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_r_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(ZCodeParser.NULL_LINES)
            self.state = 126
            self.match(ZCodeParser.ELIF)
            self.state = 127
            self.expr(0)
            self.state = 128
            self.match(ZCodeParser.NULL_LINES)
            self.state = 129
            self.stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_else




    def r_else(self):

        localctx = ZCodeParser.R_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_r_else)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(ZCodeParser.NULL_LINES)
                self.state = 132
                self.match(ZCodeParser.ELSE)
                self.state = 133
                self.match(ZCodeParser.NULL_LINES)
                self.state = 134
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 26, self.RULE_r_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(ZCodeParser.FOR)
            self.state = 139
            self.expr(0)
            self.state = 140
            self.match(ZCodeParser.UNTIL)
            self.state = 141
            self.expr(0)
            self.state = 142
            self.match(ZCodeParser.BY)
            self.state = 143
            self.expr(0)
            self.state = 144
            self.match(ZCodeParser.NULL_LINES)
            self.state = 145
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
        self.enterRule(localctx, 28, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(ZCodeParser.BEGIN)
            self.state = 148
            self.match(ZCodeParser.NULL_LINES)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10512826892390) != 0):
                self.state = 149
                self.stm()
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 150
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 151
                        self.stm() 
                    self.state = 156
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)



            self.state = 159
            self.match(ZCodeParser.NULL_LINES)
            self.state = 160
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
        self.enterRule(localctx, 30, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(ZCodeParser.FUNC)
            self.state = 163
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 164
            self.args()
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 165
                self.match(ZCodeParser.NULL_LINES)
                self.state = 168
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34]:
                    self.state = 166
                    self.r_return()
                    pass
                elif token in [24]:
                    self.state = 167
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
        self.enterRule(localctx, 32, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ZCodeParser.LP)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 173
                self.match(ZCodeParser.TYPE)
                self.state = 174
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 175
                    self.type_index()


                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 178
                    self.match(ZCodeParser.COMMA)
                    self.state = 179
                    self.match(ZCodeParser.TYPE)
                    self.state = 180
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 182
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==22:
                        self.state = 181
                        self.type_index()


                    self.state = 188
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 191
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
        self.enterRule(localctx, 34, self.RULE_type_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(ZCodeParser.LB)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 194
                self.match(ZCodeParser.NUMBER)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 195
                    self.match(ZCodeParser.COMMA)
                    self.state = 196
                    self.match(ZCodeParser.NUMBER)
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 204
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
        self.enterRule(localctx, 36, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expr(0)
            self.state = 207
            self.match(ZCodeParser.ASSIGN)
            self.state = 208
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
        self.enterRule(localctx, 38, self.RULE_decl)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(ZCodeParser.TYPE)
                self.state = 211
                self.expr(0)
                self.state = 212
                self.match(ZCodeParser.ASSIGN)
                self.state = 213
                self.expr(0)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(ZCodeParser.VAR)
                self.state = 216
                self.expr(0)
                self.state = 217
                self.match(ZCodeParser.ASSIGN)
                self.state = 218
                self.expr(0)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(ZCodeParser.DYN)
                self.state = 221
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 227
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 228
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 68719477504) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 229
                    self.expr1(0) 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.expr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 238
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 239
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==6 or _la==7):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 240
                    self.expr2() 
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.expr3(0)
                self.state = 247
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135249920) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 248
                self.expr3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 258
                    self.expr4() 
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_expr4)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.expr5()
                self.state = 265
                self.match(ZCodeParser.CONCAT)
                self.state = 266
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
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
        self.enterRule(localctx, 50, self.RULE_expr5)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(ZCodeParser.SUB)
                self.state = 272
                self.expr5()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(ZCodeParser.NOT)
                self.state = 274
                self.expr5()
                pass
            elif token in [20, 22, 39, 40, 43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 304
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 281
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 282
                        self.match(ZCodeParser.LB)
                        self.state = 283
                        localctx.indexer = self.expr(0)
                        self.state = 287
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                            self.state = 284
                            localctx.COMMAindexer = self.expr(0)
                            self.state = 289
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 290
                        self.match(ZCodeParser.RB)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 292
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 293
                        self.match(ZCodeParser.LP)
                        self.state = 301
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                            self.state = 294
                            localctx.param = self.expr(0)
                            self.state = 298
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                                self.state = 295
                                localctx.COMMAparam = self.expr(0)
                                self.state = 300
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 303
                        self.match(ZCodeParser.RP)
                        pass

             
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(ZCodeParser.LB)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                    self.state = 310
                    self.expr(0)
                    self.state = 311
                    self.match(ZCodeParser.COMMA)
                    self.state = 315
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                        self.state = 312
                        self.expr(0)
                        self.state = 317
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 320
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 324
                self.match(ZCodeParser.LB)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                    self.state = 325
                    self.expr(0)
                    self.state = 330
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==30:
                        self.state = 326
                        self.match(ZCodeParser.COMMA)
                        self.state = 327
                        self.expr(0)
                        self.state = 332
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 335
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 336
                self.match(ZCodeParser.LP)
                self.state = 337
                self.expr(0)
                self.state = 338
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
        self._predicates[20] = self.expr_sempred
        self._predicates[21] = self.expr1_sempred
        self._predicates[23] = self.expr3_sempred
        self._predicates[26] = self.expr6_sempred
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
         




