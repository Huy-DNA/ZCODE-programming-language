# Generated from /home/hell/projects/ZCODE-programming-language/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,52,452,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,130,8,0,1,1,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,
        6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,
        16,1,16,1,17,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,
        22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,
        25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,
        31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,
        34,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,278,8,38,1,39,1,39,3,
        39,282,8,39,1,39,3,39,285,8,39,1,40,1,40,3,40,289,8,40,1,40,1,40,
        1,40,3,40,294,8,40,1,40,1,40,1,41,1,41,3,41,300,8,41,1,41,4,41,303,
        8,41,11,41,12,41,304,1,41,1,41,3,41,309,8,41,1,41,4,41,312,8,41,
        11,41,12,41,313,1,41,1,41,1,42,1,42,3,42,320,8,42,1,42,4,42,323,
        8,42,11,42,12,42,324,1,42,1,42,1,43,1,43,5,43,331,8,43,10,43,12,
        43,334,9,43,1,44,1,44,5,44,338,8,44,10,44,12,44,341,9,44,1,44,1,
        44,1,45,4,45,346,8,45,11,45,12,45,347,1,46,1,46,5,46,352,8,46,10,
        46,12,46,355,9,46,1,47,1,47,1,47,3,47,360,8,47,1,47,4,47,363,8,47,
        11,47,12,47,364,1,48,1,48,1,48,1,48,5,48,371,8,48,10,48,12,48,374,
        9,48,1,48,4,48,377,8,48,11,48,12,48,378,1,48,1,48,1,48,5,48,384,
        8,48,10,48,12,48,387,9,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,5,49,
        396,8,49,10,49,12,49,399,9,49,1,49,1,49,3,49,403,8,49,1,49,1,49,
        1,50,1,50,1,50,1,50,1,50,1,50,1,50,3,50,414,8,50,5,50,416,8,50,10,
        50,12,50,419,9,50,1,50,1,50,1,50,1,51,1,51,1,51,1,52,1,52,1,52,1,
        52,5,52,431,8,52,10,52,12,52,434,9,52,1,52,1,52,1,53,4,53,439,8,
        53,11,53,12,53,440,1,53,1,53,1,54,3,54,446,8,54,1,54,1,54,1,55,1,
        55,1,55,1,397,0,56,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,
        21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,
        43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,
        65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,
        87,44,89,45,91,0,93,0,95,0,97,46,99,47,101,48,103,0,105,49,107,50,
        109,51,111,52,1,0,10,2,0,69,69,101,101,3,0,65,90,95,95,97,122,1,
        0,48,57,4,0,48,57,65,90,95,95,97,122,1,0,34,34,4,0,10,10,13,13,34,
        34,92,92,5,0,39,39,92,92,98,98,102,102,116,116,7,0,39,39,92,92,98,
        98,102,102,110,110,114,114,116,116,2,0,10,10,13,13,3,0,9,9,12,12,
        32,32,484,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,
        0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,
        0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,
        0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,
        0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,
        0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,
        0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,
        0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,
        0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,
        0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,105,1,0,0,0,0,107,
        1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,1,129,1,0,0,0,3,131,1,0,0,0,
        5,134,1,0,0,0,7,139,1,0,0,0,9,144,1,0,0,0,11,148,1,0,0,0,13,150,
        1,0,0,0,15,152,1,0,0,0,17,154,1,0,0,0,19,156,1,0,0,0,21,160,1,0,
        0,0,23,163,1,0,0,0,25,167,1,0,0,0,27,170,1,0,0,0,29,172,1,0,0,0,
        31,175,1,0,0,0,33,178,1,0,0,0,35,180,1,0,0,0,37,183,1,0,0,0,39,185,
        1,0,0,0,41,187,1,0,0,0,43,189,1,0,0,0,45,191,1,0,0,0,47,193,1,0,
        0,0,49,199,1,0,0,0,51,203,1,0,0,0,53,207,1,0,0,0,55,210,1,0,0,0,
        57,214,1,0,0,0,59,222,1,0,0,0,61,224,1,0,0,0,63,230,1,0,0,0,65,236,
        1,0,0,0,67,245,1,0,0,0,69,252,1,0,0,0,71,257,1,0,0,0,73,259,1,0,
        0,0,75,265,1,0,0,0,77,277,1,0,0,0,79,279,1,0,0,0,81,286,1,0,0,0,
        83,297,1,0,0,0,85,317,1,0,0,0,87,328,1,0,0,0,89,335,1,0,0,0,91,345,
        1,0,0,0,93,349,1,0,0,0,95,356,1,0,0,0,97,366,1,0,0,0,99,391,1,0,
        0,0,101,406,1,0,0,0,103,423,1,0,0,0,105,426,1,0,0,0,107,438,1,0,
        0,0,109,445,1,0,0,0,111,449,1,0,0,0,113,114,5,110,0,0,114,115,5,
        117,0,0,115,116,5,109,0,0,116,117,5,98,0,0,117,118,5,101,0,0,118,
        130,5,114,0,0,119,120,5,115,0,0,120,121,5,116,0,0,121,122,5,114,
        0,0,122,123,5,105,0,0,123,124,5,110,0,0,124,130,5,103,0,0,125,126,
        5,98,0,0,126,127,5,111,0,0,127,128,5,111,0,0,128,130,5,108,0,0,129,
        113,1,0,0,0,129,119,1,0,0,0,129,125,1,0,0,0,130,2,1,0,0,0,131,132,
        5,105,0,0,132,133,5,102,0,0,133,4,1,0,0,0,134,135,5,101,0,0,135,
        136,5,108,0,0,136,137,5,105,0,0,137,138,5,102,0,0,138,6,1,0,0,0,
        139,140,5,101,0,0,140,141,5,108,0,0,141,142,5,115,0,0,142,143,5,
        101,0,0,143,8,1,0,0,0,144,145,5,102,0,0,145,146,5,111,0,0,146,147,
        5,114,0,0,147,10,1,0,0,0,148,149,5,45,0,0,149,12,1,0,0,0,150,151,
        5,43,0,0,151,14,1,0,0,0,152,153,5,42,0,0,153,16,1,0,0,0,154,155,
        5,47,0,0,155,18,1,0,0,0,156,157,5,97,0,0,157,158,5,110,0,0,158,159,
        5,100,0,0,159,20,1,0,0,0,160,161,5,111,0,0,161,162,5,114,0,0,162,
        22,1,0,0,0,163,164,5,46,0,0,164,165,5,46,0,0,165,166,5,46,0,0,166,
        24,1,0,0,0,167,168,5,60,0,0,168,169,5,45,0,0,169,26,1,0,0,0,170,
        171,5,61,0,0,171,28,1,0,0,0,172,173,5,61,0,0,173,174,5,61,0,0,174,
        30,1,0,0,0,175,176,5,62,0,0,176,177,5,61,0,0,177,32,1,0,0,0,178,
        179,5,62,0,0,179,34,1,0,0,0,180,181,5,60,0,0,181,182,5,61,0,0,182,
        36,1,0,0,0,183,184,5,60,0,0,184,38,1,0,0,0,185,186,5,40,0,0,186,
        40,1,0,0,0,187,188,5,41,0,0,188,42,1,0,0,0,189,190,5,91,0,0,190,
        44,1,0,0,0,191,192,5,93,0,0,192,46,1,0,0,0,193,194,5,98,0,0,194,
        195,5,101,0,0,195,196,5,103,0,0,196,197,5,105,0,0,197,198,5,110,
        0,0,198,48,1,0,0,0,199,200,5,101,0,0,200,201,5,110,0,0,201,202,5,
        100,0,0,202,50,1,0,0,0,203,204,5,110,0,0,204,205,5,111,0,0,205,206,
        5,116,0,0,206,52,1,0,0,0,207,208,5,33,0,0,208,209,5,61,0,0,209,54,
        1,0,0,0,210,211,5,118,0,0,211,212,5,97,0,0,212,213,5,114,0,0,213,
        56,1,0,0,0,214,215,5,100,0,0,215,216,5,121,0,0,216,217,5,110,0,0,
        217,218,5,97,0,0,218,219,5,109,0,0,219,220,5,105,0,0,220,221,5,99,
        0,0,221,58,1,0,0,0,222,223,5,44,0,0,223,60,1,0,0,0,224,225,5,112,
        0,0,225,226,5,114,0,0,226,227,5,105,0,0,227,228,5,110,0,0,228,229,
        5,116,0,0,229,62,1,0,0,0,230,231,5,98,0,0,231,232,5,114,0,0,232,
        233,5,101,0,0,233,234,5,97,0,0,234,235,5,107,0,0,235,64,1,0,0,0,
        236,237,5,99,0,0,237,238,5,111,0,0,238,239,5,110,0,0,239,240,5,116,
        0,0,240,241,5,105,0,0,241,242,5,110,0,0,242,243,5,117,0,0,243,244,
        5,101,0,0,244,66,1,0,0,0,245,246,5,114,0,0,246,247,5,101,0,0,247,
        248,5,116,0,0,248,249,5,117,0,0,249,250,5,114,0,0,250,251,5,110,
        0,0,251,68,1,0,0,0,252,253,5,102,0,0,253,254,5,117,0,0,254,255,5,
        110,0,0,255,256,5,99,0,0,256,70,1,0,0,0,257,258,5,37,0,0,258,72,
        1,0,0,0,259,260,5,117,0,0,260,261,5,110,0,0,261,262,5,116,0,0,262,
        263,5,105,0,0,263,264,5,108,0,0,264,74,1,0,0,0,265,266,5,98,0,0,
        266,267,5,121,0,0,267,76,1,0,0,0,268,269,5,116,0,0,269,270,5,114,
        0,0,270,271,5,117,0,0,271,278,5,101,0,0,272,273,5,102,0,0,273,274,
        5,97,0,0,274,275,5,108,0,0,275,276,5,115,0,0,276,278,5,101,0,0,277,
        268,1,0,0,0,277,272,1,0,0,0,278,78,1,0,0,0,279,281,3,91,45,0,280,
        282,3,93,46,0,281,280,1,0,0,0,281,282,1,0,0,0,282,284,1,0,0,0,283,
        285,3,95,47,0,284,283,1,0,0,0,284,285,1,0,0,0,285,80,1,0,0,0,286,
        288,3,91,45,0,287,289,3,93,46,0,288,287,1,0,0,0,288,289,1,0,0,0,
        289,290,1,0,0,0,290,293,7,0,0,0,291,294,3,13,6,0,292,294,3,11,5,
        0,293,291,1,0,0,0,293,292,1,0,0,0,293,294,1,0,0,0,294,295,1,0,0,
        0,295,296,6,40,0,0,296,82,1,0,0,0,297,299,3,91,45,0,298,300,3,93,
        46,0,299,298,1,0,0,0,299,300,1,0,0,0,300,302,1,0,0,0,301,303,7,1,
        0,0,302,301,1,0,0,0,303,304,1,0,0,0,304,302,1,0,0,0,304,305,1,0,
        0,0,305,308,1,0,0,0,306,309,3,13,6,0,307,309,3,11,5,0,308,306,1,
        0,0,0,308,307,1,0,0,0,308,309,1,0,0,0,309,311,1,0,0,0,310,312,7,
        2,0,0,311,310,1,0,0,0,312,313,1,0,0,0,313,311,1,0,0,0,313,314,1,
        0,0,0,314,315,1,0,0,0,315,316,6,41,1,0,316,84,1,0,0,0,317,319,3,
        91,45,0,318,320,3,93,46,0,319,318,1,0,0,0,319,320,1,0,0,0,320,322,
        1,0,0,0,321,323,7,1,0,0,322,321,1,0,0,0,323,324,1,0,0,0,324,322,
        1,0,0,0,324,325,1,0,0,0,325,326,1,0,0,0,326,327,6,42,2,0,327,86,
        1,0,0,0,328,332,7,1,0,0,329,331,7,3,0,0,330,329,1,0,0,0,331,334,
        1,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,88,1,0,0,0,334,332,1,
        0,0,0,335,339,7,2,0,0,336,338,7,3,0,0,337,336,1,0,0,0,338,341,1,
        0,0,0,339,337,1,0,0,0,339,340,1,0,0,0,340,342,1,0,0,0,341,339,1,
        0,0,0,342,343,6,44,3,0,343,90,1,0,0,0,344,346,7,2,0,0,345,344,1,
        0,0,0,346,347,1,0,0,0,347,345,1,0,0,0,347,348,1,0,0,0,348,92,1,0,
        0,0,349,353,5,46,0,0,350,352,7,2,0,0,351,350,1,0,0,0,352,355,1,0,
        0,0,353,351,1,0,0,0,353,354,1,0,0,0,354,94,1,0,0,0,355,353,1,0,0,
        0,356,359,7,0,0,0,357,360,3,13,6,0,358,360,3,11,5,0,359,357,1,0,
        0,0,359,358,1,0,0,0,359,360,1,0,0,0,360,362,1,0,0,0,361,363,7,2,
        0,0,362,361,1,0,0,0,363,364,1,0,0,0,364,362,1,0,0,0,364,365,1,0,
        0,0,365,96,1,0,0,0,366,372,5,34,0,0,367,371,8,4,0,0,368,369,5,39,
        0,0,369,371,5,34,0,0,370,367,1,0,0,0,370,368,1,0,0,0,371,374,1,0,
        0,0,372,370,1,0,0,0,372,373,1,0,0,0,373,376,1,0,0,0,374,372,1,0,
        0,0,375,377,3,103,51,0,376,375,1,0,0,0,377,378,1,0,0,0,378,376,1,
        0,0,0,378,379,1,0,0,0,379,385,1,0,0,0,380,384,8,4,0,0,381,382,5,
        39,0,0,382,384,5,34,0,0,383,380,1,0,0,0,383,381,1,0,0,0,384,387,
        1,0,0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,388,1,0,0,0,387,385,
        1,0,0,0,388,389,5,34,0,0,389,390,6,48,4,0,390,98,1,0,0,0,391,397,
        5,34,0,0,392,396,8,4,0,0,393,394,5,39,0,0,394,396,5,34,0,0,395,392,
        1,0,0,0,395,393,1,0,0,0,396,399,1,0,0,0,397,398,1,0,0,0,397,395,
        1,0,0,0,398,402,1,0,0,0,399,397,1,0,0,0,400,403,3,109,54,0,401,403,
        5,0,0,1,402,400,1,0,0,0,402,401,1,0,0,0,403,404,1,0,0,0,404,405,
        6,49,5,0,405,100,1,0,0,0,406,417,5,34,0,0,407,416,8,5,0,0,408,409,
        5,39,0,0,409,416,5,34,0,0,410,411,5,92,0,0,411,413,7,6,0,0,412,414,
        8,4,0,0,413,412,1,0,0,0,413,414,1,0,0,0,414,416,1,0,0,0,415,407,
        1,0,0,0,415,408,1,0,0,0,415,410,1,0,0,0,416,419,1,0,0,0,417,415,
        1,0,0,0,417,418,1,0,0,0,418,420,1,0,0,0,419,417,1,0,0,0,420,421,
        5,34,0,0,421,422,6,50,6,0,422,102,1,0,0,0,423,424,5,92,0,0,424,425,
        8,7,0,0,425,104,1,0,0,0,426,427,5,35,0,0,427,428,5,35,0,0,428,432,
        1,0,0,0,429,431,8,8,0,0,430,429,1,0,0,0,431,434,1,0,0,0,432,430,
        1,0,0,0,432,433,1,0,0,0,433,435,1,0,0,0,434,432,1,0,0,0,435,436,
        6,52,7,0,436,106,1,0,0,0,437,439,7,9,0,0,438,437,1,0,0,0,439,440,
        1,0,0,0,440,438,1,0,0,0,440,441,1,0,0,0,441,442,1,0,0,0,442,443,
        6,53,7,0,443,108,1,0,0,0,444,446,5,13,0,0,445,444,1,0,0,0,445,446,
        1,0,0,0,446,447,1,0,0,0,447,448,5,10,0,0,448,110,1,0,0,0,449,450,
        9,0,0,0,450,451,6,55,8,0,451,112,1,0,0,0,33,0,129,277,281,284,288,
        293,299,304,308,313,319,324,332,339,347,353,359,364,370,372,378,
        383,385,395,397,402,413,415,417,432,440,445,9,1,40,0,1,41,1,1,42,
        2,1,44,3,1,48,4,1,49,5,1,50,6,6,0,0,1,55,7
    ]

