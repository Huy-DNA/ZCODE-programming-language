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
        4,1,48,363,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,1,1,1,1,3,1,76,8,1,1,1,1,1,1,1,3,1,81,
        8,1,1,1,3,1,84,8,1,1,2,1,2,1,2,1,2,1,2,3,2,91,8,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,104,8,3,1,4,1,4,1,4,1,5,1,5,1,
        6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,3,8,128,8,8,1,9,1,9,3,9,132,8,9,1,10,1,10,1,10,1,10,3,10,138,8,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,151,
        8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,15,1,15,3,15,170,8,15,1,16,1,16,1,16,1,16,1,16,
        3,16,177,8,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,185,8,17,1,17,3,
        17,188,8,17,1,18,1,18,1,18,1,18,1,19,1,19,3,19,196,8,19,1,20,1,20,
        1,20,1,20,1,20,3,20,203,8,20,1,21,1,21,1,21,1,21,3,21,209,8,21,1,
        22,1,22,1,22,1,22,1,23,1,23,3,23,217,8,23,1,24,1,24,1,24,1,24,3,
        24,223,8,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,3,26,241,8,26,1,27,1,27,1,27,1,27,1,
        27,1,27,5,27,249,8,27,10,27,12,27,252,9,27,1,28,1,28,1,28,1,28,1,
        28,1,28,5,28,260,8,28,10,28,12,28,263,9,28,1,29,1,29,1,29,1,29,1,
        29,3,29,270,8,29,1,30,1,30,1,30,1,30,1,30,1,30,5,30,278,8,30,10,
        30,12,30,281,9,30,1,31,1,31,1,31,1,31,1,31,3,31,288,8,31,1,32,1,
        32,1,32,1,32,1,32,3,32,295,8,32,1,33,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,5,33,305,8,33,10,33,12,33,308,9,33,1,33,1,33,1,33,1,33,1,
        33,1,33,1,33,5,33,317,8,33,10,33,12,33,320,9,33,3,33,322,8,33,1,
        33,5,33,325,8,33,10,33,12,33,328,9,33,1,34,1,34,1,34,1,34,5,34,334,
        8,34,10,34,12,34,337,9,34,3,34,339,8,34,1,34,1,34,1,34,1,34,1,34,
        1,34,1,34,1,34,5,34,349,8,34,10,34,12,34,352,9,34,3,34,354,8,34,
        1,34,1,34,1,34,1,34,1,34,3,34,361,8,34,1,34,0,4,54,56,60,66,35,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,66,68,0,4,2,0,8,9,36,36,1,0,6,7,2,0,14,
        19,27,27,1,0,10,11,377,0,70,1,0,0,0,2,83,1,0,0,0,4,90,1,0,0,0,6,
        103,1,0,0,0,8,105,1,0,0,0,10,108,1,0,0,0,12,110,1,0,0,0,14,112,1,
        0,0,0,16,127,1,0,0,0,18,131,1,0,0,0,20,137,1,0,0,0,22,139,1,0,0,
        0,24,150,1,0,0,0,26,152,1,0,0,0,28,161,1,0,0,0,30,169,1,0,0,0,32,
        176,1,0,0,0,34,178,1,0,0,0,36,189,1,0,0,0,38,195,1,0,0,0,40,202,
        1,0,0,0,42,204,1,0,0,0,44,210,1,0,0,0,46,216,1,0,0,0,48,222,1,0,
        0,0,50,224,1,0,0,0,52,240,1,0,0,0,54,242,1,0,0,0,56,253,1,0,0,0,
        58,269,1,0,0,0,60,271,1,0,0,0,62,287,1,0,0,0,64,294,1,0,0,0,66,296,
        1,0,0,0,68,360,1,0,0,0,70,71,3,2,1,0,71,72,5,0,0,1,72,1,1,0,0,0,
        73,76,5,44,0,0,74,76,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,77,1,
        0,0,0,77,80,3,4,2,0,78,81,5,44,0,0,79,81,1,0,0,0,80,78,1,0,0,0,80,
        79,1,0,0,0,81,84,1,0,0,0,82,84,1,0,0,0,83,75,1,0,0,0,83,82,1,0,0,
        0,84,3,1,0,0,0,85,91,3,6,3,0,86,87,3,6,3,0,87,88,5,44,0,0,88,89,
        3,4,2,0,89,91,1,0,0,0,90,85,1,0,0,0,90,86,1,0,0,0,91,5,1,0,0,0,92,
        104,3,54,27,0,93,104,3,52,26,0,94,104,3,50,25,0,95,104,3,28,14,0,
        96,104,3,34,17,0,97,104,3,10,5,0,98,104,3,12,6,0,99,104,3,14,7,0,
        100,104,3,16,8,0,101,104,3,26,13,0,102,104,3,8,4,0,103,92,1,0,0,
        0,103,93,1,0,0,0,103,94,1,0,0,0,103,95,1,0,0,0,103,96,1,0,0,0,103,
        97,1,0,0,0,103,98,1,0,0,0,103,99,1,0,0,0,103,100,1,0,0,0,103,101,
        1,0,0,0,103,102,1,0,0,0,104,7,1,0,0,0,105,106,5,31,0,0,106,107,3,
        54,27,0,107,9,1,0,0,0,108,109,5,32,0,0,109,11,1,0,0,0,110,111,5,
        33,0,0,111,13,1,0,0,0,112,113,5,34,0,0,113,114,3,54,27,0,114,15,
        1,0,0,0,115,116,5,2,0,0,116,117,3,54,27,0,117,118,5,44,0,0,118,119,
        3,6,3,0,119,128,1,0,0,0,120,121,5,2,0,0,121,122,3,54,27,0,122,123,
        5,44,0,0,123,124,3,6,3,0,124,125,3,18,9,0,125,126,3,24,12,0,126,
        128,1,0,0,0,127,115,1,0,0,0,127,120,1,0,0,0,128,17,1,0,0,0,129,132,
        3,20,10,0,130,132,1,0,0,0,131,129,1,0,0,0,131,130,1,0,0,0,132,19,
        1,0,0,0,133,138,3,22,11,0,134,135,3,22,11,0,135,136,3,20,10,0,136,
        138,1,0,0,0,137,133,1,0,0,0,137,134,1,0,0,0,138,21,1,0,0,0,139,140,
        5,44,0,0,140,141,5,3,0,0,141,142,3,54,27,0,142,143,5,44,0,0,143,
        144,3,6,3,0,144,23,1,0,0,0,145,146,5,44,0,0,146,147,5,4,0,0,147,
        148,5,44,0,0,148,151,3,6,3,0,149,151,1,0,0,0,150,145,1,0,0,0,150,
        149,1,0,0,0,151,25,1,0,0,0,152,153,5,5,0,0,153,154,3,54,27,0,154,
        155,5,37,0,0,155,156,3,54,27,0,156,157,5,38,0,0,157,158,3,54,27,
        0,158,159,5,44,0,0,159,160,3,6,3,0,160,27,1,0,0,0,161,162,5,24,0,
        0,162,163,5,44,0,0,163,164,3,30,15,0,164,165,5,44,0,0,165,166,5,
        25,0,0,166,29,1,0,0,0,167,170,3,32,16,0,168,170,1,0,0,0,169,167,
        1,0,0,0,169,168,1,0,0,0,170,31,1,0,0,0,171,177,3,6,3,0,172,173,3,
        6,3,0,173,174,5,44,0,0,174,175,3,32,16,0,175,177,1,0,0,0,176,171,
        1,0,0,0,176,172,1,0,0,0,177,33,1,0,0,0,178,179,5,35,0,0,179,180,
        5,39,0,0,180,187,3,36,18,0,181,184,5,44,0,0,182,185,3,14,7,0,183,
        185,3,28,14,0,184,182,1,0,0,0,184,183,1,0,0,0,185,188,1,0,0,0,186,
        188,1,0,0,0,187,181,1,0,0,0,187,186,1,0,0,0,188,35,1,0,0,0,189,190,
        5,20,0,0,190,191,3,38,19,0,191,192,5,21,0,0,192,37,1,0,0,0,193,196,
        3,40,20,0,194,196,1,0,0,0,195,193,1,0,0,0,195,194,1,0,0,0,196,39,
        1,0,0,0,197,203,3,42,21,0,198,199,3,42,21,0,199,200,5,30,0,0,200,
        201,3,40,20,0,201,203,1,0,0,0,202,197,1,0,0,0,202,198,1,0,0,0,203,
        41,1,0,0,0,204,205,5,1,0,0,205,208,5,39,0,0,206,209,3,44,22,0,207,
        209,1,0,0,0,208,206,1,0,0,0,208,207,1,0,0,0,209,43,1,0,0,0,210,211,
        5,22,0,0,211,212,3,46,23,0,212,213,5,23,0,0,213,45,1,0,0,0,214,217,
        3,48,24,0,215,217,1,0,0,0,216,214,1,0,0,0,216,215,1,0,0,0,217,47,
        1,0,0,0,218,223,5,40,0,0,219,220,5,40,0,0,220,221,5,30,0,0,221,223,
        3,48,24,0,222,218,1,0,0,0,222,219,1,0,0,0,223,49,1,0,0,0,224,225,
        3,54,27,0,225,226,5,13,0,0,226,227,3,54,27,0,227,51,1,0,0,0,228,
        229,5,1,0,0,229,230,3,54,27,0,230,231,5,13,0,0,231,232,3,54,27,0,
        232,241,1,0,0,0,233,234,5,28,0,0,234,235,3,54,27,0,235,236,5,13,
        0,0,236,237,3,54,27,0,237,241,1,0,0,0,238,239,5,29,0,0,239,241,3,
        54,27,0,240,228,1,0,0,0,240,233,1,0,0,0,240,238,1,0,0,0,241,53,1,
        0,0,0,242,243,6,27,-1,0,243,244,3,56,28,0,244,250,1,0,0,0,245,246,
        10,2,0,0,246,247,7,0,0,0,247,249,3,56,28,0,248,245,1,0,0,0,249,252,
        1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,55,1,0,0,0,252,250,1,
        0,0,0,253,254,6,28,-1,0,254,255,3,58,29,0,255,261,1,0,0,0,256,257,
        10,2,0,0,257,258,7,1,0,0,258,260,3,58,29,0,259,256,1,0,0,0,260,263,
        1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,57,1,0,0,0,263,261,1,
        0,0,0,264,265,3,60,30,0,265,266,7,2,0,0,266,267,3,60,30,0,267,270,
        1,0,0,0,268,270,3,60,30,0,269,264,1,0,0,0,269,268,1,0,0,0,270,59,
        1,0,0,0,271,272,6,30,-1,0,272,273,3,62,31,0,273,279,1,0,0,0,274,
        275,10,2,0,0,275,276,7,3,0,0,276,278,3,62,31,0,277,274,1,0,0,0,278,
        281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,61,1,0,0,0,281,279,
        1,0,0,0,282,283,3,64,32,0,283,284,5,12,0,0,284,285,3,64,32,0,285,
        288,1,0,0,0,286,288,3,64,32,0,287,282,1,0,0,0,287,286,1,0,0,0,288,
        63,1,0,0,0,289,290,5,6,0,0,290,295,3,64,32,0,291,292,5,26,0,0,292,
        295,3,64,32,0,293,295,3,66,33,0,294,289,1,0,0,0,294,291,1,0,0,0,
        294,293,1,0,0,0,295,65,1,0,0,0,296,297,6,33,-1,0,297,298,3,68,34,
        0,298,326,1,0,0,0,299,300,10,3,0,0,300,301,5,22,0,0,301,306,3,54,
        27,0,302,303,5,30,0,0,303,305,3,54,27,0,304,302,1,0,0,0,305,308,
        1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,309,1,0,0,0,308,306,
        1,0,0,0,309,310,5,23,0,0,310,325,1,0,0,0,311,312,10,2,0,0,312,321,
        5,20,0,0,313,318,3,54,27,0,314,315,5,30,0,0,315,317,3,54,27,0,316,
        314,1,0,0,0,317,320,1,0,0,0,318,316,1,0,0,0,318,319,1,0,0,0,319,
        322,1,0,0,0,320,318,1,0,0,0,321,313,1,0,0,0,321,322,1,0,0,0,322,
        323,1,0,0,0,323,325,5,21,0,0,324,299,1,0,0,0,324,311,1,0,0,0,325,
        328,1,0,0,0,326,324,1,0,0,0,326,327,1,0,0,0,327,67,1,0,0,0,328,326,
        1,0,0,0,329,338,5,22,0,0,330,331,3,54,27,0,331,335,5,30,0,0,332,
        334,3,54,27,0,333,332,1,0,0,0,334,337,1,0,0,0,335,333,1,0,0,0,335,
        336,1,0,0,0,336,339,1,0,0,0,337,335,1,0,0,0,338,330,1,0,0,0,338,
        339,1,0,0,0,339,340,1,0,0,0,340,361,5,23,0,0,341,361,5,40,0,0,342,
        361,5,43,0,0,343,361,5,39,0,0,344,353,5,22,0,0,345,350,3,54,27,0,
        346,347,5,30,0,0,347,349,3,54,27,0,348,346,1,0,0,0,349,352,1,0,0,
        0,350,348,1,0,0,0,350,351,1,0,0,0,351,354,1,0,0,0,352,350,1,0,0,
        0,353,345,1,0,0,0,353,354,1,0,0,0,354,355,1,0,0,0,355,361,5,23,0,
        0,356,357,5,20,0,0,357,358,3,54,27,0,358,359,5,21,0,0,359,361,1,
        0,0,0,360,329,1,0,0,0,360,341,1,0,0,0,360,342,1,0,0,0,360,343,1,
        0,0,0,360,344,1,0,0,0,360,356,1,0,0,0,361,69,1,0,0,0,35,75,80,83,
        90,103,127,131,137,150,169,176,184,187,195,202,208,216,222,240,250,
        261,269,279,287,294,306,318,321,324,326,335,338,350,353,360
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
    RULE_block_stms = 15
    RULE_block_stm_list = 16
    RULE_func = 17
    RULE_arg_group = 18
    RULE_args = 19
    RULE_arg_list = 20
    RULE_arg = 21
    RULE_type_index = 22
    RULE_type_index_nums = 23
    RULE_type_index_num_list = 24
    RULE_ass = 25
    RULE_decl = 26
    RULE_expr = 27
    RULE_expr1 = 28
    RULE_expr2 = 29
    RULE_expr3 = 30
    RULE_expr4 = 31
    RULE_expr5 = 32
    RULE_expr6 = 33
    RULE_term = 34

    ruleNames =  [ "program", "stms", "stm_lists", "stm", "r_print", "r_break", 
                   "r_continue", "r_return", "r_if", "r_elif_list", "r_elifs", 
                   "r_elif", "r_else", "r_for", "block", "block_stms", "block_stm_list", 
                   "func", "arg_group", "args", "arg_list", "arg", "type_index", 
                   "type_index_nums", "type_index_num_list", "ass", "decl", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "term" ]

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
            self.state = 70
            self.stms()
            self.state = 71
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
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [44]:
                    self.state = 73
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 43]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 77
                self.stm_lists()
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [44]:
                    self.state = 78
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
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.stm()
                self.state = 87
                self.match(ZCodeParser.NULL_LINES)
                self.state = 88
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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 97
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 98
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 99
                self.r_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 100
                self.r_if()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 101
                self.r_for()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 102
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
            self.state = 105
            self.match(ZCodeParser.PRINT)
            self.state = 106
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
            self.state = 108
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
            self.state = 110
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
            self.state = 112
            self.match(ZCodeParser.RETURN)
            self.state = 113
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(ZCodeParser.IF)
                self.state = 116
                self.expr(0)
                self.state = 117
                self.match(ZCodeParser.NULL_LINES)
                self.state = 118
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(ZCodeParser.IF)
                self.state = 121
                self.expr(0)
                self.state = 122
                self.match(ZCodeParser.NULL_LINES)
                self.state = 123
                self.stm()
                self.state = 124
                self.r_elif_list()
                self.state = 125
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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
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
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.r_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.r_elif()
                self.state = 135
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
            self.state = 139
            self.match(ZCodeParser.NULL_LINES)
            self.state = 140
            self.match(ZCodeParser.ELIF)
            self.state = 141
            self.expr(0)
            self.state = 142
            self.match(ZCodeParser.NULL_LINES)
            self.state = 143
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
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(ZCodeParser.NULL_LINES)
                self.state = 146
                self.match(ZCodeParser.ELSE)
                self.state = 147
                self.match(ZCodeParser.NULL_LINES)
                self.state = 148
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
            self.state = 152
            self.match(ZCodeParser.FOR)
            self.state = 153
            self.expr(0)
            self.state = 154
            self.match(ZCodeParser.UNTIL)
            self.state = 155
            self.expr(0)
            self.state = 156
            self.match(ZCodeParser.BY)
            self.state = 157
            self.expr(0)
            self.state = 158
            self.match(ZCodeParser.NULL_LINES)
            self.state = 159
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

        def block_stms(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmsContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ZCodeParser.BEGIN)
            self.state = 162
            self.match(ZCodeParser.NULL_LINES)
            self.state = 163
            self.block_stms()
            self.state = 164
            self.match(ZCodeParser.NULL_LINES)
            self.state = 165
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stm_list(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stm_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stms




    def block_stms(self):

        localctx = ZCodeParser.Block_stmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block_stms)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.block_stm_list()
                pass
            elif token in [44]:
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


    class Block_stm_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def NULL_LINES(self):
            return self.getToken(ZCodeParser.NULL_LINES, 0)

        def block_stm_list(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stm_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stm_list




    def block_stm_list(self):

        localctx = ZCodeParser.Block_stm_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block_stm_list)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.stm()
                self.state = 173
                self.match(ZCodeParser.NULL_LINES)
                self.state = 174
                self.block_stm_list()
                pass


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

        def arg_group(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_groupContext,0)


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
        self.enterRule(localctx, 34, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ZCodeParser.FUNC)
            self.state = 179
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 180
            self.arg_group()
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 181
                self.match(ZCodeParser.NULL_LINES)
                self.state = 184
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34]:
                    self.state = 182
                    self.r_return()
                    pass
                elif token in [24]:
                    self.state = 183
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def args(self):
            return self.getTypedRuleContext(ZCodeParser.ArgsContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arg_group




    def arg_group(self):

        localctx = ZCodeParser.Arg_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arg_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(ZCodeParser.LP)
            self.state = 190
            self.args()
            self.state = 191
            self.match(ZCodeParser.RP)
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

        def arg_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_args




    def args(self):

        localctx = ZCodeParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_args)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.arg_list()
                pass
            elif token in [21]:
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


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self):
            return self.getTypedRuleContext(ZCodeParser.ArgContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arg_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg_list




    def arg_list(self):

        localctx = ZCodeParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arg_list)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.arg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.arg()
                self.state = 199
                self.match(ZCodeParser.COMMA)
                self.state = 200
                self.arg_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(ZCodeParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def type_index(self):
            return self.getTypedRuleContext(ZCodeParser.Type_indexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg




    def arg(self):

        localctx = ZCodeParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ZCodeParser.TYPE)
            self.state = 205
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 206
                self.type_index()
                pass
            elif token in [21, 30]:
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


    class Type_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def type_index_nums(self):
            return self.getTypedRuleContext(ZCodeParser.Type_index_numsContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type_index




    def type_index(self):

        localctx = ZCodeParser.Type_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_type_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ZCodeParser.LB)
            self.state = 211
            self.type_index_nums()
            self.state = 212
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_index_numsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_index_num_list(self):
            return self.getTypedRuleContext(ZCodeParser.Type_index_num_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_type_index_nums




    def type_index_nums(self):

        localctx = ZCodeParser.Type_index_numsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_type_index_nums)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.type_index_num_list()
                pass
            elif token in [23]:
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


    class Type_index_num_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def type_index_num_list(self):
            return self.getTypedRuleContext(ZCodeParser.Type_index_num_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_type_index_num_list




    def type_index_num_list(self):

        localctx = ZCodeParser.Type_index_num_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_type_index_num_list)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(ZCodeParser.NUMBER)
                self.state = 220
                self.match(ZCodeParser.COMMA)
                self.state = 221
                self.type_index_num_list()
                pass


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
        self.enterRule(localctx, 50, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.expr(0)
            self.state = 225
            self.match(ZCodeParser.ASSIGN)
            self.state = 226
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
        self.enterRule(localctx, 52, self.RULE_decl)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(ZCodeParser.TYPE)
                self.state = 229
                self.expr(0)
                self.state = 230
                self.match(ZCodeParser.ASSIGN)
                self.state = 231
                self.expr(0)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(ZCodeParser.VAR)
                self.state = 234
                self.expr(0)
                self.state = 235
                self.match(ZCodeParser.ASSIGN)
                self.state = 236
                self.expr(0)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.match(ZCodeParser.DYN)
                self.state = 239
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 245
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 246
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 68719477504) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 247
                    self.expr1(0) 
                self.state = 252
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.expr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==6 or _la==7):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 258
                    self.expr2() 
                self.state = 263
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
        self.enterRule(localctx, 58, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.expr3(0)
                self.state = 265
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135249920) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 266
                self.expr3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 274
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 275
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 276
                    self.expr4() 
                self.state = 281
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
        self.enterRule(localctx, 62, self.RULE_expr4)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.expr5()
                self.state = 283
                self.match(ZCodeParser.CONCAT)
                self.state = 284
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
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
        self.enterRule(localctx, 64, self.RULE_expr5)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(ZCodeParser.SUB)
                self.state = 290
                self.expr5()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.match(ZCodeParser.NOT)
                self.state = 292
                self.expr5()
                pass
            elif token in [20, 22, 39, 40, 43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 293
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
            self.param = None # ExprContext

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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 324
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 299
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 300
                        self.match(ZCodeParser.LB)
                        self.state = 301
                        localctx.indexer = self.expr(0)
                        self.state = 306
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==30:
                            self.state = 302
                            self.match(ZCodeParser.COMMA)
                            self.state = 303
                            localctx.indexer = self.expr(0)
                            self.state = 308
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 309
                        self.match(ZCodeParser.RB)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 311
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 312
                        self.match(ZCodeParser.LP)
                        self.state = 321
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                            self.state = 313
                            localctx.param = self.expr(0)
                            self.state = 318
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==30:
                                self.state = 314
                                self.match(ZCodeParser.COMMA)
                                self.state = 315
                                localctx.param = self.expr(0)
                                self.state = 320
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 323
                        self.match(ZCodeParser.RP)
                        pass

             
                self.state = 328
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
        self.enterRule(localctx, 68, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(ZCodeParser.LB)
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                    self.state = 330
                    self.expr(0)
                    self.state = 331
                    self.match(ZCodeParser.COMMA)
                    self.state = 335
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                        self.state = 332
                        self.expr(0)
                        self.state = 337
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 340
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 342
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 343
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 344
                self.match(ZCodeParser.LB)
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10445432815680) != 0):
                    self.state = 345
                    self.expr(0)
                    self.state = 350
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==30:
                        self.state = 346
                        self.match(ZCodeParser.COMMA)
                        self.state = 347
                        self.expr(0)
                        self.state = 352
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 355
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 356
                self.match(ZCodeParser.LP)
                self.state = 357
                self.expr(0)
                self.state = 358
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
        self._predicates[27] = self.expr_sempred
        self._predicates[28] = self.expr1_sempred
        self._predicates[30] = self.expr3_sempred
        self._predicates[33] = self.expr6_sempred
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
         




