# Generated from ./AnalizadorSintactico/gramaticaprueba.g4 by ANTLR 4.13.1
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
        4,1,39,531,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,91,8,1,1,1,1,1,1,1,
        1,1,5,1,97,8,1,10,1,12,1,100,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,111,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,125,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,149,8,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,160,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,174,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,
        10,196,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,3,11,209,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,3,12,224,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,253,8,16,1,16,1,16,1,
        16,1,16,1,16,1,16,5,16,261,8,16,10,16,12,16,264,9,16,1,17,1,17,1,
        17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,5,
        20,281,8,20,10,20,12,20,284,9,20,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,304,
        8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,
        317,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,3,23,383,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,
        1,25,1,25,3,25,396,8,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,3,34,442,8,34,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        5,35,457,8,35,10,35,12,35,460,9,35,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,5,36,475,8,36,10,36,12,36,478,
        9,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,37,1,37,1,37,3,37,495,8,37,1,38,1,38,1,38,1,38,1,38,1,38,3,38,
        503,8,38,1,39,1,39,1,39,1,39,3,39,509,8,39,1,40,1,40,1,40,1,40,1,
        40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,3,40,529,8,40,1,40,0,5,2,32,40,70,72,41,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,0,1,3,0,13,15,22,22,31,32,543,0,82,
        1,0,0,0,2,90,1,0,0,0,4,110,1,0,0,0,6,112,1,0,0,0,8,124,1,0,0,0,10,
        126,1,0,0,0,12,135,1,0,0,0,14,148,1,0,0,0,16,159,1,0,0,0,18,173,
        1,0,0,0,20,195,1,0,0,0,22,208,1,0,0,0,24,223,1,0,0,0,26,225,1,0,
        0,0,28,237,1,0,0,0,30,244,1,0,0,0,32,252,1,0,0,0,34,265,1,0,0,0,
        36,268,1,0,0,0,38,271,1,0,0,0,40,275,1,0,0,0,42,303,1,0,0,0,44,316,
        1,0,0,0,46,382,1,0,0,0,48,384,1,0,0,0,50,395,1,0,0,0,52,397,1,0,
        0,0,54,400,1,0,0,0,56,406,1,0,0,0,58,410,1,0,0,0,60,415,1,0,0,0,
        62,417,1,0,0,0,64,423,1,0,0,0,66,427,1,0,0,0,68,441,1,0,0,0,70,443,
        1,0,0,0,72,461,1,0,0,0,74,494,1,0,0,0,76,502,1,0,0,0,78,508,1,0,
        0,0,80,528,1,0,0,0,82,83,5,35,0,0,83,84,3,2,1,0,84,85,5,36,0,0,85,
        86,6,0,-1,0,86,1,1,0,0,0,87,88,6,1,-1,0,88,91,3,4,2,0,89,91,3,42,
        21,0,90,87,1,0,0,0,90,89,1,0,0,0,91,98,1,0,0,0,92,93,10,4,0,0,93,
        97,3,4,2,0,94,95,10,3,0,0,95,97,3,42,21,0,96,92,1,0,0,0,96,94,1,
        0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,3,1,0,0,0,100,
        98,1,0,0,0,101,102,3,6,3,0,102,103,6,2,-1,0,103,111,1,0,0,0,104,
        105,3,10,5,0,105,106,6,2,-1,0,106,111,1,0,0,0,107,108,3,28,14,0,
        108,109,6,2,-1,0,109,111,1,0,0,0,110,101,1,0,0,0,110,104,1,0,0,0,
        110,107,1,0,0,0,111,5,1,0,0,0,112,113,3,68,34,0,113,114,3,8,4,0,
        114,115,5,26,0,0,115,116,6,3,-1,0,116,7,1,0,0,0,117,118,5,16,0,0,
        118,125,6,4,-1,0,119,120,5,16,0,0,120,121,5,33,0,0,121,122,3,8,4,
        0,122,123,6,4,-1,0,123,125,1,0,0,0,124,117,1,0,0,0,124,119,1,0,0,
        0,125,9,1,0,0,0,126,127,3,12,6,0,127,128,6,5,-1,0,128,129,3,14,7,
        0,129,130,5,35,0,0,130,131,3,16,8,0,131,132,5,36,0,0,132,133,5,26,
        0,0,133,134,6,5,-1,0,134,11,1,0,0,0,135,136,5,6,0,0,136,137,5,16,
        0,0,137,138,6,6,-1,0,138,13,1,0,0,0,139,140,5,29,0,0,140,141,5,30,
        0,0,141,149,6,7,-1,0,142,143,5,29,0,0,143,144,3,68,34,0,144,145,
        5,16,0,0,145,146,5,30,0,0,146,147,6,7,-1,0,147,149,1,0,0,0,148,139,
        1,0,0,0,148,142,1,0,0,0,149,15,1,0,0,0,150,151,6,8,-1,0,151,152,
        3,2,1,0,152,153,3,18,9,0,153,154,5,26,0,0,154,160,1,0,0,0,155,156,
        6,8,-1,0,156,157,3,18,9,0,157,158,5,26,0,0,158,160,1,0,0,0,159,150,
        1,0,0,0,159,155,1,0,0,0,160,17,1,0,0,0,161,174,3,20,10,0,162,163,
        3,20,10,0,163,164,5,26,0,0,164,165,3,18,9,0,165,174,1,0,0,0,166,
        174,3,26,13,0,167,168,3,26,13,0,168,169,5,26,0,0,169,170,3,18,9,
        0,170,174,1,0,0,0,171,172,5,12,0,0,172,174,6,9,-1,0,173,161,1,0,
        0,0,173,162,1,0,0,0,173,166,1,0,0,0,173,167,1,0,0,0,173,171,1,0,
        0,0,174,19,1,0,0,0,175,176,3,54,27,0,176,177,3,22,11,0,177,178,5,
        3,0,0,178,196,1,0,0,0,179,180,3,54,27,0,180,181,3,22,11,0,181,182,
        5,2,0,0,182,183,3,56,28,0,183,184,5,3,0,0,184,196,1,0,0,0,185,186,
        3,54,27,0,186,187,3,56,28,0,187,188,3,24,12,0,188,189,5,3,0,0,189,
        196,1,0,0,0,190,191,3,54,27,0,191,192,3,22,11,0,192,193,3,24,12,
        0,193,194,5,3,0,0,194,196,1,0,0,0,195,175,1,0,0,0,195,179,1,0,0,
        0,195,185,1,0,0,0,195,190,1,0,0,0,196,21,1,0,0,0,197,198,5,35,0,
        0,198,199,3,18,9,0,199,200,5,26,0,0,200,201,5,36,0,0,201,209,1,0,
        0,0,202,203,5,35,0,0,203,204,3,40,20,0,204,205,3,18,9,0,205,206,
        5,26,0,0,206,207,5,36,0,0,207,209,1,0,0,0,208,197,1,0,0,0,208,202,
        1,0,0,0,209,23,1,0,0,0,210,211,5,2,0,0,211,212,5,35,0,0,212,213,
        3,18,9,0,213,214,5,26,0,0,214,215,5,36,0,0,215,224,1,0,0,0,216,217,
        5,2,0,0,217,218,5,35,0,0,218,219,3,40,20,0,219,220,3,18,9,0,220,
        221,5,26,0,0,221,222,5,36,0,0,222,224,1,0,0,0,223,210,1,0,0,0,223,
        216,1,0,0,0,224,25,1,0,0,0,225,226,5,10,0,0,226,227,5,29,0,0,227,
        228,3,58,29,0,228,229,5,30,0,0,229,230,5,11,0,0,230,231,5,35,0,0,
        231,232,3,40,20,0,232,233,5,12,0,0,233,234,5,26,0,0,234,235,5,36,
        0,0,235,236,6,13,-1,0,236,27,1,0,0,0,237,238,3,30,15,0,238,239,5,
        35,0,0,239,240,3,32,16,0,240,241,5,36,0,0,241,242,5,26,0,0,242,243,
        6,14,-1,0,243,29,1,0,0,0,244,245,5,5,0,0,245,246,5,16,0,0,246,247,
        6,15,-1,0,247,31,1,0,0,0,248,249,6,16,-1,0,249,253,3,34,17,0,250,
        253,3,36,18,0,251,253,3,38,19,0,252,248,1,0,0,0,252,250,1,0,0,0,
        252,251,1,0,0,0,253,262,1,0,0,0,254,255,10,3,0,0,255,261,3,34,17,
        0,256,257,10,2,0,0,257,261,3,36,18,0,258,259,10,1,0,0,259,261,3,
        38,19,0,260,254,1,0,0,0,260,256,1,0,0,0,260,258,1,0,0,0,261,264,
        1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,33,1,0,0,0,264,262,1,
        0,0,0,265,266,3,6,3,0,266,267,6,17,-1,0,267,35,1,0,0,0,268,269,3,
        10,5,0,269,270,6,18,-1,0,270,37,1,0,0,0,271,272,5,16,0,0,272,273,
        5,26,0,0,273,274,6,19,-1,0,274,39,1,0,0,0,275,276,6,20,-1,0,276,
        277,3,42,21,0,277,282,1,0,0,0,278,279,10,2,0,0,279,281,3,42,21,0,
        280,278,1,0,0,0,281,284,1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,
        283,41,1,0,0,0,284,282,1,0,0,0,285,286,3,44,22,0,286,287,5,26,0,
        0,287,304,1,0,0,0,288,289,3,46,23,0,289,290,5,26,0,0,290,304,1,0,
        0,0,291,292,3,48,24,0,292,293,5,26,0,0,293,304,1,0,0,0,294,295,3,
        62,31,0,295,296,5,26,0,0,296,304,1,0,0,0,297,298,3,64,32,0,298,299,
        5,26,0,0,299,304,1,0,0,0,300,301,5,17,0,0,301,302,5,26,0,0,302,304,
        6,21,-1,0,303,285,1,0,0,0,303,288,1,0,0,0,303,291,1,0,0,0,303,294,
        1,0,0,0,303,297,1,0,0,0,303,300,1,0,0,0,304,43,1,0,0,0,305,306,5,
        16,0,0,306,307,5,34,0,0,307,308,3,70,35,0,308,309,6,22,-1,0,309,
        317,1,0,0,0,310,311,3,80,40,0,311,312,5,34,0,0,312,313,6,22,-1,0,
        313,314,3,70,35,0,314,315,6,22,-1,0,315,317,1,0,0,0,316,305,1,0,
        0,0,316,310,1,0,0,0,317,45,1,0,0,0,318,319,5,16,0,0,319,320,5,29,
        0,0,320,321,3,70,35,0,321,322,5,30,0,0,322,323,6,23,-1,0,323,383,
        1,0,0,0,324,325,5,16,0,0,325,326,5,29,0,0,326,327,5,30,0,0,327,383,
        6,23,-1,0,328,329,5,16,0,0,329,330,5,38,0,0,330,331,5,16,0,0,331,
        332,5,29,0,0,332,333,5,30,0,0,333,383,6,23,-1,0,334,335,5,16,0,0,
        335,336,5,38,0,0,336,337,5,16,0,0,337,338,5,29,0,0,338,339,3,70,
        35,0,339,340,5,30,0,0,340,341,6,23,-1,0,341,383,1,0,0,0,342,343,
        5,16,0,0,343,344,5,38,0,0,344,345,5,16,0,0,345,346,5,38,0,0,346,
        347,5,16,0,0,347,348,5,29,0,0,348,349,5,30,0,0,349,383,6,23,-1,0,
        350,351,5,16,0,0,351,352,5,38,0,0,352,353,5,16,0,0,353,354,5,38,
        0,0,354,355,5,16,0,0,355,356,5,29,0,0,356,357,3,70,35,0,357,358,
        5,30,0,0,358,359,6,23,-1,0,359,383,1,0,0,0,360,361,5,16,0,0,361,
        362,5,38,0,0,362,363,5,16,0,0,363,364,5,38,0,0,364,365,5,16,0,0,
        365,366,5,38,0,0,366,367,5,16,0,0,367,368,5,29,0,0,368,369,5,30,
        0,0,369,383,6,23,-1,0,370,371,5,16,0,0,371,372,5,38,0,0,372,373,
        5,16,0,0,373,374,5,38,0,0,374,375,5,16,0,0,375,376,5,38,0,0,376,
        377,5,16,0,0,377,378,5,29,0,0,378,379,3,70,35,0,379,380,5,30,0,0,
        380,381,6,23,-1,0,381,383,1,0,0,0,382,318,1,0,0,0,382,324,1,0,0,
        0,382,328,1,0,0,0,382,334,1,0,0,0,382,342,1,0,0,0,382,350,1,0,0,
        0,382,360,1,0,0,0,382,370,1,0,0,0,383,47,1,0,0,0,384,385,3,54,27,
        0,385,386,3,56,28,0,386,387,3,50,25,0,387,388,5,3,0,0,388,389,6,
        24,-1,0,389,49,1,0,0,0,390,391,3,52,26,0,391,392,3,56,28,0,392,393,
        6,25,-1,0,393,396,1,0,0,0,394,396,1,0,0,0,395,390,1,0,0,0,395,394,
        1,0,0,0,396,51,1,0,0,0,397,398,5,2,0,0,398,399,6,26,-1,0,399,53,
        1,0,0,0,400,401,5,1,0,0,401,402,5,29,0,0,402,403,3,58,29,0,403,404,
        5,30,0,0,404,405,6,27,-1,0,405,55,1,0,0,0,406,407,5,35,0,0,407,408,
        3,40,20,0,408,409,5,36,0,0,409,57,1,0,0,0,410,411,3,70,35,0,411,
        412,3,60,30,0,412,413,3,70,35,0,413,414,6,29,-1,0,414,59,1,0,0,0,
        415,416,7,0,0,0,416,61,1,0,0,0,417,418,5,4,0,0,418,419,5,29,0,0,
        419,420,5,21,0,0,420,421,5,30,0,0,421,422,6,31,-1,0,422,63,1,0,0,
        0,423,424,3,66,33,0,424,425,3,56,28,0,425,426,6,32,-1,0,426,65,1,
        0,0,0,427,428,6,33,-1,0,428,429,5,10,0,0,429,430,6,33,-1,0,430,431,
        5,29,0,0,431,432,3,58,29,0,432,433,5,30,0,0,433,434,5,11,0,0,434,
        435,6,33,-1,0,435,67,1,0,0,0,436,442,5,7,0,0,437,442,5,8,0,0,438,
        442,5,9,0,0,439,440,5,16,0,0,440,442,6,34,-1,0,441,436,1,0,0,0,441,
        437,1,0,0,0,441,438,1,0,0,0,441,439,1,0,0,0,442,69,1,0,0,0,443,444,
        6,35,-1,0,444,445,3,72,36,0,445,458,1,0,0,0,446,447,10,3,0,0,447,
        448,5,24,0,0,448,449,3,72,36,0,449,450,6,35,-1,0,450,457,1,0,0,0,
        451,452,10,2,0,0,452,453,5,25,0,0,453,454,3,72,36,0,454,455,6,35,
        -1,0,455,457,1,0,0,0,456,446,1,0,0,0,456,451,1,0,0,0,457,460,1,0,
        0,0,458,456,1,0,0,0,458,459,1,0,0,0,459,71,1,0,0,0,460,458,1,0,0,
        0,461,462,6,36,-1,0,462,463,3,74,37,0,463,476,1,0,0,0,464,465,10,
        3,0,0,465,466,5,28,0,0,466,467,3,74,37,0,467,468,6,36,-1,0,468,475,
        1,0,0,0,469,470,10,2,0,0,470,471,5,27,0,0,471,472,3,74,37,0,472,
        473,6,36,-1,0,473,475,1,0,0,0,474,464,1,0,0,0,474,469,1,0,0,0,475,
        478,1,0,0,0,476,474,1,0,0,0,476,477,1,0,0,0,477,73,1,0,0,0,478,476,
        1,0,0,0,479,495,3,76,38,0,480,481,5,25,0,0,481,482,5,18,0,0,482,
        495,6,37,-1,0,483,484,5,19,0,0,484,495,6,37,-1,0,485,486,5,20,0,
        0,486,495,6,37,-1,0,487,488,5,25,0,0,488,489,5,20,0,0,489,495,6,
        37,-1,0,490,491,5,18,0,0,491,495,6,37,-1,0,492,493,5,17,0,0,493,
        495,6,37,-1,0,494,479,1,0,0,0,494,480,1,0,0,0,494,483,1,0,0,0,494,
        485,1,0,0,0,494,487,1,0,0,0,494,490,1,0,0,0,494,492,1,0,0,0,495,
        75,1,0,0,0,496,497,5,16,0,0,497,498,6,38,-1,0,498,499,3,78,39,0,
        499,500,6,38,-1,0,500,503,1,0,0,0,501,503,3,80,40,0,502,496,1,0,
        0,0,502,501,1,0,0,0,503,77,1,0,0,0,504,505,5,25,0,0,505,506,5,25,
        0,0,506,509,6,39,-1,0,507,509,1,0,0,0,508,504,1,0,0,0,508,507,1,
        0,0,0,509,79,1,0,0,0,510,511,5,16,0,0,511,512,5,38,0,0,512,513,5,
        16,0,0,513,529,6,40,-1,0,514,515,5,16,0,0,515,516,5,38,0,0,516,517,
        5,16,0,0,517,518,5,38,0,0,518,519,5,16,0,0,519,529,6,40,-1,0,520,
        521,5,16,0,0,521,522,5,38,0,0,522,523,5,16,0,0,523,524,5,38,0,0,
        524,525,5,16,0,0,525,526,5,38,0,0,526,527,5,16,0,0,527,529,6,40,
        -1,0,528,510,1,0,0,0,528,514,1,0,0,0,528,520,1,0,0,0,529,81,1,0,
        0,0,28,90,96,98,110,124,148,159,173,195,208,223,252,260,262,282,
        303,316,382,395,441,456,458,474,476,494,502,508,528
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
    RULE_encabezado_funcion = 6
    RULE_parametro = 7
    RULE_cuerpo_func = 8
    RULE_ejecucion_retorno = 9
    RULE_control_retorno = 10
    RULE_then_retorno = 11
    RULE_else_retorno = 12
    RULE_while_retorno = 13
    RULE_declaracion_clase = 14
    RULE_encabezado_clase = 15
    RULE_componentes_clase = 16
    RULE_componente_var = 17
    RULE_componente_func = 18
    RULE_componente_herencia = 19
    RULE_cuerpo_ejecucion = 20
    RULE_ejecucion = 21
    RULE_asignacion = 22
    RULE_invocacion = 23
    RULE_seleccion = 24
    RULE_posible_else = 25
    RULE_else = 26
    RULE_if_condicion = 27
    RULE_bloque_control = 28
    RULE_condicion = 29
    RULE_comparador = 30
    RULE_print = 31
    RULE_while = 32
    RULE_while_condicion = 33
    RULE_tipo = 34
    RULE_expresion = 35
    RULE_termino = 36
    RULE_factor = 37
    RULE_referencia = 38
    RULE_posible_guion_doble = 39
    RULE_uso_clase = 40

    ruleNames =  [ "programa", "cuerpo", "declaracion", "declaracion_var", 
                   "lista_variable", "declaracion_func", "encabezado_funcion", 
                   "parametro", "cuerpo_func", "ejecucion_retorno", "control_retorno", 
                   "then_retorno", "else_retorno", "while_retorno", "declaracion_clase", 
                   "encabezado_clase", "componentes_clase", "componente_var", 
                   "componente_func", "componente_herencia", "cuerpo_ejecucion", 
                   "ejecucion", "asignacion", "invocacion", "seleccion", 
                   "posible_else", "else", "if_condicion", "bloque_control", 
                   "condicion", "comparador", "print", "while", "while_condicion", 
                   "tipo", "expresion", "termino", "factor", "referencia", 
                   "posible_guion_doble", "uso_clase" ]

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



        self.archivo_tabla = open("tabla_de_simbolos.txt", "w")
        self.archivo_salida = open("salida.txt", "a")
        self.archivo_errores = open("errores.txt", "a")
        self.simbolos = tablasimbolos.TablaDeSimbolos(self.archivo_tabla)
        self.menos_menos = False
        self.listaVar = []
        self.text = ""
        self.polacaInversa = Polaca.ExpresionPolacaInversa()
        self.aux = 1
        self.elseaux = False
        self.auxIDFunc = ""
        self.auxIDClass = ""
        self.ambitoActual = ":main"
        self.declaracionesVariables = {}
        self.clasesUsadas = {}
        self.clasesDeclaradas = []
        self.inClase = False
        self.inFuncion = False
        self.segundaFuncion = False
        self.auxBorrado = -1


    def yyerror(self, texto, linea):
        if linea != 0:
            self.archivo_errores.write(str("ERROR " + texto + " En la linea " + str(linea) + "\n"))
        else:
            self.archivo_errores.write(str("ERROR " + texto) +  "\n")

    def getValor(self, texto):
        valor = ""
        for caracter in texto:
            if caracter.isdigit() or caracter in [".", "E", "e", "-"]:
                valor += caracter
        return valor

    def reducirAmbito(self):
        self.ambitoActual = self.ambitoActual[:self.ambitoActual.rfind(":")]

    def verificarId(self, identificador):  # identificador viene con el ambito
        ambito_id = identificador[identificador.find(":"):]
        id_sin_ambito = identificador[:identificador.find(":")]
        while ambito_id != "":
            if self.simbolos.isKey(id_sin_ambito+ambito_id):
                return id_sin_ambito+ambito_id
            else:
                ambito_id = ambito_id[:ambito_id.rfind(":")]
        return ""

    def getAmbitoId(self, identificador):
        return identificador[str(identificador).find(":"):]

    def getIdSinAmbito(self, identificador):
        return identificador[:str(identificador).find(":")]



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
            self.state = 82
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 83
            self.cuerpo(0)
            self.state = 84
            self.match(gramaticaprueba.RIGHT_BRACE)

            for key in self.declaracionesVariables.keys():
                self.yyerror("SEMANTICO: variable " + key + " no fue asignada en el ambito donde se declaro", self.declaracionesVariables[key])
            for clase in self.clasesUsadas.keys():
                if clase not in self.clasesDeclaradas:
                    self.yyerror("SEMANTICO: clase " + clase + " fue usada sin declarar", 0)
                else:
                    referencias = self.clasesUsadas[clase]

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
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 88
                self.declaracion()
                pass

            elif la_ == 2:
                self.state = 89
                self.ejecucion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 96
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 92
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 93
                        self.declaracion()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 94
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 95
                        self.ejecucion()
                        pass

             
                self.state = 100
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
            self._declaracion_var = None # Declaracion_varContext

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
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                localctx._declaracion_var = self.declaracion_var()

                for key in self.listaVar:
                    if localctx._declaracion_var.t in ["INT","FLOAT","ULONG"]:
                        self.declaracionesVariables[key+self.ambitoActual] = localctx._declaracion_var.line
                self.listaVar = []

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.declaracion_func()

                            
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.declaracion_clase()


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
            self.line = None
            self.t = None
            self._tipo = None # TipoContext
            self._lista_variable = None # Lista_variableContext

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
            self.state = 112
            localctx._tipo = self.tipo()
            self.state = 113
            localctx._lista_variable = self.lista_variable()
            self.state = 114
            self.match(gramaticaprueba.COMMA)

            for key in self.listaVar:
                self.simbolos.addCaracteristica(key + self.ambitoActual, "tipo", (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))
                self.simbolos.addCaracteristica(key+self.ambitoActual, "uso", "variable")
                localctx.line = localctx._lista_variable.line
                localctx.t = (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop))

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
            self.line = None
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
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                localctx._ID = self.match(gramaticaprueba.ID)

                self.listaVar.append((None if localctx._ID is None else localctx._ID.text))
                localctx.line = (0 if localctx._ID is None else localctx._ID.line)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 120
                self.match(gramaticaprueba.SEMICOLON)
                self.state = 121
                self.lista_variable()

                self.listaVar.append((None if localctx._ID is None else localctx._ID.text))
                localctx.line = (0 if localctx._ID is None else localctx._ID.line)

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
            self._encabezado_funcion = None # Encabezado_funcionContext

        def encabezado_funcion(self):
            return self.getTypedRuleContext(gramaticaprueba.Encabezado_funcionContext,0)


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

        def getRuleIndex(self):
            return gramaticaprueba.RULE_declaracion_func




    def declaracion_func(self):

        localctx = gramaticaprueba.Declaracion_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracion_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            localctx._encabezado_funcion = self.encabezado_funcion()

            if self.inFuncion and self.inClass:
                self.segundaFuncion = True
            if (not self.inClass) or (not self.inFuncion):
                self.polacaInversa.addElemento(('FUNCION' + ' ' + localctx._encabezado_funcion.funcion))

            self.state = 128
            self.parametro()
            self.state = 129
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 130
            self.cuerpo_func()
            self.state = 131
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.state = 132
            self.match(gramaticaprueba.COMMA)

            self.reducirAmbito()
            if self.segundaFuncion:
                while self.polacaInversa.reference_counter > self.auxBorrado:
                    self.polacaInversa.removeLast()
            self.inFuncion = False

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Encabezado_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.funcion = None
            self._ID = None # Token

        def VOID(self):
            return self.getToken(gramaticaprueba.VOID, 0)

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_encabezado_funcion




    def encabezado_funcion(self):

        localctx = gramaticaprueba.Encabezado_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_encabezado_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(gramaticaprueba.VOID)
            self.state = 136
            localctx._ID = self.match(gramaticaprueba.ID)

            if self.inClass and self.inFuncion:
                self.yyerror("SEMANTICO: no se puede anidar funciones dentro de una clase", (0 if localctx._ID is None else localctx._ID.line))
                self.auxBorrado = self.polacaInversa.reference_counter
            else:
                if not self.simbolos.isKey((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual):
                    self.auxIDFunc = (None if localctx._ID is None else localctx._ID.text) + self.ambitoActual
                    self.simbolos.addCaracteristica(self.auxIDFunc, "uso", "funcion")
                    localctx.funcion = (None if localctx._ID is None else localctx._ID.text) + self.ambitoActual
                    self.ambitoActual = self.ambitoActual + ":" + (None if localctx._ID is None else localctx._ID.text)
                else:
                    self.yyerror(" SEMANTICO: variable " + (None if localctx._ID is None else localctx._ID.text) + " ya existe en el ambito actual", (0 if localctx._ID is None else localctx._ID.line))

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
        self.enterRule(localctx, 14, self.RULE_parametro)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 140
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.addCaracteristica(self.auxIDFunc, "nroParametros", "0")

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 143
                localctx._tipo = self.tipo()
                self.state = 144
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 145
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.addCaracteristica(self.auxIDFunc, "tipoParametro", (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))
                self.simbolos.addCaracteristica(self.auxIDFunc, "nroParametros", "1")
                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual, "tipo", (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))


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
        self.enterRule(localctx, 16, self.RULE_cuerpo_func)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.inFuncion = True
                self.state = 151
                self.cuerpo(0)
                self.state = 152
                self.ejecucion_retorno()
                self.state = 153
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.inFuncion = True
                self.state = 156
                self.ejecucion_retorno()
                self.state = 157
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
        self.enterRule(localctx, 18, self.RULE_ejecucion_retorno)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.control_retorno()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.control_retorno()
                self.state = 163
                self.match(gramaticaprueba.COMMA)
                self.state = 164
                self.ejecucion_retorno()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.while_retorno()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 167
                self.while_retorno()
                self.state = 168
                self.match(gramaticaprueba.COMMA)
                self.state = 169
                self.ejecucion_retorno()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 171
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
        self.enterRule(localctx, 20, self.RULE_control_retorno)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.if_condicion()
                self.state = 176
                self.then_retorno()
                self.state = 177
                self.match(gramaticaprueba.END_IF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.if_condicion()
                self.state = 180
                self.then_retorno()
                self.state = 181
                self.match(gramaticaprueba.ELSE)
                self.state = 182
                self.bloque_control()
                self.state = 183
                self.match(gramaticaprueba.END_IF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.if_condicion()
                self.state = 186
                self.bloque_control()
                self.state = 187
                self.else_retorno()
                self.state = 188
                self.match(gramaticaprueba.END_IF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 190
                self.if_condicion()
                self.state = 191
                self.then_retorno()
                self.state = 192
                self.else_retorno()
                self.state = 193
                self.match(gramaticaprueba.END_IF)
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
        self.enterRule(localctx, 22, self.RULE_then_retorno)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 198
                self.ejecucion_retorno()
                self.state = 199
                self.match(gramaticaprueba.COMMA)
                self.state = 200
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 203
                self.cuerpo_ejecucion(0)
                self.state = 204
                self.ejecucion_retorno()
                self.state = 205
                self.match(gramaticaprueba.COMMA)
                self.state = 206
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
        self.enterRule(localctx, 24, self.RULE_else_retorno)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(gramaticaprueba.ELSE)
                self.state = 211
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 212
                self.ejecucion_retorno()
                self.state = 213
                self.match(gramaticaprueba.COMMA)
                self.state = 214
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(gramaticaprueba.ELSE)
                self.state = 217
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 218
                self.cuerpo_ejecucion(0)
                self.state = 219
                self.ejecucion_retorno()
                self.state = 220
                self.match(gramaticaprueba.COMMA)
                self.state = 221
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
        self.enterRule(localctx, 26, self.RULE_while_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(gramaticaprueba.WHILE)
            self.state = 226
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 227
            self.condicion()
            self.state = 228
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 229
            self.match(gramaticaprueba.DO)
            self.state = 230
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 231
            self.cuerpo_ejecucion(0)
            self.state = 232
            self.match(gramaticaprueba.RETURN)
            self.state = 233
            self.match(gramaticaprueba.COMMA)
            self.state = 234
            self.match(gramaticaprueba.RIGHT_BRACE)

            self.polacaInversa.addElemento("ret")

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

        def encabezado_clase(self):
            return self.getTypedRuleContext(gramaticaprueba.Encabezado_claseContext,0)


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
        self.enterRule(localctx, 28, self.RULE_declaracion_clase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.encabezado_clase()
            self.state = 238
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 239
            self.componentes_clase(0)
            self.state = 240
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.state = 241
            self.match(gramaticaprueba.COMMA)

            self.reducirAmbito()
            self.inClass = False

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Encabezado_claseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def CLASS(self):
            return self.getToken(gramaticaprueba.CLASS, 0)

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_encabezado_clase




    def encabezado_clase(self):

        localctx = gramaticaprueba.Encabezado_claseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_encabezado_clase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(gramaticaprueba.CLASS)
            self.state = 245
            localctx._ID = self.match(gramaticaprueba.ID)

            self.auxIDClass = (None if localctx._ID is None else localctx._ID.text) + self.ambitoActual
            self.clasesDeclaradas.append((None if localctx._ID is None else localctx._ID.text))
            self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual, "uso", "nombre de clase")
            self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual, "ambito de clase", self.ambitoActual + ":" + (None if localctx._ID is None else localctx._ID.text))
            self.ambitoActual = self.ambitoActual + ":" + (None if localctx._ID is None else localctx._ID.text)
            self.inClass = True

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

        def componente_var(self):
            return self.getTypedRuleContext(gramaticaprueba.Componente_varContext,0)


        def componente_func(self):
            return self.getTypedRuleContext(gramaticaprueba.Componente_funcContext,0)


        def componente_herencia(self):
            return self.getTypedRuleContext(gramaticaprueba.Componente_herenciaContext,0)


        def componentes_clase(self):
            return self.getTypedRuleContext(gramaticaprueba.Componentes_claseContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_componentes_clase



    def componentes_clase(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaprueba.Componentes_claseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_componentes_clase, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 249
                self.componente_var()
                pass

            elif la_ == 2:
                self.state = 250
                self.componente_func()
                pass

            elif la_ == 3:
                self.state = 251
                self.componente_herencia()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 260
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 254
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 255
                        self.componente_var()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 256
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 257
                        self.componente_func()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 258
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 259
                        self.componente_herencia()
                        pass

             
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Componente_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion_var(self):
            return self.getTypedRuleContext(gramaticaprueba.Declaracion_varContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_componente_var




    def componente_var(self):

        localctx = gramaticaprueba.Componente_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_componente_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.declaracion_var()

            componentesActuales = self.simbolos.getCaracteristica(self.auxIDClass, "propiedades")
            if isinstance(componentesActuales, list):
                for value in self.listaVar:
                    componentesActuales.append(value)
            else:
                self.simbolos.addCaracteristica(self.auxIDClass, "propiedades", self.listaVar)
            self.listaVar = []

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Componente_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion_func(self):
            return self.getTypedRuleContext(gramaticaprueba.Declaracion_funcContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_componente_func




    def componente_func(self):

        localctx = gramaticaprueba.Componente_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_componente_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.declaracion_func()

            componentesActuales = self.simbolos.getCaracteristica(self.auxIDClass, "miembros de clase")
            if isinstance(componentesActuales, list):
                componentesActuales.append(self.auxIDFunc[:self.auxIDFunc.find(":")])
            else:
                componentesActuales = [self.auxIDFunc[:self.auxIDFunc.find(":")]]
                self.simbolos.addCaracteristica(self.auxIDClass, "miembros de clase", componentesActuales)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Componente_herenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_componente_herencia




    def componente_herencia(self):

        localctx = gramaticaprueba.Componente_herenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_componente_herencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            localctx._ID = self.match(gramaticaprueba.ID)
            self.state = 272
            self.match(gramaticaprueba.COMMA)

            identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
            if identificador != "":
                herenciasActuales = self.simbolos.getCaracteristica(identificador, "numero de herencias")
                if isinstance(herenciasActuales, int):
                    if herenciasActuales < 2:
                        self.simbolos.aumentarReferencia(identificador)
                        self.simbolos.addCaracteristica(self.auxIDClass, "numero de herencias", herenciasActuales + 1)
                        self.simbolos.addCaracteristica(self.auxIDClass, "clase herencia", identificador)
                        propiedades = self.simbolos.getCaracteristica(identificador, "propiedades")
                        if isinstance(propiedades, list):
                            self.simbolos.addCaracteristica(self.auxIDClass, "propiedades heredadas", propiedades)
                    else:
                        self.yyerror("SEMANTICO: se exeden los niveles de herencia", (0 if localctx._ID is None else localctx._ID.line))
                else:
                    self.simbolos.addCaracteristica(self.auxIDClass, "numero de herencias", 1)
                    self.simbolos.addCaracteristica(self.auxIDClass, "clase herencia", identificador)
                    propiedades = self.simbolos.getCaracteristica(identificador, "propiedades")
                    if isinstance(propiedades, list):
                        self.simbolos.addCaracteristica(self.auxIDClass, "propiedades heredadas", propiedades)
            else:
                simbolo = (None if localctx._ID is None else localctx._ID.text)
                if simbolo in self.clasesUsadas.keys():
                    self.clasesUsadas[simbolo] += 1
                else:
                    self.clasesUsadas[simbolo] = 1

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_cuerpo_ejecucion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.ejecucion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaprueba.Cuerpo_ejecucionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo_ejecucion)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    self.ejecucion() 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_ejecucion)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.asignacion()
                self.state = 286
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.invocacion()
                self.state = 289
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
                self.seleccion()
                self.state = 292
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 294
                self.print_()
                self.state = 295
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 297
                self.while_()
                self.state = 298
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 300
                localctx._ERROR = self.match(gramaticaprueba.ERROR)
                self.state = 301
                self.match(gramaticaprueba.COMMA)
                self.yyerror("SINTACTICO: error en sentencia ejecutable", (0 if localctx._ERROR is None else localctx._ERROR.line))
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


        def uso_clase(self):
            return self.getTypedRuleContext(gramaticaprueba.Uso_claseContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_asignacion




    def asignacion(self):

        localctx = gramaticaprueba.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_asignacion)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 306
                self.match(gramaticaprueba.EQUALS)
                self.state = 307
                self.expresion(0)

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    if identificador in self.declaracionesVariables.keys():
                        if self.ambitoActual == self.getAmbitoId(identificador):
                            self.declaracionesVariables.pop(identificador)
                    self.simbolos.aumentarReferencia(identificador)
                    self.polacaInversa.addElemento(identificador)
                    self.polacaInversa.addElemento("=")
                else:
                    self.yyerror("SEMANTICO: identificador " + (None if localctx._ID is None else localctx._ID.text) + " no declarado en un ambito valido", (0 if localctx._ID is None else localctx._ID.line))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.uso_clase()
                self.state = 311
                self.match(gramaticaprueba.EQUALS)
                uso = self.polacaInversa.removeLast()
                self.state = 313
                self.expresion(0)

                self.polacaInversa.addElemento(uso)
                self.polacaInversa.addElemento("=")

                pass


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
            self.herencia = None # Token
            self.herencia1 = None # Token
            self.herencia2 = None # Token

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

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaprueba.DOT)
            else:
                return self.getToken(gramaticaprueba.DOT, i)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_invocacion




    def invocacion(self):

        localctx = gramaticaprueba.InvocacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_invocacion)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 319
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 320
                self.expresion(0)
                self.state = 321
                self.match(gramaticaprueba.RIGHT_PAREN)

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    if self.simbolos.getCaracteristica(identificador, "uso") == "funcion":
                        if self.simbolos.getCaracteristica(identificador, "nroParametros") == "1":
                            self.simbolos.aumentarReferencia(identificador)
                            aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + identificador)
                            self.polacaInversa.addElemento(aux)
                            self.polacaInversa.addElemento("CALLFUNC")
                        else:
                            self.yyerror("SEMANTICO: numero incorrecto de parametros", (0 if localctx._ID is None else localctx._ID.line))
                    else:
                        self.yyerror("SEMANTICO: identificador no es una funcion", (0 if localctx._ID is None else localctx._ID.line))
                else:
                    self.yyerror("SEMANTICO: funcion no declarada en un ambito valido", (0 if localctx._ID is None else localctx._ID.line))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 325
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 326
                self.match(gramaticaprueba.RIGHT_PAREN)

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    if self.simbolos.getCaracteristica(identificador, "uso") == "funcion":
                        if self.simbolos.getCaracteristica(identificador, "nroParametros") == "0":
                            self.simbolos.aumentarReferencia(identificador)
                            aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + identificador)
                            self.polacaInversa.addElemento(aux)
                            self.polacaInversa.addElemento("CALLFUNC")
                        else:
                            self.yyerror("SEMANTICO: numero incorrecto de parametros", (0 if localctx._ID is None else localctx._ID.line))
                    else:
                        self.yyerror("SEMANTICO: identificador no es una funcion", (0 if localctx._ID is None else localctx._ID.line))
                else:
                    self.yyerror("SEMANTICO: funcion no declarada en un ambito valido", (0 if localctx._ID is None else localctx._ID.line))

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 329
                self.match(gramaticaprueba.DOT)
                self.state = 330
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 331
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 332
                self.match(gramaticaprueba.RIGHT_PAREN)

                simbolo = self.verificarId((None if localctx.clase is None else localctx.clase.text) + self.ambitoActual)
                if  simbolo != "":
                    self.simbolos.aumentarReferencia(simbolo)
                    claseAmbito = self.verificarId(self.simbolos.getCaracteristica(simbolo, "tipo") + self.ambitoActual)
                    miembros = self.simbolos.getCaracteristica(claseAmbito, "miembros de clase")
                    if (None if localctx.funcion is None else localctx.funcion.text) in miembros:
                        ambitoClase = self.simbolos.getCaracteristica(claseAmbito, "ambito de clase")
                        simboloFuncion = self.verificarId((None if localctx.funcion is None else localctx.funcion.text) + ambitoClase)
                        if self.simbolos.getCaracteristica(simboloFuncion, "nroParametros") == "0":
                            self.simbolos.aumentarReferencia(simboloFuncion)
                            aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + simboloFuncion)
                            print(aux)
                            self.polacaInversa.addElemento(aux)
                            self.polacaInversa.addElemento("CALLFUNC")
                        else:
                            self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrado en clase " + claseAmbito, (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 334
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 335
                self.match(gramaticaprueba.DOT)
                self.state = 336
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 337
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 338
                self.expresion(0)
                self.state = 339
                self.match(gramaticaprueba.RIGHT_PAREN)

                simbolo = self.verificarId((None if localctx.clase is None else localctx.clase.text) + self.ambitoActual)
                if  simbolo != "":
                    self.simbolos.aumentarReferencia(simbolo)
                    claseAmbito = self.verificarId(self.simbolos.getCaracteristica(simbolo, "tipo") + self.ambitoActual)
                    miembros = self.simbolos.getCaracteristica(claseAmbito, "miembros de clase")
                    if (None if localctx.funcion is None else localctx.funcion.text) in miembros:
                        ambitoClase = self.simbolos.getCaracteristica(claseAmbito, "ambito de clase")
                        simboloFuncion = self.verificarId((None if localctx.funcion is None else localctx.funcion.text) + ambitoClase)
                        if self.simbolos.getCaracteristica(simboloFuncion, "nroParametros") == "1":
                            self.simbolos.aumentarReferencia(simboloFuncion)
                            aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + simboloFuncion)
                            print(aux)
                            self.polacaInversa.addElemento(aux)
                            self.polacaInversa.addElemento("CALLFUNC")
                        else:
                            self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrado en clase " + claseAmbito, (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 342
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 343
                self.match(gramaticaprueba.DOT)
                self.state = 344
                localctx.herencia = self.match(gramaticaprueba.ID)
                self.state = 345
                self.match(gramaticaprueba.DOT)
                self.state = 346
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 347
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 348
                self.match(gramaticaprueba.RIGHT_PAREN)

                simbolo = self.verificarId((None if localctx.clase is None else localctx.clase.text) + self.ambitoActual)
                if  simbolo != "":
                    self.simbolos.aumentarReferencia(simbolo)
                    claseAmbito = self.verificarId(self.simbolos.getCaracteristica(simbolo, "tipo") + self.ambitoActual)
                    claseHerencia = self.simbolos.getCaracteristica(claseAmbito, "clase herencia")
                    if (None if localctx.herencia is None else localctx.herencia.text) == self.getIdSinAmbito(claseHerencia):
                        miembros = self.simbolos.getCaracteristica(claseHerencia, "miembros de clase")
                        if (None if localctx.funcion is None else localctx.funcion.text) in miembros:
                            ambitoClase = self.simbolos.getCaracteristica(claseHerencia, "ambito de clase")
                            simboloFuncion = self.verificarId((None if localctx.funcion is None else localctx.funcion.text) + ambitoClase)
                            if self.simbolos.getCaracteristica(simboloFuncion, "nroParametros") == "0":
                                self.simbolos.aumentarReferencia(simboloFuncion)
                                aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + simboloFuncion)
                                self.polacaInversa.addElemento(aux)
                                self.polacaInversa.addElemento("CALLFUNC")
                            else:
                                self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                        else:
                            self.yyerror("SEMANTICO: " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrado en clase " + (None if localctx.herencia is None else localctx.herencia.text), (0 if localctx.clase is None else localctx.clase.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.clase is None else localctx.clase.text) + " no hereda de " + (None if localctx.herencia is None else localctx.herencia.text), (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 350
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 351
                self.match(gramaticaprueba.DOT)
                self.state = 352
                localctx.herencia = self.match(gramaticaprueba.ID)
                self.state = 353
                self.match(gramaticaprueba.DOT)
                self.state = 354
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 355
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 356
                self.expresion(0)
                self.state = 357
                self.match(gramaticaprueba.RIGHT_PAREN)

                simbolo = self.verificarId((None if localctx.clase is None else localctx.clase.text) + self.ambitoActual)
                if  simbolo != "":
                    self.simbolos.aumentarReferencia(simbolo)
                    claseAmbito = self.verificarId(self.simbolos.getCaracteristica(simbolo, "tipo") + self.ambitoActual)
                    claseHerencia = self.simbolos.getCaracteristica(claseAmbito, "clase herencia")
                    if (None if localctx.herencia is None else localctx.herencia.text) == self.getIdSinAmbito(claseHerencia):
                        miembros = self.simbolos.getCaracteristica(claseHerencia, "miembros de clase")
                        if (None if localctx.funcion is None else localctx.funcion.text) in miembros:
                            ambitoClase = self.simbolos.getCaracteristica(claseHerencia, "ambito de clase")
                            simboloFuncion = self.verificarId((None if localctx.funcion is None else localctx.funcion.text) + ambitoClase)
                            if self.simbolos.getCaracteristica(simboloFuncion, "nroParametros") == "1":
                                self.simbolos.aumentarReferencia(simboloFuncion)
                                aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + simboloFuncion)
                                self.polacaInversa.addElemento(aux)
                                self.polacaInversa.addElemento("CALLFUNC")
                            else:
                                self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                        else:
                            self.yyerror("SEMANTICO: " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrado en clase " + (None if localctx.herencia is None else localctx.herencia.text), (0 if localctx.clase is None else localctx.clase.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.clase is None else localctx.clase.text) + " no hereda de " + (None if localctx.herencia is None else localctx.herencia.text), (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 360
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 361
                self.match(gramaticaprueba.DOT)
                self.state = 362
                localctx.herencia1 = self.match(gramaticaprueba.ID)
                self.state = 363
                self.match(gramaticaprueba.DOT)
                self.state = 364
                localctx.herencia2 = self.match(gramaticaprueba.ID)
                self.state = 365
                self.match(gramaticaprueba.DOT)
                self.state = 366
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 367
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 368
                self.match(gramaticaprueba.RIGHT_PAREN)

                simbolo = self.verificarId((None if localctx.clase is None else localctx.clase.text) + self.ambitoActual)
                if  simbolo != "":
                    self.simbolos.aumentarReferencia(simbolo)
                    claseAmbito = self.verificarId(self.simbolos.getCaracteristica(simbolo, "tipo") + self.ambitoActual)
                    claseHerencia = self.simbolos.getCaracteristica(claseAmbito, "clase herencia")
                    if (None if localctx.herencia1 is None else localctx.herencia1.text) == self.getIdSinAmbito(claseHerencia):
                        claseHerencia = self.simbolos.getCaracteristica(claseHerencia, "clase herencia")
                        if (None if localctx.herencia2 is None else localctx.herencia2.text) == self.getIdSinAmbito(claseHerencia):
                            miembros = self.simbolos.getCaracteristica(claseHerencia, "miembros de clase")
                            if (None if localctx.funcion is None else localctx.funcion.text) in miembros:
                                ambitoClase = self.simbolos.getCaracteristica(claseHerencia, "ambito de clase")
                                simboloFuncion = self.verificarId((None if localctx.funcion is None else localctx.funcion.text) + ambitoClase)
                                if self.simbolos.getCaracteristica(simboloFuncion, "nroParametros") == "0":
                                    self.simbolos.aumentarReferencia(simboloFuncion)
                                    aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + simboloFuncion)
                                    self.polacaInversa.addElemento(aux)
                                    self.polacaInversa.addElemento("CALLFUNC")
                                else:
                                    self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                            else:
                                self.yyerror("SEMANTICO: funcion " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrada en " + (None if localctx.herencia2 is None else localctx.herencia2.text), (0 if localctx.clase is None else localctx.clase.line))
                        else:
                            self.yyerror("SEMANTICO: " + (None if localctx.herencia1 is None else localctx.herencia1.text) + " no hereda de " + (None if localctx.herencia2 is None else localctx.herencia2.text), (0 if localctx.clase is None else localctx.clase.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.clase is None else localctx.clase.text) + " no hereda de " + (None if localctx.herencia1 is None else localctx.herencia1.text), (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 370
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 371
                self.match(gramaticaprueba.DOT)
                self.state = 372
                localctx.herencia1 = self.match(gramaticaprueba.ID)
                self.state = 373
                self.match(gramaticaprueba.DOT)
                self.state = 374
                localctx.herencia2 = self.match(gramaticaprueba.ID)
                self.state = 375
                self.match(gramaticaprueba.DOT)
                self.state = 376
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 377
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 378
                self.expresion(0)
                self.state = 379
                self.match(gramaticaprueba.RIGHT_PAREN)

                simbolo = self.verificarId((None if localctx.clase is None else localctx.clase.text) + self.ambitoActual)
                if  simbolo != "":
                    self.simbolos.aumentarReferencia(simbolo)
                    claseAmbito = self.verificarId(self.simbolos.getCaracteristica(simbolo, "tipo") + self.ambitoActual)
                    claseHerencia = self.simbolos.getCaracteristica(claseAmbito, "clase herencia")
                    if (None if localctx.herencia1 is None else localctx.herencia1.text) == self.getIdSinAmbito(claseHerencia):
                        claseHerencia = self.simbolos.getCaracteristica(claseHerencia, "clase herencia")
                        if (None if localctx.herencia2 is None else localctx.herencia2.text) == self.getIdSinAmbito(claseHerencia):
                            miembros = self.simbolos.getCaracteristica(claseHerencia, "miembros de clase")
                            if (None if localctx.funcion is None else localctx.funcion.text) in miembros:
                                ambitoClase = self.simbolos.getCaracteristica(claseHerencia, "ambito de clase")
                                simboloFuncion = self.verificarId((None if localctx.funcion is None else localctx.funcion.text) + ambitoClase)
                                if self.simbolos.getCaracteristica(simboloFuncion, "nroParametros") == "1":
                                    self.simbolos.aumentarReferencia(simboloFuncion)
                                    aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + simboloFuncion)
                                    self.polacaInversa.addElemento(aux)
                                    self.polacaInversa.addElemento("CALLFUNC")
                                else:
                                    self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                            else:
                                self.yyerror("SEMANTICO: funcion " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrada en " + (None if localctx.herencia2 is None else localctx.herencia2.text), (0 if localctx.clase is None else localctx.clase.line))
                        else:
                            self.yyerror("SEMANTICO: " + (None if localctx.herencia1 is None else localctx.herencia1.text) + " no hereda de " + (None if localctx.herencia2 is None else localctx.herencia2.text), (0 if localctx.clase is None else localctx.clase.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.clase is None else localctx.clase.text) + " no hereda de " + (None if localctx.herencia1 is None else localctx.herencia1.text), (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))

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
        self.enterRule(localctx, 48, self.RULE_seleccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.if_condicion()
            self.state = 385
            self.bloque_control()
            self.state = 386
            self.posible_else()
            self.state = 387
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
        self.enterRule(localctx, 50, self.RULE_posible_else)
        try:
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.else_()
                self.state = 391
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
        self.enterRule(localctx, 52, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
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
        self.enterRule(localctx, 54, self.RULE_if_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(gramaticaprueba.IF)
            self.state = 401
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 402
            self.condicion()
            self.state = 403
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
        self.enterRule(localctx, 56, self.RULE_bloque_control)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 407
            self.cuerpo_ejecucion(0)
            self.state = 408
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
        self.enterRule(localctx, 58, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.expresion(0)
            self.state = 411
            localctx._comparador = self.comparador()
            self.state = 412
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
        self.enterRule(localctx, 60, self.RULE_comparador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
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
        self.enterRule(localctx, 62, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(gramaticaprueba.PRINT)
            self.state = 418
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 419
            localctx._CADENA = self.match(gramaticaprueba.CADENA)
            self.state = 420
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
        self.enterRule(localctx, 64, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.while_condicion()
            self.state = 424
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
        self.enterRule(localctx, 66, self.RULE_while_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.aux = self.polacaInversa.reference_counter
            self.state = 428
            self.match(gramaticaprueba.WHILE)
            self.polacaInversa.addElemento("TAG"+str(self.aux))
            self.state = 430
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 431
            self.condicion()
            self.state = 432
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 433
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
        self.enterRule(localctx, 68, self.RULE_tipo)
        try:
            self.state = 441
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(gramaticaprueba.INT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(gramaticaprueba.ULONG)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.match(gramaticaprueba.FLOAT)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 439
                localctx._ID = self.match(gramaticaprueba.ID)

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    self.simbolos.aumentarReferencia(identificador)
                else:
                    simbolo = (None if localctx._ID is None else localctx._ID.text)
                    if simbolo in self.clasesUsadas.keys():
                        self.clasesUsadas[simbolo] += 1
                    else:
                        self.clasesUsadas[simbolo] = 1

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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 458
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 456
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 446
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 447
                        self.match(gramaticaprueba.PLUS)
                        self.state = 448
                        self.termino(0)
                        self.polacaInversa.addElemento("+")
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 451
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 452
                        self.match(gramaticaprueba.MINUS)
                        self.state = 453
                        self.termino(0)
                        self.polacaInversa.addElemento("-")
                        pass

             
                self.state = 460
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_termino, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 476
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 474
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 464
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 465
                        self.match(gramaticaprueba.MULTIPLY)
                        self.state = 466
                        self.factor()
                        self.polacaInversa.addElemento("*")
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 469
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 470
                        self.match(gramaticaprueba.DIVIDE)
                        self.state = 471
                        self.factor()
                        self.polacaInversa.addElemento("/")
                        pass

             
                self.state = 478
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
        self.enterRule(localctx, 74, self.RULE_factor)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.referencia()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.match(gramaticaprueba.MINUS)
                self.state = 481
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                key = (None if localctx._NUM_INT is None else localctx._NUM_INT.text)
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove(key)
                    else:
                        self.simbolos.reducirReferencia(key)
                self.simbolos.addSimbolo("-" + (None if localctx._NUM_INT is None else localctx._NUM_INT.text))
                self.simbolos.addCaracteristica("-" + (None if localctx._NUM_INT is None else localctx._NUM_INT.text), "tipo", "INT")
                self.simbolos.addCaracteristica("-" + (None if localctx._NUM_INT is None else localctx._NUM_INT.text), "valor", self.getValor("-" + (None if localctx._NUM_INT is None else localctx._NUM_INT.text)))
                self.polacaInversa.addElemento((None if localctx._NUM_INT is None else localctx._NUM_INT.text))

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                localctx._NUM_ULONG = self.match(gramaticaprueba.NUM_ULONG)

                texto = (None if localctx._NUM_ULONG is None else localctx._NUM_ULONG.text)
                self.simbolos.addCaracteristica(texto, "tipo", "ULONG")
                self.simbolos.addCaracteristica(texto, "valor", self.getValor(texto))
                self.polacaInversa.addElemento((None if localctx._NUM_ULONG is None else localctx._NUM_ULONG.text))

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 485
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                self.simbolos.addCaracteristica((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text), "tipo", "FLOAT")
                self.polacaInversa.addElemento((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))
                # TODO calcular el float y guardarlo en la tabla

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 487
                self.match(gramaticaprueba.MINUS)
                self.state = 488
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                key = (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text)
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove(key)
                    else:
                        self.simbolos.reducirReferencia(key)
                self.simbolos.addSimbolo("-" + (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))
                self.polacaInversa.addElemento((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))
                # TODO calcular el float

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 490
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                if (None if localctx._NUM_INT is None else localctx._NUM_INT.text) == "32768_i":
                    self.yyerror("LEXICO: INT fuera de rango",(0 if localctx._NUM_INT is None else localctx._NUM_INT.line))
                else:
                    texto = (None if localctx._NUM_INT is None else localctx._NUM_INT.text)
                    self.simbolos.addCaracteristica(texto, "tipo", "INT")
                    self.simbolos.addCaracteristica(texto, "valor", self.getValor(texto))
                    self.polacaInversa.addElemento((None if localctx._NUM_INT is None else localctx._NUM_INT.text))

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 492
                localctx._ERROR = self.match(gramaticaprueba.ERROR)
                self.yyerror("SINTACTICO: se espera una constante o id",(0 if localctx._ERROR is None else localctx._ERROR.line))
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
        self.enterRule(localctx, 76, self.RULE_referencia)
        try:
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                localctx._ID = self.match(gramaticaprueba.ID)

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    self.polacaInversa.addElemento(identificador)
                self.state = 498
                self.posible_guion_doble()

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    self.simbolos.aumentarReferencia(identificador)
                    if (self.menos_menos is True):
                        self.polacaInversa.addElemento(identificador)
                        self.polacaInversa.addElemento('=')
                        self.menos_menos = False
                else:
                    self.yyerror("SEMANTICO: id " + (None if localctx._ID is None else localctx._ID.text) + " no existe en un ambito valido", (0 if localctx._ID is None else localctx._ID.line))


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
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
        self.enterRule(localctx, 78, self.RULE_posible_guion_doble)
        try:
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.match(gramaticaprueba.MINUS)
                self.state = 505
                self.match(gramaticaprueba.MINUS)

                self.menos_menos = True
                self.polacaInversa.addElemento('1')
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
            self.herencia = None # Token
            self.herencia1 = None # Token
            self.herencia2 = None # Token

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaprueba.DOT)
            else:
                return self.getToken(gramaticaprueba.DOT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaprueba.ID)
            else:
                return self.getToken(gramaticaprueba.ID, i)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_uso_clase




    def uso_clase(self):

        localctx = gramaticaprueba.Uso_claseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_uso_clase)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 511
                self.match(gramaticaprueba.DOT)
                self.state = 512
                localctx.atributo = self.match(gramaticaprueba.ID)

                idClase = self.verificarId((None if localctx.clase is None else localctx.clase.text) + self.ambitoActual)
                if idClase != "":
                    self.simbolos.aumentarReferencia(idClase)
                    ambitoClase = self.verificarId(self.simbolos.getCaracteristica(idClase, "tipo") + self.ambitoActual)
                    if (None if localctx.atributo is None else localctx.atributo.text) in self.simbolos.getCaracteristica(ambitoClase, "propiedades"):
                        atributo = (None if localctx.atributo is None else localctx.atributo.text) + self.simbolos.getCaracteristica(ambitoClase, "ambito de clase")
                        if atributo != "":
                            self.simbolos.aumentarReferencia(atributo)
                            clase = (None if localctx.clase is None else localctx.clase.text) + self.ambitoActual + "." + (None if localctx.atributo is None else localctx.atributo.text)
                            self.polacaInversa.addElemento(str(clase))
                    else:
                        self.yyerror("SEMANTICO: propiedad " + (None if localctx.atributo is None else localctx.atributo.text) + " no encontrada en clase " + idClase, (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 515
                self.match(gramaticaprueba.DOT)
                self.state = 516
                localctx.herencia = self.match(gramaticaprueba.ID)
                self.state = 517
                self.match(gramaticaprueba.DOT)
                self.state = 518
                localctx.atributo = self.match(gramaticaprueba.ID)

                idClase = self.verificarId((None if localctx.clase is None else localctx.clase.text) + self.ambitoActual)
                if idClase != "":
                    self.simbolos.aumentarReferencia(idClase)
                    ambitoClase = self.verificarId(self.simbolos.getCaracteristica(idClase, "tipo") + self.ambitoActual)
                    claseHerencia = self.simbolos.getCaracteristica(ambitoClase, "clase herencia")
                    if (None if localctx.herencia is None else localctx.herencia.text) == self.getIdSinAmbito(claseHerencia):
                        if (None if localctx.atributo is None else localctx.atributo.text) in self.simbolos.getCaracteristica(claseHerencia, "propiedades"):
                            atributo = (None if localctx.atributo is None else localctx.atributo.text) + self.simbolos.getCaracteristica(claseHerencia, "ambito de clase")
                            self.simbolos.aumentarReferencia(atributo)
                            clase = (None if localctx.clase is None else localctx.clase.text) + self.ambitoActual + "." + (None if localctx.herencia is None else localctx.herencia.text) + "." + (None if localctx.atributo is None else localctx.atributo.text)
                            self.polacaInversa.addElemento(str(clase))
                        else:
                            self.yyerror("SEMANTICO: propiedad " + (None if localctx.atributo is None else localctx.atributo.text) + " no encontrada en clase " + claseHerencia, (0 if localctx.clase is None else localctx.clase.line))
                    else:
                        self.yyerror("SEMANTICO: clase " + idClase + " no hereda de " + (None if localctx.herencia is None else localctx.herencia.text), (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 520
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 521
                self.match(gramaticaprueba.DOT)
                self.state = 522
                localctx.herencia1 = self.match(gramaticaprueba.ID)
                self.state = 523
                self.match(gramaticaprueba.DOT)
                self.state = 524
                localctx.herencia2 = self.match(gramaticaprueba.ID)
                self.state = 525
                self.match(gramaticaprueba.DOT)
                self.state = 526
                localctx.atributo = self.match(gramaticaprueba.ID)

                idClase = self.verificarId((None if localctx.clase is None else localctx.clase.text) + self.ambitoActual)
                if idClase != "":
                    self.simbolos.aumentarReferencia(idClase)
                    ambitoClase = self.verificarId(self.simbolos.getCaracteristica(idClase, "tipo") + self.ambitoActual)
                    claseHerencia = self.simbolos.getCaracteristica(ambitoClase, "clase herencia")
                    if (None if localctx.herencia1 is None else localctx.herencia1.text) == self.getIdSinAmbito(claseHerencia):
                        claseHerencia = self.simbolos.getCaracteristica(claseHerencia, "clase herencia")
                        if (None if localctx.herencia2 is None else localctx.herencia2.text) == self.getIdSinAmbito(claseHerencia):
                            if (None if localctx.atributo is None else localctx.atributo.text) in self.simbolos.getCaracteristica(claseHerencia, "propiedades"):
                                atributo = (None if localctx.atributo is None else localctx.atributo.text) + self.simbolos.getCaracteristica(claseHerencia, "ambito de clase")
                                self.simbolos.aumentarReferencia(atributo)
                                clase = (None if localctx.clase is None else localctx.clase.text) + self.ambitoActual + "." + (None if localctx.herencia1 is None else localctx.herencia1.text) + "." + (None if localctx.herencia2 is None else localctx.herencia2.text) + "." + (None if localctx.atributo is None else localctx.atributo.text)
                                self.polacaInversa.addElemento(str(clase))
                            else:
                                self.yyerror("SEMANTICO: propiedad " + (None if localctx.atributo is None else localctx.atributo.text) + " no encontrada en clase " + claseHerencia, (0 if localctx.clase is None else localctx.clase.line))
                        else:
                            self.yyerror("SEMANTICO: clase " + (None if localctx.herencia1 is None else localctx.herencia1.text) + " no hereda de " + (None if localctx.herencia2 is None else localctx.herencia2.text), (0 if localctx.clase is None else localctx.clase.line))
                    else:
                        self.yyerror("SEMANTICO: clase " + idClase + " no hereda de " + (None if localctx.herencia1 is None else localctx.herencia1.text), (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))

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
        self._predicates[1] = self.cuerpo_sempred
        self._predicates[16] = self.componentes_clase_sempred
        self._predicates[20] = self.cuerpo_ejecucion_sempred
        self._predicates[35] = self.expresion_sempred
        self._predicates[36] = self.termino_sempred
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
         




