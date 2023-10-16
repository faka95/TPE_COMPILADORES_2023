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

def serializedATN():
    return [
        4,1,39,430,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,75,8,1,1,1,1,1,1,1,1,1,5,1,81,8,
        1,10,1,12,1,84,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,93,8,2,1,3,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,107,8,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,128,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,138,8,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,147,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,3,8,160,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,186,
        8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,
        199,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,3,11,214,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,3,14,241,8,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,5,14,250,8,14,10,14,12,14,253,9,14,1,15,1,15,1,15,1,15,1,15,
        5,15,260,8,15,10,15,12,15,263,9,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,288,8,16,1,17,1,17,1,17,1,17,1,17,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,319,8,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,331,8,19,
        1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,
        1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,26,1,26,1,26,1,26,1,26,3,26,365,8,26,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,5,27,376,8,27,10,27,12,27,379,9,27,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,390,8,28,10,28,12,28,
        393,9,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,3,29,410,8,29,1,30,1,30,1,30,1,30,1,30,3,30,
        417,8,30,1,31,1,31,1,31,1,31,3,31,423,8,31,1,32,1,32,1,32,1,32,1,
        32,1,32,0,5,2,28,30,54,56,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,1,3,0,
        13,15,22,22,31,32,444,0,66,1,0,0,0,2,74,1,0,0,0,4,92,1,0,0,0,6,94,
        1,0,0,0,8,106,1,0,0,0,10,127,1,0,0,0,12,137,1,0,0,0,14,146,1,0,0,
        0,16,159,1,0,0,0,18,185,1,0,0,0,20,198,1,0,0,0,22,213,1,0,0,0,24,
        215,1,0,0,0,26,227,1,0,0,0,28,240,1,0,0,0,30,254,1,0,0,0,32,287,
        1,0,0,0,34,289,1,0,0,0,36,318,1,0,0,0,38,330,1,0,0,0,40,332,1,0,
        0,0,42,337,1,0,0,0,44,341,1,0,0,0,46,345,1,0,0,0,48,347,1,0,0,0,
        50,352,1,0,0,0,52,364,1,0,0,0,54,366,1,0,0,0,56,380,1,0,0,0,58,409,
        1,0,0,0,60,416,1,0,0,0,62,422,1,0,0,0,64,424,1,0,0,0,66,67,5,35,
        0,0,67,68,3,2,1,0,68,69,5,36,0,0,69,70,6,0,-1,0,70,1,1,0,0,0,71,
        72,6,1,-1,0,72,75,3,4,2,0,73,75,3,32,16,0,74,71,1,0,0,0,74,73,1,
        0,0,0,75,82,1,0,0,0,76,77,10,4,0,0,77,81,3,4,2,0,78,79,10,3,0,0,
        79,81,3,32,16,0,80,76,1,0,0,0,80,78,1,0,0,0,81,84,1,0,0,0,82,80,
        1,0,0,0,82,83,1,0,0,0,83,3,1,0,0,0,84,82,1,0,0,0,85,86,3,6,3,0,86,
        87,6,2,-1,0,87,93,1,0,0,0,88,93,3,10,5,0,89,90,3,26,13,0,90,91,6,
        2,-1,0,91,93,1,0,0,0,92,85,1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,0,93,
        5,1,0,0,0,94,95,3,52,26,0,95,96,3,8,4,0,96,97,5,26,0,0,97,98,6,3,
        -1,0,98,7,1,0,0,0,99,100,5,16,0,0,100,107,6,4,-1,0,101,102,5,16,
        0,0,102,103,5,33,0,0,103,104,3,8,4,0,104,105,6,4,-1,0,105,107,1,
        0,0,0,106,99,1,0,0,0,106,101,1,0,0,0,107,9,1,0,0,0,108,109,5,6,0,
        0,109,110,5,16,0,0,110,111,3,12,6,0,111,112,5,35,0,0,112,113,3,14,
        7,0,113,114,5,36,0,0,114,115,5,26,0,0,115,116,6,5,-1,0,116,128,1,
        0,0,0,117,118,5,6,0,0,118,119,5,16,0,0,119,120,5,29,0,0,120,121,
        5,30,0,0,121,122,5,35,0,0,122,123,3,14,7,0,123,124,5,36,0,0,124,
        125,5,26,0,0,125,126,6,5,-1,0,126,128,1,0,0,0,127,108,1,0,0,0,127,
        117,1,0,0,0,128,11,1,0,0,0,129,130,5,29,0,0,130,138,5,30,0,0,131,
        132,5,29,0,0,132,133,3,52,26,0,133,134,5,16,0,0,134,135,5,30,0,0,
        135,136,6,6,-1,0,136,138,1,0,0,0,137,129,1,0,0,0,137,131,1,0,0,0,
        138,13,1,0,0,0,139,140,3,2,1,0,140,141,3,16,8,0,141,142,5,26,0,0,
        142,147,1,0,0,0,143,144,3,16,8,0,144,145,5,26,0,0,145,147,1,0,0,
        0,146,139,1,0,0,0,146,143,1,0,0,0,147,15,1,0,0,0,148,160,3,18,9,
        0,149,150,3,18,9,0,150,151,5,26,0,0,151,152,3,16,8,0,152,160,1,0,
        0,0,153,160,3,24,12,0,154,155,3,24,12,0,155,156,5,26,0,0,156,157,
        3,16,8,0,157,160,1,0,0,0,158,160,5,12,0,0,159,148,1,0,0,0,159,149,
        1,0,0,0,159,153,1,0,0,0,159,154,1,0,0,0,159,158,1,0,0,0,160,17,1,
        0,0,0,161,162,3,40,20,0,162,163,3,20,10,0,163,164,5,3,0,0,164,165,
        6,9,-1,0,165,186,1,0,0,0,166,167,3,40,20,0,167,168,3,20,10,0,168,
        169,5,2,0,0,169,170,3,42,21,0,170,171,5,3,0,0,171,172,6,9,-1,0,172,
        186,1,0,0,0,173,174,3,40,20,0,174,175,3,42,21,0,175,176,3,22,11,
        0,176,177,5,3,0,0,177,178,6,9,-1,0,178,186,1,0,0,0,179,180,3,40,
        20,0,180,181,3,20,10,0,181,182,3,22,11,0,182,183,5,3,0,0,183,184,
        6,9,-1,0,184,186,1,0,0,0,185,161,1,0,0,0,185,166,1,0,0,0,185,173,
        1,0,0,0,185,179,1,0,0,0,186,19,1,0,0,0,187,188,5,35,0,0,188,189,
        3,16,8,0,189,190,5,26,0,0,190,191,5,36,0,0,191,199,1,0,0,0,192,193,
        5,35,0,0,193,194,3,30,15,0,194,195,3,16,8,0,195,196,5,26,0,0,196,
        197,5,36,0,0,197,199,1,0,0,0,198,187,1,0,0,0,198,192,1,0,0,0,199,
        21,1,0,0,0,200,201,5,2,0,0,201,202,5,35,0,0,202,203,3,16,8,0,203,
        204,5,26,0,0,204,205,5,36,0,0,205,214,1,0,0,0,206,207,5,2,0,0,207,
        208,5,35,0,0,208,209,3,30,15,0,209,210,3,16,8,0,210,211,5,26,0,0,
        211,212,5,36,0,0,212,214,1,0,0,0,213,200,1,0,0,0,213,206,1,0,0,0,
        214,23,1,0,0,0,215,216,5,10,0,0,216,217,5,29,0,0,217,218,3,44,22,
        0,218,219,5,30,0,0,219,220,5,11,0,0,220,221,5,35,0,0,221,222,3,30,
        15,0,222,223,5,12,0,0,223,224,5,26,0,0,224,225,5,36,0,0,225,226,
        6,12,-1,0,226,25,1,0,0,0,227,228,5,5,0,0,228,229,5,16,0,0,229,230,
        5,35,0,0,230,231,3,28,14,0,231,232,5,36,0,0,232,233,5,26,0,0,233,
        234,6,13,-1,0,234,27,1,0,0,0,235,236,6,14,-1,0,236,241,3,6,3,0,237,
        241,3,10,5,0,238,239,5,16,0,0,239,241,5,26,0,0,240,235,1,0,0,0,240,
        237,1,0,0,0,240,238,1,0,0,0,241,251,1,0,0,0,242,243,10,3,0,0,243,
        250,3,6,3,0,244,245,10,2,0,0,245,250,3,10,5,0,246,247,10,1,0,0,247,
        248,5,16,0,0,248,250,5,26,0,0,249,242,1,0,0,0,249,244,1,0,0,0,249,
        246,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,
        29,1,0,0,0,253,251,1,0,0,0,254,255,6,15,-1,0,255,256,3,32,16,0,256,
        261,1,0,0,0,257,258,10,2,0,0,258,260,3,32,16,0,259,257,1,0,0,0,260,
        263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,31,1,0,0,0,263,261,
        1,0,0,0,264,265,3,34,17,0,265,266,5,26,0,0,266,267,6,16,-1,0,267,
        288,1,0,0,0,268,269,3,36,18,0,269,270,5,26,0,0,270,271,6,16,-1,0,
        271,288,1,0,0,0,272,273,3,38,19,0,273,274,5,26,0,0,274,275,6,16,
        -1,0,275,288,1,0,0,0,276,277,3,48,24,0,277,278,5,26,0,0,278,279,
        6,16,-1,0,279,288,1,0,0,0,280,281,3,50,25,0,281,282,5,26,0,0,282,
        283,6,16,-1,0,283,288,1,0,0,0,284,285,5,17,0,0,285,286,5,26,0,0,
        286,288,6,16,-1,0,287,264,1,0,0,0,287,268,1,0,0,0,287,272,1,0,0,
        0,287,276,1,0,0,0,287,280,1,0,0,0,287,284,1,0,0,0,288,33,1,0,0,0,
        289,290,5,16,0,0,290,291,5,34,0,0,291,292,3,54,27,0,292,293,6,17,
        -1,0,293,35,1,0,0,0,294,295,5,16,0,0,295,296,5,29,0,0,296,297,3,
        54,27,0,297,298,5,30,0,0,298,299,6,18,-1,0,299,319,1,0,0,0,300,301,
        5,16,0,0,301,302,5,29,0,0,302,303,5,30,0,0,303,319,6,18,-1,0,304,
        305,5,16,0,0,305,306,5,38,0,0,306,307,5,16,0,0,307,308,5,29,0,0,
        308,309,5,30,0,0,309,319,6,18,-1,0,310,311,5,16,0,0,311,312,5,38,
        0,0,312,313,5,16,0,0,313,314,5,29,0,0,314,315,3,54,27,0,315,316,
        5,30,0,0,316,317,6,18,-1,0,317,319,1,0,0,0,318,294,1,0,0,0,318,300,
        1,0,0,0,318,304,1,0,0,0,318,310,1,0,0,0,319,37,1,0,0,0,320,321,3,
        40,20,0,321,322,3,42,21,0,322,323,5,3,0,0,323,331,1,0,0,0,324,325,
        3,40,20,0,325,326,3,42,21,0,326,327,5,2,0,0,327,328,3,42,21,0,328,
        329,5,3,0,0,329,331,1,0,0,0,330,320,1,0,0,0,330,324,1,0,0,0,331,
        39,1,0,0,0,332,333,5,1,0,0,333,334,5,29,0,0,334,335,3,44,22,0,335,
        336,5,30,0,0,336,41,1,0,0,0,337,338,5,35,0,0,338,339,3,30,15,0,339,
        340,5,36,0,0,340,43,1,0,0,0,341,342,3,54,27,0,342,343,3,46,23,0,
        343,344,3,54,27,0,344,45,1,0,0,0,345,346,7,0,0,0,346,47,1,0,0,0,
        347,348,5,4,0,0,348,349,5,29,0,0,349,350,5,21,0,0,350,351,5,30,0,
        0,351,49,1,0,0,0,352,353,5,10,0,0,353,354,5,29,0,0,354,355,3,44,
        22,0,355,356,5,30,0,0,356,357,5,11,0,0,357,358,3,42,21,0,358,51,
        1,0,0,0,359,365,5,7,0,0,360,365,5,8,0,0,361,365,5,9,0,0,362,363,
        5,16,0,0,363,365,6,26,-1,0,364,359,1,0,0,0,364,360,1,0,0,0,364,361,
        1,0,0,0,364,362,1,0,0,0,365,53,1,0,0,0,366,367,6,27,-1,0,367,368,
        3,56,28,0,368,377,1,0,0,0,369,370,10,3,0,0,370,371,5,24,0,0,371,
        376,3,56,28,0,372,373,10,2,0,0,373,374,5,25,0,0,374,376,3,56,28,
        0,375,369,1,0,0,0,375,372,1,0,0,0,376,379,1,0,0,0,377,375,1,0,0,
        0,377,378,1,0,0,0,378,55,1,0,0,0,379,377,1,0,0,0,380,381,6,28,-1,
        0,381,382,3,58,29,0,382,391,1,0,0,0,383,384,10,3,0,0,384,385,5,28,
        0,0,385,390,3,58,29,0,386,387,10,2,0,0,387,388,5,27,0,0,388,390,
        3,58,29,0,389,383,1,0,0,0,389,386,1,0,0,0,390,393,1,0,0,0,391,389,
        1,0,0,0,391,392,1,0,0,0,392,57,1,0,0,0,393,391,1,0,0,0,394,410,3,
        60,30,0,395,396,5,25,0,0,396,397,5,18,0,0,397,410,6,29,-1,0,398,
        399,5,19,0,0,399,410,6,29,-1,0,400,401,5,20,0,0,401,410,6,29,-1,
        0,402,403,5,25,0,0,403,404,5,20,0,0,404,410,6,29,-1,0,405,406,5,
        18,0,0,406,410,6,29,-1,0,407,408,5,17,0,0,408,410,6,29,-1,0,409,
        394,1,0,0,0,409,395,1,0,0,0,409,398,1,0,0,0,409,400,1,0,0,0,409,
        402,1,0,0,0,409,405,1,0,0,0,409,407,1,0,0,0,410,59,1,0,0,0,411,412,
        5,16,0,0,412,413,3,62,31,0,413,414,6,30,-1,0,414,417,1,0,0,0,415,
        417,3,64,32,0,416,411,1,0,0,0,416,415,1,0,0,0,417,61,1,0,0,0,418,
        419,5,25,0,0,419,420,5,25,0,0,420,423,6,31,-1,0,421,423,1,0,0,0,
        422,418,1,0,0,0,422,421,1,0,0,0,423,63,1,0,0,0,424,425,5,16,0,0,
        425,426,5,38,0,0,426,427,5,16,0,0,427,428,6,32,-1,0,428,65,1,0,0,
        0,27,74,80,82,92,106,127,137,146,159,185,198,213,240,249,251,261,
        287,318,330,364,375,377,389,391,409,416,422
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
    RULE_if_condicion = 20
    RULE_bloque_control = 21
    RULE_condicion = 22
    RULE_comparador = 23
    RULE_print = 24
    RULE_while = 25
    RULE_tipo = 26
    RULE_expresion = 27
    RULE_termino = 28
    RULE_factor = 29
    RULE_referencia = 30
    RULE_posible_guion_doble = 31
    RULE_uso_clase = 32

    ruleNames =  [ "programa", "cuerpo", "declaracion", "declaracion_var", 
                   "lista_variable", "declaracion_func", "parametro", "cuerpo_func", 
                   "ejecucion_retorno", "control_retorno", "then_retorno", 
                   "else_retorno", "while_retorno", "declaracion_clase", 
                   "componentes_clase", "cuerpo_ejecucion", "ejecucion", 
                   "asignacion", "invocacion", "seleccion", "if_condicion", 
                   "bloque_control", "condicion", "comparador", "print", 
                   "while", "tipo", "expresion", "termino", "factor", "referencia", 
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



        self.archivo_tabla = open("tabla_de_simbolos.txt", "a")
        self.archivo_salida = open("salida.txt", "a")
        self.archivo_errores = open("errores.txt", "a")
        self.simbolos = tablasimbolos.TablaDeSimbolos(self.archivo_tabla)
        self.menos_menos = False
        self.listaVar = []
        self.text = ""

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
            self.state = 66
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 67
            self.cuerpo(0)
            self.state = 68
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
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 72
                self.declaracion()
                pass

            elif la_ == 2:
                self.state = 73
                self.ejecucion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 76
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 77
                        self.declaracion()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 78
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 79
                        self.ejecucion()
                        pass

             
                self.state = 84
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
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.declaracion_var()

                self.agregarEstructura("DECLARACION VAR detectado")

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.declaracion_func()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
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
            self.state = 94
            localctx._tipo = self.tipo()
            self.state = 95
            self.lista_variable()
            self.state = 96
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
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                localctx._ID = self.match(gramaticaprueba.ID)

                self.listaVar.append((None if localctx._ID is None else localctx._ID.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 102
                self.match(gramaticaprueba.SEMICOLON)
                self.state = 103
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(gramaticaprueba.VOID)
                self.state = 109
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 110
                self.parametro()
                self.state = 111
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 112
                self.cuerpo_func()
                self.state = 113
                self.match(gramaticaprueba.RIGHT_BRACE)
                self.state = 114
                self.match(gramaticaprueba.COMMA)

                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text), "tipo", "func")
                self.agregarEstructura("DECLARACION FUNCION detectado")

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(gramaticaprueba.VOID)
                self.state = 118
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 119
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 120
                self.match(gramaticaprueba.RIGHT_PAREN)
                self.state = 121
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 122
                self.cuerpo_func()
                self.state = 123
                self.match(gramaticaprueba.RIGHT_BRACE)
                self.state = 124
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
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 130
                self.match(gramaticaprueba.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 132
                localctx._tipo = self.tipo()
                self.state = 133
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 134
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
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.cuerpo(0)
                self.state = 140
                self.ejecucion_retorno()
                self.state = 141
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.ejecucion_retorno()
                self.state = 144
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
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.control_retorno()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.control_retorno()
                self.state = 150
                self.match(gramaticaprueba.COMMA)
                self.state = 151
                self.ejecucion_retorno()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.while_retorno()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.while_retorno()
                self.state = 155
                self.match(gramaticaprueba.COMMA)
                self.state = 156
                self.ejecucion_retorno()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(gramaticaprueba.RETURN)
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
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.if_condicion()
                self.state = 162
                self.then_retorno()
                self.state = 163
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.if_condicion()
                self.state = 167
                self.then_retorno()
                self.state = 168
                self.match(gramaticaprueba.ELSE)
                self.state = 169
                self.bloque_control()
                self.state = 170
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.if_condicion()
                self.state = 174
                self.bloque_control()
                self.state = 175
                self.else_retorno()
                self.state = 176
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.if_condicion()
                self.state = 180
                self.then_retorno()
                self.state = 181
                self.else_retorno()
                self.state = 182
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
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 188
                self.ejecucion_retorno()
                self.state = 189
                self.match(gramaticaprueba.COMMA)
                self.state = 190
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 193
                self.cuerpo_ejecucion(0)
                self.state = 194
                self.ejecucion_retorno()
                self.state = 195
                self.match(gramaticaprueba.COMMA)
                self.state = 196
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
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(gramaticaprueba.ELSE)
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
                self.match(gramaticaprueba.ELSE)
                self.state = 207
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 208
                self.cuerpo_ejecucion(0)
                self.state = 209
                self.ejecucion_retorno()
                self.state = 210
                self.match(gramaticaprueba.COMMA)
                self.state = 211
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
            self.state = 215
            self.match(gramaticaprueba.WHILE)
            self.state = 216
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 217
            self.condicion()
            self.state = 218
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 219
            self.match(gramaticaprueba.DO)
            self.state = 220
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 221
            self.cuerpo_ejecucion(0)
            self.state = 222
            self.match(gramaticaprueba.RETURN)
            self.state = 223
            self.match(gramaticaprueba.COMMA)
            self.state = 224
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.agregarEstructura("WHILE detectado")
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
            self.state = 227
            self.match(gramaticaprueba.CLASS)
            self.state = 228
            localctx._ID = self.match(gramaticaprueba.ID)
            self.state = 229
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 230
            self.componentes_clase(0)
            self.state = 231
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.state = 232
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
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 236
                self.declaracion_var()
                pass

            elif la_ == 2:
                self.state = 237
                self.declaracion_func()
                pass

            elif la_ == 3:
                self.state = 238
                self.match(gramaticaprueba.ID)
                self.state = 239
                self.match(gramaticaprueba.COMMA)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 249
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 242
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 243
                        self.declaracion_var()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 244
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 245
                        self.declaracion_func()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 246
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 247
                        self.match(gramaticaprueba.ID)
                        self.state = 248
                        self.match(gramaticaprueba.COMMA)
                        pass

             
                self.state = 253
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
            self.state = 255
            self.ejecucion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaprueba.Cuerpo_ejecucionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo_ejecucion)
                    self.state = 257
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 258
                    self.ejecucion() 
                self.state = 263
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
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.asignacion()
                self.state = 265
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("ASIGNACION detectado")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.invocacion()
                self.state = 269
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("INVOCACION detectado")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.seleccion()
                self.state = 273
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 276
                self.print_()
                self.state = 277
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("PRINT detectado")
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 280
                self.while_()
                self.state = 281
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("WHILE detectado")
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 284
                localctx._ERROR = self.match(gramaticaprueba.ERROR)
                self.state = 285
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
            self.state = 289
            localctx._ID = self.match(gramaticaprueba.ID)
            self.state = 290
            self.match(gramaticaprueba.EQUALS)
            self.state = 291
            self.expresion(0)

            self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))

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
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 295
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 296
                self.expresion(0)
                self.state = 297
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 301
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 302
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 305
                self.match(gramaticaprueba.DOT)
                self.state = 306
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 307
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 308
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.aumentarReferencia((None if localctx.clase is None else localctx.clase.text))
                self.simbolos.aumentarReferencia((None if localctx.funcion is None else localctx.funcion.text))

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 310
                localctx.clase = self.match(gramaticaprueba.ID)
                self.state = 311
                self.match(gramaticaprueba.DOT)
                self.state = 312
                localctx.funcion = self.match(gramaticaprueba.ID)
                self.state = 313
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 314
                self.expresion(0)
                self.state = 315
                self.match(gramaticaprueba.RIGHT_PAREN)

                self.simbolos.aumentarReferencia((None if localctx.clase is None else localctx.clase.text))
                self.simbolos.aumentarReferencia((None if localctx.funcion is None else localctx.funcion.text))

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


        def bloque_control(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaprueba.Bloque_controlContext)
            else:
                return self.getTypedRuleContext(gramaticaprueba.Bloque_controlContext,i)


        def END_IF(self):
            return self.getToken(gramaticaprueba.END_IF, 0)

        def ELSE(self):
            return self.getToken(gramaticaprueba.ELSE, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_seleccion




    def seleccion(self):

        localctx = gramaticaprueba.SeleccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_seleccion)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.if_condicion()
                self.state = 321
                self.bloque_control()
                self.state = 322
                self.match(gramaticaprueba.END_IF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.if_condicion()
                self.state = 325
                self.bloque_control()
                self.state = 326
                self.match(gramaticaprueba.ELSE)
                self.state = 327
                self.bloque_control()
                self.state = 328
                self.match(gramaticaprueba.END_IF)
                pass


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
        self.enterRule(localctx, 40, self.RULE_if_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(gramaticaprueba.IF)
            self.state = 333
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 334
            self.condicion()
            self.state = 335
            self.match(gramaticaprueba.RIGHT_PAREN)
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
        self.enterRule(localctx, 42, self.RULE_bloque_control)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 338
            self.cuerpo_ejecucion(0)
            self.state = 339
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
        self.enterRule(localctx, 44, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.expresion(0)
            self.state = 342
            self.comparador()
            self.state = 343
            self.expresion(0)
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
        self.enterRule(localctx, 46, self.RULE_comparador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
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
        self.enterRule(localctx, 48, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(gramaticaprueba.PRINT)
            self.state = 348
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 349
            self.match(gramaticaprueba.CADENA)
            self.state = 350
            self.match(gramaticaprueba.RIGHT_PAREN)
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

        def bloque_control(self):
            return self.getTypedRuleContext(gramaticaprueba.Bloque_controlContext,0)


        def getRuleIndex(self):
            return gramaticaprueba.RULE_while




    def while_(self):

        localctx = gramaticaprueba.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(gramaticaprueba.WHILE)
            self.state = 353
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 354
            self.condicion()
            self.state = 355
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 356
            self.match(gramaticaprueba.DO)
            self.state = 357
            self.bloque_control()
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
        self.enterRule(localctx, 52, self.RULE_tipo)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.match(gramaticaprueba.INT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(gramaticaprueba.ULONG)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.match(gramaticaprueba.FLOAT)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 362
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 375
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 369
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 370
                        self.match(gramaticaprueba.PLUS)
                        self.state = 371
                        self.termino(0)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 372
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 373
                        self.match(gramaticaprueba.MINUS)
                        self.state = 374
                        self.termino(0)
                        pass

             
                self.state = 379
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_termino, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 389
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 383
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 384
                        self.match(gramaticaprueba.MULTIPLY)
                        self.state = 385
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 386
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 387
                        self.match(gramaticaprueba.DIVIDE)
                        self.state = 388
                        self.factor()
                        pass

             
                self.state = 393
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
        self.enterRule(localctx, 58, self.RULE_factor)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.referencia()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(gramaticaprueba.MINUS)
                self.state = 396
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                key = (None if localctx._NUM_INT is None else localctx._NUM_INT.text)
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove(key)
                    else:
                        self.simbolos.reducirReferencia(key)
                # TODO chequear rango
                self.simbolos.addSimbolo("-" + (None if localctx._NUM_INT is None else localctx._NUM_INT.text))

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 398
                localctx._NUM_ULONG = self.match(gramaticaprueba.NUM_ULONG)

                self.simbolos.addCaracteristica((None if localctx._NUM_ULONG is None else localctx._NUM_ULONG.text), "tipo", "ULONG")

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 400
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                self.simbolos.addCaracteristica((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text), "tipo", "FLOAT")

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 402
                self.match(gramaticaprueba.MINUS)
                self.state = 403
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                key = (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text)
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove(key)
                    else:
                        self.simbolos.reducirReferencia(key)
                self.simbolos.addSimbolo("-" + (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 405
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                if (None if localctx._NUM_INT is None else localctx._NUM_INT.text) == "32768_i":
                    self.yyerror("INT fuera de rango",(0 if localctx._NUM_INT is None else localctx._NUM_INT.line))
                else:
                    self.simbolos.addCaracteristica((None if localctx._NUM_INT is None else localctx._NUM_INT.text), "tipo", "INT")
                    texto = (None if localctx._NUM_INT is None else localctx._NUM_INT.text)
                    self.simbolos.addCaracteristica(texto, "valor", self.getValor(texto))

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 407
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
        self.enterRule(localctx, 60, self.RULE_referencia)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 412
                self.posible_guion_doble()

                self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
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
        self.enterRule(localctx, 62, self.RULE_posible_guion_doble)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(gramaticaprueba.MINUS)
                self.state = 419
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
        self.enterRule(localctx, 64, self.RULE_uso_clase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            localctx.clase = self.match(gramaticaprueba.ID)
            self.state = 425
            self.match(gramaticaprueba.DOT)
            self.state = 426
            localctx.atributo = self.match(gramaticaprueba.ID)

            self.simbolos.aumentarReferencia((None if localctx.clase is None else localctx.clase.text))
            self.simbolos.aumentarReferencia((None if localctx.atributo is None else localctx.atributo.text))

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
        self._predicates[27] = self.expresion_sempred
        self._predicates[28] = self.termino_sempred
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
         




