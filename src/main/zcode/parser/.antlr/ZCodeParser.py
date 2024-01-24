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
        4,1,48,360,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,3,0,46,8,0,1,0,1,0,1,0,5,0,51,8,0,10,0,12,0,54,
        9,0,3,0,56,8,0,1,0,3,0,59,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,
        1,5,1,6,1,6,1,6,5,6,89,8,6,10,6,12,6,92,9,6,1,6,1,6,1,6,1,6,1,6,
        5,6,99,8,6,10,6,12,6,102,9,6,1,6,1,6,5,6,106,8,6,10,6,12,6,109,9,
        6,1,6,1,6,1,6,5,6,114,8,6,10,6,12,6,117,9,6,1,6,1,6,5,6,121,8,6,
        10,6,12,6,124,9,6,1,6,5,6,127,8,6,10,6,12,6,130,9,6,1,6,1,6,5,6,
        134,8,6,10,6,12,6,137,9,6,1,6,3,6,140,8,6,3,6,142,8,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,5,7,151,8,7,10,7,12,7,154,9,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,5,8,163,8,8,10,8,12,8,166,9,8,3,8,168,8,8,1,8,1,8,1,
        8,1,9,1,9,1,9,1,9,5,9,177,8,9,10,9,12,9,180,9,9,1,9,1,9,3,9,184,
        8,9,3,9,186,8,9,1,10,1,10,1,10,1,10,3,10,192,8,10,1,10,1,10,1,10,
        1,10,3,10,198,8,10,5,10,200,8,10,10,10,12,10,203,9,10,3,10,205,8,
        10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,213,8,11,10,11,12,11,216,9,
        11,3,11,218,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,238,8,13,1,14,1,
        14,1,14,1,14,1,14,1,14,5,14,246,8,14,10,14,12,14,249,9,14,1,15,1,
        15,1,15,1,15,1,15,1,15,5,15,257,8,15,10,15,12,15,260,9,15,1,16,1,
        16,1,16,1,16,1,16,3,16,267,8,16,1,17,1,17,1,17,1,17,1,17,1,17,5,
        17,275,8,17,10,17,12,17,278,9,17,1,18,1,18,1,18,1,18,1,18,3,18,285,
        8,18,1,19,1,19,1,19,1,19,1,19,3,19,292,8,19,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,5,20,302,8,20,10,20,12,20,305,9,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,5,20,314,8,20,10,20,12,20,317,9,20,3,20,
        319,8,20,1,20,5,20,322,8,20,10,20,12,20,325,9,20,1,21,1,21,1,21,
        1,21,5,21,331,8,21,10,21,12,21,334,9,21,3,21,336,8,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,5,21,346,8,21,10,21,12,21,349,9,21,
        3,21,351,8,21,1,21,1,21,1,21,1,21,1,21,3,21,358,8,21,1,21,1,122,
        4,28,30,34,40,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,0,4,1,0,22,24,1,0,25,26,1,0,27,33,1,0,34,35,395,0,45,
        1,0,0,0,2,73,1,0,0,0,4,75,1,0,0,0,6,78,1,0,0,0,8,80,1,0,0,0,10,82,
        1,0,0,0,12,141,1,0,0,0,14,143,1,0,0,0,16,157,1,0,0,0,18,172,1,0,
        0,0,20,187,1,0,0,0,22,208,1,0,0,0,24,221,1,0,0,0,26,237,1,0,0,0,
        28,239,1,0,0,0,30,250,1,0,0,0,32,266,1,0,0,0,34,268,1,0,0,0,36,284,
        1,0,0,0,38,291,1,0,0,0,40,293,1,0,0,0,42,357,1,0,0,0,44,46,5,44,
        0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,55,1,0,0,0,47,52,3,2,1,0,48,49,
        5,44,0,0,49,51,3,2,1,0,50,48,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,
        52,53,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,55,47,1,0,0,0,55,56,1,
        0,0,0,56,58,1,0,0,0,57,59,5,44,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,
        60,1,0,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,74,3,28,14,0,63,74,3,26,
        13,0,64,74,3,24,12,0,65,74,3,16,8,0,66,74,3,18,9,0,67,74,3,6,3,0,
        68,74,3,8,4,0,69,74,3,10,5,0,70,74,3,12,6,0,71,74,3,14,7,0,72,74,
        3,4,2,0,73,62,1,0,0,0,73,63,1,0,0,0,73,64,1,0,0,0,73,65,1,0,0,0,
        73,66,1,0,0,0,73,67,1,0,0,0,73,68,1,0,0,0,73,69,1,0,0,0,73,70,1,
        0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,3,1,0,0,0,75,76,5,1,0,0,76,
        77,3,28,14,0,77,5,1,0,0,0,78,79,5,2,0,0,79,7,1,0,0,0,80,81,5,3,0,
        0,81,9,1,0,0,0,82,83,5,4,0,0,83,84,3,28,14,0,84,11,1,0,0,0,85,86,
        5,5,0,0,86,90,3,28,14,0,87,89,5,44,0,0,88,87,1,0,0,0,89,92,1,0,0,
        0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,90,1,0,0,0,93,94,
        3,2,1,0,94,142,1,0,0,0,95,96,5,5,0,0,96,100,3,28,14,0,97,99,5,44,
        0,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,
        101,103,1,0,0,0,102,100,1,0,0,0,103,122,3,2,1,0,104,106,5,44,0,0,
        105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,
        108,110,1,0,0,0,109,107,1,0,0,0,110,111,5,6,0,0,111,115,3,28,14,
        0,112,114,5,44,0,0,113,112,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,
        0,115,116,1,0,0,0,116,118,1,0,0,0,117,115,1,0,0,0,118,119,3,2,1,
        0,119,121,1,0,0,0,120,107,1,0,0,0,121,124,1,0,0,0,122,123,1,0,0,
        0,122,120,1,0,0,0,123,139,1,0,0,0,124,122,1,0,0,0,125,127,5,44,0,
        0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,
        0,129,131,1,0,0,0,130,128,1,0,0,0,131,135,5,7,0,0,132,134,5,44,0,
        0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,
        0,136,138,1,0,0,0,137,135,1,0,0,0,138,140,3,2,1,0,139,128,1,0,0,
        0,139,140,1,0,0,0,140,142,1,0,0,0,141,85,1,0,0,0,141,95,1,0,0,0,
        142,13,1,0,0,0,143,144,5,8,0,0,144,145,3,28,14,0,145,146,5,9,0,0,
        146,147,3,28,14,0,147,148,5,10,0,0,148,152,3,28,14,0,149,151,5,44,
        0,0,150,149,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,
        0,0,153,155,1,0,0,0,154,152,1,0,0,0,155,156,3,2,1,0,156,15,1,0,0,
        0,157,158,5,11,0,0,158,167,5,44,0,0,159,164,3,2,1,0,160,161,5,44,
        0,0,161,163,3,2,1,0,162,160,1,0,0,0,163,166,1,0,0,0,164,162,1,0,
        0,0,164,165,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,167,159,1,0,
        0,0,167,168,1,0,0,0,168,169,1,0,0,0,169,170,5,44,0,0,170,171,5,12,
        0,0,171,17,1,0,0,0,172,173,5,13,0,0,173,174,5,39,0,0,174,185,3,20,
        10,0,175,177,5,44,0,0,176,175,1,0,0,0,177,180,1,0,0,0,178,176,1,
        0,0,0,178,179,1,0,0,0,179,183,1,0,0,0,180,178,1,0,0,0,181,184,3,
        10,5,0,182,184,3,16,8,0,183,181,1,0,0,0,183,182,1,0,0,0,184,186,
        1,0,0,0,185,178,1,0,0,0,185,186,1,0,0,0,186,19,1,0,0,0,187,204,5,
        14,0,0,188,189,5,38,0,0,189,191,5,39,0,0,190,192,3,22,11,0,191,190,
        1,0,0,0,191,192,1,0,0,0,192,201,1,0,0,0,193,194,5,15,0,0,194,195,
        5,38,0,0,195,197,5,39,0,0,196,198,3,22,11,0,197,196,1,0,0,0,197,
        198,1,0,0,0,198,200,1,0,0,0,199,193,1,0,0,0,200,203,1,0,0,0,201,
        199,1,0,0,0,201,202,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,204,
        188,1,0,0,0,204,205,1,0,0,0,205,206,1,0,0,0,206,207,5,16,0,0,207,
        21,1,0,0,0,208,217,5,17,0,0,209,214,5,40,0,0,210,211,5,15,0,0,211,
        213,5,40,0,0,212,210,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,
        215,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,217,209,1,0,0,0,217,
        218,1,0,0,0,218,219,1,0,0,0,219,220,5,18,0,0,220,23,1,0,0,0,221,
        222,3,28,14,0,222,223,5,19,0,0,223,224,3,28,14,0,224,25,1,0,0,0,
        225,226,5,38,0,0,226,227,3,28,14,0,227,228,5,19,0,0,228,229,3,28,
        14,0,229,238,1,0,0,0,230,231,5,20,0,0,231,232,3,28,14,0,232,233,
        5,19,0,0,233,234,3,28,14,0,234,238,1,0,0,0,235,236,5,21,0,0,236,
        238,3,28,14,0,237,225,1,0,0,0,237,230,1,0,0,0,237,235,1,0,0,0,238,
        27,1,0,0,0,239,240,6,14,-1,0,240,241,3,30,15,0,241,247,1,0,0,0,242,
        243,10,2,0,0,243,244,7,0,0,0,244,246,3,30,15,0,245,242,1,0,0,0,246,
        249,1,0,0,0,247,245,1,0,0,0,247,248,1,0,0,0,248,29,1,0,0,0,249,247,
        1,0,0,0,250,251,6,15,-1,0,251,252,3,32,16,0,252,258,1,0,0,0,253,
        254,10,2,0,0,254,255,7,1,0,0,255,257,3,32,16,0,256,253,1,0,0,0,257,
        260,1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,259,31,1,0,0,0,260,258,
        1,0,0,0,261,262,3,34,17,0,262,263,7,2,0,0,263,264,3,34,17,0,264,
        267,1,0,0,0,265,267,3,34,17,0,266,261,1,0,0,0,266,265,1,0,0,0,267,
        33,1,0,0,0,268,269,6,17,-1,0,269,270,3,36,18,0,270,276,1,0,0,0,271,
        272,10,2,0,0,272,273,7,3,0,0,273,275,3,36,18,0,274,271,1,0,0,0,275,
        278,1,0,0,0,276,274,1,0,0,0,276,277,1,0,0,0,277,35,1,0,0,0,278,276,
        1,0,0,0,279,280,3,38,19,0,280,281,5,36,0,0,281,282,3,38,19,0,282,
        285,1,0,0,0,283,285,3,38,19,0,284,279,1,0,0,0,284,283,1,0,0,0,285,
        37,1,0,0,0,286,287,5,26,0,0,287,292,3,38,19,0,288,289,5,37,0,0,289,
        292,3,38,19,0,290,292,3,40,20,0,291,286,1,0,0,0,291,288,1,0,0,0,
        291,290,1,0,0,0,292,39,1,0,0,0,293,294,6,20,-1,0,294,295,3,42,21,
        0,295,323,1,0,0,0,296,297,10,3,0,0,297,298,5,17,0,0,298,303,3,28,
        14,0,299,300,5,15,0,0,300,302,3,28,14,0,301,299,1,0,0,0,302,305,
        1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,306,1,0,0,0,305,303,
        1,0,0,0,306,307,5,18,0,0,307,322,1,0,0,0,308,309,10,2,0,0,309,318,
        5,14,0,0,310,315,3,28,14,0,311,312,5,15,0,0,312,314,3,28,14,0,313,
        311,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,315,316,1,0,0,0,316,
        319,1,0,0,0,317,315,1,0,0,0,318,310,1,0,0,0,318,319,1,0,0,0,319,
        320,1,0,0,0,320,322,5,16,0,0,321,296,1,0,0,0,321,308,1,0,0,0,322,
        325,1,0,0,0,323,321,1,0,0,0,323,324,1,0,0,0,324,41,1,0,0,0,325,323,
        1,0,0,0,326,335,5,17,0,0,327,328,3,28,14,0,328,332,5,15,0,0,329,
        331,3,28,14,0,330,329,1,0,0,0,331,334,1,0,0,0,332,330,1,0,0,0,332,
        333,1,0,0,0,333,336,1,0,0,0,334,332,1,0,0,0,335,327,1,0,0,0,335,
        336,1,0,0,0,336,337,1,0,0,0,337,358,5,18,0,0,338,358,5,40,0,0,339,
        358,5,43,0,0,340,358,5,39,0,0,341,350,5,17,0,0,342,347,3,28,14,0,
        343,344,5,15,0,0,344,346,3,28,14,0,345,343,1,0,0,0,346,349,1,0,0,
        0,347,345,1,0,0,0,347,348,1,0,0,0,348,351,1,0,0,0,349,347,1,0,0,
        0,350,342,1,0,0,0,350,351,1,0,0,0,351,352,1,0,0,0,352,358,5,18,0,
        0,353,354,5,14,0,0,354,355,3,28,14,0,355,356,5,16,0,0,356,358,1,
        0,0,0,357,326,1,0,0,0,357,338,1,0,0,0,357,339,1,0,0,0,357,340,1,
        0,0,0,357,341,1,0,0,0,357,353,1,0,0,0,358,43,1,0,0,0,43,45,52,55,
        58,73,90,100,107,115,122,128,135,139,141,152,164,167,178,183,185,
        191,197,201,204,214,217,237,247,258,266,276,284,291,303,315,318,
        321,323,332,335,347,350,357
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'break'", "'continue'", "'return'", 
                     "'if'", "'elif'", "'else'", "'for'", "'until'", "'by'", 
                     "'begin'", "'end'", "'func'", "'('", "','", "')'", 
                     "'['", "']'", "'<-'", "'var'", "'dynamic'", "'*'", 
                     "'/'", "'%'", "'+'", "'-'", "'='", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'and'", "'or'", "'...'", 
                     "'not'" ]

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
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 44
                self.match(ZCodeParser.NULL_LINES)


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10857747736894) != 0):
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
            self.match(ZCodeParser.T__0)
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_r_break




    def r_break(self):

        localctx = ZCodeParser.R_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_r_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
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
            self.state = 80
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
            self.state = 82
            self.match(ZCodeParser.T__3)
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(ZCodeParser.T__4)
                self.state = 86
                self.expr(0)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 87
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 93
                self.stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(ZCodeParser.T__4)
                self.state = 96
                self.expr(0)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 97
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.stm()
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 107
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==44:
                            self.state = 104
                            self.match(ZCodeParser.NULL_LINES)
                            self.state = 109
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 110
                        self.match(ZCodeParser.T__5)
                        self.state = 111
                        self.expr(0)
                        self.state = 115
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==44:
                            self.state = 112
                            self.match(ZCodeParser.NULL_LINES)
                            self.state = 117
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 118
                        self.stm() 
                    self.state = 124
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 139
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 128
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==44:
                        self.state = 125
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 130
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 131
                    self.match(ZCodeParser.T__6)
                    self.state = 135
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==44:
                        self.state = 132
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 137
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 138
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
            self.state = 143
            self.match(ZCodeParser.T__7)
            self.state = 144
            self.expr(0)
            self.state = 145
            self.match(ZCodeParser.T__8)
            self.state = 146
            self.expr(0)
            self.state = 147
            self.match(ZCodeParser.T__9)
            self.state = 148
            self.expr(0)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 149
                self.match(ZCodeParser.NULL_LINES)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
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
            self.state = 157
            self.match(ZCodeParser.T__10)
            self.state = 158
            self.match(ZCodeParser.NULL_LINES)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10857747736894) != 0):
                self.state = 159
                self.stm()
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 160
                        self.match(ZCodeParser.NULL_LINES)
                        self.state = 161
                        self.stm() 
                    self.state = 166
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)



            self.state = 169
            self.match(ZCodeParser.NULL_LINES)
            self.state = 170
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
            self.state = 172
            self.match(ZCodeParser.T__12)
            self.state = 173
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 174
            self.args()
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 175
                    self.match(ZCodeParser.NULL_LINES)
                    self.state = 180
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 183
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 181
                    self.r_return()
                    pass
                elif token in [11]:
                    self.state = 182
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
            self.state = 187
            self.match(ZCodeParser.T__13)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
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


                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 193
                    self.match(ZCodeParser.T__14)
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


                    self.state = 203
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 206
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
            self.state = 208
            self.match(ZCodeParser.T__16)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 209
                self.match(ZCodeParser.NUMBER)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 210
                    self.match(ZCodeParser.T__14)
                    self.state = 211
                    self.match(ZCodeParser.NUMBER)
                    self.state = 216
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 219
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
            self.state = 221
            self.expr(0)
            self.state = 222
            self.match(ZCodeParser.T__18)
            self.state = 223
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
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(ZCodeParser.TYPE)
                self.state = 226
                self.expr(0)
                self.state = 227
                self.match(ZCodeParser.T__18)
                self.state = 228
                self.expr(0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(ZCodeParser.T__19)
                self.state = 231
                self.expr(0)
                self.state = 232
                self.match(ZCodeParser.T__18)
                self.state = 233
                self.expr(0)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.match(ZCodeParser.T__20)
                self.state = 236
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
            self.state = 240
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 244
                    self.expr1(0) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
            self.state = 251
            self.expr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==26):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 255
                    self.expr2() 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2




    def expr2(self):

        localctx = ZCodeParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.expr3(0)
                self.state = 262
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17045651456) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 263
                self.expr3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
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
            self.state = 269
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 271
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 272
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==34 or _la==35):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 273
                    self.expr4() 
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4




    def expr4(self):

        localctx = ZCodeParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr4)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.expr5()
                self.state = 280
                self.match(ZCodeParser.T__35)
                self.state = 281
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
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

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr5)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(ZCodeParser.T__25)
                self.state = 287
                self.expr5()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.match(ZCodeParser.T__36)
                self.state = 289
                self.expr5()
                pass
            elif token in [14, 17, 39, 40, 43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
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


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


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
            self.state = 294
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 321
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.array = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 296
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 297
                        self.match(ZCodeParser.T__16)
                        self.state = 298
                        localctx.indexer = self.expr(0)
                        self.state = 303
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==15:
                            self.state = 299
                            self.match(ZCodeParser.T__14)
                            self.state = 300
                            localctx.indexer = self.expr(0)
                            self.state = 305
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 306
                        self.match(ZCodeParser.T__17)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr6Context(self, _parentctx, _parentState)
                        localctx.callee = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 308
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 309
                        self.match(ZCodeParser.T__13)
                        self.state = 318
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10582866673664) != 0):
                            self.state = 310
                            localctx.param = self.expr(0)
                            self.state = 315
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==15:
                                self.state = 311
                                self.match(ZCodeParser.T__14)
                                self.state = 312
                                localctx.param = self.expr(0)
                                self.state = 317
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 320
                        self.match(ZCodeParser.T__15)
                        pass

             
                self.state = 325
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
            return ZCodeParser.RULE_term




    def term(self):

        localctx = ZCodeParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(ZCodeParser.T__16)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10582866673664) != 0):
                    self.state = 327
                    self.expr(0)
                    self.state = 328
                    self.match(ZCodeParser.T__14)
                    self.state = 332
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10582866673664) != 0):
                        self.state = 329
                        self.expr(0)
                        self.state = 334
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 337
                self.match(ZCodeParser.T__17)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 340
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 341
                self.match(ZCodeParser.T__16)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 10582866673664) != 0):
                    self.state = 342
                    self.expr(0)
                    self.state = 347
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==15:
                        self.state = 343
                        self.match(ZCodeParser.T__14)
                        self.state = 344
                        self.expr(0)
                        self.state = 349
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 352
                self.match(ZCodeParser.T__17)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 353
                self.match(ZCodeParser.T__13)
                self.state = 354
                self.expr(0)
                self.state = 355
                self.match(ZCodeParser.T__15)
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
         




