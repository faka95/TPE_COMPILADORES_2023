# Generated from gramaticaprueba.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import TablaSimbolos as tablasimbolos
from antlr4.Token import Token
import AnalizadorSemantico.PolacaInversa as Polaca

def serializedATN():
    return [
        4,1,39,459,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,81,
        8,1,1,1,1,1,1,1,1,1,5,1,87,8,1,10,1,12,1,90,9,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,99,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,113,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,135,8,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,145,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,154,8,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,168,8,8,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,194,8,9,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,207,8,10,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,222,8,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,249,
        8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,258,8,14,10,14,12,14,
        261,9,14,1,15,1,15,1,15,1,15,1,15,5,15,268,8,15,10,15,12,15,271,
        9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,296,
        8,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,3,18,327,8,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,20,1,20,1,20,1,20,1,20,3,20,340,8,20,1,21,1,21,1,21,1,22,1,22,
        1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,
        1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,3,29,
        385,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,5,30,400,8,30,10,30,12,30,403,9,30,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,418,8,31,10,31,
        12,31,421,9,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,3,32,438,8,32,1,33,1,33,1,33,1,33,1,33,
        1,33,3,33,446,8,33,1,34,1,34,1,34,1,34,3,34,452,8,34,1,35,1,35,1,
        35,1,35,1,35,1,35,0,5,2,28,30,60,62,36,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,70,0,1,3,0,13,15,22,22,31,32,470,0,72,1,0,0,0,2,80,1,0,
        0,0,4,98,1,0,0,0,6,100,1,0,0,0,8,112,1,0,0,0,10,134,1,0,0,0,12,144,
        1,0,0,0,14,153,1,0,0,0,16,167,1,0,0,0,18,193,1,0,0,0,20,206,1,0,
        0,0,22,221,1,0,0,0,24,223,1,0,0,0,26,235,1,0,0,0,28,248,1,0,0,0,
        30,262,1,0,0,0,32,295,1,0,0,0,34,297,1,0,0,0,36,326,1,0,0,0,38,328,
        1,0,0,0,40,339,1,0,0,0,42,341,1,0,0,0,44,344,1,0,0,0,46,350,1,0,
        0,0,48,354,1,0,0,0,50,359,1,0,0,0,52,361,1,0,0,0,54,367,1,0,0,0,
        56,371,1,0,0,0,58,384,1,0,0,0,60,386,1,0,0,0,62,404,1,0,0,0,64,437,
        1,0,0,0,66,445,1,0,0,0,68,451,1,0,0,0,70,453,1,0,0,0,72,73,5,35,
        0,0,73,74,3,2,1,0,74,75,5,36,0,0,75,76,6,0,-1,0,76,1,1,0,0,0,77,
        78,6,1,-1,0,78,81,3,4,2,0,79,81,3,32,16,0,80,77,1,0,0,0,80,79,1,
        0,0,0,81,88,1,0,0,0,82,83,10,4,0,0,83,87,3,4,2,0,84,85,10,3,0,0,
        85,87,3,32,16,0,86,82,1,0,0,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,
        1,0,0,0,88,89,1,0,0,0,89,3,1,0,0,0,90,88,1,0,0,0,91,92,3,6,3,0,92,
        93,6,2,-1,0,93,99,1,0,0,0,94,99,3,10,5,0,95,96,3,26,13,0,96,97,6,
        2,-1,0,97,99,1,0,0,0,98,91,1,0,0,0,98,94,1,0,0,0,98,95,1,0,0,0,99,
        5,1,0,0,0,100,101,3,58,29,0,101,102,3,8,4,0,102,103,5,26,0,0,103,
        104,6,3,-1,0,104,7,1,0,0,0,105,106,5,16,0,0,106,113,6,4,-1,0,107,
        108,5,16,0,0,108,109,5,33,0,0,109,110,3,8,4,0,110,111,6,4,-1,0,111,
        113,1,0,0,0,112,105,1,0,0,0,112,107,1,0,0,0,113,9,1,0,0,0,114,115,
        5,6,0,0,115,116,5,16,0,0,116,117,6,5,-1,0,117,118,3,12,6,0,118,119,
        5,35,0,0,119,120,3,14,7,0,120,121,5,36,0,0,121,122,5,26,0,0,122,
        123,6,5,-1,0,123,135,1,0,0,0,124,125,5,6,0,0,125,126,5,16,0,0,126,
        127,5,29,0,0,127,128,5,30,0,0,128,129,5,35,0,0,129,130,3,14,7,0,
        130,131,5,36,0,0,131,132,5,26,0,0,132,133,6,5,-1,0,133,135,1,0,0,
        0,134,114,1,0,0,0,134,124,1,0,0,0,135,11,1,0,0,0,136,137,5,29,0,
        0,137,145,5,30,0,0,138,139,5,29,0,0,139,140,3,58,29,0,140,141,5,
        16,0,0,141,142,5,30,0,0,142,143,6,6,-1,0,143,145,1,0,0,0,144,136,
        1,0,0,0,144,138,1,0,0,0,145,13,1,0,0,0,146,147,3,2,1,0,147,148,3,
        16,8,0,148,149,5,26,0,0,149,154,1,0,0,0,150,151,3,16,8,0,151,152,
        5,26,0,0,152,154,1,0,0,0,153,146,1,0,0,0,153,150,1,0,0,0,154,15,
        1,0,0,0,155,168,3,18,9,0,156,157,3,18,9,0,157,158,5,26,0,0,158,159,
        3,16,8,0,159,168,1,0,0,0,160,168,3,24,12,0,161,162,3,24,12,0,162,
        163,5,26,0,0,163,164,3,16,8,0,164,168,1,0,0,0,165,166,5,12,0,0,166,
        168,6,8,-1,0,167,155,1,0,0,0,167,156,1,0,0,0,167,160,1,0,0,0,167,
        161,1,0,0,0,167,165,1,0,0,0,168,17,1,0,0,0,169,170,3,44,22,0,170,
        171,3,20,10,0,171,172,5,3,0,0,172,173,6,9,-1,0,173,194,1,0,0,0,174,
        175,3,44,22,0,175,176,3,20,10,0,176,177,5,2,0,0,177,178,3,46,23,
        0,178,179,5,3,0,0,179,180,6,9,-1,0,180,194,1,0,0,0,181,182,3,44,
        22,0,182,183,3,46,23,0,183,184,3,22,11,0,184,185,5,3,0,0,185,186,
        6,9,-1,0,186,194,1,0,0,0,187,188,3,44,22,0,188,189,3,20,10,0,189,
        190,3,22,11,0,190,191,5,3,0,0,191,192,6,9,-1,0,192,194,1,0,0,0,193,
        169,1,0,0,0,193,174,1,0,0,0,193,181,1,0,0,0,193,187,1,0,0,0,194,
        19,1,0,0,0,195,196,5,35,0,0,196,197,3,16,8,0,197,198,5,26,0,0,198,
        199,5,36,0,0,199,207,1,0,0,0,200,201,5,35,0,0,201,202,3,30,15,0,
        202,203,3,16,8,0,203,204,5,26,0,0,204,205,5,36,0,0,205,207,1,0,0,
        0,206,195,1,0,0,0,206,200,1,0,0,0,207,21,1,0,0,0,208,209,5,2,0,0,
        209,210,5,35,0,0,210,211,3,16,8,0,211,212,5,26,0,0,212,213,5,36,
        0,0,213,222,1,0,0,0,214,215,5,2,0,0,215,216,5,35,0,0,216,217,3,30,
        15,0,217,218,3,16,8,0,218,219,5,26,0,0,219,220,5,36,0,0,220,222,
        1,0,0,0,221,208,1,0,0,0,221,214,1,0,0,0,222,23,1,0,0,0,223,224,5,
        10,0,0,224,225,5,29,0,0,225,226,3,48,24,0,226,227,5,30,0,0,227,228,
        5,11,0,0,228,229,5,35,0,0,229,230,3,30,15,0,230,231,5,12,0,0,231,
        232,5,26,0,0,232,233,5,36,0,0,233,234,6,12,-1,0,234,25,1,0,0,0,235,
        236,5,5,0,0,236,237,5,16,0,0,237,238,5,35,0,0,238,239,3,28,14,0,
        239,240,5,36,0,0,240,241,5,26,0,0,241,242,6,13,-1,0,242,27,1,0,0,
        0,243,244,6,14,-1,0,244,249,3,6,3,0,245,249,3,10,5,0,246,247,5,16,
        0,0,247,249,5,26,0,0,248,243,1,0,0,0,248,245,1,0,0,0,248,246,1,0,
        0,0,249,259,1,0,0,0,250,251,10,3,0,0,251,258,3,6,3,0,252,253,10,
        2,0,0,253,258,3,10,5,0,254,255,10,1,0,0,255,256,5,16,0,0,256,258,
        5,26,0,0,257,250,1,0,0,0,257,252,1,0,0,0,257,254,1,0,0,0,258,261,
        1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,29,1,0,0,0,261,259,1,
        0,0,0,262,263,6,15,-1,0,263,264,3,32,16,0,264,269,1,0,0,0,265,266,
        10,2,0,0,266,268,3,32,16,0,267,265,1,0,0,0,268,271,1,0,0,0,269,267,
        1,0,0,0,269,270,1,0,0,0,270,31,1,0,0,0,271,269,1,0,0,0,272,273,3,
        34,17,0,273,274,5,26,0,0,274,275,6,16,-1,0,275,296,1,0,0,0,276,277,
        3,36,18,0,277,278,5,26,0,0,278,279,6,16,-1,0,279,296,1,0,0,0,280,
        281,3,38,19,0,281,282,5,26,0,0,282,283,6,16,-1,0,283,296,1,0,0,0,
        284,285,3,52,26,0,285,286,5,26,0,0,286,287,6,16,-1,0,287,296,1,0,
        0,0,288,289,3,54,27,0,289,290,5,26,0,0,290,291,6,16,-1,0,291,296,
        1,0,0,0,292,293,5,17,0,0,293,294,5,26,0,0,294,296,6,16,-1,0,295,
        272,1,0,0,0,295,276,1,0,0,0,295,280,1,0,0,0,295,284,1,0,0,0,295,
        288,1,0,0,0,295,292,1,0,0,0,296,33,1,0,0,0,297,298,5,16,0,0,298,
        299,5,34,0,0,299,300,3,60,30,0,300,301,6,17,-1,0,301,35,1,0,0,0,
        302,303,5,16,0,0,303,304,5,29,0,0,304,305,3,60,30,0,305,306,5,30,
        0,0,306,307,6,18,-1,0,307,327,1,0,0,0,308,309,5,16,0,0,309,310,5,
        29,0,0,310,311,5,30,0,0,311,327,6,18,-1,0,312,313,5,16,0,0,313,314,
        5,38,0,0,314,315,5,16,0,0,315,316,5,29,0,0,316,317,5,30,0,0,317,
        327,6,18,-1,0,318,319,5,16,0,0,319,320,5,38,0,0,320,321,5,16,0,0,
        321,322,5,29,0,0,322,323,3,60,30,0,323,324,5,30,0,0,324,325,6,18,
        -1,0,325,327,1,0,0,0,326,302,1,0,0,0,326,308,1,0,0,0,326,312,1,0,
        0,0,326,318,1,0,0,0,327,37,1,0,0,0,328,329,3,44,22,0,329,330,3,46,
        23,0,330,331,3,40,20,0,331,332,5,3,0,0,332,333,6,19,-1,0,333,39,
        1,0,0,0,334,335,3,42,21,0,335,336,3,46,23,0,336,337,6,20,-1,0,337,
        340,1,0,0,0,338,340,1,0,0,0,339,334,1,0,0,0,339,338,1,0,0,0,340,
        41,1,0,0,0,341,342,5,2,0,0,342,343,6,21,-1,0,343,43,1,0,0,0,344,
        345,5,1,0,0,345,346,5,29,0,0,346,347,3,48,24,0,347,348,5,30,0,0,
        348,349,6,22,-1,0,349,45,1,0,0,0,350,351,5,35,0,0,351,352,3,30,15,
        0,352,353,5,36,0,0,353,47,1,0,0,0,354,355,3,60,30,0,355,356,3,50,
        25,0,356,357,3,60,30,0,357,358,6,24,-1,0,358,49,1,0,0,0,359,360,
        7,0,0,0,360,51,1,0,0,0,361,362,5,4,0,0,362,363,5,29,0,0,363,364,
        5,21,0,0,364,365,5,30,0,0,365,366,6,26,-1,0,366,53,1,0,0,0,367,368,
        3,56,28,0,368,369,3,46,23,0,369,370,6,27,-1,0,370,55,1,0,0,0,371,
        372,6,28,-1,0,372,373,5,10,0,0,373,374,5,29,0,0,374,375,3,48,24,
        0,375,376,5,30,0,0,376,377,5,11,0,0,377,378,6,28,-1,0,378,57,1,0,
        0,0,379,385,5,7,0,0,380,385,5,8,0,0,381,385,5,9,0,0,382,383,5,16,
        0,0,383,385,6,29,-1,0,384,379,1,0,0,0,384,380,1,0,0,0,384,381,1,
        0,0,0,384,382,1,0,0,0,385,59,1,0,0,0,386,387,6,30,-1,0,387,388,3,
        62,31,0,388,401,1,0,0,0,389,390,10,3,0,0,390,391,5,24,0,0,391,392,
        3,62,31,0,392,393,6,30,-1,0,393,400,1,0,0,0,394,395,10,2,0,0,395,
        396,5,25,0,0,396,397,3,62,31,0,397,398,6,30,-1,0,398,400,1,0,0,0,
        399,389,1,0,0,0,399,394,1,0,0,0,400,403,1,0,0,0,401,399,1,0,0,0,
        401,402,1,0,0,0,402,61,1,0,0,0,403,401,1,0,0,0,404,405,6,31,-1,0,
        405,406,3,64,32,0,406,419,1,0,0,0,407,408,10,3,0,0,408,409,5,28,
        0,0,409,410,3,64,32,0,410,411,6,31,-1,0,411,418,1,0,0,0,412,413,
        10,2,0,0,413,414,5,27,0,0,414,415,3,64,32,0,415,416,6,31,-1,0,416,
        418,1,0,0,0,417,407,1,0,0,0,417,412,1,0,0,0,418,421,1,0,0,0,419,
        417,1,0,0,0,419,420,1,0,0,0,420,63,1,0,0,0,421,419,1,0,0,0,422,438,
        3,66,33,0,423,424,5,25,0,0,424,425,5,18,0,0,425,438,6,32,-1,0,426,
        427,5,19,0,0,427,438,6,32,-1,0,428,429,5,20,0,0,429,438,6,32,-1,
        0,430,431,5,25,0,0,431,432,5,20,0,0,432,438,6,32,-1,0,433,434,5,
        18,0,0,434,438,6,32,-1,0,435,436,5,17,0,0,436,438,6,32,-1,0,437,
        422,1,0,0,0,437,423,1,0,0,0,437,426,1,0,0,0,437,428,1,0,0,0,437,
        430,1,0,0,0,437,433,1,0,0,0,437,435,1,0,0,0,438,65,1,0,0,0,439,440,
        5,16,0,0,440,441,6,33,-1,0,441,442,3,68,34,0,442,443,6,33,-1,0,443,
        446,1,0,0,0,444,446,3,70,35,0,445,439,1,0,0,0,445,444,1,0,0,0,446,
        67,1,0,0,0,447,448,5,25,0,0,448,449,5,25,0,0,449,452,6,34,-1,0,450,
        452,1,0,0,0,451,447,1,0,0,0,451,450,1,0,0,0,452,69,1,0,0,0,453,454,
        5,16,0,0,454,455,5,38,0,0,455,456,5,16,0,0,456,457,6,35,-1,0,457,
        71,1,0,0,0,27,80,86,88,98,112,134,144,153,167,193,206,221,248,257,
        259,269,295,326,339,384,399,401,417,419,437,445,451
    ]

