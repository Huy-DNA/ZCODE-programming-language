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
        4,1,46,370,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,48,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,58,8,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,5,6,78,8,6,10,6,12,6,81,9,6,1,6,1,6,3,6,85,
        8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,98,8,8,10,8,
        12,8,101,9,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,111,8,9,1,10,1,
        10,1,10,1,10,3,10,117,8,10,1,10,1,10,1,10,1,10,3,10,123,8,10,5,10,
        125,8,10,10,10,12,10,128,9,10,3,10,130,8,10,1,10,1,10,1,11,1,11,
        1,11,1,11,5,11,138,8,11,10,11,12,11,141,9,11,3,11,143,8,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,163,8,13,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,178,8,14,10,14,12,14,181,
        9,14,3,14,183,8,14,1,14,1,14,1,14,1,14,3,14,189,8,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,5,14,211,8,14,10,14,12,14,214,9,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,5,14,223,8,14,10,14,12,14,226,9,14,3,
        14,228,8,14,1,14,5,14,231,8,14,10,14,12,14,234,9,14,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,245,8,15,10,15,12,15,248,9,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,257,8,15,10,15,12,15,
        260,9,15,3,15,262,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,5,15,290,8,15,10,15,12,15,293,9,15,3,15,295,
        8,15,1,15,1,15,1,15,1,15,3,15,301,8,15,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,5,16,312,8,16,10,16,12,16,315,9,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,5,16,324,8,16,10,16,12,16,327,9,16,3,16,
        329,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,5,16,357,8,16,10,16,12,16,360,9,16,3,16,362,8,16,1,16,
        1,16,1,16,1,16,3,16,368,8,16,1,16,1,79,1,28,17,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,0,4,1,0,23,25,2,0,21,21,26,26,1,0,27,
        33,1,0,35,36,426,0,37,1,0,0,0,2,47,1,0,0,0,4,57,1,0,0,0,6,59,1,0,
        0,0,8,61,1,0,0,0,10,63,1,0,0,0,12,66,1,0,0,0,14,86,1,0,0,0,16,94,
        1,0,0,0,18,105,1,0,0,0,20,112,1,0,0,0,22,133,1,0,0,0,24,146,1,0,
        0,0,26,162,1,0,0,0,28,188,1,0,0,0,30,300,1,0,0,0,32,367,1,0,0,0,
        34,36,3,2,1,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,
        0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,0,0,1,41,1,1,0,0,0,42,
        43,3,4,2,0,43,44,5,45,0,0,44,48,1,0,0,0,45,48,5,43,0,0,46,48,5,45,
        0,0,47,42,1,0,0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,3,1,0,0,0,49,58,
        3,28,14,0,50,58,3,26,13,0,51,58,3,24,12,0,52,58,3,16,8,0,53,58,3,
        18,9,0,54,58,3,6,3,0,55,58,3,8,4,0,56,58,3,10,5,0,57,49,1,0,0,0,
        57,50,1,0,0,0,57,51,1,0,0,0,57,52,1,0,0,0,57,53,1,0,0,0,57,54,1,
        0,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,5,1,0,0,0,59,60,5,1,0,0,60,
        7,1,0,0,0,61,62,5,2,0,0,62,9,1,0,0,0,63,64,5,3,0,0,64,65,3,28,14,
        0,65,11,1,0,0,0,66,67,5,4,0,0,67,68,5,5,0,0,68,69,3,28,14,0,69,70,
        5,6,0,0,70,79,3,16,8,0,71,72,5,7,0,0,72,73,5,5,0,0,73,74,3,28,14,
        0,74,75,5,6,0,0,75,76,3,16,8,0,76,78,1,0,0,0,77,71,1,0,0,0,78,81,
        1,0,0,0,79,80,1,0,0,0,79,77,1,0,0,0,80,84,1,0,0,0,81,79,1,0,0,0,
        82,83,5,8,0,0,83,85,3,16,8,0,84,82,1,0,0,0,84,85,1,0,0,0,85,13,1,
        0,0,0,86,87,5,9,0,0,87,88,3,28,14,0,88,89,5,10,0,0,89,90,3,28,14,
        0,90,91,5,11,0,0,91,92,3,28,14,0,92,93,3,28,14,0,93,15,1,0,0,0,94,
        95,5,12,0,0,95,99,5,45,0,0,96,98,3,2,1,0,97,96,1,0,0,0,98,101,1,
        0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,
        0,102,103,5,45,0,0,103,104,5,13,0,0,104,17,1,0,0,0,105,106,5,14,
        0,0,106,107,5,38,0,0,107,110,3,20,10,0,108,111,3,10,5,0,109,111,
        3,16,8,0,110,108,1,0,0,0,110,109,1,0,0,0,111,19,1,0,0,0,112,129,
        5,5,0,0,113,114,5,37,0,0,114,116,5,38,0,0,115,117,3,22,11,0,116,
        115,1,0,0,0,116,117,1,0,0,0,117,126,1,0,0,0,118,119,5,15,0,0,119,
        120,5,37,0,0,120,122,5,38,0,0,121,123,3,22,11,0,122,121,1,0,0,0,
        122,123,1,0,0,0,123,125,1,0,0,0,124,118,1,0,0,0,125,128,1,0,0,0,
        126,124,1,0,0,0,126,127,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,
        129,113,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,132,5,6,0,0,
        132,21,1,0,0,0,133,142,5,16,0,0,134,139,5,39,0,0,135,136,5,15,0,
        0,136,138,5,39,0,0,137,135,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,
        0,139,140,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,142,134,1,0,0,
        0,142,143,1,0,0,0,143,144,1,0,0,0,144,145,5,17,0,0,145,23,1,0,0,
        0,146,147,3,28,14,0,147,148,5,18,0,0,148,149,3,28,14,0,149,25,1,
        0,0,0,150,151,5,37,0,0,151,152,3,28,14,0,152,153,5,18,0,0,153,154,
        3,28,14,0,154,163,1,0,0,0,155,156,5,19,0,0,156,157,3,28,14,0,157,
        158,5,18,0,0,158,159,3,28,14,0,159,163,1,0,0,0,160,161,5,20,0,0,
        161,163,3,28,14,0,162,150,1,0,0,0,162,155,1,0,0,0,162,160,1,0,0,
        0,163,27,1,0,0,0,164,165,6,14,-1,0,165,166,5,5,0,0,166,167,3,28,
        14,0,167,168,5,6,0,0,168,189,1,0,0,0,169,170,5,21,0,0,170,189,3,
        28,14,11,171,172,5,22,0,0,172,189,3,28,14,10,173,182,5,16,0,0,174,
        179,3,28,14,0,175,176,5,15,0,0,176,178,3,28,14,0,177,175,1,0,0,0,
        178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,183,1,0,0,0,
        181,179,1,0,0,0,182,174,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,
        184,189,5,17,0,0,185,189,5,39,0,0,186,189,5,42,0,0,187,189,5,38,
        0,0,188,164,1,0,0,0,188,169,1,0,0,0,188,171,1,0,0,0,188,173,1,0,
        0,0,188,185,1,0,0,0,188,186,1,0,0,0,188,187,1,0,0,0,189,232,1,0,
        0,0,190,191,10,9,0,0,191,192,7,0,0,0,192,231,3,28,14,10,193,194,
        10,8,0,0,194,195,7,1,0,0,195,231,3,28,14,9,196,197,10,7,0,0,197,
        198,7,2,0,0,198,231,3,28,14,8,199,200,10,6,0,0,200,201,5,34,0,0,
        201,231,3,28,14,7,202,203,10,5,0,0,203,204,7,3,0,0,204,231,3,28,
        14,6,205,206,10,13,0,0,206,207,5,16,0,0,207,212,3,28,14,0,208,209,
        5,15,0,0,209,211,3,28,14,0,210,208,1,0,0,0,211,214,1,0,0,0,212,210,
        1,0,0,0,212,213,1,0,0,0,213,215,1,0,0,0,214,212,1,0,0,0,215,216,
        5,17,0,0,216,231,1,0,0,0,217,218,10,12,0,0,218,227,5,5,0,0,219,224,
        3,28,14,0,220,221,5,15,0,0,221,223,3,28,14,0,222,220,1,0,0,0,223,
        226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,228,1,0,0,0,226,
        224,1,0,0,0,227,219,1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,
        231,5,6,0,0,230,190,1,0,0,0,230,193,1,0,0,0,230,196,1,0,0,0,230,
        199,1,0,0,0,230,202,1,0,0,0,230,205,1,0,0,0,230,217,1,0,0,0,231,
        234,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,29,1,0,0,0,234,232,
        1,0,0,0,235,236,5,5,0,0,236,237,3,28,14,0,237,238,5,6,0,0,238,301,
        1,0,0,0,239,240,3,28,14,0,240,241,5,16,0,0,241,246,3,28,14,0,242,
        243,5,15,0,0,243,245,3,28,14,0,244,242,1,0,0,0,245,248,1,0,0,0,246,
        244,1,0,0,0,246,247,1,0,0,0,247,249,1,0,0,0,248,246,1,0,0,0,249,
        250,5,17,0,0,250,301,1,0,0,0,251,252,3,28,14,0,252,261,5,5,0,0,253,
        258,3,28,14,0,254,255,5,15,0,0,255,257,3,28,14,0,256,254,1,0,0,0,
        257,260,1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,259,262,1,0,0,0,
        260,258,1,0,0,0,261,253,1,0,0,0,261,262,1,0,0,0,262,263,1,0,0,0,
        263,264,5,6,0,0,264,301,1,0,0,0,265,266,5,21,0,0,266,301,3,28,14,
        0,267,268,5,22,0,0,268,301,3,28,14,0,269,270,3,28,14,0,270,271,7,
        0,0,0,271,272,3,28,14,0,272,301,1,0,0,0,273,274,3,28,14,0,274,275,
        7,1,0,0,275,276,3,28,14,0,276,301,1,0,0,0,277,278,3,28,14,0,278,
        279,7,2,0,0,279,280,3,28,14,0,280,301,1,0,0,0,281,282,3,28,14,0,
        282,283,7,3,0,0,283,284,3,28,14,0,284,301,1,0,0,0,285,294,5,16,0,
        0,286,291,3,28,14,0,287,288,5,15,0,0,288,290,3,28,14,0,289,287,1,
        0,0,0,290,293,1,0,0,0,291,289,1,0,0,0,291,292,1,0,0,0,292,295,1,
        0,0,0,293,291,1,0,0,0,294,286,1,0,0,0,294,295,1,0,0,0,295,296,1,
        0,0,0,296,301,5,17,0,0,297,301,5,39,0,0,298,301,5,42,0,0,299,301,
        5,38,0,0,300,235,1,0,0,0,300,239,1,0,0,0,300,251,1,0,0,0,300,265,
        1,0,0,0,300,267,1,0,0,0,300,269,1,0,0,0,300,273,1,0,0,0,300,277,
        1,0,0,0,300,281,1,0,0,0,300,285,1,0,0,0,300,297,1,0,0,0,300,298,
        1,0,0,0,300,299,1,0,0,0,301,31,1,0,0,0,302,303,5,5,0,0,303,304,3,
        28,14,0,304,305,5,6,0,0,305,368,1,0,0,0,306,307,3,28,14,0,307,308,
        5,16,0,0,308,313,3,28,14,0,309,310,5,15,0,0,310,312,3,28,14,0,311,
        309,1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,
        316,1,0,0,0,315,313,1,0,0,0,316,317,5,17,0,0,317,368,1,0,0,0,318,
        319,3,28,14,0,319,328,5,5,0,0,320,325,3,28,14,0,321,322,5,15,0,0,
        322,324,3,28,14,0,323,321,1,0,0,0,324,327,1,0,0,0,325,323,1,0,0,
        0,325,326,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,328,320,1,0,0,
        0,328,329,1,0,0,0,329,330,1,0,0,0,330,331,5,6,0,0,331,368,1,0,0,
        0,332,333,5,21,0,0,333,368,3,28,14,0,334,335,5,22,0,0,335,368,3,
        28,14,0,336,337,3,28,14,0,337,338,7,0,0,0,338,339,3,28,14,0,339,
        368,1,0,0,0,340,341,3,28,14,0,341,342,7,1,0,0,342,343,3,28,14,0,
        343,368,1,0,0,0,344,345,3,28,14,0,345,346,5,34,0,0,346,347,3,28,
        14,0,347,368,1,0,0,0,348,349,3,28,14,0,349,350,7,3,0,0,350,351,3,
        28,14,0,351,368,1,0,0,0,352,361,5,16,0,0,353,358,3,28,14,0,354,355,
        5,15,0,0,355,357,3,28,14,0,356,354,1,0,0,0,357,360,1,0,0,0,358,356,
        1,0,0,0,358,359,1,0,0,0,359,362,1,0,0,0,360,358,1,0,0,0,361,353,
        1,0,0,0,361,362,1,0,0,0,362,363,1,0,0,0,363,368,5,17,0,0,364,368,
        5,39,0,0,365,368,5,42,0,0,366,368,5,38,0,0,367,302,1,0,0,0,367,306,
        1,0,0,0,367,318,1,0,0,0,367,332,1,0,0,0,367,334,1,0,0,0,367,336,
        1,0,0,0,367,340,1,0,0,0,367,344,1,0,0,0,367,348,1,0,0,0,367,352,
        1,0,0,0,367,364,1,0,0,0,367,365,1,0,0,0,367,366,1,0,0,0,368,33,1,
        0,0,0,34,37,47,57,79,84,99,110,116,122,126,129,139,142,162,179,182,
        188,212,224,227,230,232,246,258,261,291,294,300,313,325,328,358,
        361,367
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
    RULE_line = 1
    RULE_stm = 2
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
    RULE_expr_without_str_concat = 15
    RULE_expr_without_relational = 16

    ruleNames =  [ "program", "line", "stm", "r_break", "r_continue", "r_return", 
                   "r_if", "r_for", "block", "func", "args", "type_index", 
                   "ass", "decl", "expr", "expr_without_str_concat", "expr_without_relational" ]

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

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.LineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.LineContext,i)


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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 49340592246830) != 0):
                self.state = 34
                self.line()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(ZCodeParser.StmContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def COMMENT(self):
            return self.getToken(ZCodeParser.COMMENT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_line




    def line(self):

        localctx = ZCodeParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 5, 12, 14, 16, 19, 20, 21, 22, 37, 38, 39, 42]:
                self.state = 42
                self.stm()
                self.state = 43
                self.match(ZCodeParser.NEWLINE)
                pass
            elif token in [43]:
                self.state = 45
                self.match(ZCodeParser.COMMENT)
                pass
            elif token in [45]:
                self.state = 46
                self.match(ZCodeParser.NEWLINE)
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm




    def stm(self):

        localctx = ZCodeParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stm)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.ass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.r_break()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 55
                self.r_continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 56
                self.r_return()
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
        self.enterRule(localctx, 6, self.RULE_r_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
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
        self.enterRule(localctx, 8, self.RULE_r_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
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
        self.enterRule(localctx, 10, self.RULE_r_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ZCodeParser.T__2)
            self.state = 64
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


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.BlockContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.BlockContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_if




    def r_if(self):

        localctx = ZCodeParser.R_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_r_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ZCodeParser.T__3)
            self.state = 67
            self.match(ZCodeParser.T__4)
            self.state = 68
            self.expr(0)
            self.state = 69
            self.match(ZCodeParser.T__5)
            self.state = 70
            self.block()
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 71
                    self.match(ZCodeParser.T__6)
                    self.state = 72
                    self.match(ZCodeParser.T__4)
                    self.state = 73
                    self.expr(0)
                    self.state = 74
                    self.match(ZCodeParser.T__5)
                    self.state = 75
                    self.block() 
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 82
                self.match(ZCodeParser.T__7)
                self.state = 83
                self.block()


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


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_for




    def r_for(self):

        localctx = ZCodeParser.R_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_r_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ZCodeParser.T__8)
            self.state = 87
            self.expr(0)
            self.state = 88
            self.match(ZCodeParser.T__9)
            self.state = 89
            self.expr(0)
            self.state = 90
            self.match(ZCodeParser.T__10)
            self.state = 91
            self.expr(0)
            self.state = 92
            self.expr(0)
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

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.LineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.LineContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(ZCodeParser.T__11)
            self.state = 95
            self.match(ZCodeParser.NEWLINE)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 96
                    self.line() 
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 102
            self.match(ZCodeParser.NEWLINE)
            self.state = 103
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
        self.enterRule(localctx, 18, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ZCodeParser.T__13)
            self.state = 106
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 107
            self.args()
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 108
                self.r_return()
                pass
            elif token in [12]:
                self.state = 109
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
            self.state = 112
            self.match(ZCodeParser.T__4)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 113
                self.match(ZCodeParser.TYPE)
                self.state = 114
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 115
                    self.type_index()


                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 118
                    self.match(ZCodeParser.T__14)
                    self.state = 119
                    self.match(ZCodeParser.TYPE)
                    self.state = 120
                    self.match(ZCodeParser.IDENTIFIER)
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==16:
                        self.state = 121
                        self.type_index()


                    self.state = 128
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 131
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
        self.enterRule(localctx, 22, self.RULE_type_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(ZCodeParser.T__15)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 134
                self.match(ZCodeParser.NUMBER)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 135
                    self.match(ZCodeParser.T__14)
                    self.state = 136
                    self.match(ZCodeParser.NUMBER)
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 144
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
        self.enterRule(localctx, 24, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.expr(0)
            self.state = 147
            self.match(ZCodeParser.T__17)
            self.state = 148
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
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(ZCodeParser.TYPE)
                self.state = 151
                self.expr(0)
                self.state = 152
                self.match(ZCodeParser.T__17)
                self.state = 153
                self.expr(0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(ZCodeParser.T__18)
                self.state = 156
                self.expr(0)
                self.state = 157
                self.match(ZCodeParser.T__17)
                self.state = 158
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(ZCodeParser.T__19)
                self.state = 161
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
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.indexer = None # ExprContext
            self.param = None # ExprContext

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
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 165
                self.match(ZCodeParser.T__4)
                self.state = 166
                self.expr(0)
                self.state = 167
                self.match(ZCodeParser.T__5)
                pass
            elif token in [21]:
                self.state = 169
                self.match(ZCodeParser.T__20)
                self.state = 170
                self.expr(11)
                pass
            elif token in [22]:
                self.state = 171
                self.match(ZCodeParser.T__21)
                self.state = 172
                self.expr(10)
                pass
            elif token in [16]:
                self.state = 173
                self.match(ZCodeParser.T__15)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                    self.state = 174
                    self.expr(0)
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==15:
                        self.state = 175
                        self.match(ZCodeParser.T__14)
                        self.state = 176
                        self.expr(0)
                        self.state = 181
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 184
                self.match(ZCodeParser.T__16)
                pass
            elif token in [39]:
                self.state = 185
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [42]:
                self.state = 186
                self.match(ZCodeParser.STRING)
                pass
            elif token in [38]:
                self.state = 187
                self.match(ZCodeParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 230
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 190
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 191
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 192
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 193
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 194
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 195
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 196
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 197
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17045651456) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 198
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 199
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 200
                        self.match(ZCodeParser.T__33)
                        self.state = 201
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 202
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 203
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 204
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 6:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 205
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 206
                        self.match(ZCodeParser.T__15)
                        self.state = 207
                        localctx.indexer = self.expr(0)
                        self.state = 212
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 208
                            self.match(ZCodeParser.T__14)
                            self.state = 209
                            localctx.indexer = self.expr(0)
                            self.state = 214
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 215
                        self.match(ZCodeParser.T__16)
                        pass

                    elif la_ == 7:
                        localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 217
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 218
                        self.match(ZCodeParser.T__4)
                        self.state = 227
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                            self.state = 219
                            localctx.param = self.expr(0)
                            self.state = 224
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 220
                                self.match(ZCodeParser.T__14)
                                self.state = 221
                                localctx.param = self.expr(0)
                                self.state = 226
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 229
                        self.match(ZCodeParser.T__5)
                        pass

             
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_without_str_concatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.array = None # ExprContext
            self.indexer = None # ExprContext
            self.callee = None # ExprContext
            self.param = None # ExprContext
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext

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

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_without_str_concat




    def expr_without_str_concat(self):

        localctx = ZCodeParser.Expr_without_str_concatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_without_str_concat)
        self._la = 0 # Token type
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(ZCodeParser.T__4)
                self.state = 236
                self.expr(0)
                self.state = 237
                self.match(ZCodeParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                localctx.array = self.expr(0)
                self.state = 240
                self.match(ZCodeParser.T__15)
                self.state = 241
                localctx.indexer = self.expr(0)
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 242
                    self.match(ZCodeParser.T__14)
                    self.state = 243
                    localctx.indexer = self.expr(0)
                    self.state = 248
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 249
                self.match(ZCodeParser.T__16)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                localctx.callee = self.expr(0)
                self.state = 252
                self.match(ZCodeParser.T__4)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                    self.state = 253
                    localctx.param = self.expr(0)
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==15:
                        self.state = 254
                        self.match(ZCodeParser.T__14)
                        self.state = 255
                        localctx.param = self.expr(0)
                        self.state = 260
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 263
                self.match(ZCodeParser.T__5)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 265
                self.match(ZCodeParser.T__20)
                self.state = 266
                self.expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.match(ZCodeParser.T__21)
                self.state = 268
                self.expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 269
                localctx.left = self.expr(0)
                self.state = 270
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 271
                localctx.right = self.expr(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 273
                localctx.left = self.expr(0)
                self.state = 274
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==21 or _la==26):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                localctx.right = self.expr(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 277
                localctx.left = self.expr(0)
                self.state = 278
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17045651456) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 279
                localctx.right = self.expr(0)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 281
                localctx.left = self.expr(0)
                self.state = 282
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==35 or _la==36):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 283
                localctx.right = self.expr(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 285
                self.match(ZCodeParser.T__15)
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                    self.state = 286
                    self.expr(0)
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==15:
                        self.state = 287
                        self.match(ZCodeParser.T__14)
                        self.state = 288
                        self.expr(0)
                        self.state = 293
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 296
                self.match(ZCodeParser.T__16)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 297
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 298
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 299
                self.match(ZCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_without_relationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.array = None # ExprContext
            self.indexer = None # ExprContext
            self.callee = None # ExprContext
            self.param = None # ExprContext
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext

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

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_without_relational




    def expr_without_relational(self):

        localctx = ZCodeParser.Expr_without_relationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr_without_relational)
        self._la = 0 # Token type
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(ZCodeParser.T__4)
                self.state = 303
                self.expr(0)
                self.state = 304
                self.match(ZCodeParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                localctx.array = self.expr(0)
                self.state = 307
                self.match(ZCodeParser.T__15)
                self.state = 308
                localctx.indexer = self.expr(0)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 309
                    self.match(ZCodeParser.T__14)
                    self.state = 310
                    localctx.indexer = self.expr(0)
                    self.state = 315
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 316
                self.match(ZCodeParser.T__16)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                localctx.callee = self.expr(0)
                self.state = 319
                self.match(ZCodeParser.T__4)
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                    self.state = 320
                    localctx.param = self.expr(0)
                    self.state = 325
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==15:
                        self.state = 321
                        self.match(ZCodeParser.T__14)
                        self.state = 322
                        localctx.param = self.expr(0)
                        self.state = 327
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 330
                self.match(ZCodeParser.T__5)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 332
                self.match(ZCodeParser.T__20)
                self.state = 333
                self.expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 334
                self.match(ZCodeParser.T__21)
                self.state = 335
                self.expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 336
                localctx.left = self.expr(0)
                self.state = 337
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 338
                localctx.right = self.expr(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 340
                localctx.left = self.expr(0)
                self.state = 341
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==21 or _la==26):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 342
                localctx.right = self.expr(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 344
                localctx.left = self.expr(0)
                self.state = 345
                self.match(ZCodeParser.T__33)
                self.state = 346
                localctx.right = self.expr(0)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 348
                localctx.left = self.expr(0)
                self.state = 349
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==35 or _la==36):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 350
                localctx.right = self.expr(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 352
                self.match(ZCodeParser.T__15)
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5222686588960) != 0):
                    self.state = 353
                    self.expr(0)
                    self.state = 358
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==15:
                        self.state = 354
                        self.match(ZCodeParser.T__14)
                        self.state = 355
                        self.expr(0)
                        self.state = 360
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 363
                self.match(ZCodeParser.T__16)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 364
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 365
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 366
                self.match(ZCodeParser.IDENTIFIER)
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
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 12)
         




