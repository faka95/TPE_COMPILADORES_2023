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
        4,1,39,485,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,93,8,1,1,
        1,1,1,1,1,1,1,5,1,99,8,1,10,1,12,1,102,9,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,113,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,127,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,151,8,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,3,8,160,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,3,9,174,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,3,10,200,8,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,213,8,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,228,8,12,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,
        257,8,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,265,8,16,10,16,12,16,
        268,9,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,
        1,20,1,20,1,20,1,20,5,20,285,8,20,10,20,12,20,288,9,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,313,8,21,1,22,1,22,
        1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,3,23,344,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,
        1,25,1,25,3,25,357,8,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,3,34,402,8,34,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,5,35,
        417,8,35,10,35,12,35,420,9,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,5,36,435,8,36,10,36,12,36,438,9,36,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,37,1,37,3,37,455,8,37,1,38,1,38,1,38,1,38,1,38,1,38,3,38,463,8,
        38,1,39,1,39,1,39,1,39,3,39,469,8,39,1,40,1,40,1,40,1,40,1,40,1,
        41,1,41,1,41,1,41,1,41,1,41,1,41,3,41,483,8,41,1,41,0,5,2,32,40,
        70,72,42,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,
        0,1,3,0,13,15,22,22,31,32,490,0,84,1,0,0,0,2,92,1,0,0,0,4,112,1,
        0,0,0,6,114,1,0,0,0,8,126,1,0,0,0,10,128,1,0,0,0,12,137,1,0,0,0,
        14,150,1,0,0,0,16,159,1,0,0,0,18,173,1,0,0,0,20,199,1,0,0,0,22,212,
        1,0,0,0,24,227,1,0,0,0,26,229,1,0,0,0,28,241,1,0,0,0,30,248,1,0,
        0,0,32,256,1,0,0,0,34,269,1,0,0,0,36,272,1,0,0,0,38,275,1,0,0,0,
        40,279,1,0,0,0,42,312,1,0,0,0,44,314,1,0,0,0,46,343,1,0,0,0,48,345,
        1,0,0,0,50,356,1,0,0,0,52,358,1,0,0,0,54,361,1,0,0,0,56,367,1,0,
        0,0,58,371,1,0,0,0,60,376,1,0,0,0,62,378,1,0,0,0,64,384,1,0,0,0,
        66,388,1,0,0,0,68,401,1,0,0,0,70,403,1,0,0,0,72,421,1,0,0,0,74,454,
        1,0,0,0,76,462,1,0,0,0,78,468,1,0,0,0,80,470,1,0,0,0,82,482,1,0,
        0,0,84,85,5,35,0,0,85,86,3,2,1,0,86,87,5,36,0,0,87,88,6,0,-1,0,88,
        1,1,0,0,0,89,90,6,1,-1,0,90,93,3,4,2,0,91,93,3,42,21,0,92,89,1,0,
        0,0,92,91,1,0,0,0,93,100,1,0,0,0,94,95,10,4,0,0,95,99,3,4,2,0,96,
        97,10,3,0,0,97,99,3,42,21,0,98,94,1,0,0,0,98,96,1,0,0,0,99,102,1,
        0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,3,1,0,0,0,102,100,1,0,0,
        0,103,104,3,6,3,0,104,105,6,2,-1,0,105,113,1,0,0,0,106,107,3,10,
        5,0,107,108,6,2,-1,0,108,113,1,0,0,0,109,110,3,28,14,0,110,111,6,
        2,-1,0,111,113,1,0,0,0,112,103,1,0,0,0,112,106,1,0,0,0,112,109,1,
        0,0,0,113,5,1,0,0,0,114,115,3,68,34,0,115,116,3,8,4,0,116,117,5,
        26,0,0,117,118,6,3,-1,0,118,7,1,0,0,0,119,120,5,16,0,0,120,127,6,
        4,-1,0,121,122,5,16,0,0,122,123,5,33,0,0,123,124,3,8,4,0,124,125,
        6,4,-1,0,125,127,1,0,0,0,126,119,1,0,0,0,126,121,1,0,0,0,127,9,1,
        0,0,0,128,129,3,12,6,0,129,130,6,5,-1,0,130,131,3,14,7,0,131,132,
        5,35,0,0,132,133,3,16,8,0,133,134,5,36,0,0,134,135,5,26,0,0,135,
        136,6,5,-1,0,136,11,1,0,0,0,137,138,5,6,0,0,138,139,5,16,0,0,139,
        140,6,6,-1,0,140,13,1,0,0,0,141,142,5,29,0,0,142,143,5,30,0,0,143,
        151,6,7,-1,0,144,145,5,29,0,0,145,146,3,68,34,0,146,147,5,16,0,0,
        147,148,5,30,0,0,148,149,6,7,-1,0,149,151,1,0,0,0,150,141,1,0,0,
        0,150,144,1,0,0,0,151,15,1,0,0,0,152,153,3,2,1,0,153,154,3,18,9,
        0,154,155,5,26,0,0,155,160,1,0,0,0,156,157,3,18,9,0,157,158,5,26,
        0,0,158,160,1,0,0,0,159,152,1,0,0,0,159,156,1,0,0,0,160,17,1,0,0,
        0,161,174,3,20,10,0,162,163,3,20,10,0,163,164,5,26,0,0,164,165,3,
        18,9,0,165,174,1,0,0,0,166,174,3,26,13,0,167,168,3,26,13,0,168,169,
        5,26,0,0,169,170,3,18,9,0,170,174,1,0,0,0,171,172,5,12,0,0,172,174,
        6,9,-1,0,173,161,1,0,0,0,173,162,1,0,0,0,173,166,1,0,0,0,173,167,
        1,0,0,0,173,171,1,0,0,0,174,19,1,0,0,0,175,176,3,54,27,0,176,177,
        3,22,11,0,177,178,5,3,0,0,178,179,6,10,-1,0,179,200,1,0,0,0,180,
        181,3,54,27,0,181,182,3,22,11,0,182,183,5,2,0,0,183,184,3,56,28,
        0,184,185,5,3,0,0,185,186,6,10,-1,0,186,200,1,0,0,0,187,188,3,54,
        27,0,188,189,3,56,28,0,189,190,3,24,12,0,190,191,5,3,0,0,191,192,
        6,10,-1,0,192,200,1,0,0,0,193,194,3,54,27,0,194,195,3,22,11,0,195,
        196,3,24,12,0,196,197,5,3,0,0,197,198,6,10,-1,0,198,200,1,0,0,0,
        199,175,1,0,0,0,199,180,1,0,0,0,199,187,1,0,0,0,199,193,1,0,0,0,
        200,21,1,0,0,0,201,202,5,35,0,0,202,203,3,18,9,0,203,204,5,26,0,
        0,204,205,5,36,0,0,205,213,1,0,0,0,206,207,5,35,0,0,207,208,3,40,
        20,0,208,209,3,18,9,0,209,210,5,26,0,0,210,211,5,36,0,0,211,213,
        1,0,0,0,212,201,1,0,0,0,212,206,1,0,0,0,213,23,1,0,0,0,214,215,5,
        2,0,0,215,216,5,35,0,0,216,217,3,18,9,0,217,218,5,26,0,0,218,219,
        5,36,0,0,219,228,1,0,0,0,220,221,5,2,0,0,221,222,5,35,0,0,222,223,
        3,40,20,0,223,224,3,18,9,0,224,225,5,26,0,0,225,226,5,36,0,0,226,
        228,1,0,0,0,227,214,1,0,0,0,227,220,1,0,0,0,228,25,1,0,0,0,229,230,
        5,10,0,0,230,231,5,29,0,0,231,232,3,58,29,0,232,233,5,30,0,0,233,
        234,5,11,0,0,234,235,5,35,0,0,235,236,3,40,20,0,236,237,5,12,0,0,
        237,238,5,26,0,0,238,239,5,36,0,0,239,240,6,13,-1,0,240,27,1,0,0,
        0,241,242,3,30,15,0,242,243,5,35,0,0,243,244,3,32,16,0,244,245,5,
        36,0,0,245,246,5,26,0,0,246,247,6,14,-1,0,247,29,1,0,0,0,248,249,
        5,5,0,0,249,250,5,16,0,0,250,251,6,15,-1,0,251,31,1,0,0,0,252,253,
        6,16,-1,0,253,257,3,34,17,0,254,257,3,36,18,0,255,257,3,38,19,0,
        256,252,1,0,0,0,256,254,1,0,0,0,256,255,1,0,0,0,257,266,1,0,0,0,
        258,259,10,3,0,0,259,265,3,34,17,0,260,261,10,2,0,0,261,265,3,36,
        18,0,262,263,10,1,0,0,263,265,3,38,19,0,264,258,1,0,0,0,264,260,
        1,0,0,0,264,262,1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,0,266,267,
        1,0,0,0,267,33,1,0,0,0,268,266,1,0,0,0,269,270,3,6,3,0,270,271,6,
        17,-1,0,271,35,1,0,0,0,272,273,3,10,5,0,273,274,6,18,-1,0,274,37,
        1,0,0,0,275,276,5,16,0,0,276,277,5,26,0,0,277,278,6,19,-1,0,278,
        39,1,0,0,0,279,280,6,20,-1,0,280,281,3,42,21,0,281,286,1,0,0,0,282,
        283,10,2,0,0,283,285,3,42,21,0,284,282,1,0,0,0,285,288,1,0,0,0,286,
        284,1,0,0,0,286,287,1,0,0,0,287,41,1,0,0,0,288,286,1,0,0,0,289,290,
        3,44,22,0,290,291,5,26,0,0,291,292,6,21,-1,0,292,313,1,0,0,0,293,
        294,3,46,23,0,294,295,5,26,0,0,295,296,6,21,-1,0,296,313,1,0,0,0,
        297,298,3,48,24,0,298,299,5,26,0,0,299,300,6,21,-1,0,300,313,1,0,
        0,0,301,302,3,62,31,0,302,303,5,26,0,0,303,304,6,21,-1,0,304,313,
        1,0,0,0,305,306,3,64,32,0,306,307,5,26,0,0,307,308,6,21,-1,0,308,
        313,1,0,0,0,309,310,5,17,0,0,310,311,5,26,0,0,311,313,6,21,-1,0,
        312,289,1,0,0,0,312,293,1,0,0,0,312,297,1,0,0,0,312,301,1,0,0,0,
        312,305,1,0,0,0,312,309,1,0,0,0,313,43,1,0,0,0,314,315,5,16,0,0,
        315,316,5,34,0,0,316,317,3,70,35,0,317,318,6,22,-1,0,318,45,1,0,
        0,0,319,320,5,16,0,0,320,321,5,29,0,0,321,322,3,70,35,0,322,323,
        5,30,0,0,323,324,6,23,-1,0,324,344,1,0,0,0,325,326,5,16,0,0,326,
        327,5,29,0,0,327,328,5,30,0,0,328,344,6,23,-1,0,329,330,5,16,0,0,
        330,331,5,38,0,0,331,332,5,16,0,0,332,333,5,29,0,0,333,334,5,30,
        0,0,334,344,6,23,-1,0,335,336,5,16,0,0,336,337,5,38,0,0,337,338,
        5,16,0,0,338,339,5,29,0,0,339,340,3,70,35,0,340,341,5,30,0,0,341,
        342,6,23,-1,0,342,344,1,0,0,0,343,319,1,0,0,0,343,325,1,0,0,0,343,
        329,1,0,0,0,343,335,1,0,0,0,344,47,1,0,0,0,345,346,3,54,27,0,346,
        347,3,56,28,0,347,348,3,50,25,0,348,349,5,3,0,0,349,350,6,24,-1,
        0,350,49,1,0,0,0,351,352,3,52,26,0,352,353,3,56,28,0,353,354,6,25,
        -1,0,354,357,1,0,0,0,355,357,1,0,0,0,356,351,1,0,0,0,356,355,1,0,
        0,0,357,51,1,0,0,0,358,359,5,2,0,0,359,360,6,26,-1,0,360,53,1,0,
        0,0,361,362,5,1,0,0,362,363,5,29,0,0,363,364,3,58,29,0,364,365,5,
        30,0,0,365,366,6,27,-1,0,366,55,1,0,0,0,367,368,5,35,0,0,368,369,
        3,40,20,0,369,370,5,36,0,0,370,57,1,0,0,0,371,372,3,70,35,0,372,
        373,3,60,30,0,373,374,3,70,35,0,374,375,6,29,-1,0,375,59,1,0,0,0,
        376,377,7,0,0,0,377,61,1,0,0,0,378,379,5,4,0,0,379,380,5,29,0,0,
        380,381,5,21,0,0,381,382,5,30,0,0,382,383,6,31,-1,0,383,63,1,0,0,
        0,384,385,3,66,33,0,385,386,3,56,28,0,386,387,6,32,-1,0,387,65,1,
        0,0,0,388,389,6,33,-1,0,389,390,5,10,0,0,390,391,5,29,0,0,391,392,
        3,58,29,0,392,393,5,30,0,0,393,394,5,11,0,0,394,395,6,33,-1,0,395,
        67,1,0,0,0,396,402,5,7,0,0,397,402,5,8,0,0,398,402,5,9,0,0,399,400,
        5,16,0,0,400,402,6,34,-1,0,401,396,1,0,0,0,401,397,1,0,0,0,401,398,
        1,0,0,0,401,399,1,0,0,0,402,69,1,0,0,0,403,404,6,35,-1,0,404,405,
        3,72,36,0,405,418,1,0,0,0,406,407,10,3,0,0,407,408,5,24,0,0,408,
        409,3,72,36,0,409,410,6,35,-1,0,410,417,1,0,0,0,411,412,10,2,0,0,
        412,413,5,25,0,0,413,414,3,72,36,0,414,415,6,35,-1,0,415,417,1,0,
        0,0,416,406,1,0,0,0,416,411,1,0,0,0,417,420,1,0,0,0,418,416,1,0,
        0,0,418,419,1,0,0,0,419,71,1,0,0,0,420,418,1,0,0,0,421,422,6,36,
        -1,0,422,423,3,74,37,0,423,436,1,0,0,0,424,425,10,3,0,0,425,426,
        5,28,0,0,426,427,3,74,37,0,427,428,6,36,-1,0,428,435,1,0,0,0,429,
        430,10,2,0,0,430,431,5,27,0,0,431,432,3,74,37,0,432,433,6,36,-1,
        0,433,435,1,0,0,0,434,424,1,0,0,0,434,429,1,0,0,0,435,438,1,0,0,
        0,436,434,1,0,0,0,436,437,1,0,0,0,437,73,1,0,0,0,438,436,1,0,0,0,
        439,455,3,76,38,0,440,441,5,25,0,0,441,442,5,18,0,0,442,455,6,37,
        -1,0,443,444,5,19,0,0,444,455,6,37,-1,0,445,446,5,20,0,0,446,455,
        6,37,-1,0,447,448,5,25,0,0,448,449,5,20,0,0,449,455,6,37,-1,0,450,
        451,5,18,0,0,451,455,6,37,-1,0,452,453,5,17,0,0,453,455,6,37,-1,
        0,454,439,1,0,0,0,454,440,1,0,0,0,454,443,1,0,0,0,454,445,1,0,0,
        0,454,447,1,0,0,0,454,450,1,0,0,0,454,452,1,0,0,0,455,75,1,0,0,0,
        456,457,5,16,0,0,457,458,6,38,-1,0,458,459,3,78,39,0,459,460,6,38,
        -1,0,460,463,1,0,0,0,461,463,3,80,40,0,462,456,1,0,0,0,462,461,1,
        0,0,0,463,77,1,0,0,0,464,465,5,25,0,0,465,466,5,25,0,0,466,469,6,
        39,-1,0,467,469,1,0,0,0,468,464,1,0,0,0,468,467,1,0,0,0,469,79,1,
        0,0,0,470,471,5,16,0,0,471,472,5,38,0,0,472,473,5,16,0,0,473,474,
        6,40,-1,0,474,81,1,0,0,0,475,476,5,38,0,0,476,477,5,16,0,0,477,478,
        3,82,41,0,478,479,6,41,-1,0,479,483,1,0,0,0,480,481,5,38,0,0,481,
        483,5,16,0,0,482,475,1,0,0,0,482,480,1,0,0,0,483,83,1,0,0,0,27,92,
        98,100,112,126,150,159,173,199,212,227,256,264,266,286,312,343,356,
        401,416,418,434,436,454,462,468,482
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
    RULE_uso_posible_herencia = 41

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
                   "posible_guion_doble", "uso_clase", "uso_posible_herencia" ]

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
        self.inClass = False

    def agregarEstructura(self, texto):
        self.archivo_salida.write(str(texto+"\n"))

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
            self.state = 84
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 85
            self.cuerpo(0)
            self.state = 86
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
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 90
                self.declaracion()
                pass

            elif la_ == 2:
                self.state = 91
                self.ejecucion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 98
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 94
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 95
                        self.declaracion()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 96
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 97
                        self.ejecucion()
                        pass

             
                self.state = 102
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
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                localctx._declaracion_var = self.declaracion_var()

                self.agregarEstructura("DECLARACION VAR detectado")
                for key in self.listaVar:
                    self.simbolos.addCaracteristica(key+self.ambitoActual, "uso", "variable")
                    self.declaracionesVariables[key+self.ambitoActual] = localctx._declaracion_var.line
                self.listaVar = []

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.declaracion_func()

                            
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
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
            self.state = 114
            localctx._tipo = self.tipo()
            self.state = 115
            localctx._lista_variable = self.lista_variable()
            self.state = 116
            self.match(gramaticaprueba.COMMA)

            for key in self.listaVar:
                self.simbolos.addCaracteristica(key + self.ambitoActual, "tipo", (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))
                localctx.line = localctx._lista_variable.line

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
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                localctx._ID = self.match(gramaticaprueba.ID)

                self.listaVar.append((None if localctx._ID is None else localctx._ID.text))
                localctx.line = (0 if localctx._ID is None else localctx._ID.line)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 122
                self.match(gramaticaprueba.SEMICOLON)
                self.state = 123
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
            self.state = 128
            localctx._encabezado_funcion = self.encabezado_funcion()
            self.polacaInversa.addElemento(('FUNCION' + ' ' + localctx._encabezado_funcion.funcion))
            self.state = 130
            self.parametro()
            self.state = 131
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 132
            self.cuerpo_func()
            self.state = 133
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.state = 134
            self.match(gramaticaprueba.COMMA)

            self.simbolos.addCaracteristica(localctx._encabezado_funcion.funcion, "tipo", "func")
            self.agregarEstructura("DECLARACION FUNCION detectado")
            self.reducirAmbito()

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
            self.state = 137
            self.match(gramaticaprueba.VOID)
            self.state = 138
            localctx._ID = self.match(gramaticaprueba.ID)

            if not self.simbolos.isKey((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual):
                self.auxIDFunc = (None if localctx._ID is None else localctx._ID.text) + self.ambitoActual
                self.simbolos.addCaracteristica(self.auxIDFunc, "uso", "funcion")
                self.ambitoActual = self.ambitoActual + ":" + (None if localctx._ID is None else localctx._ID.text)
            else:
                self.yyerror(" SEMANTICO: variable " + (None if localctx._ID is None else localctx._ID.text) + " ya existe en el ambito actual", (0 if localctx._ID is None else localctx._ID.line))
            localctx.funcion = (None if localctx._ID is None else localctx._ID.text)

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
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 142
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.addCaracteristica(self.auxIDFunc, "nroParametros", "0")

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 145
                localctx._tipo = self.tipo()
                self.state = 146
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 147
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
                self.state = 152
                self.cuerpo(0)
                self.state = 153
                self.ejecucion_retorno()
                self.state = 154
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
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
            self.state = 199
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
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.if_condicion()
                self.state = 181
                self.then_retorno()
                self.state = 182
                self.match(gramaticaprueba.ELSE)
                self.state = 183
                self.bloque_control()
                self.state = 184
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.if_condicion()
                self.state = 188
                self.bloque_control()
                self.state = 189
                self.else_retorno()
                self.state = 190
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 193
                self.if_condicion()
                self.state = 194
                self.then_retorno()
                self.state = 195
                self.else_retorno()
                self.state = 196
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
        self.enterRule(localctx, 22, self.RULE_then_retorno)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 202
                self.ejecucion_retorno()
                self.state = 203
                self.match(gramaticaprueba.COMMA)
                self.state = 204
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 207
                self.cuerpo_ejecucion(0)
                self.state = 208
                self.ejecucion_retorno()
                self.state = 209
                self.match(gramaticaprueba.COMMA)
                self.state = 210
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
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(gramaticaprueba.ELSE)
                self.state = 215
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 216
                self.ejecucion_retorno()
                self.state = 217
                self.match(gramaticaprueba.COMMA)
                self.state = 218
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(gramaticaprueba.ELSE)
                self.state = 221
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 222
                self.cuerpo_ejecucion(0)
                self.state = 223
                self.ejecucion_retorno()
                self.state = 224
                self.match(gramaticaprueba.COMMA)
                self.state = 225
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
            self.state = 229
            self.match(gramaticaprueba.WHILE)
            self.state = 230
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 231
            self.condicion()
            self.state = 232
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 233
            self.match(gramaticaprueba.DO)
            self.state = 234
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 235
            self.cuerpo_ejecucion(0)
            self.state = 236
            self.match(gramaticaprueba.RETURN)
            self.state = 237
            self.match(gramaticaprueba.COMMA)
            self.state = 238
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
            self.state = 241
            self.encabezado_clase()
            self.state = 242
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 243
            self.componentes_clase(0)
            self.state = 244
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.state = 245
            self.match(gramaticaprueba.COMMA)

            self.reducirAmbito()

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
            self.state = 248
            self.match(gramaticaprueba.CLASS)
            self.state = 249
            localctx._ID = self.match(gramaticaprueba.ID)

            self.auxIDClass = (None if localctx._ID is None else localctx._ID.text) + self.ambitoActual
            self.clasesDeclaradas.append((None if localctx._ID is None else localctx._ID.text))
            self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual, "uso", "nombre de clase")
            self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual, "ambito de clase", self.ambitoActual + ":" + (None if localctx._ID is None else localctx._ID.text))
            self.ambitoActual = self.ambitoActual + ":" + (None if localctx._ID is None else localctx._ID.text)

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
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 253
                self.componente_var()
                pass

            elif la_ == 2:
                self.state = 254
                self.componente_func()
                pass

            elif la_ == 3:
                self.state = 255
                self.componente_herencia()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 264
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 258
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 259
                        self.componente_var()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 260
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 261
                        self.componente_func()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 262
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 263
                        self.componente_herencia()
                        pass

             
                self.state = 268
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
            self.state = 269
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
            self.state = 272
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
            self.state = 275
            localctx._ID = self.match(gramaticaprueba.ID)
            self.state = 276
            self.match(gramaticaprueba.COMMA)

            identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
            if identificador != "":
                herenciasActuales = self.simbolos.getCaracteristica(identificador, "numero de herencias")
                if isinstance(herenciasActuales, int):
                    if herenciasActuales < 2:
                        self.simbolos.aumentarReferencia(identificador)
                        self.simbolos.addCaracteristica(self.auxIDClass, "numero de herencias", herenciasActuales + 1)
                        self.simbolos.addCaracteristica(self.auxIDClass, "clase herencia", identificador)
                    else:
                        self.yyerror("SEMANTICO: se exeden los niveles de herencia", (0 if localctx._ID is None else localctx._ID.line))
                else:
                    self.simbolos.addCaracteristica(self.auxIDClass, "numero de herencias", 1)
                    self.simbolos.addCaracteristica(self.auxIDClass, "clase herencia", identificador)
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
            self.state = 280
            self.ejecucion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaprueba.Cuerpo_ejecucionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo_ejecucion)
                    self.state = 282
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 283
                    self.ejecucion() 
                self.state = 288
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
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.asignacion()
                self.state = 290
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("ASIGNACION detectado")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.invocacion()
                self.state = 294
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("INVOCACION detectado")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 297
                self.seleccion()
                self.state = 298
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 301
                self.print_()
                self.state = 302
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("PRINT detectado")
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 305
                self.while_()
                self.state = 306
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("WHILE detectado")
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 309
                localctx._ERROR = self.match(gramaticaprueba.ERROR)
                self.state = 310
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


        def getRuleIndex(self):
            return gramaticaprueba.RULE_asignacion




    def asignacion(self):

        localctx = gramaticaprueba.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            localctx._ID = self.match(gramaticaprueba.ID)
            self.state = 315
            self.match(gramaticaprueba.EQUALS)
            self.state = 316
            self.expresion(0)

            identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
            if identificador != "":
                if identificador in self.declaracionesVariables.keys():
                    if self.ambitoActual == self.getAmbitoId(identificador):
                        self.declaracionesVariables.pop(identificador)
                self.simbolos.aumentarReferencia(identificador)
                self.polacaInversa.addElemento((None if localctx._ID is None else localctx._ID.text))
                self.polacaInversa.addElemento("=")
            else:
                self.yyerror("SEMANTICO: identificador " + (None if localctx._ID is None else localctx._ID.text) + " no declarado en un ambito valido", (0 if localctx._ID is None else localctx._ID.line))

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
        self.enterRule(localctx, 46, self.RULE_invocacion)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 320
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 321
                self.expresion(0)
                self.state = 322
                self.match(gramaticaprueba.RIGHT_PAREN)

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    if self.simbolos.getCaracteristica(identificador, "uso") == "funcion":
                        if self.simbolos.getCaracteristica(identificador, "nroParametros") == "1":
                            self.simbolos.aumentarReferencia(identificador)
                            aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + (None if localctx._ID is None else localctx._ID.text))
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
                self.state = 325
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 326
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 327
                self.match(gramaticaprueba.RIGHT_PAREN)

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    if self.simbolos.getCaracteristica(identificador, "uso") == "funcion":
                        if self.simbolos.getCaracteristica(identificador, "nroParametros") == "0":
                            self.simbolos.aumentarReferencia(identificador)
                            aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + (None if localctx._ID is None else localctx._ID.text))
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
                self.state = 329
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 330
                self.match(gramaticaprueba.DOT)
                self.state = 331
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 332
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 333
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
                            aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + (None if localctx.funcion is None else localctx.funcion.text))
                            self.polacaInversa.addElemento(aux)
                            self.polacaInversa.addElemento("CALLFUNC")
                        else:
                            self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrado en clase " + claseAmbito, (0 if localctx.clase is None else localctx.clase.line))
                else:
                    simbolo = (None if localctx._ID is None else localctx._ID.text)
                    if simbolo in self.clasesUsadas.keys():
                        self.clasesUsadas[simbolo] += 1
                    else:
                        self.clasesUsadas[simbolo] = 1

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 335
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 336
                self.match(gramaticaprueba.DOT)
                self.state = 337
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 338
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 339
                self.expresion(0)
                self.state = 340
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
                            aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + (None if localctx.funcion is None else localctx.funcion.text))
                            self.polacaInversa.addElemento(aux)
                            self.polacaInversa.addElemento("CALLFUNC")
                        else:
                            self.yyerror("SEMANTICO: numero incorrecto de parametros en la funcion " + (None if localctx.funcion is None else localctx.funcion.text), (0 if localctx.funcion is None else localctx.funcion.line))
                    else:
                        self.yyerror("SEMANTICO: " + (None if localctx.funcion is None else localctx.funcion.text) + " no encontrado en clase " + claseAmbito, (0 if localctx.clase is None else localctx.clase.line))
                else:
                    simbolo = (None if localctx._ID is None else localctx._ID.text)
                    if simbolo in self.clasesUsadas.keys():
                        self.clasesUsadas[simbolo] += 1
                    else:
                        self.clasesUsadas[simbolo] = 1

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
            self.state = 345
            self.if_condicion()
            self.state = 346
            self.bloque_control()
            self.state = 347
            self.posible_else()
            self.state = 348
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
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.else_()
                self.state = 352
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
            self.state = 358
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
            self.state = 361
            self.match(gramaticaprueba.IF)
            self.state = 362
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 363
            self.condicion()
            self.state = 364
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
            self.state = 367
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 368
            self.cuerpo_ejecucion(0)
            self.state = 369
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
            self.state = 371
            self.expresion(0)
            self.state = 372
            localctx._comparador = self.comparador()
            self.state = 373
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
            self.state = 376
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
            self.state = 378
            self.match(gramaticaprueba.PRINT)
            self.state = 379
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 380
            localctx._CADENA = self.match(gramaticaprueba.CADENA)
            self.state = 381
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
            self.state = 384
            self.while_condicion()
            self.state = 385
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
            self.state = 389
            self.match(gramaticaprueba.WHILE)
            self.state = 390
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 391
            self.condicion()
            self.state = 392
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 393
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
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(gramaticaprueba.INT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.match(gramaticaprueba.ULONG)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 398
                self.match(gramaticaprueba.FLOAT)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 399
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
            self.state = 404
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 416
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 406
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 407
                        self.match(gramaticaprueba.PLUS)
                        self.state = 408
                        self.termino(0)
                        self.polacaInversa.addElemento("+")
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 411
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 412
                        self.match(gramaticaprueba.MINUS)
                        self.state = 413
                        self.termino(0)
                        self.polacaInversa.addElemento("-")
                        pass

             
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.state = 422
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 436
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 434
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 424
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 425
                        self.match(gramaticaprueba.MULTIPLY)
                        self.state = 426
                        self.factor()
                        self.polacaInversa.addElemento("*")
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 429
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 430
                        self.match(gramaticaprueba.DIVIDE)
                        self.state = 431
                        self.factor()
                        self.polacaInversa.addElemento("/")
                        pass

             
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.referencia()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.match(gramaticaprueba.MINUS)
                self.state = 441
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
                self.state = 443
                localctx._NUM_ULONG = self.match(gramaticaprueba.NUM_ULONG)

                texto = (None if localctx._NUM_ULONG is None else localctx._NUM_ULONG.text)
                self.simbolos.addCaracteristica(texto, "tipo", "ULONG")
                self.simbolos.addCaracteristica(texto, "valor", self.getValor(texto))
                self.polacaInversa.addElemento((None if localctx._NUM_ULONG is None else localctx._NUM_ULONG.text))

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 445
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                self.simbolos.addCaracteristica((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text), "tipo", "FLOAT")
                self.polacaInversa.addElemento((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))
                # TODO calcular el float y guardarlo en la tabla

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 447
                self.match(gramaticaprueba.MINUS)
                self.state = 448
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
                self.state = 450
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
                self.state = 452
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
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                localctx._ID = self.match(gramaticaprueba.ID)
                self.polacaInversa.addElemento((None if localctx._ID is None else localctx._ID.text))
                self.state = 458
                self.posible_guion_doble()

                identificador = self.verificarId((None if localctx._ID is None else localctx._ID.text) + self.ambitoActual)
                if identificador != "":
                    self.simbolos.aumentarReferencia(identificador)
                    if (self.menos_menos is True):
                        self.polacaInversa.addElemento((None if localctx._ID is None else localctx._ID.text))
                        self.polacaInversa.addElemento('=')
                        self.menos_menos = False
                else:
                    self.yyerror("SEMANTICO: id " + (None if localctx._ID is None else localctx._ID.text) + " no existe en un ambito valido", (0 if localctx._ID is None else localctx._ID.line))


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
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
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(gramaticaprueba.MINUS)
                self.state = 465
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
        self.enterRule(localctx, 80, self.RULE_uso_clase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            localctx.clase = self.match(gramaticaprueba.ID)
            self.state = 471
            self.match(gramaticaprueba.DOT)
            self.state = 472
            localctx.atributo = self.match(gramaticaprueba.ID)

            idClase = self.verificarId((None if localctx.clase is None else localctx.clase.text) + self.ambitoActual)
            if idClase != "":
                self.simbolos.aumentarReferencia(idClase)
                ambitoClase = self.verificarId(self.simbolos.getCaracteristica(idClase, "tipo") + self.ambitoActual)
                if (None if localctx.atributo is None else localctx.atributo.text) in self.simbolos.getCaracteristica(ambitoClase, "propiedades"):
                    atributo = self.verificarId((None if localctx.atributo is None else localctx.atributo.text))
                    if atributo != "":
                        self.simbolos.aumentarReferencia(atributo)
                        clase = (None if localctx.clase is None else localctx.clase.text) + "." + (None if localctx.atributo is None else localctx.atributo.text)
                        self.polacaInversa.addElemento(str(clase))
                else:
                    self.yyerror("SEMANTICO: propiedad " + (None if localctx.atributo is None else localctx.atributo.text) + " no encontrada en clase " + idClase, (0 if localctx.clase is None else localctx.clase.line))
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


    class Uso_posible_herenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.clase_herencia = None # Token

        def DOT(self):
            return self.getToken(gramaticaprueba.DOT, 0)

        def uso_posible_herencia(self):
            return self.getTypedRuleContext(gramaticaprueba.Uso_posible_herenciaContext,0)


        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_uso_posible_herencia




    def uso_posible_herencia(self):

        localctx = gramaticaprueba.Uso_posible_herenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_uso_posible_herencia)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.match(gramaticaprueba.DOT)
                self.state = 476
                localctx.clase_herencia = self.match(gramaticaprueba.ID)
                self.state = 477
                self.uso_posible_herencia()

                simbolo = self.verificarId((None if localctx.clase_herencia is None else localctx.clase_herencia.text) + self.ambitoActual)
                if  simbolo != "":
                    self.simbolos.aumentarReferencia(simbolo)
                    claseAmbito = self.verificarId(self.simbolos.getCaracteristica(simbolo, "tipo") + self.ambitoActual)
                    miembros = self.simbolos.getCaracteristica(claseAmbito, "miembros de clase")

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.match(gramaticaprueba.DOT)
                self.state = 481
                localctx.clase_herencia = self.match(gramaticaprueba.ID)
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
         