class gramaticaprueba ( Parser ):

    grammarFileName = "gramaticaprueba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'IF'", "'ELSE'", "'END_IF'", "'PRINT'", 
                     "'CLASS'", "'VOID'", "'INT'", "'ULONG'", "'FLOAT'", 
                     "'WHILE'", "'DO'", "'RETURN'", "'<='", "'>='", "'!!'", 
                     "<INVALID>", "'ERROR'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'=='", "'FIN'", "'+'", "'-'", "','", 
                     "'/'", "'*'", "'('", "')'", "'<'", "'>'", "';'", "'='", 
                     "'{'", "'}'", "'--'", "'.'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "END_IF", "PRINT", "CLASS", 
                      "VOID", "INT", "ULONG", "FLOAT", "WHILE", "DO", "RETURN", 
                      "MENORIGUAL", "MAYORIGUAL", "DISTINTO", "ID", "ERROR", 
                      "NUM_INT", "NUM_ULONG", "NUM_FLOAT", "CADENA", "COMPIGUAL", 
                      "FIN", "PLUS", "MINUS", "COMMA", "DIVIDE", "MULTIPLY", 
                      "LEFT_PAREN", "RIGHT_PAREN", "LESS_THAN", "GREATER_THAN", 
                      "SEMICOLON", "EQUALS", "LEFT_BRACE", "RIGHT_BRACE", 
                      "DOUBLE_MINUS", "DOT", "WS" ]

    RULE_programa = 0
    RULE_cuerpo = 1
    RULE_declaracion = 2
    RULE_declaracion_var = 3
    RULE_lista_variable = 4
    RULE_declaracion_func = 5
    RULE_parametro = 6
    RULE_cuerpo_func = 7
    RULE_ejecucion_retorno = 8
    RULE_control_retorno = 9
    RULE_then_retorno = 10
    RULE_else_retorno = 11
    RULE_while_retorno = 12
    RULE_declaracion_clase = 13
    RULE_componentes_clase = 14
    RULE_cuerpo_ejecucion = 15
    RULE_ejecucion = 16
    RULE_asignacion = 17
    RULE_invocacion = 18
    RULE_seleccion = 19
    RULE_posible_else = 20
    RULE_else = 21
    RULE_if_condicion = 22
    RULE_bloque_control = 23
    RULE_condicion = 24
    RULE_comparador = 25
    RULE_print = 26
    RULE_while = 27
    RULE_while_condicion = 28
    RULE_tipo = 29
    RULE_expresion = 30
    RULE_termino = 31
    RULE_factor = 32
    RULE_referencia = 33
    RULE_posible_guion_doble = 34
    RULE_uso_clase = 35

    ruleNames =  [ "programa", "cuerpo", "declaracion", "declaracion_var", 
                   "lista_variable", "declaracion_func", "parametro", "cuerpo_func", 
                   "ejecucion_retorno", "control_retorno", "then_retorno", 
                   "else_retorno", "while_retorno", "declaracion_clase", 
                   "componentes_clase", "cuerpo_ejecucion", "ejecucion", 
                   "asignacion", "invocacion", "seleccion", "posible_else", 
                   "else", "if_condicion", "bloque_control", "condicion", 
                   "comparador", "print", "while", "while_condicion", "tipo", 
                   "expresion", "termino", "factor", "referencia", "posible_guion_doble", 
                   "uso_clase" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    END_IF=3
    PRINT=4
    CLASS=5
    VOID=6
    INT=7
    ULONG=8
    FLOAT=9
    WHILE=10
    DO=11
    RETURN=12
    MENORIGUAL=13
    MAYORIGUAL=14
    DISTINTO=15
    ID=16
    ERROR=17
    NUM_INT=18
    NUM_ULONG=19
    NUM_FLOAT=20
    CADENA=21
    COMPIGUAL=22
    FIN=23
    PLUS=24
    MINUS=25
    COMMA=26
    DIVIDE=27
    MULTIPLY=28
    LEFT_PAREN=29
    RIGHT_PAREN=30
    LESS_THAN=31
    GREATER_THAN=32
    SEMICOLON=33
    EQUALS=34
    LEFT_BRACE=35
    RIGHT_BRACE=36
    DOUBLE_MINUS=37
    DOT=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        self.archivo_tabla = open("tabla_de_simbolos.txt", "a")
        self.archivo_salida = open("salida.txt", "a")
        self.archivo_errores = open("errores.txt", "a")
        self.simbolos = tablasimbolos.TablaDeSimbolos(self.archivo_tabla)
        self.menos_menos = False
        self.listaVar = []
        self.text = ""
        self.polacaInversa = Polaca.ExpresionPolacaInversa()
        self.aux = 1
        self.elseaux = False
    def agregarEstructura(self, texto):
        self.archivo_salida.write(str(texto+"\n"))

    def yyerror(self, texto, linea):
        self.archivo_errores.write(str("ERROR DE SINTAXIS: " + texto + " En la linea " + str(linea) + "\n"))

    def getValor(self, texto):
        valor = ""
        for caracter in texto:
            if caracter.isdigit() or caracter in [".","E","e"]:
                valor += caracter
        return valor



    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(gramaticaprueba.LEFT_BRACE, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(gramaticaprueba.CuerpoContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(gramaticaprueba.RIGHT_BRACE, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_programa




    def programa(self):

        localctx = gramaticaprueba.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 73
            self.cuerpo(0)
            self.state = 74
            self.match(gramaticaprueba.RIGHT_BRACE)

            self.simbolos.imprimirTabla()
            self.archivo_tabla.close()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CuerpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(gramaticaprueba.DeclaracionContext,0)


        def ejecucion(self):
            return self.getTypedRuleContext(gramaticaprueba.EjecucionContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(gramaticaprueba.CuerpoContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_cuerpo



    def cuerpo(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaprueba.CuerpoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_cuerpo, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 78
                self.declaracion()
                pass

            elif la_ == 2:
                self.state = 79
                self.ejecucion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 86
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 82
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 83
                        self.declaracion()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 84
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 85
                        self.ejecucion()
                        pass

             
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion_var(self):
            return self.getTypedRuleContext(gramaticaprueba.Declaracion_varContext,0)


        def declaracion_func(self):
            return self.getTypedRuleContext(gramaticaprueba.Declaracion_funcContext,0)


        def declaracion_clase(self):
            return self.getTypedRuleContext(gramaticaprueba.Declaracion_claseContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_declaracion




    def declaracion(self):

        localctx = gramaticaprueba.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.declaracion_var()

                self.agregarEstructura("DECLARACION VAR detectado")

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.declaracion_func()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.declaracion_clase()

                self.agregarEstructura("DECLARACION CLASE detectado")

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


    class Declaracion_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext

        def tipo(self):
            return self.getTypedRuleContext(gramaticaprueba.TipoContext,0)


        def lista_variable(self):
            return self.getTypedRuleContext(gramaticaprueba.Lista_variableContext,0)


        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_declaracion_var




    def declaracion_var(self):

        localctx = gramaticaprueba.Declaracion_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            localctx._tipo = self.tipo()
            self.state = 101
            self.lista_variable()
            self.state = 102
            self.match(gramaticaprueba.COMMA)

            for key in self.listaVar:
                self.simbolos.addCaracteristica(key, "tipo", (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))
            self.listaVar = []

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def SEMICOLON(self):
            return self.getToken(gramaticaprueba.SEMICOLON, 0)

        def lista_variable(self):
            return self.getTypedRuleContext(gramaticaprueba.Lista_variableContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_lista_variable




    def lista_variable(self):

        localctx = gramaticaprueba.Lista_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lista_variable)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                localctx._ID = self.match(gramaticaprueba.ID)

                self.listaVar.append((None if localctx._ID is None else localctx._ID.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 108
                self.match(gramaticaprueba.SEMICOLON)
                self.state = 109
                self.lista_variable()

                self.listaVar.append((None if localctx._ID is None else localctx._ID.text))

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def VOID(self):
            return self.getToken(gramaticaprueba.VOID, 0)

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def parametro(self):
            return self.getTypedRuleContext(gramaticaprueba.ParametroContext,0)


        def LEFT_BRACE(self):
            return self.getToken(gramaticaprueba.LEFT_BRACE, 0)

        def cuerpo_func(self):
            return self.getTypedRuleContext(gramaticaprueba.Cuerpo_funcContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(gramaticaprueba.RIGHT_BRACE, 0)

        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def LEFT_PAREN(self):
            return self.getToken(gramaticaprueba.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(gramaticaprueba.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_declaracion_func




    def declaracion_func(self):

        localctx = gramaticaprueba.Declaracion_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracion_func)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(gramaticaprueba.VOID)
                self.state = 115
                localctx._ID = self.match(gramaticaprueba.ID)
                self.polacaInversa.addElemento(('FUNCION' + ' ' + (None if localctx._ID is None else localctx._ID.text)))
                self.state = 117
                self.parametro()
                self.state = 118
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 119
                self.cuerpo_func()
                self.state = 120
                self.match(gramaticaprueba.RIGHT_BRACE)
                self.state = 121
                self.match(gramaticaprueba.COMMA)

                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text), "tipo", "func")
                self.agregarEstructura("DECLARACION FUNCION detectado")

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(gramaticaprueba.VOID)
                self.state = 125
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 126
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 127
                self.match(gramaticaprueba.RIGHT_PAREN)
                self.state = 128
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 129
                self.cuerpo_func()
                self.state = 130
                self.match(gramaticaprueba.RIGHT_BRACE)
                self.state = 131
                self.match(gramaticaprueba.COMMA)

                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text), "tipo", "func")
                self.agregarEstructura("DECLARACION FUNCION detectado")

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._ID = None # Token

        def LEFT_PAREN(self):
            return self.getToken(gramaticaprueba.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(gramaticaprueba.RIGHT_PAREN, 0)

        def tipo(self):
            return self.getTypedRuleContext(gramaticaprueba.TipoContext,0)


        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_parametro




    def parametro(self):

        localctx = gramaticaprueba.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parametro)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 137
                self.match(gramaticaprueba.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 139
                localctx._tipo = self.tipo()
                self.state = 140
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 141
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text), "tipo", (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cuerpo_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cuerpo(self):
            return self.getTypedRuleContext(gramaticaprueba.CuerpoContext,0)


        def ejecucion_retorno(self):
            return self.getTypedRuleContext(gramaticaprueba.Ejecucion_retornoContext,0)


        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_cuerpo_func




    def cuerpo_func(self):

        localctx = gramaticaprueba.Cuerpo_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cuerpo_func)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.cuerpo(0)
                self.state = 147
                self.ejecucion_retorno()
                self.state = 148
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.ejecucion_retorno()
                self.state = 151
                self.match(gramaticaprueba.COMMA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ejecucion_retornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def control_retorno(self):
            return self.getTypedRuleContext(gramaticaprueba.Control_retornoContext,0)


        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def ejecucion_retorno(self):
            return self.getTypedRuleContext(gramaticaprueba.Ejecucion_retornoContext,0)


        def while_retorno(self):
            return self.getTypedRuleContext(gramaticaprueba.While_retornoContext,0)


        def RETURN(self):
            return self.getToken(gramaticaprueba.RETURN, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_ejecucion_retorno




    def ejecucion_retorno(self):

        localctx = gramaticaprueba.Ejecucion_retornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ejecucion_retorno)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.control_retorno()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.control_retorno()
                self.state = 157
                self.match(gramaticaprueba.COMMA)
                self.state = 158
                self.ejecucion_retorno()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.while_retorno()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.while_retorno()
                self.state = 162
                self.match(gramaticaprueba.COMMA)
                self.state = 163
                self.ejecucion_retorno()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.match(gramaticaprueba.RETURN)
                self.polacaInversa.addElemento("ret")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Control_retornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_condicion(self):
            return self.getTypedRuleContext(gramaticaprueba.If_condicionContext,0)


        def then_retorno(self):
            return self.getTypedRuleContext(gramaticaprueba.Then_retornoContext,0)


        def END_IF(self):
            return self.getToken(gramaticaprueba.END_IF, 0)

        def ELSE(self):
            return self.getToken(gramaticaprueba.ELSE, 0)

        def bloque_control(self):
            return self.getTypedRuleContext(gramaticaprueba.Bloque_controlContext,0)


        def else_retorno(self):
            return self.getTypedRuleContext(gramaticaprueba.Else_retornoContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_control_retorno




    def control_retorno(self):

        localctx = gramaticaprueba.Control_retornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_control_retorno)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.if_condicion()
                self.state = 170
                self.then_retorno()
                self.state = 171
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.if_condicion()
                self.state = 175
                self.then_retorno()
                self.state = 176
                self.match(gramaticaprueba.ELSE)
                self.state = 177
                self.bloque_control()
                self.state = 178
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.if_condicion()
                self.state = 182
                self.bloque_control()
                self.state = 183
                self.else_retorno()
                self.state = 184
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.if_condicion()
                self.state = 188
                self.then_retorno()
                self.state = 189
                self.else_retorno()
                self.state = 190
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Then_retornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(gramaticaprueba.LEFT_BRACE, 0)

        def ejecucion_retorno(self):
            return self.getTypedRuleContext(gramaticaprueba.Ejecucion_retornoContext,0)


        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def RIGHT_BRACE(self):
            return self.getToken(gramaticaprueba.RIGHT_BRACE, 0)

        def cuerpo_ejecucion(self):
            return self.getTypedRuleContext(gramaticaprueba.Cuerpo_ejecucionContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_then_retorno




    def then_retorno(self):

        localctx = gramaticaprueba.Then_retornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_then_retorno)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 196
                self.ejecucion_retorno()
                self.state = 197
                self.match(gramaticaprueba.COMMA)
                self.state = 198
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 201
                self.cuerpo_ejecucion(0)
                self.state = 202
                self.ejecucion_retorno()
                self.state = 203
                self.match(gramaticaprueba.COMMA)
                self.state = 204
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_retornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(gramaticaprueba.ELSE, 0)

        def LEFT_BRACE(self):
            return self.getToken(gramaticaprueba.LEFT_BRACE, 0)

        def ejecucion_retorno(self):
            return self.getTypedRuleContext(gramaticaprueba.Ejecucion_retornoContext,0)


        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def RIGHT_BRACE(self):
            return self.getToken(gramaticaprueba.RIGHT_BRACE, 0)

        def cuerpo_ejecucion(self):
            return self.getTypedRuleContext(gramaticaprueba.Cuerpo_ejecucionContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_else_retorno




    def else_retorno(self):

        localctx = gramaticaprueba.Else_retornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_else_retorno)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(gramaticaprueba.ELSE)
                self.state = 209
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 210
                self.ejecucion_retorno()
                self.state = 211
                self.match(gramaticaprueba.COMMA)
                self.state = 212
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.match(gramaticaprueba.ELSE)
                self.state = 215
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 216
                self.cuerpo_ejecucion(0)
                self.state = 217
                self.ejecucion_retorno()
                self.state = 218
                self.match(gramaticaprueba.COMMA)
                self.state = 219
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_retornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(gramaticaprueba.WHILE, 0)

        def LEFT_PAREN(self):
            return self.getToken(gramaticaprueba.LEFT_PAREN, 0)

        def condicion(self):
            return self.getTypedRuleContext(gramaticaprueba.CondicionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(gramaticaprueba.RIGHT_PAREN, 0)

        def DO(self):
            return self.getToken(gramaticaprueba.DO, 0)

        def LEFT_BRACE(self):
            return self.getToken(gramaticaprueba.LEFT_BRACE, 0)

        def cuerpo_ejecucion(self):
            return self.getTypedRuleContext(gramaticaprueba.Cuerpo_ejecucionContext,0)


        def RETURN(self):
            return self.getToken(gramaticaprueba.RETURN, 0)

        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def RIGHT_BRACE(self):
            return self.getToken(gramaticaprueba.RIGHT_BRACE, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_while_retorno




    def while_retorno(self):

        localctx = gramaticaprueba.While_retornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_while_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(gramaticaprueba.WHILE)
            self.state = 224
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 225
            self.condicion()
            self.state = 226
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 227
            self.match(gramaticaprueba.DO)
            self.state = 228
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 229
            self.cuerpo_ejecucion(0)
            self.state = 230
            self.match(gramaticaprueba.RETURN)
            self.state = 231
            self.match(gramaticaprueba.COMMA)
            self.state = 232
            self.match(gramaticaprueba.RIGHT_BRACE)

            self.agregarEstructura("WHILE detectado")
            {self.polacaInversa.addElemento("ret")}

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_claseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def CLASS(self):
            return self.getToken(gramaticaprueba.CLASS, 0)

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def LEFT_BRACE(self):
            return self.getToken(gramaticaprueba.LEFT_BRACE, 0)

        def componentes_clase(self):
            return self.getTypedRuleContext(gramaticaprueba.Componentes_claseContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(gramaticaprueba.RIGHT_BRACE, 0)

        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_declaracion_clase




    def declaracion_clase(self):

        localctx = gramaticaprueba.Declaracion_claseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_declaracion_clase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(gramaticaprueba.CLASS)
            self.state = 236
            localctx._ID = self.match(gramaticaprueba.ID)
            self.state = 237
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 238
            self.componentes_clase(0)
            self.state = 239
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.state = 240
            self.match(gramaticaprueba.COMMA)

            self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text), "tipo", "clase")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Componentes_claseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion_var(self):
            return self.getTypedRuleContext(gramaticaprueba.Declaracion_varContext,0)


        def declaracion_func(self):
            return self.getTypedRuleContext(gramaticaprueba.Declaracion_funcContext,0)


        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def componentes_clase(self):
            return self.getTypedRuleContext(gramaticaprueba.Componentes_claseContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_componentes_clase



    def componentes_clase(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaprueba.Componentes_claseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_componentes_clase, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 244
                self.declaracion_var()
                pass

            elif la_ == 2:
                self.state = 245
                self.declaracion_func()
                pass

            elif la_ == 3:
                self.state = 246
                self.match(gramaticaprueba.ID)
                self.state = 247
                self.match(gramaticaprueba.COMMA)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 257
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 250
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 251
                        self.declaracion_var()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 252
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 253
                        self.declaracion_func()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 254
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 255
                        self.match(gramaticaprueba.ID)
                        self.state = 256
                        self.match(gramaticaprueba.COMMA)
                        pass

             
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Cuerpo_ejecucionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ejecucion(self):
            return self.getTypedRuleContext(gramaticaprueba.EjecucionContext,0)


        def cuerpo_ejecucion(self):
            return self.getTypedRuleContext(gramaticaprueba.Cuerpo_ejecucionContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_cuerpo_ejecucion



    def cuerpo_ejecucion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaprueba.Cuerpo_ejecucionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_cuerpo_ejecucion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.ejecucion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaprueba.Cuerpo_ejecucionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo_ejecucion)
                    self.state = 265
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 266
                    self.ejecucion() 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EjecucionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ERROR = None # Token

        def asignacion(self):
            return self.getTypedRuleContext(gramaticaprueba.AsignacionContext,0)


        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def invocacion(self):
            return self.getTypedRuleContext(gramaticaprueba.InvocacionContext,0)


        def seleccion(self):
            return self.getTypedRuleContext(gramaticaprueba.SeleccionContext,0)


        def print_(self):
            return self.getTypedRuleContext(gramaticaprueba.PrintContext,0)


        def while_(self):
            return self.getTypedRuleContext(gramaticaprueba.WhileContext,0)


        def ERROR(self):
            return self.getToken(gramaticaprueba.ERROR, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_ejecucion




    def ejecucion(self):

        localctx = gramaticaprueba.EjecucionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ejecucion)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.asignacion()
                self.state = 273
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("ASIGNACION detectado")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.invocacion()
                self.state = 277
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("INVOCACION detectado")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.seleccion()
                self.state = 281
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.print_()
                self.state = 285
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("PRINT detectado")
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 288
                self.while_()
                self.state = 289
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("WHILE detectado")
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 292
                localctx._ERROR = self.match(gramaticaprueba.ERROR)
                self.state = 293
                self.match(gramaticaprueba.COMMA)
                self.yyerror(str("ERROR en sentencia ejecutable en linea: {}"),(0 if localctx._ERROR is None else localctx._ERROR.line))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def EQUALS(self):
            return self.getToken(gramaticaprueba.EQUALS, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaprueba.ExpresionContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_asignacion




    def asignacion(self):

        localctx = gramaticaprueba.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            localctx._ID = self.match(gramaticaprueba.ID)
            self.state = 298
            self.match(gramaticaprueba.EQUALS)
            self.state = 299
            self.expresion(0)

            self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))
            self.polacaInversa.addElemento((None if localctx._ID is None else localctx._ID.text))
            self.polacaInversa.addElemento("=")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvocacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self.clase = None # Token
            self.funcion = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaprueba.ID)
            else:
                return self.getToken(gramaticaprueba.ID, i)

        def LEFT_PAREN(self):
            return self.getToken(gramaticaprueba.LEFT_PAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaprueba.ExpresionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(gramaticaprueba.RIGHT_PAREN, 0)

        def DOT(self):
            return self.getToken(gramaticaprueba.DOT, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_invocacion




    def invocacion(self):

        localctx = gramaticaprueba.InvocacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_invocacion)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 303
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 304
                self.expresion(0)
                self.state = 305
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))
                aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + (None if localctx._ID is None else localctx._ID.text))
                self.polacaInversa.addElemento(aux)
                self.polacaInversa.addElemento("CALLFUNC")

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 309
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 310
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))
                aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + (None if localctx._ID is None else localctx._ID.text))
                self.polacaInversa.addElemento(aux)
                self.polacaInversa.addElemento("CALLFUNC")

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 313
                self.match(gramaticaprueba.DOT)
                self.state = 314
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 315
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 316
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.aumentarReferencia((None if localctx.clase is None else localctx.clase.text))
                self.simbolos.aumentarReferencia((None if localctx.funcion is None else localctx.funcion.text))
                aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + (None if localctx.funcion is None else localctx.funcion.text))
                self.polacaInversa.addElemento(aux)
                self.polacaInversa.addElemento("CALLFUNC")

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 318
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 319
                self.match(gramaticaprueba.DOT)
                self.state = 320
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 321
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 322
                self.expresion(0)
                self.state = 323
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.aumentarReferencia((None if localctx.clase is None else localctx.clase.text))
                self.simbolos.aumentarReferencia((None if localctx.funcion is None else localctx.funcion.text))
                aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + (None if localctx.funcion is None else localctx.funcion.text))
                self.polacaInversa.addElemento(aux)
                self.polacaInversa.addElemento("CALLFUNC")

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeleccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_condicion(self):
            return self.getTypedRuleContext(gramaticaprueba.If_condicionContext,0)


        def bloque_control(self):
            return self.getTypedRuleContext(gramaticaprueba.Bloque_controlContext,0)


        def posible_else(self):
            return self.getTypedRuleContext(gramaticaprueba.Posible_elseContext,0)


        def END_IF(self):
            return self.getToken(gramaticaprueba.END_IF, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_seleccion




    def seleccion(self):

        localctx = gramaticaprueba.SeleccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_seleccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.if_condicion()
            self.state = 329
            self.bloque_control()
            self.state = 330
            self.posible_else()
            self.state = 331
            self.match(gramaticaprueba.END_IF)

            if self.elseaux is False:
                number = self.polacaInversa.getLastPendingStep()
                self.polacaInversa.setElemento(number)
            else:
                self.elseaux = False

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Posible_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_(self):
            return self.getTypedRuleContext(gramaticaprueba.ElseContext,0)


        def bloque_control(self):
            return self.getTypedRuleContext(gramaticaprueba.Bloque_controlContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_posible_else




    def posible_else(self):

        localctx = gramaticaprueba.Posible_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_posible_else)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.else_()
                self.state = 335
                self.bloque_control()

                number = self.polacaInversa.getLastPendingStep()
                self.polacaInversa.setElemento(number)

                pass
            elif token in [3]:
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


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(gramaticaprueba.ELSE, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_else




    def else_(self):

        localctx = gramaticaprueba.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(gramaticaprueba.ELSE)

            self.elseaux = True
            number = self.polacaInversa.getLastPendingStep()
            self.polacaInversa.addPendingStep(self.polacaInversa.reference_counter)
            self.polacaInversa.addElemento(" ")
            self.polacaInversa.addElemento("BI")
            self.polacaInversa.setElemento(number)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_condicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(gramaticaprueba.IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(gramaticaprueba.LEFT_PAREN, 0)

        def condicion(self):
            return self.getTypedRuleContext(gramaticaprueba.CondicionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(gramaticaprueba.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_if_condicion




    def if_condicion(self):

        localctx = gramaticaprueba.If_condicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_if_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(gramaticaprueba.IF)
            self.state = 345
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 346
            self.condicion()
            self.state = 347
            self.match(gramaticaprueba.RIGHT_PAREN)

            self.polacaInversa.addPendingStep(self.polacaInversa.reference_counter)
            self.polacaInversa.addElemento(" ")
            self.polacaInversa.addElemento("BF")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bloque_controlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(gramaticaprueba.LEFT_BRACE, 0)

        def cuerpo_ejecucion(self):
            return self.getTypedRuleContext(gramaticaprueba.Cuerpo_ejecucionContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(gramaticaprueba.RIGHT_BRACE, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_bloque_control




    def bloque_control(self):

        localctx = gramaticaprueba.Bloque_controlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_bloque_control)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 351
            self.cuerpo_ejecucion(0)
            self.state = 352
            self.match(gramaticaprueba.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._comparador = None # ComparadorContext

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaprueba.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaprueba.ExpresionContext,i)


        def comparador(self):
            return self.getTypedRuleContext(gramaticaprueba.ComparadorContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_condicion




    def condicion(self):

        localctx = gramaticaprueba.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.expresion(0)
            self.state = 355
            localctx._comparador = self.comparador()
            self.state = 356
            self.expresion(0)

            self.polacaInversa.addElemento((None if localctx._comparador is None else self._input.getText(localctx._comparador.start,localctx._comparador.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS_THAN(self):
            return self.getToken(gramaticaprueba.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(gramaticaprueba.GREATER_THAN, 0)

        def MENORIGUAL(self):
            return self.getToken(gramaticaprueba.MENORIGUAL, 0)

        def MAYORIGUAL(self):
            return self.getToken(gramaticaprueba.MAYORIGUAL, 0)

        def DISTINTO(self):
            return self.getToken(gramaticaprueba.DISTINTO, 0)

        def COMPIGUAL(self):
            return self.getToken(gramaticaprueba.COMPIGUAL, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_comparador




    def comparador(self):

        localctx = gramaticaprueba.ComparadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_comparador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6446702592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
            self._CADENA = None # Token

        def PRINT(self):
            return self.getToken(gramaticaprueba.PRINT, 0)

        def LEFT_PAREN(self):
            return self.getToken(gramaticaprueba.LEFT_PAREN, 0)

        def CADENA(self):
            return self.getToken(gramaticaprueba.CADENA, 0)

        def RIGHT_PAREN(self):
            return self.getToken(gramaticaprueba.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_print




    def print_(self):

        localctx = gramaticaprueba.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(gramaticaprueba.PRINT)
            self.state = 362
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 363
            localctx._CADENA = self.match(gramaticaprueba.CADENA)
            self.state = 364
            self.match(gramaticaprueba.RIGHT_PAREN)

            self.polacaInversa.addElemento((None if localctx._CADENA is None else localctx._CADENA.text))
            self.polacaInversa.addElemento("PRINT")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def while_condicion(self):
            return self.getTypedRuleContext(gramaticaprueba.While_condicionContext,0)


        def bloque_control(self):
            return self.getTypedRuleContext(gramaticaprueba.Bloque_controlContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_while




    def while_(self):

        localctx = gramaticaprueba.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.while_condicion()
            self.state = 368
            self.bloque_control()

            number = self.polacaInversa.getLastPendingStep()
            self.polacaInversa.addElemento(self.aux)
            self.polacaInversa.addElemento("BI")
            self.polacaInversa.setElemento(number)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_condicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(gramaticaprueba.WHILE, 0)

        def LEFT_PAREN(self):
            return self.getToken(gramaticaprueba.LEFT_PAREN, 0)

        def condicion(self):
            return self.getTypedRuleContext(gramaticaprueba.CondicionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(gramaticaprueba.RIGHT_PAREN, 0)

        def DO(self):
            return self.getToken(gramaticaprueba.DO, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_while_condicion




    def while_condicion(self):

        localctx = gramaticaprueba.While_condicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_while_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.aux = self.polacaInversa.reference_counter
            self.state = 372
            self.match(gramaticaprueba.WHILE)
            self.state = 373
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 374
            self.condicion()
            self.state = 375
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 376
            self.match(gramaticaprueba.DO)

            self.polacaInversa.addPendingStep(self.polacaInversa.reference_counter)
            self.polacaInversa.addElemento(" ")
            self.polacaInversa.addElemento("BF")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def INT(self):
            return self.getToken(gramaticaprueba.INT, 0)

        def ULONG(self):
            return self.getToken(gramaticaprueba.ULONG, 0)

        def FLOAT(self):
            return self.getToken(gramaticaprueba.FLOAT, 0)

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_tipo




    def tipo(self):

        localctx = gramaticaprueba.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_tipo)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(gramaticaprueba.INT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.match(gramaticaprueba.ULONG)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.match(gramaticaprueba.FLOAT)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 382
                localctx._ID = self.match(gramaticaprueba.ID)

                self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))

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


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(gramaticaprueba.TerminoContext,0)


        def expresion(self):
            return self.getTypedRuleContext(gramaticaprueba.ExpresionContext,0)


        def PLUS(self):
            return self.getToken(gramaticaprueba.PLUS, 0)

        def MINUS(self):
            return self.getToken(gramaticaprueba.MINUS, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_expresion



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaprueba.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 399
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 389
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 390
                        self.match(gramaticaprueba.PLUS)
                        self.state = 391
                        self.termino(0)
                        self.polacaInversa.addElemento("+")
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 394
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 395
                        self.match(gramaticaprueba.MINUS)
                        self.state = 396
                        self.termino(0)
                        self.polacaInversa.addElemento("-")
                        pass

             
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(gramaticaprueba.FactorContext,0)


        def termino(self):
            return self.getTypedRuleContext(gramaticaprueba.TerminoContext,0)


        def MULTIPLY(self):
            return self.getToken(gramaticaprueba.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(gramaticaprueba.DIVIDE, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_termino



    def termino(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaprueba.TerminoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_termino, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 419
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 417
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 407
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 408
                        self.match(gramaticaprueba.MULTIPLY)
                        self.state = 409
                        self.factor()
                        self.polacaInversa.addElemento("*")
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 412
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 413
                        self.match(gramaticaprueba.DIVIDE)
                        self.state = 414
                        self.factor()
                        self.polacaInversa.addElemento("/")
                        pass

             
                self.state = 421
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NUM_INT = None # Token
            self._NUM_ULONG = None # Token
            self._NUM_FLOAT = None # Token
            self._ERROR = None # Token

        def referencia(self):
            return self.getTypedRuleContext(gramaticaprueba.ReferenciaContext,0)


        def MINUS(self):
            return self.getToken(gramaticaprueba.MINUS, 0)

        def NUM_INT(self):
            return self.getToken(gramaticaprueba.NUM_INT, 0)

        def NUM_ULONG(self):
            return self.getToken(gramaticaprueba.NUM_ULONG, 0)

        def NUM_FLOAT(self):
            return self.getToken(gramaticaprueba.NUM_FLOAT, 0)

        def ERROR(self):
            return self.getToken(gramaticaprueba.ERROR, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_factor




    def factor(self):

        localctx = gramaticaprueba.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_factor)
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.referencia()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.match(gramaticaprueba.MINUS)
                self.state = 424
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                key = (None if localctx._NUM_INT is None else localctx._NUM_INT.text)
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove(key)
                    else:
                        self.simbolos.reducirReferencia(key)
                # TODO chequear rango
                self.simbolos.addSimbolo("-" + (None if localctx._NUM_INT is None else localctx._NUM_INT.text))
                self.polacaInversa.addElemento((None if localctx._NUM_INT is None else localctx._NUM_INT.text))

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
                localctx._NUM_ULONG = self.match(gramaticaprueba.NUM_ULONG)

                self.simbolos.addCaracteristica((None if localctx._NUM_ULONG is None else localctx._NUM_ULONG.text), "tipo", "ULONG")
                self.polacaInversa.addElemento((None if localctx._NUM_ULONG is None else localctx._NUM_ULONG.text))

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 428
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                self.simbolos.addCaracteristica((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text), "tipo", "FLOAT")
                self.polacaInversa.addElemento((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 430
                self.match(gramaticaprueba.MINUS)
                self.state = 431
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                key = (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text)
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove(key)
                    else:
                        self.simbolos.reducirReferencia(key)
                self.simbolos.addSimbolo("-" + (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))
                self.polacaInversa.addElemento((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 433
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                if (None if localctx._NUM_INT is None else localctx._NUM_INT.text) == "32768_i":
                    self.yyerror("INT fuera de rango",(0 if localctx._NUM_INT is None else localctx._NUM_INT.line))
                else:
                    self.simbolos.addCaracteristica((None if localctx._NUM_INT is None else localctx._NUM_INT.text), "tipo", "INT")
                    texto = (None if localctx._NUM_INT is None else localctx._NUM_INT.text)
                    self.simbolos.addCaracteristica(texto, "valor", self.getValor(texto))
                    self.polacaInversa.addElemento((None if localctx._NUM_INT is None else localctx._NUM_INT.text))

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 435
                localctx._ERROR = self.match(gramaticaprueba.ERROR)
                self.yyerror("se espera una constante o id",(0 if localctx._ERROR is None else localctx._ERROR.line))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def posible_guion_doble(self):
            return self.getTypedRuleContext(gramaticaprueba.Posible_guion_dobleContext,0)


        def uso_clase(self):
            return self.getTypedRuleContext(gramaticaprueba.Uso_claseContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_referencia




    def referencia(self):

        localctx = gramaticaprueba.ReferenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_referencia)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                localctx._ID = self.match(gramaticaprueba.ID)
                self.polacaInversa.addElemento((None if localctx._ID is None else localctx._ID.text))
                self.state = 441
                self.posible_guion_doble()

                self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))
                if (self.menos_menos is True):
                    self.polacaInversa.addElemento((None if localctx._ID is None else localctx._ID.text))
                    self.polacaInversa.addElemento('=')
                    self.menos_menos = False

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.uso_clase()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Posible_guion_dobleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaprueba.MINUS)
            else:
                return self.getToken(gramaticaprueba.MINUS, i)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_posible_guion_doble




    def posible_guion_doble(self):

        localctx = gramaticaprueba.Posible_guion_dobleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_posible_guion_doble)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(gramaticaprueba.MINUS)
                self.state = 448
                self.match(gramaticaprueba.MINUS)

                self.menos_menos = True
                self.polacaInversa.addElemento('1_i')
                self.polacaInversa.addElemento("-")


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


    class Uso_claseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.clase = None # Token
            self.atributo = None # Token

        def DOT(self):
            return self.getToken(gramaticaprueba.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaprueba.ID)
            else:
                return self.getToken(gramaticaprueba.ID, i)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_uso_clase




    def uso_clase(self):

        localctx = gramaticaprueba.Uso_claseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_uso_clase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            localctx.clase = self.match(gramaticaprueba.ID)
            self.state = 454
            self.match(gramaticaprueba.DOT)
            self.state = 455
            localctx.atributo = self.match(gramaticaprueba.ID)

            self.simbolos.aumentarReferencia((None if localctx.clase is None else localctx.clase.text))
            self.simbolos.aumentarReferencia((None if localctx.atributo is None else localctx.atributo.text))
            clase = (None if localctx.clase is None else localctx.clase.text) + "." + (None if localctx.atributo is None else localctx.atributo.text)
            self.polacaInversa.addElemento(str(clase))

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
        self._predicates[1] = self.cuerpo_sempred
        self._predicates[14] = self.componentes_clase_sempred
        self._predicates[15] = self.cuerpo_ejecucion_sempred
        self._predicates[30] = self.expresion_sempred
        self._predicates[31] = self.termino_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def cuerpo_sempred(self, localctx:CuerpoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def componentes_clase_sempred(self, localctx:Componentes_claseContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def cuerpo_ejecucion_sempred(self, localctx:Cuerpo_ejecucionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def termino_sempred(self, localctx:TerminoContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




