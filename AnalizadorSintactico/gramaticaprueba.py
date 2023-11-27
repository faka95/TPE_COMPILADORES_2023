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
        4,1,39,468,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,
        1,3,1,83,8,1,1,1,1,1,1,1,1,1,5,1,89,8,1,10,1,12,1,92,9,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,106,8,2,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,120,8,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,144,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,155,
        8,8,1,9,1,9,1,9,1,9,3,9,161,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,178,8,12,1,12,1,
        12,1,12,1,12,1,12,1,12,5,12,186,8,12,10,12,12,12,189,9,12,1,13,1,
        13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,
        16,5,16,206,8,16,10,16,12,16,209,9,16,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,
        17,229,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,3,18,244,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,
        19,318,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,
        21,1,21,3,21,332,8,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,
        23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,27,1,
        27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,3,30,379,8,
        30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,5,31,394,8,31,10,31,12,31,397,9,31,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,5,32,412,8,32,10,32,12,32,
        415,9,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,3,33,432,8,33,1,34,1,34,1,34,1,34,1,34,1,34,
        3,34,440,8,34,1,35,1,35,1,35,1,35,3,35,446,8,35,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,3,36,466,8,36,1,36,0,5,2,24,32,62,64,37,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,0,1,3,0,13,15,22,22,31,32,477,0,74,1,0,0,
        0,2,82,1,0,0,0,4,105,1,0,0,0,6,107,1,0,0,0,8,119,1,0,0,0,10,121,
        1,0,0,0,12,130,1,0,0,0,14,143,1,0,0,0,16,154,1,0,0,0,18,160,1,0,
        0,0,20,162,1,0,0,0,22,169,1,0,0,0,24,177,1,0,0,0,26,190,1,0,0,0,
        28,193,1,0,0,0,30,196,1,0,0,0,32,200,1,0,0,0,34,228,1,0,0,0,36,243,
        1,0,0,0,38,317,1,0,0,0,40,319,1,0,0,0,42,331,1,0,0,0,44,333,1,0,
        0,0,46,336,1,0,0,0,48,342,1,0,0,0,50,346,1,0,0,0,52,351,1,0,0,0,
        54,353,1,0,0,0,56,359,1,0,0,0,58,364,1,0,0,0,60,378,1,0,0,0,62,380,
        1,0,0,0,64,398,1,0,0,0,66,431,1,0,0,0,68,439,1,0,0,0,70,445,1,0,
        0,0,72,465,1,0,0,0,74,75,5,35,0,0,75,76,3,2,1,0,76,77,5,36,0,0,77,
        78,6,0,-1,0,78,1,1,0,0,0,79,80,6,1,-1,0,80,83,3,4,2,0,81,83,3,34,
        17,0,82,79,1,0,0,0,82,81,1,0,0,0,83,90,1,0,0,0,84,85,10,4,0,0,85,
        89,3,4,2,0,86,87,10,3,0,0,87,89,3,34,17,0,88,84,1,0,0,0,88,86,1,
        0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,3,1,0,0,0,92,
        90,1,0,0,0,93,94,3,6,3,0,94,95,6,2,-1,0,95,106,1,0,0,0,96,97,3,10,
        5,0,97,98,6,2,-1,0,98,106,1,0,0,0,99,100,3,20,10,0,100,101,6,2,-1,
        0,101,106,1,0,0,0,102,103,5,17,0,0,103,104,5,26,0,0,104,106,6,2,
        -1,0,105,93,1,0,0,0,105,96,1,0,0,0,105,99,1,0,0,0,105,102,1,0,0,
        0,106,5,1,0,0,0,107,108,3,60,30,0,108,109,3,8,4,0,109,110,5,26,0,
        0,110,111,6,3,-1,0,111,7,1,0,0,0,112,113,5,16,0,0,113,120,6,4,-1,
        0,114,115,5,16,0,0,115,116,5,33,0,0,116,117,3,8,4,0,117,118,6,4,
        -1,0,118,120,1,0,0,0,119,112,1,0,0,0,119,114,1,0,0,0,120,9,1,0,0,
        0,121,122,3,12,6,0,122,123,6,5,-1,0,123,124,3,14,7,0,124,125,5,35,
        0,0,125,126,3,16,8,0,126,127,5,36,0,0,127,128,5,26,0,0,128,129,6,
        5,-1,0,129,11,1,0,0,0,130,131,5,6,0,0,131,132,5,16,0,0,132,133,6,
        6,-1,0,133,13,1,0,0,0,134,135,5,29,0,0,135,136,5,30,0,0,136,144,
        6,7,-1,0,137,138,5,29,0,0,138,139,3,60,30,0,139,140,5,16,0,0,140,
        141,5,30,0,0,141,142,6,7,-1,0,142,144,1,0,0,0,143,134,1,0,0,0,143,
        137,1,0,0,0,144,15,1,0,0,0,145,146,6,8,-1,0,146,147,3,2,1,0,147,
        148,3,18,9,0,148,149,6,8,-1,0,149,155,1,0,0,0,150,151,6,8,-1,0,151,
        152,3,18,9,0,152,153,6,8,-1,0,153,155,1,0,0,0,154,145,1,0,0,0,154,
        150,1,0,0,0,155,17,1,0,0,0,156,157,5,12,0,0,157,158,5,26,0,0,158,
        161,6,9,-1,0,159,161,6,9,-1,0,160,156,1,0,0,0,160,159,1,0,0,0,161,
        19,1,0,0,0,162,163,3,22,11,0,163,164,5,35,0,0,164,165,3,24,12,0,
        165,166,5,36,0,0,166,167,5,26,0,0,167,168,6,10,-1,0,168,21,1,0,0,
        0,169,170,5,5,0,0,170,171,5,16,0,0,171,172,6,11,-1,0,172,23,1,0,
        0,0,173,174,6,12,-1,0,174,178,3,26,13,0,175,178,3,28,14,0,176,178,
        3,30,15,0,177,173,1,0,0,0,177,175,1,0,0,0,177,176,1,0,0,0,178,187,
        1,0,0,0,179,180,10,3,0,0,180,186,3,26,13,0,181,182,10,2,0,0,182,
        186,3,28,14,0,183,184,10,1,0,0,184,186,3,30,15,0,185,179,1,0,0,0,
        185,181,1,0,0,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,
        187,188,1,0,0,0,188,25,1,0,0,0,189,187,1,0,0,0,190,191,3,6,3,0,191,
        192,6,13,-1,0,192,27,1,0,0,0,193,194,3,10,5,0,194,195,6,14,-1,0,
        195,29,1,0,0,0,196,197,5,16,0,0,197,198,5,26,0,0,198,199,6,15,-1,
        0,199,31,1,0,0,0,200,201,6,16,-1,0,201,202,3,34,17,0,202,207,1,0,
        0,0,203,204,10,2,0,0,204,206,3,34,17,0,205,203,1,0,0,0,206,209,1,
        0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,33,1,0,0,0,209,207,1,0,
        0,0,210,211,3,36,18,0,211,212,5,26,0,0,212,229,1,0,0,0,213,214,3,
        38,19,0,214,215,5,26,0,0,215,229,1,0,0,0,216,217,3,40,20,0,217,218,
        5,26,0,0,218,229,1,0,0,0,219,220,3,54,27,0,220,221,5,26,0,0,221,
        229,1,0,0,0,222,223,3,56,28,0,223,224,5,26,0,0,224,229,1,0,0,0,225,
        226,5,17,0,0,226,227,5,26,0,0,227,229,6,17,-1,0,228,210,1,0,0,0,
        228,213,1,0,0,0,228,216,1,0,0,0,228,219,1,0,0,0,228,222,1,0,0,0,
        228,225,1,0,0,0,229,35,1,0,0,0,230,231,6,18,-1,0,231,232,5,16,0,
        0,232,233,5,34,0,0,233,234,3,62,31,0,234,235,6,18,-1,0,235,244,1,
        0,0,0,236,237,6,18,-1,0,237,238,3,72,36,0,238,239,5,34,0,0,239,240,
        6,18,-1,0,240,241,3,62,31,0,241,242,6,18,-1,0,242,244,1,0,0,0,243,
        230,1,0,0,0,243,236,1,0,0,0,244,37,1,0,0,0,245,246,6,19,-1,0,246,
        247,5,16,0,0,247,248,5,29,0,0,248,249,3,62,31,0,249,250,5,30,0,0,
        250,251,6,19,-1,0,251,318,1,0,0,0,252,253,6,19,-1,0,253,254,5,16,
        0,0,254,255,5,29,0,0,255,256,5,30,0,0,256,318,6,19,-1,0,257,258,
        6,19,-1,0,258,259,5,16,0,0,259,260,5,38,0,0,260,261,5,16,0,0,261,
        262,5,29,0,0,262,263,5,30,0,0,263,318,6,19,-1,0,264,265,6,19,-1,
        0,265,266,5,16,0,0,266,267,5,38,0,0,267,268,5,16,0,0,268,269,5,29,
        0,0,269,270,3,62,31,0,270,271,5,30,0,0,271,272,6,19,-1,0,272,318,
        1,0,0,0,273,274,6,19,-1,0,274,275,5,16,0,0,275,276,5,38,0,0,276,
        277,5,16,0,0,277,278,5,38,0,0,278,279,5,16,0,0,279,280,5,29,0,0,
        280,281,5,30,0,0,281,318,6,19,-1,0,282,283,6,19,-1,0,283,284,5,16,
        0,0,284,285,5,38,0,0,285,286,5,16,0,0,286,287,5,38,0,0,287,288,5,
        16,0,0,288,289,5,29,0,0,289,290,3,62,31,0,290,291,5,30,0,0,291,292,
        6,19,-1,0,292,318,1,0,0,0,293,294,6,19,-1,0,294,295,5,16,0,0,295,
        296,5,38,0,0,296,297,5,16,0,0,297,298,5,38,0,0,298,299,5,16,0,0,
        299,300,5,38,0,0,300,301,5,16,0,0,301,302,5,29,0,0,302,303,5,30,
        0,0,303,318,6,19,-1,0,304,305,6,19,-1,0,305,306,5,16,0,0,306,307,
        5,38,0,0,307,308,5,16,0,0,308,309,5,38,0,0,309,310,5,16,0,0,310,
        311,5,38,0,0,311,312,5,16,0,0,312,313,5,29,0,0,313,314,3,62,31,0,
        314,315,5,30,0,0,315,316,6,19,-1,0,316,318,1,0,0,0,317,245,1,0,0,
        0,317,252,1,0,0,0,317,257,1,0,0,0,317,264,1,0,0,0,317,273,1,0,0,
        0,317,282,1,0,0,0,317,293,1,0,0,0,317,304,1,0,0,0,318,39,1,0,0,0,
        319,320,6,20,-1,0,320,321,3,46,23,0,321,322,3,48,24,0,322,323,3,
        42,21,0,323,324,5,3,0,0,324,325,6,20,-1,0,325,41,1,0,0,0,326,327,
        3,44,22,0,327,328,3,48,24,0,328,329,6,21,-1,0,329,332,1,0,0,0,330,
        332,1,0,0,0,331,326,1,0,0,0,331,330,1,0,0,0,332,43,1,0,0,0,333,334,
        5,2,0,0,334,335,6,22,-1,0,335,45,1,0,0,0,336,337,5,1,0,0,337,338,
        5,29,0,0,338,339,3,50,25,0,339,340,5,30,0,0,340,341,6,23,-1,0,341,
        47,1,0,0,0,342,343,5,35,0,0,343,344,3,32,16,0,344,345,5,36,0,0,345,
        49,1,0,0,0,346,347,3,62,31,0,347,348,3,52,26,0,348,349,3,62,31,0,
        349,350,6,25,-1,0,350,51,1,0,0,0,351,352,7,0,0,0,352,53,1,0,0,0,
        353,354,5,4,0,0,354,355,5,29,0,0,355,356,5,21,0,0,356,357,5,30,0,
        0,357,358,6,27,-1,0,358,55,1,0,0,0,359,360,6,28,-1,0,360,361,3,58,
        29,0,361,362,3,48,24,0,362,363,6,28,-1,0,363,57,1,0,0,0,364,365,
        6,29,-1,0,365,366,5,10,0,0,366,367,6,29,-1,0,367,368,5,29,0,0,368,
        369,3,50,25,0,369,370,5,30,0,0,370,371,5,11,0,0,371,372,6,29,-1,
        0,372,59,1,0,0,0,373,379,5,7,0,0,374,379,5,8,0,0,375,379,5,9,0,0,
        376,377,5,16,0,0,377,379,6,30,-1,0,378,373,1,0,0,0,378,374,1,0,0,
        0,378,375,1,0,0,0,378,376,1,0,0,0,379,61,1,0,0,0,380,381,6,31,-1,
        0,381,382,3,64,32,0,382,395,1,0,0,0,383,384,10,3,0,0,384,385,5,24,
        0,0,385,386,3,64,32,0,386,387,6,31,-1,0,387,394,1,0,0,0,388,389,
        10,2,0,0,389,390,5,25,0,0,390,391,3,64,32,0,391,392,6,31,-1,0,392,
        394,1,0,0,0,393,383,1,0,0,0,393,388,1,0,0,0,394,397,1,0,0,0,395,
        393,1,0,0,0,395,396,1,0,0,0,396,63,1,0,0,0,397,395,1,0,0,0,398,399,
        6,32,-1,0,399,400,3,66,33,0,400,413,1,0,0,0,401,402,10,3,0,0,402,
        403,5,28,0,0,403,404,3,66,33,0,404,405,6,32,-1,0,405,412,1,0,0,0,
        406,407,10,2,0,0,407,408,5,27,0,0,408,409,3,66,33,0,409,410,6,32,
        -1,0,410,412,1,0,0,0,411,401,1,0,0,0,411,406,1,0,0,0,412,415,1,0,
        0,0,413,411,1,0,0,0,413,414,1,0,0,0,414,65,1,0,0,0,415,413,1,0,0,
        0,416,432,3,68,34,0,417,418,5,25,0,0,418,419,5,18,0,0,419,432,6,
        33,-1,0,420,421,5,19,0,0,421,432,6,33,-1,0,422,423,5,20,0,0,423,
        432,6,33,-1,0,424,425,5,25,0,0,425,426,5,20,0,0,426,432,6,33,-1,
        0,427,428,5,18,0,0,428,432,6,33,-1,0,429,430,5,17,0,0,430,432,6,
        33,-1,0,431,416,1,0,0,0,431,417,1,0,0,0,431,420,1,0,0,0,431,422,
        1,0,0,0,431,424,1,0,0,0,431,427,1,0,0,0,431,429,1,0,0,0,432,67,1,
        0,0,0,433,434,5,16,0,0,434,435,6,34,-1,0,435,436,3,70,35,0,436,437,
        6,34,-1,0,437,440,1,0,0,0,438,440,3,72,36,0,439,433,1,0,0,0,439,
        438,1,0,0,0,440,69,1,0,0,0,441,442,5,25,0,0,442,443,5,25,0,0,443,
        446,6,35,-1,0,444,446,1,0,0,0,445,441,1,0,0,0,445,444,1,0,0,0,446,
        71,1,0,0,0,447,448,5,16,0,0,448,449,5,38,0,0,449,450,5,16,0,0,450,
        466,6,36,-1,0,451,452,5,16,0,0,452,453,5,38,0,0,453,454,5,16,0,0,
        454,455,5,38,0,0,455,456,5,16,0,0,456,466,6,36,-1,0,457,458,5,16,
        0,0,458,459,5,38,0,0,459,460,5,16,0,0,460,461,5,38,0,0,461,462,5,
        16,0,0,462,463,5,38,0,0,463,464,5,16,0,0,464,466,6,36,-1,0,465,447,
        1,0,0,0,465,451,1,0,0,0,465,457,1,0,0,0,466,73,1,0,0,0,25,82,88,
        90,105,119,143,154,160,177,185,187,207,228,243,317,331,378,393,395,
        411,413,431,439,445,465
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
    RULE_declaracion_clase = 10
    RULE_encabezado_clase = 11
    RULE_componentes_clase = 12
    RULE_componente_var = 13
    RULE_componente_func = 14
    RULE_componente_herencia = 15
    RULE_cuerpo_ejecucion = 16
    RULE_ejecucion = 17
    RULE_asignacion = 18
    RULE_invocacion = 19
    RULE_seleccion = 20
    RULE_posible_else = 21
    RULE_else = 22
    RULE_if_condicion = 23
    RULE_bloque_control = 24
    RULE_condicion = 25
    RULE_comparador = 26
    RULE_print = 27
    RULE_while = 28
    RULE_while_condicion = 29
    RULE_tipo = 30
    RULE_expresion = 31
    RULE_termino = 32
    RULE_factor = 33
    RULE_referencia = 34
    RULE_posible_guion_doble = 35
    RULE_uso_clase = 36

    ruleNames =  [ "programa", "cuerpo", "declaracion", "declaracion_var", 
                   "lista_variable", "declaracion_func", "encabezado_funcion", 
                   "parametro", "cuerpo_func", "ejecucion_retorno", "declaracion_clase", 
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
        self.auxAnterior = 0
        self.flag = 0
        self.error = False
        self.errorCondicion = False
        self.flagCondicion = 0
        self.herenciasFoward = {}

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
            self.state = 74
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 75
            self.cuerpo(0)
            self.state = 76
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
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 80
                self.declaracion()
                pass

            elif la_ == 2:
                self.state = 81
                self.ejecucion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 88
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 84
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 85
                        self.declaracion()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 86
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 87
                        self.ejecucion()
                        pass

             
                self.state = 92
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
            self._ERROR = None # Token

        def declaracion_var(self):
            return self.getTypedRuleContext(gramaticaprueba.Declaracion_varContext,0)


        def declaracion_func(self):
            return self.getTypedRuleContext(gramaticaprueba.Declaracion_funcContext,0)


        def declaracion_clase(self):
            return self.getTypedRuleContext(gramaticaprueba.Declaracion_claseContext,0)


        def ERROR(self):
            return self.getToken(gramaticaprueba.ERROR, 0)

        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_declaracion




    def declaracion(self):

        localctx = gramaticaprueba.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                localctx._declaracion_var = self.declaracion_var()

                for key in self.listaVar:
                    if localctx._declaracion_var.t in ["INT","FLOAT","ULONG"]:
                        self.declaracionesVariables[key+self.ambitoActual] = localctx._declaracion_var.line
                self.listaVar = []

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.declaracion_func()

                            
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.declaracion_clase()


                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                localctx._ERROR = self.match(gramaticaprueba.ERROR)
                self.state = 103
                self.match(gramaticaprueba.COMMA)
                self.yyerror("SINTACTICO: error en declaración", (0 if localctx._ERROR is None else localctx._ERROR.line))
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
            self.state = 107
            localctx._tipo = self.tipo()
            self.state = 108
            localctx._lista_variable = self.lista_variable()
            self.state = 109
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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                localctx._ID = self.match(gramaticaprueba.ID)

                self.listaVar.append((None if localctx._ID is None else localctx._ID.text))
                localctx.line = (0 if localctx._ID is None else localctx._ID.line)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 115
                self.match(gramaticaprueba.SEMICOLON)
                self.state = 116
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
            self._cuerpo_func = None # Cuerpo_funcContext

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
            self.state = 121
            localctx._encabezado_funcion = self.encabezado_funcion()

            if self.inFuncion and self.inClase:
                self.segundaFuncion = True
            if (not self.inClase) or (not self.inFuncion):
                self.polacaInversa.addElemento(('FUNCION' + ' ' + localctx._encabezado_funcion.funcion))

            self.state = 123
            self.parametro()
            self.state = 124
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 125
            localctx._cuerpo_func = self.cuerpo_func()
            self.state = 126
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.state = 127
            self.match(gramaticaprueba.COMMA)

            self.reducirAmbito()
            if self.segundaFuncion:
                while self.polacaInversa.reference_counter > self.auxBorrado:
                    self.polacaInversa.removeLast()
            self.inFuncion = False
            if localctx._cuerpo_func.faltaRetorno:
                self.yyerror("SINTACTICO: falta sentencia RETURN en funcion "+localctx._encabezado_funcion.funcion,localctx._encabezado_funcion.line)

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
            self.line = None
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
            self.state = 130
            self.match(gramaticaprueba.VOID)
            self.state = 131
            localctx._ID = self.match(gramaticaprueba.ID)

            if self.inClase and self.inFuncion:
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
            localctx.line = (0 if localctx._ID is None else localctx._ID.line)

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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 135
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.addCaracteristica(self.auxIDFunc, "nroParametros", "0")

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 138
                localctx._tipo = self.tipo()
                self.state = 139
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 140
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.addCaracteristica(self.auxIDFunc, "tipoParametro", (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))
                self.simbolos.addCaracteristica(self.auxIDFunc, "nroParametros", "1")
                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual, "tipo", (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))
                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual, "uso", "parametro")
                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual, "funcion_padre", self.auxIDFunc)

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
            self.faltaRetorno = None
            self._ejecucion_retorno = None # Ejecucion_retornoContext

        def cuerpo(self):
            return self.getTypedRuleContext(gramaticaprueba.CuerpoContext,0)


        def ejecucion_retorno(self):
            return self.getTypedRuleContext(gramaticaprueba.Ejecucion_retornoContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_cuerpo_func




    def cuerpo_func(self):

        localctx = gramaticaprueba.Cuerpo_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cuerpo_func)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 4, 5, 6, 7, 8, 9, 10, 16, 17]:
                self.enterOuterAlt(localctx, 1)
                self.inFuncion = True
                self.state = 146
                self.cuerpo(0)
                self.state = 147
                localctx._ejecucion_retorno = self.ejecucion_retorno()

                localctx.faltaRetorno = localctx._ejecucion_retorno.faltaRet

                pass
            elif token in [12, 36]:
                self.enterOuterAlt(localctx, 2)
                self.inFuncion = True
                self.state = 151
                localctx._ejecucion_retorno = self.ejecucion_retorno()

                localctx.faltaRetorno = localctx._ejecucion_retorno.faltaRet

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


    class Ejecucion_retornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.faltaRet = None

        def RETURN(self):
            return self.getToken(gramaticaprueba.RETURN, 0)

        def COMMA(self):
            return self.getToken(gramaticaprueba.COMMA, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_ejecucion_retorno




    def ejecucion_retorno(self):

        localctx = gramaticaprueba.Ejecucion_retornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ejecucion_retorno)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(gramaticaprueba.RETURN)
                self.state = 157
                self.match(gramaticaprueba.COMMA)

                self.polacaInversa.addElemento("ret")
                localctx.faltaRet = False
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)

                self.polacaInversa.addElemento("ret")
                localctx.faltaRet = True
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


    class Declaracion_claseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._encabezado_clase = None # Encabezado_claseContext

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
        self.enterRule(localctx, 20, self.RULE_declaracion_clase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            localctx._encabezado_clase = self.encabezado_clase()
            self.state = 163
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 164
            self.componentes_clase(0)
            self.state = 165
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.state = 166
            self.match(gramaticaprueba.COMMA)

            self.reducirAmbito()
            self.inClase = False
            clase = ""
            if self.getIdSinAmbito(self.auxIDClass) in self.herenciasFoward.values():
                for key in self.herenciasFoward:
                    if self.herenciasFoward[key] == self.getIdSinAmbito(self.auxIDClass):
                        identificador = key
                        herenciasActuales = self.simbolos.getCaracteristica(identificador, "numero de herencias")
                        if isinstance(herenciasActuales, int):
                            if herenciasActuales < 2:
                                self.simbolos.aumentarReferencia(identificador)
                                self.simbolos.addCaracteristica(identificador, "numero de herencias", herenciasActuales + 1)
                                self.simbolos.addCaracteristica(identificador, "clase herencia", self.auxIDClass)
                                propiedades = self.simbolos.getCaracteristica(self.auxIDClass, "propiedades")
                                if isinstance(propiedades, list):
                                    self.simbolos.addCaracteristica(identificador, "propiedades heredadas", propiedades)
                            else:
                                self.yyerror("SEMANTICO: se exeden los niveles de herencia", localctx._encabezado_clase.line)
                        else:
                            self.simbolos.addCaracteristica(identificador, "numero de herencias", 1)
                            self.simbolos.addCaracteristica(identificador, "clase herencia", self.auxIDClass)
                            propiedades = self.simbolos.getCaracteristica(self.auxIDClass, "propiedades")
                            if isinstance(propiedades, list):
                                self.simbolos.addCaracteristica(identificador, "propiedades heredadas", propiedades)

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
            self.line = None
            self._ID = None # Token

        def CLASS(self):
            return self.getToken(gramaticaprueba.CLASS, 0)

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_encabezado_clase




    def encabezado_clase(self):

        localctx = gramaticaprueba.Encabezado_claseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_encabezado_clase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(gramaticaprueba.CLASS)
            self.state = 170
            localctx._ID = self.match(gramaticaprueba.ID)

            self.auxIDClass = (None if localctx._ID is None else localctx._ID.text) + self.ambitoActual
            self.clasesDeclaradas.append((None if localctx._ID is None else localctx._ID.text))
            self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual, "uso", "nombre de clase")
            self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual, "ambito de clase", self.ambitoActual + ":" + (None if localctx._ID is None else localctx._ID.text))
            self.ambitoActual = self.ambitoActual + ":" + (None if localctx._ID is None else localctx._ID.text)
            self.inClase = True
            localctx.line = (0 if localctx._ID is None else localctx._ID.line)

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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_componentes_clase, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 174
                self.componente_var()
                pass

            elif la_ == 2:
                self.state = 175
                self.componente_func()
                pass

            elif la_ == 3:
                self.state = 176
                self.componente_herencia()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 185
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 179
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 180
                        self.componente_var()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 181
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 182
                        self.componente_func()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 183
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 184
                        self.componente_herencia()
                        pass

             
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_componente_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
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
        self.enterRule(localctx, 28, self.RULE_componente_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.declaracion_func()

            componentesActuales = self.simbolos.getCaracteristica(self.auxIDClass, "miembros de clase")
            componentesActuales = self.simbolos.getCaracteristica(self.auxIDClass, "miembros")
            if isinstance(componentesActuales, list):
                componentesActuales.append(self.auxIDFunc[:self.auxIDFunc.find(":")])
                componentes = [self.auxIDFunc.replace(":","_")]
            else:
                componentesActuales = [self.auxIDFunc[:self.auxIDFunc.find(":")]]
                componentes = [self.auxIDFunc.replace(":","_")]
                self.simbolos.addCaracteristica(self.auxIDClass, "miembros de clase", componentesActuales)
                self.simbolos.addCaracteristica(self.auxIDClass, "miembros", componentes)

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
        self.enterRule(localctx, 30, self.RULE_componente_herencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            localctx._ID = self.match(gramaticaprueba.ID)
            self.state = 197
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
                self.herenciasFoward[self.auxIDClass] = (None if localctx._ID is None else localctx._ID.text)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_cuerpo_ejecucion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.ejecucion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaprueba.Cuerpo_ejecucionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo_ejecucion)
                    self.state = 203
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 204
                    self.ejecucion() 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_ejecucion)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.asignacion()
                self.state = 211
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.invocacion()
                self.state = 214
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.seleccion()
                self.state = 217
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.print_()
                self.state = 220
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                self.while_()
                self.state = 223
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 225
                localctx._ERROR = self.match(gramaticaprueba.ERROR)
                self.state = 226
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
        self.enterRule(localctx, 36, self.RULE_asignacion)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.flag = self.polacaInversa.reference_counter
                self.state = 231
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 232
                self.match(gramaticaprueba.EQUALS)
                self.state = 233
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
                if self.error is True:
                    while   self.polacaInversa.reference_counter != self.flag:
                        self.polacaInversa.removeLast()
                    self.error = False

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.flag = self.polacaInversa.reference_counter
                self.state = 237
                self.uso_clase()
                self.state = 238
                self.match(gramaticaprueba.EQUALS)
                uso = self.polacaInversa.removeLast()
                self.state = 240
                self.expresion(0)

                self.polacaInversa.addElemento(uso)
                self.polacaInversa.addElemento("=")
                if self.error is True:
                    while   self.polacaInversa.reference_counter != self.flag:
                        self.polacaInversa.removeLast()
                    self.error = False

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
        self.enterRule(localctx, 38, self.RULE_invocacion)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.flag = self.polacaInversa.reference_counter
                self.state = 246
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 247
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 248
                self.expresion(0)
                self.state = 249
                self.match(gramaticaprueba.RIGHT_PAREN)

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    if self.simbolos.getCaracteristica(identificador, "uso") == "funcion":
                        if self.simbolos.getCaracteristica(identificador, "nroParametros") == "1":
                            self.simbolos.aumentarReferencia(identificador)
                            aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + identificador)
                            self.polacaInversa.addElemento(aux)
                            self.polacaInversa.addElemento("CALLFUNCP")
                        else:
                            self.yyerror("SEMANTICO: numero incorrecto de parametros", (0 if localctx._ID is None else localctx._ID.line))
                    else:
                        self.yyerror("SEMANTICO: identificador no es una funcion", (0 if localctx._ID is None else localctx._ID.line))
                else:
                    self.yyerror("SEMANTICO: funcion no declarada en un ambito valido", (0 if localctx._ID is None else localctx._ID.line))
                if self.error is True:
                    while   self.polacaInversa.reference_counter != self.flag:
                        self.polacaInversa.removeLast()
                    self.error = False

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.flag = self.polacaInversa.reference_counter
                self.state = 253
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 254
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 255
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
                if self.error is True:
                    while   self.polacaInversa.reference_counter != self.flag:
                        self.polacaInversa.removeLast()
                    self.error = False

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.flag = self.polacaInversa.reference_counter
                self.state = 258
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 259
                self.match(gramaticaprueba.DOT)
                self.state = 260
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 261
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 262
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
                            self.polacaInversa.addElemento(aux)
                            self.polacaInversa.addElemento("CALLFUNC")
                        else:
                            self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrado en clase " + claseAmbito, (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))
                if self.error is True:
                    while   self.polacaInversa.reference_counter != self.flag:
                        self.polacaInversa.removeLast()
                    self.error = False

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.flag = self.polacaInversa.reference_counter
                self.state = 265
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 266
                self.match(gramaticaprueba.DOT)
                self.state = 267
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 268
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 269
                self.expresion(0)
                self.state = 270
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
                            self.polacaInversa.addElemento(aux)
                            self.polacaInversa.addElemento("CALLFUNCP")
                        else:
                            self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrado en clase " + claseAmbito, (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))
                if self.error is True:
                    while   self.polacaInversa.reference_counter != self.flag:
                        self.polacaInversa.removeLast()
                    self.error = False

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.flag = self.polacaInversa.reference_counter
                self.state = 274
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 275
                self.match(gramaticaprueba.DOT)
                self.state = 276
                localctx.herencia = self.match(gramaticaprueba.ID)
                self.state = 277
                self.match(gramaticaprueba.DOT)
                self.state = 278
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 279
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 280
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
                if self.error is True:
                    while   self.polacaInversa.reference_counter != self.flag:
                        self.polacaInversa.removeLast()
                    self.error = False

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.flag = self.polacaInversa.reference_counter
                self.state = 283
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 284
                self.match(gramaticaprueba.DOT)
                self.state = 285
                localctx.herencia = self.match(gramaticaprueba.ID)
                self.state = 286
                self.match(gramaticaprueba.DOT)
                self.state = 287
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 288
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 289
                self.expresion(0)
                self.state = 290
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
                                self.polacaInversa.addElemento("CALLFUNCP")
                            else:
                                self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                        else:
                            self.yyerror("SEMANTICO: " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrado en clase " + (None if localctx.herencia is None else localctx.herencia.text), (0 if localctx.clase is None else localctx.clase.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.clase is None else localctx.clase.text) + " no hereda de " + (None if localctx.herencia is None else localctx.herencia.text), (0 if localctx.clase is None else localctx.clase.line))
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))
                if self.error is True:
                    while   self.polacaInversa.reference_counter != self.flag:
                        self.polacaInversa.removeLast()
                    self.error = False

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.flag = self.polacaInversa.reference_counter
                self.state = 294
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 295
                self.match(gramaticaprueba.DOT)
                self.state = 296
                localctx.herencia1 = self.match(gramaticaprueba.ID)
                self.state = 297
                self.match(gramaticaprueba.DOT)
                self.state = 298
                localctx.herencia2 = self.match(gramaticaprueba.ID)
                self.state = 299
                self.match(gramaticaprueba.DOT)
                self.state = 300
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 301
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 302
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
                if self.error is True:
                    while   self.polacaInversa.reference_counter != self.flag:
                        self.polacaInversa.removeLast()
                    self.error = False

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.flag = self.polacaInversa.reference_counter
                self.state = 305
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 306
                self.match(gramaticaprueba.DOT)
                self.state = 307
                localctx.herencia1 = self.match(gramaticaprueba.ID)
                self.state = 308
                self.match(gramaticaprueba.DOT)
                self.state = 309
                localctx.herencia2 = self.match(gramaticaprueba.ID)
                self.state = 310
                self.match(gramaticaprueba.DOT)
                self.state = 311
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 312
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 313
                self.expresion(0)
                self.state = 314
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
                                    self.polacaInversa.addElemento("CALLFUNCP")
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
                if self.error is True:
                    while   self.polacaInversa.reference_counter != self.flag:
                        self.polacaInversa.removeLast()
                    self.error = False

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
        self.enterRule(localctx, 40, self.RULE_seleccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.flagCondicion = self.polacaInversa.reference_counter

            self.state = 320
            self.if_condicion()
            self.state = 321
            self.bloque_control()
            self.state = 322
            self.posible_else()
            self.state = 323
            self.match(gramaticaprueba.END_IF)

            if self.elseaux is False:
                number = self.polacaInversa.getLastPendingStep()
                self.polacaInversa.setElemento(number)
            else:
                self.elseaux = False
            if self.errorCondicion is True:
                while   self.polacaInversa.reference_counter != self.flagCondicion:
                    self.polacaInversa.removeLast()
                self.errorCondicion = False

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
        self.enterRule(localctx, 42, self.RULE_posible_else)
        try:
            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.else_()
                self.state = 327
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
        self.enterRule(localctx, 44, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
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
        self.enterRule(localctx, 46, self.RULE_if_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(gramaticaprueba.IF)
            self.state = 337
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 338
            self.condicion()
            self.state = 339
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
        self.enterRule(localctx, 48, self.RULE_bloque_control)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 343
            self.cuerpo_ejecucion(0)
            self.state = 344
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
        self.enterRule(localctx, 50, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.expresion(0)
            self.state = 347
            localctx._comparador = self.comparador()
            self.state = 348
            self.expresion(0)

            self.polacaInversa.addElemento((None if localctx._comparador is None else self._input.getText(localctx._comparador.start,localctx._comparador.stop)))
            if self.error is True:
                self.errorCondicion = True
                self.error = False

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
        self.enterRule(localctx, 52, self.RULE_comparador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
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
        self.enterRule(localctx, 54, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(gramaticaprueba.PRINT)
            self.state = 354
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 355
            localctx._CADENA = self.match(gramaticaprueba.CADENA)
            self.state = 356
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
        self.enterRule(localctx, 56, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.flagCondicion = self.polacaInversa.reference_counter
            self.state = 360
            self.while_condicion()
            self.state = 361
            self.bloque_control()

            number = self.polacaInversa.getLastPendingStep()
            self.polacaInversa.addElemento(self.aux)
            self.polacaInversa.addElemento("BI")
            self.aux = self.auxAnterior
            self.polacaInversa.setElemento(number)
            if self.errorCondicion is True:
                while   self.polacaInversa.reference_counter != self.flagCondicion:
                    self.polacaInversa.removeLast()
                self.errorCondicion = False

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
        self.enterRule(localctx, 58, self.RULE_while_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.auxAnterior = self.aux
            self.aux = self.polacaInversa.reference_counter

            self.state = 365
            self.match(gramaticaprueba.WHILE)
            self.polacaInversa.addElemento("TAG"+str(self.aux))
            self.state = 367
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 368
            self.condicion()
            self.state = 369
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 370
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
        self.enterRule(localctx, 60, self.RULE_tipo)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(gramaticaprueba.INT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(gramaticaprueba.ULONG)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.match(gramaticaprueba.FLOAT)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 376
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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 393
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 383
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 384
                        self.match(gramaticaprueba.PLUS)
                        self.state = 385
                        self.termino(0)
                        self.polacaInversa.addElemento("+")
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 388
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 389
                        self.match(gramaticaprueba.MINUS)
                        self.state = 390
                        self.termino(0)
                        self.polacaInversa.addElemento("-")
                        pass

             
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_termino, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 413
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 411
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 401
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 402
                        self.match(gramaticaprueba.MULTIPLY)
                        self.state = 403
                        self.factor()
                        self.polacaInversa.addElemento("*")
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 406
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 407
                        self.match(gramaticaprueba.DIVIDE)
                        self.state = 408
                        self.factor()
                        self.polacaInversa.addElemento("/")
                        pass

             
                self.state = 415
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 66, self.RULE_factor)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.referencia()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(gramaticaprueba.MINUS)
                self.state = 418
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                text = "_".join(reversed((None if localctx._NUM_INT is None else localctx._NUM_INT.text).split("_")))
                key = text
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove(key)
                    else:
                        self.simbolos.reducirReferencia(key)
                self.simbolos.addSimbolo("-" + text)
                self.simbolos.addCaracteristica("-" + text, "tipo", "INT")
                self.simbolos.addCaracteristica("-" + text, "valor", self.getValor("-" + text))
                self.simbolos.addCaracteristica("-" + text, "uso","constante")
                self.polacaInversa.addElemento(text)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 420
                localctx._NUM_ULONG = self.match(gramaticaprueba.NUM_ULONG)

                texto = (None if localctx._NUM_ULONG is None else localctx._NUM_ULONG.text)
                text = "_".join(reversed(texto.split("_")))
                self.simbolos.addCaracteristica(text, "tipo", "ULONG")
                self.simbolos.addCaracteristica(text, "valor", self.getValor(text))
                self.simbolos.addCaracteristica(text, "uso","constante")
                self.polacaInversa.addElemento(text)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 422
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                guion = (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text).replace(".","_")
                guion = guion.replace("+","")
                self.simbolos.addCaracteristica("f"+guion, "tipo", "FLOAT")
                self.simbolos.addCaracteristica("f"+guion, "uso","constante")
                aux = float((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))
                self.simbolos.addCaracteristica("f"+guion, "valor",str(aux).replace("+",""))
                self.polacaInversa.addElemento("f"+guion)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 424
                self.match(gramaticaprueba.MINUS)
                self.state = 425
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                key = (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text)
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove(key)
                    else:
                        self.simbolos.reducirReferencia(key)
                guion = (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text).replace(".","_")
                guion = guion.replace("-","_")
                self.simbolos.addSimbolo("f_" + guion)
                aux = float((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))
                self.simbolos.addCaracteristica("f_" + guion, "valor", str("-" + aux))
                self.polacaInversa.addElemento("f_"+guion)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 427
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                text = "_".join(reversed((None if localctx._NUM_INT is None else localctx._NUM_INT.text).split("_")))
                if text == "i_32768":
                    self.yyerror("LEXICO: INT fuera de rango",(0 if localctx._NUM_INT is None else localctx._NUM_INT.line))
                else:
                    texto = text
                    self.simbolos.addCaracteristica(texto, "tipo", "INT")
                    self.simbolos.addCaracteristica(texto, "valor", self.getValor(texto))
                    self.simbolos.addCaracteristica(texto, "uso","constante")
                    self.polacaInversa.addElemento(texto)

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 429
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
        self.enterRule(localctx, 68, self.RULE_referencia)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                localctx._ID = self.match(gramaticaprueba.ID)

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    self.polacaInversa.addElemento(identificador)
                self.state = 435
                self.posible_guion_doble()

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    self.simbolos.aumentarReferencia(identificador)
                    if (self.menos_menos is True):
                        aux = self.simbolos.getCaracteristica(identificador,"tipo")
                        if aux == "INT":
                            text = "_".join(reversed("1_i".split("_")))
                            self.simbolos.addSimbolo(text)
                            self.polacaInversa.addElemento(text)
                            self.simbolos.addCaracteristica(text, "tipo", "INT")
                            self.simbolos.addCaracteristica(text, "valor", 1)
                            self.simbolos.addCaracteristica(text, "uso","constante")
                        elif aux == "ULONG":
                            text = "_".join(reversed("1_ul".split("_")))
                            self.simbolos.addSimbolo(text)
                            self.polacaInversa.addElemento(text)
                            self.simbolos.addCaracteristica(text, "tipo", "ULONG")
                            self.simbolos.addCaracteristica(text, "valor", 1)
                            self.simbolos.addCaracteristica(text, "uso","constante")
                        elif aux == "FLOAT":
                            text = "1.0"
                            self.simbolos.addSimbolo(text)
                            self.polacaInversa.addElemento(text)
                            self.simbolos.addCaracteristica(text, "tipo", "FLOAT")
                            self.simbolos.addCaracteristica(text, "valor", 1.0)
                            self.simbolos.addCaracteristica(text, "uso","constante")

                        self.polacaInversa.addElemento("-")
                        self.polacaInversa.addElemento(identificador)
                        self.polacaInversa.addElemento('=')
                        self.polacaInversa.addElemento(identificador)
                        self.menos_menos = False
                else:
                    self.yyerror("SEMANTICO: id " + (None if localctx._ID is None else localctx._ID.text) + " no existe en un ambito valido", (0 if localctx._ID is None else localctx._ID.line))
                    self.error = True


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
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
        self.enterRule(localctx, 70, self.RULE_posible_guion_doble)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(gramaticaprueba.MINUS)
                self.state = 442
                self.match(gramaticaprueba.MINUS)

                self.menos_menos = True

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
        self.enterRule(localctx, 72, self.RULE_uso_clase)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 448
                self.match(gramaticaprueba.DOT)
                self.state = 449
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
                        self.error = True
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))
                    self.error = True

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 452
                self.match(gramaticaprueba.DOT)
                self.state = 453
                localctx.herencia = self.match(gramaticaprueba.ID)
                self.state = 454
                self.match(gramaticaprueba.DOT)
                self.state = 455
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
                            clase = (None if localctx.clase is None else localctx.clase.text) + self.ambitoActual + "." + (None if localctx.herencia is None else localctx.herencia.text) + "_" + "." + (None if localctx.atributo is None else localctx.atributo.text)
                            self.polacaInversa.addElemento(str(clase))
                        else:
                            self.yyerror("SEMANTICO: propiedad " + (None if localctx.atributo is None else localctx.atributo.text) + " no encontrada en clase " + claseHerencia, (0 if localctx.clase is None else localctx.clase.line))
                            self.error = True
                    else:
                        self.yyerror("SEMANTICO: clase " + idClase + " no hereda de " + (None if localctx.herencia is None else localctx.herencia.text), (0 if localctx.clase is None else localctx.clase.line))
                        self.error = True
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))
                    self.error = True

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 458
                self.match(gramaticaprueba.DOT)
                self.state = 459
                localctx.herencia1 = self.match(gramaticaprueba.ID)
                self.state = 460
                self.match(gramaticaprueba.DOT)
                self.state = 461
                localctx.herencia2 = self.match(gramaticaprueba.ID)
                self.state = 462
                self.match(gramaticaprueba.DOT)
                self.state = 463
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
                                clase = (None if localctx.clase is None else localctx.clase.text) + self.ambitoActual + "." + (None if localctx.herencia1 is None else localctx.herencia1.text) + "_" + "." + (None if localctx.herencia2 is None else localctx.herencia2.text) + "_" + "." + (None if localctx.atributo is None else localctx.atributo.text)
                                self.polacaInversa.addElemento(str(clase))
                            else:
                                self.yyerror("SEMANTICO: propiedad " + (None if localctx.atributo is None else localctx.atributo.text) + " no encontrada en clase " + claseHerencia, (0 if localctx.clase is None else localctx.clase.line))
                                self.error = True
                        else:
                            self.yyerror("SEMANTICO: clase " + (None if localctx.herencia1 is None else localctx.herencia1.text) + " no hereda de " + (None if localctx.herencia2 is None else localctx.herencia2.text), (0 if localctx.clase is None else localctx.clase.line))
                            self.error = True
                    else:
                        self.yyerror("SEMANTICO: clase " + idClase + " no hereda de " + (None if localctx.herencia1 is None else localctx.herencia1.text), (0 if localctx.clase is None else localctx.clase.line))
                        self.error = True
                else:
                    self.yyerror("SEMANTICO: variable " + (None if localctx.clase is None else localctx.clase.text) + "no fue declarada en un ambito valido", (0 if localctx.clase is None else localctx.clase.line))
                    self.error = True

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
        self._predicates[12] = self.componentes_clase_sempred
        self._predicates[16] = self.cuerpo_ejecucion_sempred
        self._predicates[31] = self.expresion_sempred
        self._predicates[32] = self.termino_sempred
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
         




