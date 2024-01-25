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
        4,1,49,373,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,0,1,1,1,1,3,1,78,8,1,1,1,1,1,
        1,1,3,1,83,8,1,1,1,3,1,86,8,1,1,2,1,2,1,2,1,2,1,2,3,2,93,8,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,106,8,3,1,4,1,4,1,4,
        1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,122,8,8,1,8,1,8,
        1,8,1,8,1,8,1,8,3,8,130,8,8,1,8,1,8,1,8,1,8,3,8,136,8,8,1,9,1,9,
        3,9,140,8,9,1,10,1,10,1,10,1,10,3,10,146,8,10,1,11,1,11,3,11,150,
        8,11,1,11,1,11,1,11,1,11,3,11,156,8,11,1,11,1,11,1,12,1,12,3,12,
        162,8,12,1,12,1,12,1,12,3,12,167,8,12,1,12,1,12,3,12,171,8,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,181,8,13,1,13,1,13,1,
        14,1,14,1,14,1,14,1,14,1,14,3,14,191,8,14,1,14,1,14,1,15,1,15,1,
        15,1,15,1,15,3,15,200,8,15,1,16,1,16,1,16,1,16,1,16,3,16,207,8,16,
        1,16,1,16,3,16,211,8,16,1,16,3,16,214,8,16,1,17,1,17,1,17,1,17,1,
        18,1,18,3,18,222,8,18,1,19,1,19,1,19,1,19,1,19,3,19,229,8,19,1,20,
        1,20,1,20,1,20,3,20,235,8,20,1,21,1,21,1,21,1,21,1,22,1,22,3,22,
        243,8,22,1,23,1,23,1,23,1,23,3,23,249,8,23,1,24,1,24,1,24,1,24,1,
        25,1,25,1,25,1,25,3,25,259,8,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,3,25,270,8,25,1,26,1,26,1,26,1,26,1,26,3,26,277,8,26,
        1,27,1,27,1,27,1,27,1,27,3,27,284,8,27,1,28,1,28,1,28,1,28,1,28,
        1,28,5,28,292,8,28,10,28,12,28,295,9,28,1,29,1,29,1,29,1,29,1,29,
        1,29,5,29,303,8,29,10,29,12,29,306,9,29,1,30,1,30,1,30,1,30,1,30,
        1,30,5,30,314,8,30,10,30,12,30,317,9,30,1,31,1,31,1,31,1,31,1,31,
        3,31,324,8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,5,32,339,8,32,10,32,12,32,342,9,32,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
        3,33,360,8,33,1,34,1,34,3,34,364,8,34,1,35,1,35,1,35,1,35,1,35,3,
        35,371,8,35,1,35,0,4,56,58,60,64,36,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,0,4,2,0,14,19,27,27,1,0,10,11,1,0,6,7,2,0,8,9,36,36,391,
        0,72,1,0,0,0,2,85,1,0,0,0,4,92,1,0,0,0,6,105,1,0,0,0,8,107,1,0,0,
        0,10,110,1,0,0,0,12,112,1,0,0,0,14,114,1,0,0,0,16,135,1,0,0,0,18,
        139,1,0,0,0,20,145,1,0,0,0,22,149,1,0,0,0,24,170,1,0,0,0,26,172,
        1,0,0,0,28,184,1,0,0,0,30,199,1,0,0,0,32,201,1,0,0,0,34,215,1,0,
        0,0,36,221,1,0,0,0,38,228,1,0,0,0,40,230,1,0,0,0,42,236,1,0,0,0,
        44,242,1,0,0,0,46,248,1,0,0,0,48,250,1,0,0,0,50,269,1,0,0,0,52,276,
        1,0,0,0,54,283,1,0,0,0,56,285,1,0,0,0,58,296,1,0,0,0,60,307,1,0,
        0,0,62,323,1,0,0,0,64,325,1,0,0,0,66,359,1,0,0,0,68,363,1,0,0,0,
        70,370,1,0,0,0,72,73,3,2,1,0,73,74,5,0,0,1,74,1,1,0,0,0,75,78,5,
        45,0,0,76,78,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,79,1,0,0,0,79,
        82,3,4,2,0,80,83,5,45,0,0,81,83,1,0,0,0,82,80,1,0,0,0,82,81,1,0,
        0,0,83,86,1,0,0,0,84,86,1,0,0,0,85,77,1,0,0,0,85,84,1,0,0,0,86,3,
        1,0,0,0,87,93,3,6,3,0,88,89,3,6,3,0,89,90,5,45,0,0,90,91,3,4,2,0,
        91,93,1,0,0,0,92,87,1,0,0,0,92,88,1,0,0,0,93,5,1,0,0,0,94,106,3,
        52,26,0,95,106,3,50,25,0,96,106,3,48,24,0,97,106,3,28,14,0,98,106,
        3,32,16,0,99,106,3,10,5,0,100,106,3,12,6,0,101,106,3,14,7,0,102,
        106,3,16,8,0,103,106,3,26,13,0,104,106,3,8,4,0,105,94,1,0,0,0,105,
        95,1,0,0,0,105,96,1,0,0,0,105,97,1,0,0,0,105,98,1,0,0,0,105,99,1,
        0,0,0,105,100,1,0,0,0,105,101,1,0,0,0,105,102,1,0,0,0,105,103,1,
        0,0,0,105,104,1,0,0,0,106,7,1,0,0,0,107,108,5,31,0,0,108,109,3,52,
        26,0,109,9,1,0,0,0,110,111,5,32,0,0,111,11,1,0,0,0,112,113,5,33,
        0,0,113,13,1,0,0,0,114,115,5,34,0,0,115,116,3,52,26,0,116,15,1,0,
        0,0,117,118,5,2,0,0,118,121,3,52,26,0,119,122,5,45,0,0,120,122,1,
        0,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,123,1,0,0,0,123,124,3,
        6,3,0,124,136,1,0,0,0,125,126,5,2,0,0,126,129,3,52,26,0,127,130,
        5,45,0,0,128,130,1,0,0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,131,
        1,0,0,0,131,132,3,6,3,0,132,133,3,18,9,0,133,134,3,24,12,0,134,136,
        1,0,0,0,135,117,1,0,0,0,135,125,1,0,0,0,136,17,1,0,0,0,137,140,3,
        20,10,0,138,140,1,0,0,0,139,137,1,0,0,0,139,138,1,0,0,0,140,19,1,
        0,0,0,141,146,3,22,11,0,142,143,3,22,11,0,143,144,3,20,10,0,144,
        146,1,0,0,0,145,141,1,0,0,0,145,142,1,0,0,0,146,21,1,0,0,0,147,150,
        5,45,0,0,148,150,1,0,0,0,149,147,1,0,0,0,149,148,1,0,0,0,150,151,
        1,0,0,0,151,152,5,3,0,0,152,155,3,52,26,0,153,156,5,45,0,0,154,156,
        1,0,0,0,155,153,1,0,0,0,155,154,1,0,0,0,156,157,1,0,0,0,157,158,
        3,6,3,0,158,23,1,0,0,0,159,162,5,45,0,0,160,162,1,0,0,0,161,159,
        1,0,0,0,161,160,1,0,0,0,162,163,1,0,0,0,163,166,5,4,0,0,164,167,
        5,45,0,0,165,167,1,0,0,0,166,164,1,0,0,0,166,165,1,0,0,0,167,168,
        1,0,0,0,168,171,3,6,3,0,169,171,1,0,0,0,170,161,1,0,0,0,170,169,
        1,0,0,0,171,25,1,0,0,0,172,173,5,5,0,0,173,174,3,52,26,0,174,175,
        5,37,0,0,175,176,3,52,26,0,176,177,5,38,0,0,177,180,3,52,26,0,178,
        181,5,45,0,0,179,181,1,0,0,0,180,178,1,0,0,0,180,179,1,0,0,0,181,
        182,1,0,0,0,182,183,3,6,3,0,183,27,1,0,0,0,184,190,5,24,0,0,185,
        186,5,45,0,0,186,187,3,30,15,0,187,188,5,45,0,0,188,191,1,0,0,0,
        189,191,5,45,0,0,190,185,1,0,0,0,190,189,1,0,0,0,191,192,1,0,0,0,
        192,193,5,25,0,0,193,29,1,0,0,0,194,200,3,6,3,0,195,196,3,6,3,0,
        196,197,5,45,0,0,197,198,3,30,15,0,198,200,1,0,0,0,199,194,1,0,0,
        0,199,195,1,0,0,0,200,31,1,0,0,0,201,202,5,35,0,0,202,203,5,40,0,
        0,203,213,3,34,17,0,204,207,5,45,0,0,205,207,1,0,0,0,206,204,1,0,
        0,0,206,205,1,0,0,0,207,210,1,0,0,0,208,211,3,14,7,0,209,211,3,28,
        14,0,210,208,1,0,0,0,210,209,1,0,0,0,211,214,1,0,0,0,212,214,1,0,
        0,0,213,206,1,0,0,0,213,212,1,0,0,0,214,33,1,0,0,0,215,216,5,20,
        0,0,216,217,3,36,18,0,217,218,5,21,0,0,218,35,1,0,0,0,219,222,3,
        38,19,0,220,222,1,0,0,0,221,219,1,0,0,0,221,220,1,0,0,0,222,37,1,
        0,0,0,223,229,3,40,20,0,224,225,3,40,20,0,225,226,5,30,0,0,226,227,
        3,38,19,0,227,229,1,0,0,0,228,223,1,0,0,0,228,224,1,0,0,0,229,39,
        1,0,0,0,230,231,5,1,0,0,231,234,5,40,0,0,232,235,3,42,21,0,233,235,
        1,0,0,0,234,232,1,0,0,0,234,233,1,0,0,0,235,41,1,0,0,0,236,237,5,
        22,0,0,237,238,3,44,22,0,238,239,5,23,0,0,239,43,1,0,0,0,240,243,
        3,46,23,0,241,243,1,0,0,0,242,240,1,0,0,0,242,241,1,0,0,0,243,45,
        1,0,0,0,244,249,5,41,0,0,245,246,5,41,0,0,246,247,5,30,0,0,247,249,
        3,46,23,0,248,244,1,0,0,0,248,245,1,0,0,0,249,47,1,0,0,0,250,251,
        3,52,26,0,251,252,5,13,0,0,252,253,3,52,26,0,253,49,1,0,0,0,254,
        255,5,1,0,0,255,258,5,40,0,0,256,259,3,42,21,0,257,259,1,0,0,0,258,
        256,1,0,0,0,258,257,1,0,0,0,259,260,1,0,0,0,260,261,5,13,0,0,261,
        270,3,52,26,0,262,263,5,28,0,0,263,264,3,52,26,0,264,265,5,13,0,
        0,265,266,3,52,26,0,266,270,1,0,0,0,267,268,5,29,0,0,268,270,3,52,
        26,0,269,254,1,0,0,0,269,262,1,0,0,0,269,267,1,0,0,0,270,51,1,0,
        0,0,271,272,3,54,27,0,272,273,5,12,0,0,273,274,3,54,27,0,274,277,
        1,0,0,0,275,277,3,54,27,0,276,271,1,0,0,0,276,275,1,0,0,0,277,53,
        1,0,0,0,278,279,3,56,28,0,279,280,7,0,0,0,280,281,3,56,28,0,281,
        284,1,0,0,0,282,284,3,56,28,0,283,278,1,0,0,0,283,282,1,0,0,0,284,
        55,1,0,0,0,285,286,6,28,-1,0,286,287,3,58,29,0,287,293,1,0,0,0,288,
        289,10,2,0,0,289,290,7,1,0,0,290,292,3,58,29,0,291,288,1,0,0,0,292,
        295,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,57,1,0,0,0,295,293,
        1,0,0,0,296,297,6,29,-1,0,297,298,3,60,30,0,298,304,1,0,0,0,299,
        300,10,2,0,0,300,301,7,2,0,0,301,303,3,60,30,0,302,299,1,0,0,0,303,
        306,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,59,1,0,0,0,306,304,
        1,0,0,0,307,308,6,30,-1,0,308,309,3,62,31,0,309,315,1,0,0,0,310,
        311,10,2,0,0,311,312,7,3,0,0,312,314,3,62,31,0,313,310,1,0,0,0,314,
        317,1,0,0,0,315,313,1,0,0,0,315,316,1,0,0,0,316,61,1,0,0,0,317,315,
        1,0,0,0,318,319,5,6,0,0,319,324,3,62,31,0,320,321,5,26,0,0,321,324,
        3,62,31,0,322,324,3,64,32,0,323,318,1,0,0,0,323,320,1,0,0,0,323,
        322,1,0,0,0,324,63,1,0,0,0,325,326,6,32,-1,0,326,327,3,66,33,0,327,
        340,1,0,0,0,328,329,10,3,0,0,329,330,5,22,0,0,330,331,3,68,34,0,
        331,332,5,23,0,0,332,339,1,0,0,0,333,334,10,2,0,0,334,335,5,20,0,
        0,335,336,3,68,34,0,336,337,5,21,0,0,337,339,1,0,0,0,338,328,1,0,
        0,0,338,333,1,0,0,0,339,342,1,0,0,0,340,338,1,0,0,0,340,341,1,0,
        0,0,341,65,1,0,0,0,342,340,1,0,0,0,343,344,5,22,0,0,344,345,3,68,
        34,0,345,346,5,23,0,0,346,360,1,0,0,0,347,360,5,41,0,0,348,360,5,
        44,0,0,349,360,5,39,0,0,350,360,5,40,0,0,351,352,5,22,0,0,352,353,
        3,68,34,0,353,354,5,23,0,0,354,360,1,0,0,0,355,356,5,20,0,0,356,
        357,3,52,26,0,357,358,5,21,0,0,358,360,1,0,0,0,359,343,1,0,0,0,359,
        347,1,0,0,0,359,348,1,0,0,0,359,349,1,0,0,0,359,350,1,0,0,0,359,
        351,1,0,0,0,359,355,1,0,0,0,360,67,1,0,0,0,361,364,3,70,35,0,362,
        364,1,0,0,0,363,361,1,0,0,0,363,362,1,0,0,0,364,69,1,0,0,0,365,371,
        3,52,26,0,366,367,3,52,26,0,367,368,5,30,0,0,368,369,3,70,35,0,369,
        371,1,0,0,0,370,365,1,0,0,0,370,366,1,0,0,0,371,71,1,0,0,0,39,77,
        82,85,92,105,121,129,135,139,145,149,155,161,166,170,180,190,199,
        206,210,213,221,228,234,242,248,258,269,276,283,293,304,315,323,
        338,340,359,363,370
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
                      "FUNC", "MOD", "UNTIL", "BY", "BOOLEAN", "IDENTIFIER", 
                      "NUMBER", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRING", 
                      "NULL_LINES", "COMMENT", "WS", "NEWLINE", "ERROR_CHAR" ]

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
    RULE_func = 16
    RULE_arg_group = 17
    RULE_args = 18
    RULE_arg_list = 19
    RULE_arg = 20
    RULE_type_index = 21
    RULE_type_index_nums = 22
    RULE_type_index_num_list = 23
    RULE_ass = 24
    RULE_decl = 25
    RULE_expr = 26
    RULE_expr1 = 27
    RULE_expr2 = 28
    RULE_expr3 = 29
    RULE_expr4 = 30
    RULE_expr5 = 31
    RULE_expr6 = 32
    RULE_term = 33
    RULE_expr_list = 34
    RULE_exprs = 35

    ruleNames =  [ "program", "stms", "stm_lists", "stm", "r_print", "r_break", 
                   "r_continue", "r_return", "r_if", "r_elif_list", "r_elifs", 
                   "r_elif", "r_else", "r_for", "block", "block_stms", "func", 
                   "arg_group", "args", "arg_list", "arg", "type_index", 
                   "type_index_nums", "type_index_num_list", "ass", "decl", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "term", "expr_list", "exprs" ]

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
    BOOLEAN=39
    IDENTIFIER=40
    NUMBER=41
    ILLEGAL_ESCAPE=42
    UNCLOSE_STRING=43
    STRING=44
    NULL_LINES=45
    COMMENT=46
    WS=47
    NEWLINE=48
    ERROR_CHAR=49

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
            self.state = 72
            self.stms()
            self.state = 73
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
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 75
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 79
                self.stm_lists()
                self.state = 82
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 80
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
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.stm()
                self.state = 89
                self.match(ZCodeParser.NULL_LINES)
                self.state = 90
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
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 99
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 100
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 101
                self.r_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 102
                self.r_if()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 103
                self.r_for()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 104
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
            self.state = 107
            self.match(ZCodeParser.PRINT)
            self.state = 108
            self.expr()
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
            self.state = 110
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
            self.state = 112
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
            self.state = 114
            self.match(ZCodeParser.RETURN)
            self.state = 115
            self.expr()
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


        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def NULL_LINES(self):
            return self.getToken(ZCodeParser.NULL_LINES, 0)

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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(ZCodeParser.IF)
                self.state = 118
                self.expr()
                self.state = 121
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 119
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 123
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(ZCodeParser.IF)
                self.state = 126
                self.expr()
                self.state = 129
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 127
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 131
                self.stm()
                self.state = 132
                self.r_elif_list()
                self.state = 133
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
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
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.r_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.r_elif()
                self.state = 143
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

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_elif




    def r_elif(self):

        localctx = ZCodeParser.R_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_r_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.state = 147
                self.match(ZCodeParser.NULL_LINES)
                pass
            elif token in [3]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 151
            self.match(ZCodeParser.ELIF)
            self.state = 152
            self.expr()
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.state = 153
                self.match(ZCodeParser.NULL_LINES)
                pass
            elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 157
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

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_else




    def r_else(self):

        localctx = ZCodeParser.R_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_r_else)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 159
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [4]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 163
                self.match(ZCodeParser.ELSE)
                self.state = 166
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 164
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 168
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

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def NULL_LINES(self):
            return self.getToken(ZCodeParser.NULL_LINES, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_r_for




    def r_for(self):

        localctx = ZCodeParser.R_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_r_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ZCodeParser.FOR)
            self.state = 173
            self.expr()
            self.state = 174
            self.match(ZCodeParser.UNTIL)
            self.state = 175
            self.expr()
            self.state = 176
            self.match(ZCodeParser.BY)
            self.state = 177
            self.expr()
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.state = 178
                self.match(ZCodeParser.NULL_LINES)
                pass
            elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 182
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

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NULL_LINES(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NULL_LINES)
            else:
                return self.getToken(ZCodeParser.NULL_LINES, i)

        def block_stms(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(ZCodeParser.BEGIN)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 185
                self.match(ZCodeParser.NULL_LINES)
                self.state = 186
                self.block_stms()
                self.state = 187
                self.match(ZCodeParser.NULL_LINES)
                pass

            elif la_ == 2:
                self.state = 189
                self.match(ZCodeParser.NULL_LINES)
                pass


            self.state = 192
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

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def NULL_LINES(self):
            return self.getToken(ZCodeParser.NULL_LINES, 0)

        def block_stms(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stms




    def block_stms(self):

        localctx = ZCodeParser.Block_stmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block_stms)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.stm()
                self.state = 196
                self.match(ZCodeParser.NULL_LINES)
                self.state = 197
                self.block_stms()
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
        self.enterRule(localctx, 32, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(ZCodeParser.FUNC)
            self.state = 202
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 203
            self.arg_group()
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 206
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 204
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [24, 34]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 210
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34]:
                    self.state = 208
                    self.r_return()
                    pass
                elif token in [24]:
                    self.state = 209
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
        self.enterRule(localctx, 34, self.RULE_arg_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(ZCodeParser.LP)
            self.state = 216
            self.args()
            self.state = 217
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
        self.enterRule(localctx, 36, self.RULE_args)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
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
        self.enterRule(localctx, 38, self.RULE_arg_list)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.arg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.arg()
                self.state = 225
                self.match(ZCodeParser.COMMA)
                self.state = 226
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
        self.enterRule(localctx, 40, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ZCodeParser.TYPE)
            self.state = 231
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 232
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
        self.enterRule(localctx, 42, self.RULE_type_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(ZCodeParser.LB)
            self.state = 237
            self.type_index_nums()
            self.state = 238
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
        self.enterRule(localctx, 44, self.RULE_type_index_nums)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
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
        self.enterRule(localctx, 46, self.RULE_type_index_num_list)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.match(ZCodeParser.NUMBER)
                self.state = 246
                self.match(ZCodeParser.COMMA)
                self.state = 247
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
        self.enterRule(localctx, 48, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.expr()
            self.state = 251
            self.match(ZCodeParser.ASSIGN)
            self.state = 252
            self.expr()
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def type_index(self):
            return self.getTypedRuleContext(ZCodeParser.Type_indexContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def DYN(self):
            return self.getToken(ZCodeParser.DYN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_decl




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_decl)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(ZCodeParser.TYPE)
                self.state = 255
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 258
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [22]:
                    self.state = 256
                    self.type_index()
                    pass
                elif token in [13]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 260
                self.match(ZCodeParser.ASSIGN)
                self.state = 261
                self.expr()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.match(ZCodeParser.VAR)
                self.state = 263
                self.expr()
                self.state = 264
                self.match(ZCodeParser.ASSIGN)
                self.state = 265
                self.expr()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.match(ZCodeParser.DYN)
                self.state = 268
                self.expr()
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

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.expr1()
                self.state = 272
                localctx.op = self.match(ZCodeParser.CONCAT)
                self.state = 273
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


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
            return ZCodeParser.RULE_expr1




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.expr2(0)
                self.state = 279
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135249920) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 280
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 288
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 289
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 290
                    self.expr3(0) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 300
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==6 or _la==7):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 301
                    self.expr4(0) 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
            self.op = None # Token

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 310
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 311
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 68719477504) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 312
                    self.expr5() 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 62, self.RULE_expr5)
        try:
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(ZCodeParser.SUB)
                self.state = 319
                self.expr5()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(ZCodeParser.NOT)
                self.state = 321
                self.expr5()
                pass
            elif token in [20, 22, 39, 40, 41, 44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
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
            self.indexer = None # Expr_listContext
            self.params = None # Expr_listContext

        def term(self):
            return self.getTypedRuleContext(ZCodeParser.TermContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 338
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 328
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 329
                        self.match(ZCodeParser.LB)
                        self.state = 330
                        localctx.indexer = self.expr_list()
                        self.state = 331
                        self.match(ZCodeParser.RB)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 333
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 334
                        self.match(ZCodeParser.LP)
                        self.state = 335
                        localctx.params = self.expr_list()
                        self.state = 336
                        self.match(ZCodeParser.RP)
                        pass

             
                self.state = 342
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(ZCodeParser.BOOLEAN, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_term




    def term(self):

        localctx = ZCodeParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_term)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(ZCodeParser.LB)
                self.state = 344
                self.expr_list()
                self.state = 345
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 348
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 349
                self.match(ZCodeParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 350
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 351
                self.match(ZCodeParser.LB)
                self.state = 352
                self.expr_list()
                self.state = 353
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 355
                self.match(ZCodeParser.LP)
                self.state = 356
                self.expr()
                self.state = 357
                self.match(ZCodeParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprs(self):
            return self.getTypedRuleContext(ZCodeParser.ExprsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_list




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr_list)
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 20, 22, 26, 39, 40, 41, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.exprs()
                pass
            elif token in [21, 23]:
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


    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprs(self):
            return self.getTypedRuleContext(ZCodeParser.ExprsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprs




    def exprs(self):

        localctx = ZCodeParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exprs)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.expr()
                self.state = 367
                self.match(ZCodeParser.COMMA)
                self.state = 368
                self.exprs()
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
        self._predicates[28] = self.expr2_sempred
        self._predicates[29] = self.expr3_sempred
        self._predicates[30] = self.expr4_sempred
        self._predicates[32] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