class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TYPE = 1
    IF = 2
    ELIF = 3
    ELSE = 4
    FOR = 5
    SUB = 6
    ADD = 7
    MUL = 8
    DIV = 9
    AND = 10
    OR = 11
    CONCAT = 12
    ASSIGN = 13
    EQ = 14
    DEQ = 15
    GE = 16
    GT = 17
    LE = 18
    LT = 19
    LP = 20
    RP = 21
    LB = 22
    RB = 23
    BEGIN = 24
    END = 25
    NOT = 26
    NEQ = 27
    VAR = 28
    DYN = 29
    COMMA = 30
    PRINT = 31
    BREAK = 32
    CONTINUE = 33
    RETURN = 34
    FUNC = 35
    MOD = 36
    UNTIL = 37
    BY = 38
    BOOLEAN = 39
    NUMBER = 40
    INVALID_NUMBER_1 = 41
    INVALID_NUMBER_2 = 42
    INVALID_NUMBER_3 = 43
    IDENTIFIER = 44
    INVALID_IDENTIFIER = 45
    ILLEGAL_ESCAPE = 46
    UNCLOSE_STRING = 47
    STRING = 48
    COMMENT = 49
    WS = 50
    NEWLINE = 51
    ERROR_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'elif'", "'else'", "'for'", "'-'", "'+'", "'*'", "'/'", 
            "'and'", "'or'", "'...'", "'<-'", "'='", "'=='", "'>='", "'>'", 
            "'<='", "'<'", "'('", "')'", "'['", "']'", "'begin'", "'end'", 
            "'not'", "'!='", "'var'", "'dynamic'", "','", "'print'", "'break'", 
            "'continue'", "'return'", "'func'", "'%'", "'until'", "'by'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "IF", "ELIF", "ELSE", "FOR", "SUB", "ADD", "MUL", "DIV", 
            "AND", "OR", "CONCAT", "ASSIGN", "EQ", "DEQ", "GE", "GT", "LE", 
            "LT", "LP", "RP", "LB", "RB", "BEGIN", "END", "NOT", "NEQ", 
            "VAR", "DYN", "COMMA", "PRINT", "BREAK", "CONTINUE", "RETURN", 
            "FUNC", "MOD", "UNTIL", "BY", "BOOLEAN", "NUMBER", "INVALID_NUMBER_1", 
            "INVALID_NUMBER_2", "INVALID_NUMBER_3", "IDENTIFIER", "INVALID_IDENTIFIER", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRING", "COMMENT", "WS", 
            "NEWLINE", "ERROR_CHAR" ]

    ruleNames = [ "TYPE", "IF", "ELIF", "ELSE", "FOR", "SUB", "ADD", "MUL", 
                  "DIV", "AND", "OR", "CONCAT", "ASSIGN", "EQ", "DEQ", "GE", 
                  "GT", "LE", "LT", "LP", "RP", "LB", "RB", "BEGIN", "END", 
                  "NOT", "NEQ", "VAR", "DYN", "COMMA", "PRINT", "BREAK", 
                  "CONTINUE", "RETURN", "FUNC", "MOD", "UNTIL", "BY", "BOOLEAN", 
                  "NUMBER", "INVALID_NUMBER_1", "INVALID_NUMBER_2", "INVALID_NUMBER_3", 
                  "IDENTIFIER", "INVALID_IDENTIFIER", "INTEGRAL", "DECIMAL", 
                  "EXPONENT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRING", 
                  "INVALID_ESCAPED_SEQUENCE", "COMMENT", "WS", "NEWLINE", 
                  "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None





    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[40] = self.INVALID_NUMBER_1_action 
            actions[41] = self.INVALID_NUMBER_2_action 
            actions[42] = self.INVALID_NUMBER_3_action 
            actions[44] = self.INVALID_IDENTIFIER_action 
            actions[48] = self.ILLEGAL_ESCAPE_action 
            actions[49] = self.UNCLOSE_STRING_action 
            actions[50] = self.STRING_action 
            actions[55] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INVALID_NUMBER_1_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def INVALID_NUMBER_2_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def INVALID_NUMBER_3_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def INVALID_IDENTIFIER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise UncloseString(self.text)
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
             self.text = str(bytes(self.text, "utf-8").decode("unicode_escape"))[1:-1].replace('\'"', '"')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     


