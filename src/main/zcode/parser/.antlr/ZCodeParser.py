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
        4,1,49,388,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,1,1,1,1,3,1,76,8,1,1,1,1,1,1,1,3,1,81,
        8,1,1,1,3,1,84,8,1,1,2,1,2,1,2,1,2,1,2,3,2,91,8,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,104,8,3,1,4,1,4,1,4,1,5,1,5,1,
        6,1,6,1,7,1,7,1,7,3,7,116,8,7,1,8,1,8,1,8,1,8,3,8,122,8,8,1,8,1,
        8,1,8,1,8,1,8,1,8,3,8,130,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,139,
        8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,148,8,8,1,8,1,8,1,8,1,8,3,8,
        154,8,8,1,9,1,9,1,9,1,9,3,9,160,8,9,1,10,1,10,3,10,164,8,10,1,10,
        1,10,1,10,1,10,3,10,170,8,10,1,10,1,10,1,11,1,11,3,11,176,8,11,1,
        11,1,11,1,11,3,11,181,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,3,12,193,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,
        13,3,13,203,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,212,8,14,
        1,15,1,15,1,15,1,15,1,15,3,15,219,8,15,1,15,1,15,3,15,223,8,15,1,
        15,3,15,226,8,15,1,16,1,16,1,16,1,16,1,17,1,17,3,17,234,8,17,1,18,
        1,18,1,18,1,18,1,18,3,18,241,8,18,1,19,1,19,1,19,1,19,3,19,247,8,
        19,1,20,1,20,1,20,1,20,1,21,1,21,3,21,255,8,21,1,22,1,22,1,22,1,
        22,3,22,261,8,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,271,
        8,24,1,24,1,24,1,24,3,24,276,8,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,3,24,285,8,24,1,25,1,25,1,25,1,25,1,25,3,25,292,8,25,1,26,1,
        26,1,26,1,26,1,26,3,26,299,8,26,1,27,1,27,1,27,1,27,1,27,1,27,5,
        27,307,8,27,10,27,12,27,310,9,27,1,28,1,28,1,28,1,28,1,28,1,28,5,
        28,318,8,28,10,28,12,28,321,9,28,1,29,1,29,1,29,1,29,1,29,1,29,5,
        29,329,8,29,10,29,12,29,332,9,29,1,30,1,30,1,30,1,30,1,30,3,30,339,
        8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,5,31,354,8,31,10,31,12,31,357,9,31,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,375,
        8,32,1,33,1,33,3,33,379,8,33,1,34,1,34,1,34,1,34,1,34,3,34,386,8,
        34,1,34,0,4,54,56,58,62,35,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,0,
        4,2,0,14,19,27,27,1,0,10,11,1,0,6,7,2,0,8,9,36,36,411,0,70,1,0,0,
        0,2,83,1,0,0,0,4,90,1,0,0,0,6,103,1,0,0,0,8,105,1,0,0,0,10,108,1,
        0,0,0,12,110,1,0,0,0,14,112,1,0,0,0,16,153,1,0,0,0,18,159,1,0,0,
        0,20,163,1,0,0,0,22,175,1,0,0,0,24,184,1,0,0,0,26,196,1,0,0,0,28,
        211,1,0,0,0,30,213,1,0,0,0,32,227,1,0,0,0,34,233,1,0,0,0,36,240,
        1,0,0,0,38,242,1,0,0,0,40,248,1,0,0,0,42,254,1,0,0,0,44,260,1,0,
        0,0,46,262,1,0,0,0,48,284,1,0,0,0,50,291,1,0,0,0,52,298,1,0,0,0,
        54,300,1,0,0,0,56,311,1,0,0,0,58,322,1,0,0,0,60,338,1,0,0,0,62,340,
        1,0,0,0,64,374,1,0,0,0,66,378,1,0,0,0,68,385,1,0,0,0,70,71,3,2,1,
        0,71,72,5,0,0,1,72,1,1,0,0,0,73,76,5,45,0,0,74,76,1,0,0,0,75,73,
        1,0,0,0,75,74,1,0,0,0,76,77,1,0,0,0,77,80,3,4,2,0,78,81,5,45,0,0,
        79,81,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,84,1,0,0,0,82,84,1,
        0,0,0,83,75,1,0,0,0,83,82,1,0,0,0,84,3,1,0,0,0,85,91,3,6,3,0,86,
        87,3,6,3,0,87,88,5,45,0,0,88,89,3,4,2,0,89,91,1,0,0,0,90,85,1,0,
        0,0,90,86,1,0,0,0,91,5,1,0,0,0,92,104,3,50,25,0,93,104,3,48,24,0,
        94,104,3,46,23,0,95,104,3,26,13,0,96,104,3,30,15,0,97,104,3,10,5,
        0,98,104,3,12,6,0,99,104,3,14,7,0,100,104,3,16,8,0,101,104,3,24,
        12,0,102,104,3,8,4,0,103,92,1,0,0,0,103,93,1,0,0,0,103,94,1,0,0,
        0,103,95,1,0,0,0,103,96,1,0,0,0,103,97,1,0,0,0,103,98,1,0,0,0,103,
        99,1,0,0,0,103,100,1,0,0,0,103,101,1,0,0,0,103,102,1,0,0,0,104,7,
        1,0,0,0,105,106,5,31,0,0,106,107,3,50,25,0,107,9,1,0,0,0,108,109,
        5,32,0,0,109,11,1,0,0,0,110,111,5,33,0,0,111,13,1,0,0,0,112,115,
        5,34,0,0,113,116,3,50,25,0,114,116,1,0,0,0,115,113,1,0,0,0,115,114,
        1,0,0,0,116,15,1,0,0,0,117,118,5,2,0,0,118,121,3,50,25,0,119,122,
        5,45,0,0,120,122,1,0,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,123,
        1,0,0,0,123,124,3,6,3,0,124,154,1,0,0,0,125,126,5,2,0,0,126,129,
        3,50,25,0,127,130,5,45,0,0,128,130,1,0,0,0,129,127,1,0,0,0,129,128,
        1,0,0,0,130,131,1,0,0,0,131,132,3,6,3,0,132,133,3,18,9,0,133,154,
        1,0,0,0,134,135,5,2,0,0,135,138,3,50,25,0,136,139,5,45,0,0,137,139,
        1,0,0,0,138,136,1,0,0,0,138,137,1,0,0,0,139,140,1,0,0,0,140,141,
        3,6,3,0,141,142,3,22,11,0,142,154,1,0,0,0,143,144,5,2,0,0,144,147,
        3,50,25,0,145,148,5,45,0,0,146,148,1,0,0,0,147,145,1,0,0,0,147,146,
        1,0,0,0,148,149,1,0,0,0,149,150,3,6,3,0,150,151,3,18,9,0,151,152,
        3,22,11,0,152,154,1,0,0,0,153,117,1,0,0,0,153,125,1,0,0,0,153,134,
        1,0,0,0,153,143,1,0,0,0,154,17,1,0,0,0,155,160,3,20,10,0,156,157,
        3,20,10,0,157,158,3,18,9,0,158,160,1,0,0,0,159,155,1,0,0,0,159,156,
        1,0,0,0,160,19,1,0,0,0,161,164,5,45,0,0,162,164,1,0,0,0,163,161,
        1,0,0,0,163,162,1,0,0,0,164,165,1,0,0,0,165,166,5,3,0,0,166,169,
        3,50,25,0,167,170,5,45,0,0,168,170,1,0,0,0,169,167,1,0,0,0,169,168,
        1,0,0,0,170,171,1,0,0,0,171,172,3,6,3,0,172,21,1,0,0,0,173,176,5,
        45,0,0,174,176,1,0,0,0,175,173,1,0,0,0,175,174,1,0,0,0,176,177,1,
        0,0,0,177,180,5,4,0,0,178,181,5,45,0,0,179,181,1,0,0,0,180,178,1,
        0,0,0,180,179,1,0,0,0,181,182,1,0,0,0,182,183,3,6,3,0,183,23,1,0,
        0,0,184,185,5,5,0,0,185,186,3,50,25,0,186,187,5,37,0,0,187,188,3,
        50,25,0,188,189,5,38,0,0,189,192,3,50,25,0,190,193,5,45,0,0,191,
        193,1,0,0,0,192,190,1,0,0,0,192,191,1,0,0,0,193,194,1,0,0,0,194,
        195,3,6,3,0,195,25,1,0,0,0,196,202,5,24,0,0,197,198,5,45,0,0,198,
        199,3,28,14,0,199,200,5,45,0,0,200,203,1,0,0,0,201,203,5,45,0,0,
        202,197,1,0,0,0,202,201,1,0,0,0,203,204,1,0,0,0,204,205,5,25,0,0,
        205,27,1,0,0,0,206,212,3,6,3,0,207,208,3,6,3,0,208,209,5,45,0,0,
        209,210,3,28,14,0,210,212,1,0,0,0,211,206,1,0,0,0,211,207,1,0,0,
        0,212,29,1,0,0,0,213,214,5,35,0,0,214,215,5,40,0,0,215,225,3,32,
        16,0,216,219,5,45,0,0,217,219,1,0,0,0,218,216,1,0,0,0,218,217,1,
        0,0,0,219,222,1,0,0,0,220,223,3,14,7,0,221,223,3,26,13,0,222,220,
        1,0,0,0,222,221,1,0,0,0,223,226,1,0,0,0,224,226,1,0,0,0,225,218,
        1,0,0,0,225,224,1,0,0,0,226,31,1,0,0,0,227,228,5,20,0,0,228,229,
        3,34,17,0,229,230,5,21,0,0,230,33,1,0,0,0,231,234,3,36,18,0,232,
        234,1,0,0,0,233,231,1,0,0,0,233,232,1,0,0,0,234,35,1,0,0,0,235,241,
        3,38,19,0,236,237,3,38,19,0,237,238,5,30,0,0,238,239,3,36,18,0,239,
        241,1,0,0,0,240,235,1,0,0,0,240,236,1,0,0,0,241,37,1,0,0,0,242,243,
        5,1,0,0,243,246,5,40,0,0,244,247,3,40,20,0,245,247,1,0,0,0,246,244,
        1,0,0,0,246,245,1,0,0,0,247,39,1,0,0,0,248,249,5,22,0,0,249,250,
        3,42,21,0,250,251,5,23,0,0,251,41,1,0,0,0,252,255,3,44,22,0,253,
        255,1,0,0,0,254,252,1,0,0,0,254,253,1,0,0,0,255,43,1,0,0,0,256,261,
        5,41,0,0,257,258,5,41,0,0,258,259,5,30,0,0,259,261,3,44,22,0,260,
        256,1,0,0,0,260,257,1,0,0,0,261,45,1,0,0,0,262,263,3,50,25,0,263,
        264,5,13,0,0,264,265,3,50,25,0,265,47,1,0,0,0,266,267,5,1,0,0,267,
        270,5,40,0,0,268,271,3,40,20,0,269,271,1,0,0,0,270,268,1,0,0,0,270,
        269,1,0,0,0,271,275,1,0,0,0,272,273,5,13,0,0,273,276,3,50,25,0,274,
        276,1,0,0,0,275,272,1,0,0,0,275,274,1,0,0,0,276,285,1,0,0,0,277,
        278,5,28,0,0,278,279,3,50,25,0,279,280,5,13,0,0,280,281,3,50,25,
        0,281,285,1,0,0,0,282,283,5,29,0,0,283,285,3,50,25,0,284,266,1,0,
        0,0,284,277,1,0,0,0,284,282,1,0,0,0,285,49,1,0,0,0,286,287,3,52,
        26,0,287,288,5,12,0,0,288,289,3,52,26,0,289,292,1,0,0,0,290,292,
        3,52,26,0,291,286,1,0,0,0,291,290,1,0,0,0,292,51,1,0,0,0,293,294,
        3,54,27,0,294,295,7,0,0,0,295,296,3,54,27,0,296,299,1,0,0,0,297,
        299,3,54,27,0,298,293,1,0,0,0,298,297,1,0,0,0,299,53,1,0,0,0,300,
        301,6,27,-1,0,301,302,3,56,28,0,302,308,1,0,0,0,303,304,10,2,0,0,
        304,305,7,1,0,0,305,307,3,56,28,0,306,303,1,0,0,0,307,310,1,0,0,
        0,308,306,1,0,0,0,308,309,1,0,0,0,309,55,1,0,0,0,310,308,1,0,0,0,
        311,312,6,28,-1,0,312,313,3,58,29,0,313,319,1,0,0,0,314,315,10,2,
        0,0,315,316,7,2,0,0,316,318,3,58,29,0,317,314,1,0,0,0,318,321,1,
        0,0,0,319,317,1,0,0,0,319,320,1,0,0,0,320,57,1,0,0,0,321,319,1,0,
        0,0,322,323,6,29,-1,0,323,324,3,60,30,0,324,330,1,0,0,0,325,326,
        10,2,0,0,326,327,7,3,0,0,327,329,3,60,30,0,328,325,1,0,0,0,329,332,
        1,0,0,0,330,328,1,0,0,0,330,331,1,0,0,0,331,59,1,0,0,0,332,330,1,
        0,0,0,333,334,5,6,0,0,334,339,3,60,30,0,335,336,5,26,0,0,336,339,
        3,60,30,0,337,339,3,62,31,0,338,333,1,0,0,0,338,335,1,0,0,0,338,
        337,1,0,0,0,339,61,1,0,0,0,340,341,6,31,-1,0,341,342,3,64,32,0,342,
        355,1,0,0,0,343,344,10,3,0,0,344,345,5,22,0,0,345,346,3,66,33,0,
        346,347,5,23,0,0,347,354,1,0,0,0,348,349,10,2,0,0,349,350,5,20,0,
        0,350,351,3,66,33,0,351,352,5,21,0,0,352,354,1,0,0,0,353,343,1,0,
        0,0,353,348,1,0,0,0,354,357,1,0,0,0,355,353,1,0,0,0,355,356,1,0,
        0,0,356,63,1,0,0,0,357,355,1,0,0,0,358,359,5,22,0,0,359,360,3,66,
        33,0,360,361,5,23,0,0,361,375,1,0,0,0,362,375,5,41,0,0,363,375,5,
        44,0,0,364,375,5,39,0,0,365,375,5,40,0,0,366,367,5,22,0,0,367,368,
        3,66,33,0,368,369,5,23,0,0,369,375,1,0,0,0,370,371,5,20,0,0,371,
        372,3,50,25,0,372,373,5,21,0,0,373,375,1,0,0,0,374,358,1,0,0,0,374,
        362,1,0,0,0,374,363,1,0,0,0,374,364,1,0,0,0,374,365,1,0,0,0,374,
        366,1,0,0,0,374,370,1,0,0,0,375,65,1,0,0,0,376,379,3,68,34,0,377,
        379,1,0,0,0,378,376,1,0,0,0,378,377,1,0,0,0,379,67,1,0,0,0,380,386,
        3,50,25,0,381,382,3,50,25,0,382,383,5,30,0,0,383,384,3,68,34,0,384,
        386,1,0,0,0,385,380,1,0,0,0,385,381,1,0,0,0,386,69,1,0,0,0,41,75,
        80,83,90,103,115,121,129,138,147,153,159,163,169,175,180,192,202,
        211,218,222,225,233,240,246,254,260,270,275,284,291,298,308,319,
        330,338,353,355,374,378,385
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
    RULE_r_elifs = 9
    RULE_r_elif = 10
    RULE_r_else = 11
    RULE_r_for = 12
    RULE_block = 13
    RULE_block_stms = 14
    RULE_func = 15
    RULE_arg_group = 16
    RULE_args = 17
    RULE_arg_list = 18
    RULE_arg = 19
    RULE_type_index = 20
    RULE_type_index_nums = 21
    RULE_type_index_num_list = 22
    RULE_ass = 23
    RULE_decl = 24
    RULE_expr = 25
    RULE_expr1 = 26
    RULE_expr2 = 27
    RULE_expr3 = 28
    RULE_expr4 = 29
    RULE_expr5 = 30
    RULE_expr6 = 31
    RULE_term = 32
    RULE_expr_list = 33
    RULE_exprs = 34

    ruleNames =  [ "program", "stms", "stm_lists", "stm", "r_print", "r_break", 
                   "r_continue", "r_return", "r_if", "r_elifs", "r_elif", 
                   "r_else", "r_for", "block", "block_stms", "func", "arg_group", 
                   "args", "arg_list", "arg", "type_index", "type_index_nums", 
                   "type_index_num_list", "ass", "decl", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "term", 
                   "expr_list", "exprs" ]

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
            if token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 73
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 77
                self.stm_lists()
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
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
                self.expr()
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
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 20, 22, 26, 39, 40, 41, 44]:
                self.state = 113
                self.expr()
                pass
            elif token in [-1, 3, 4, 45]:
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

        def r_elifs(self):
            return self.getTypedRuleContext(ZCodeParser.R_elifsContext,0)


        def r_else(self):
            return self.getTypedRuleContext(ZCodeParser.R_elseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_if




    def r_if(self):

        localctx = ZCodeParser.R_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_r_if)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
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
                self.r_elifs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.match(ZCodeParser.IF)
                self.state = 135
                self.expr()
                self.state = 138
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 136
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 140
                self.stm()
                self.state = 141
                self.r_else()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.match(ZCodeParser.IF)
                self.state = 144
                self.expr()
                self.state = 147
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 145
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 149
                self.stm()
                self.state = 150
                self.r_elifs()
                self.state = 151
                self.r_else()
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
        self.enterRule(localctx, 18, self.RULE_r_elifs)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.r_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.r_elif()
                self.state = 157
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
        self.enterRule(localctx, 20, self.RULE_r_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.state = 161
                self.match(ZCodeParser.NULL_LINES)
                pass
            elif token in [3]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 165
            self.match(ZCodeParser.ELIF)
            self.state = 166
            self.expr()
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.state = 167
                self.match(ZCodeParser.NULL_LINES)
                pass
            elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 171
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
        self.enterRule(localctx, 22, self.RULE_r_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.state = 173
                self.match(ZCodeParser.NULL_LINES)
                pass
            elif token in [4]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 177
            self.match(ZCodeParser.ELSE)
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
        self.enterRule(localctx, 24, self.RULE_r_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(ZCodeParser.FOR)
            self.state = 185
            self.expr()
            self.state = 186
            self.match(ZCodeParser.UNTIL)
            self.state = 187
            self.expr()
            self.state = 188
            self.match(ZCodeParser.BY)
            self.state = 189
            self.expr()
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.state = 190
                self.match(ZCodeParser.NULL_LINES)
                pass
            elif token in [1, 2, 5, 6, 20, 22, 24, 26, 28, 29, 31, 32, 33, 34, 35, 39, 40, 41, 44]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 194
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
        self.enterRule(localctx, 26, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(ZCodeParser.BEGIN)
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 197
                self.match(ZCodeParser.NULL_LINES)
                self.state = 198
                self.block_stms()
                self.state = 199
                self.match(ZCodeParser.NULL_LINES)
                pass

            elif la_ == 2:
                self.state = 201
                self.match(ZCodeParser.NULL_LINES)
                pass


            self.state = 204
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
        self.enterRule(localctx, 28, self.RULE_block_stms)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.stm()
                self.state = 208
                self.match(ZCodeParser.NULL_LINES)
                self.state = 209
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
        self.enterRule(localctx, 30, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(ZCodeParser.FUNC)
            self.state = 214
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 215
            self.arg_group()
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 218
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 216
                    self.match(ZCodeParser.NULL_LINES)
                    pass
                elif token in [24, 34]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 222
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34]:
                    self.state = 220
                    self.r_return()
                    pass
                elif token in [24]:
                    self.state = 221
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
        self.enterRule(localctx, 32, self.RULE_arg_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(ZCodeParser.LP)
            self.state = 228
            self.args()
            self.state = 229
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
        self.enterRule(localctx, 34, self.RULE_args)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
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
        self.enterRule(localctx, 36, self.RULE_arg_list)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.arg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.arg()
                self.state = 237
                self.match(ZCodeParser.COMMA)
                self.state = 238
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
        self.enterRule(localctx, 38, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(ZCodeParser.TYPE)
            self.state = 243
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 244
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
        self.enterRule(localctx, 40, self.RULE_type_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(ZCodeParser.LB)
            self.state = 249
            self.type_index_nums()
            self.state = 250
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
        self.enterRule(localctx, 42, self.RULE_type_index_nums)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
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
        self.enterRule(localctx, 44, self.RULE_type_index_num_list)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(ZCodeParser.NUMBER)
                self.state = 258
                self.match(ZCodeParser.COMMA)
                self.state = 259
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
        self.enterRule(localctx, 46, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.expr()
            self.state = 263
            self.match(ZCodeParser.ASSIGN)
            self.state = 264
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

        def type_index(self):
            return self.getTypedRuleContext(ZCodeParser.Type_indexContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def DYN(self):
            return self.getToken(ZCodeParser.DYN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_decl




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_decl)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(ZCodeParser.TYPE)
                self.state = 267
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 270
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [22]:
                    self.state = 268
                    self.type_index()
                    pass
                elif token in [-1, 3, 4, 13, 45]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 275
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 272
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 273
                    self.expr()
                    pass
                elif token in [-1, 3, 4, 45]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(ZCodeParser.VAR)
                self.state = 278
                self.expr()
                self.state = 279
                self.match(ZCodeParser.ASSIGN)
                self.state = 280
                self.expr()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.match(ZCodeParser.DYN)
                self.state = 283
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
        self.enterRule(localctx, 50, self.RULE_expr)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.expr1()
                self.state = 287
                localctx.op = self.match(ZCodeParser.CONCAT)
                self.state = 288
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
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
        self.enterRule(localctx, 52, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.expr2(0)
                self.state = 294
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135249920) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 295
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 303
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 304
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 305
                    self.expr3(0) 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 314
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 315
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==6 or _la==7):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 316
                    self.expr4(0) 
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 330
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 325
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 326
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 68719477504) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 327
                    self.expr5() 
                self.state = 332
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_expr5)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(ZCodeParser.SUB)
                self.state = 334
                self.expr5()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(ZCodeParser.NOT)
                self.state = 336
                self.expr5()
                pass
            elif token in [20, 22, 39, 40, 41, 44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 353
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 343
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 344
                        self.match(ZCodeParser.LB)
                        self.state = 345
                        localctx.indexer = self.expr_list()
                        self.state = 346
                        self.match(ZCodeParser.RB)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 348
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 349
                        self.match(ZCodeParser.LP)
                        self.state = 350
                        localctx.params = self.expr_list()
                        self.state = 351
                        self.match(ZCodeParser.RP)
                        pass

             
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_term)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(ZCodeParser.LB)
                self.state = 359
                self.expr_list()
                self.state = 360
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 364
                self.match(ZCodeParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 365
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 366
                self.match(ZCodeParser.LB)
                self.state = 367
                self.expr_list()
                self.state = 368
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 370
                self.match(ZCodeParser.LP)
                self.state = 371
                self.expr()
                self.state = 372
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
        self.enterRule(localctx, 66, self.RULE_expr_list)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 20, 22, 26, 39, 40, 41, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
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
        self.enterRule(localctx, 68, self.RULE_exprs)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.expr()
                self.state = 382
                self.match(ZCodeParser.COMMA)
                self.state = 383
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
        self._predicates[27] = self.expr2_sempred
        self._predicates[28] = self.expr3_sempred
        self._predicates[29] = self.expr4_sempred
        self._predicates[31] = self.expr6_sempred
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
         




