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
        4,1,39,408,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,3,1,74,8,1,1,1,1,1,1,1,1,1,5,1,80,8,1,10,
        1,12,1,83,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,94,8,2,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,108,8,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,131,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,3,7,144,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,156,
        8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,182,8,9,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,195,8,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,210,8,
        11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,
        14,237,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,246,8,14,10,
        14,12,14,249,9,14,1,15,1,15,1,15,1,15,1,15,5,15,256,8,15,10,15,12,
        15,259,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,
        16,284,8,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,3,18,298,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,3,19,310,8,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,
        21,1,22,1,22,1,22,1,22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,5,27,350,8,27,10,27,12,27,353,9,27,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,364,8,28,10,28,12,28,367,9,
        28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,3,29,384,8,29,1,30,1,30,1,30,1,30,1,30,3,30,391,8,30,
        1,31,1,31,1,31,3,31,396,8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,3,32,406,8,32,1,32,0,5,2,28,30,54,56,33,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,0,2,3,0,13,15,22,22,31,32,2,0,7,9,16,16,416,0,66,1,0,0,
        0,2,73,1,0,0,0,4,93,1,0,0,0,6,95,1,0,0,0,8,107,1,0,0,0,10,130,1,
        0,0,0,12,132,1,0,0,0,14,143,1,0,0,0,16,155,1,0,0,0,18,181,1,0,0,
        0,20,194,1,0,0,0,22,209,1,0,0,0,24,211,1,0,0,0,26,223,1,0,0,0,28,
        236,1,0,0,0,30,250,1,0,0,0,32,283,1,0,0,0,34,285,1,0,0,0,36,297,
        1,0,0,0,38,309,1,0,0,0,40,311,1,0,0,0,42,316,1,0,0,0,44,320,1,0,
        0,0,46,324,1,0,0,0,48,326,1,0,0,0,50,331,1,0,0,0,52,338,1,0,0,0,
        54,340,1,0,0,0,56,354,1,0,0,0,58,383,1,0,0,0,60,390,1,0,0,0,62,395,
        1,0,0,0,64,405,1,0,0,0,66,67,5,35,0,0,67,68,3,2,1,0,68,69,5,36,0,
        0,69,1,1,0,0,0,70,71,6,1,-1,0,71,74,3,4,2,0,72,74,3,32,16,0,73,70,
        1,0,0,0,73,72,1,0,0,0,74,81,1,0,0,0,75,76,10,4,0,0,76,80,3,4,2,0,
        77,78,10,3,0,0,78,80,3,32,16,0,79,75,1,0,0,0,79,77,1,0,0,0,80,83,
        1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,3,1,0,0,0,83,81,1,0,0,0,84,
        85,3,6,3,0,85,86,6,2,-1,0,86,94,1,0,0,0,87,88,3,10,5,0,88,89,6,2,
        -1,0,89,94,1,0,0,0,90,91,3,26,13,0,91,92,6,2,-1,0,92,94,1,0,0,0,
        93,84,1,0,0,0,93,87,1,0,0,0,93,90,1,0,0,0,94,5,1,0,0,0,95,96,3,52,
        26,0,96,97,3,8,4,0,97,98,5,26,0,0,98,99,6,3,-1,0,99,7,1,0,0,0,100,
        101,5,16,0,0,101,108,6,4,-1,0,102,103,5,16,0,0,103,104,5,33,0,0,
        104,105,3,8,4,0,105,106,6,4,-1,0,106,108,1,0,0,0,107,100,1,0,0,0,
        107,102,1,0,0,0,108,9,1,0,0,0,109,110,5,6,0,0,110,111,5,16,0,0,111,
        112,5,29,0,0,112,113,3,12,6,0,113,114,5,30,0,0,114,115,5,35,0,0,
        115,116,3,14,7,0,116,117,5,36,0,0,117,118,5,26,0,0,118,119,6,5,-1,
        0,119,131,1,0,0,0,120,121,5,6,0,0,121,122,5,16,0,0,122,123,5,29,
        0,0,123,124,5,30,0,0,124,125,5,35,0,0,125,126,3,14,7,0,126,127,5,
        36,0,0,127,128,5,26,0,0,128,129,6,5,-1,0,129,131,1,0,0,0,130,109,
        1,0,0,0,130,120,1,0,0,0,131,11,1,0,0,0,132,133,3,52,26,0,133,134,
        5,16,0,0,134,135,6,6,-1,0,135,13,1,0,0,0,136,137,3,2,1,0,137,138,
        3,16,8,0,138,139,5,26,0,0,139,144,1,0,0,0,140,141,3,16,8,0,141,142,
        5,26,0,0,142,144,1,0,0,0,143,136,1,0,0,0,143,140,1,0,0,0,144,15,
        1,0,0,0,145,156,3,18,9,0,146,147,3,18,9,0,147,148,5,26,0,0,148,149,
        3,16,8,0,149,156,1,0,0,0,150,151,3,24,12,0,151,152,5,26,0,0,152,
        153,3,16,8,0,153,156,1,0,0,0,154,156,5,12,0,0,155,145,1,0,0,0,155,
        146,1,0,0,0,155,150,1,0,0,0,155,154,1,0,0,0,156,17,1,0,0,0,157,158,
        3,40,20,0,158,159,3,20,10,0,159,160,5,3,0,0,160,161,6,9,-1,0,161,
        182,1,0,0,0,162,163,3,40,20,0,163,164,3,20,10,0,164,165,5,2,0,0,
        165,166,3,42,21,0,166,167,5,3,0,0,167,168,6,9,-1,0,168,182,1,0,0,
        0,169,170,3,40,20,0,170,171,3,42,21,0,171,172,3,22,11,0,172,173,
        5,3,0,0,173,174,6,9,-1,0,174,182,1,0,0,0,175,176,3,40,20,0,176,177,
        3,20,10,0,177,178,3,22,11,0,178,179,5,3,0,0,179,180,6,9,-1,0,180,
        182,1,0,0,0,181,157,1,0,0,0,181,162,1,0,0,0,181,169,1,0,0,0,181,
        175,1,0,0,0,182,19,1,0,0,0,183,184,5,35,0,0,184,185,3,16,8,0,185,
        186,5,26,0,0,186,187,5,36,0,0,187,195,1,0,0,0,188,189,5,35,0,0,189,
        190,3,30,15,0,190,191,3,16,8,0,191,192,5,26,0,0,192,193,5,36,0,0,
        193,195,1,0,0,0,194,183,1,0,0,0,194,188,1,0,0,0,195,21,1,0,0,0,196,
        197,5,2,0,0,197,198,5,35,0,0,198,199,3,16,8,0,199,200,5,26,0,0,200,
        201,5,36,0,0,201,210,1,0,0,0,202,203,5,2,0,0,203,204,5,35,0,0,204,
        205,3,30,15,0,205,206,3,16,8,0,206,207,5,26,0,0,207,208,5,36,0,0,
        208,210,1,0,0,0,209,196,1,0,0,0,209,202,1,0,0,0,210,23,1,0,0,0,211,
        212,5,10,0,0,212,213,5,29,0,0,213,214,3,44,22,0,214,215,5,30,0,0,
        215,216,5,11,0,0,216,217,5,35,0,0,217,218,3,30,15,0,218,219,5,12,
        0,0,219,220,5,26,0,0,220,221,5,36,0,0,221,222,6,12,-1,0,222,25,1,
        0,0,0,223,224,5,5,0,0,224,225,5,16,0,0,225,226,5,35,0,0,226,227,
        3,28,14,0,227,228,5,36,0,0,228,229,5,26,0,0,229,230,6,13,-1,0,230,
        27,1,0,0,0,231,232,6,14,-1,0,232,237,3,6,3,0,233,237,3,10,5,0,234,
        235,5,16,0,0,235,237,5,26,0,0,236,231,1,0,0,0,236,233,1,0,0,0,236,
        234,1,0,0,0,237,247,1,0,0,0,238,239,10,3,0,0,239,246,3,6,3,0,240,
        241,10,2,0,0,241,246,3,10,5,0,242,243,10,1,0,0,243,244,5,16,0,0,
        244,246,5,26,0,0,245,238,1,0,0,0,245,240,1,0,0,0,245,242,1,0,0,0,
        246,249,1,0,0,0,247,245,1,0,0,0,247,248,1,0,0,0,248,29,1,0,0,0,249,
        247,1,0,0,0,250,251,6,15,-1,0,251,252,3,32,16,0,252,257,1,0,0,0,
        253,254,10,2,0,0,254,256,3,32,16,0,255,253,1,0,0,0,256,259,1,0,0,
        0,257,255,1,0,0,0,257,258,1,0,0,0,258,31,1,0,0,0,259,257,1,0,0,0,
        260,261,3,34,17,0,261,262,5,26,0,0,262,263,6,16,-1,0,263,284,1,0,
        0,0,264,265,3,36,18,0,265,266,5,26,0,0,266,267,6,16,-1,0,267,284,
        1,0,0,0,268,269,3,38,19,0,269,270,5,26,0,0,270,271,6,16,-1,0,271,
        284,1,0,0,0,272,273,3,48,24,0,273,274,5,26,0,0,274,275,6,16,-1,0,
        275,284,1,0,0,0,276,277,3,50,25,0,277,278,5,26,0,0,278,279,6,16,
        -1,0,279,284,1,0,0,0,280,281,5,17,0,0,281,282,5,26,0,0,282,284,6,
        16,-1,0,283,260,1,0,0,0,283,264,1,0,0,0,283,268,1,0,0,0,283,272,
        1,0,0,0,283,276,1,0,0,0,283,280,1,0,0,0,284,33,1,0,0,0,285,286,5,
        16,0,0,286,287,5,34,0,0,287,288,3,54,27,0,288,35,1,0,0,0,289,290,
        5,16,0,0,290,291,5,29,0,0,291,292,3,54,27,0,292,293,5,30,0,0,293,
        298,1,0,0,0,294,295,5,16,0,0,295,296,5,29,0,0,296,298,5,30,0,0,297,
        289,1,0,0,0,297,294,1,0,0,0,298,37,1,0,0,0,299,300,3,40,20,0,300,
        301,3,42,21,0,301,302,5,3,0,0,302,310,1,0,0,0,303,304,3,40,20,0,
        304,305,3,42,21,0,305,306,5,2,0,0,306,307,3,42,21,0,307,308,5,3,
        0,0,308,310,1,0,0,0,309,299,1,0,0,0,309,303,1,0,0,0,310,39,1,0,0,
        0,311,312,5,1,0,0,312,313,5,29,0,0,313,314,3,44,22,0,314,315,5,30,
        0,0,315,41,1,0,0,0,316,317,5,35,0,0,317,318,3,30,15,0,318,319,5,
        36,0,0,319,43,1,0,0,0,320,321,3,54,27,0,321,322,3,46,23,0,322,323,
        3,54,27,0,323,45,1,0,0,0,324,325,7,0,0,0,325,47,1,0,0,0,326,327,
        5,4,0,0,327,328,5,29,0,0,328,329,5,21,0,0,329,330,5,30,0,0,330,49,
        1,0,0,0,331,332,5,10,0,0,332,333,5,29,0,0,333,334,3,44,22,0,334,
        335,5,30,0,0,335,336,5,11,0,0,336,337,3,42,21,0,337,51,1,0,0,0,338,
        339,7,1,0,0,339,53,1,0,0,0,340,341,6,27,-1,0,341,342,3,56,28,0,342,
        351,1,0,0,0,343,344,10,3,0,0,344,345,5,24,0,0,345,350,3,56,28,0,
        346,347,10,2,0,0,347,348,5,25,0,0,348,350,3,56,28,0,349,343,1,0,
        0,0,349,346,1,0,0,0,350,353,1,0,0,0,351,349,1,0,0,0,351,352,1,0,
        0,0,352,55,1,0,0,0,353,351,1,0,0,0,354,355,6,28,-1,0,355,356,3,58,
        29,0,356,365,1,0,0,0,357,358,10,3,0,0,358,359,5,28,0,0,359,364,3,
        58,29,0,360,361,10,2,0,0,361,362,5,27,0,0,362,364,3,58,29,0,363,
        357,1,0,0,0,363,360,1,0,0,0,364,367,1,0,0,0,365,363,1,0,0,0,365,
        366,1,0,0,0,366,57,1,0,0,0,367,365,1,0,0,0,368,384,3,60,30,0,369,
        370,5,25,0,0,370,371,5,18,0,0,371,384,6,29,-1,0,372,373,5,19,0,0,
        373,384,6,29,-1,0,374,375,5,20,0,0,375,384,6,29,-1,0,376,377,5,25,
        0,0,377,378,5,20,0,0,378,384,6,29,-1,0,379,380,5,18,0,0,380,384,
        6,29,-1,0,381,382,5,17,0,0,382,384,6,29,-1,0,383,368,1,0,0,0,383,
        369,1,0,0,0,383,372,1,0,0,0,383,374,1,0,0,0,383,376,1,0,0,0,383,
        379,1,0,0,0,383,381,1,0,0,0,384,59,1,0,0,0,385,386,5,16,0,0,386,
        387,3,62,31,0,387,388,6,30,-1,0,388,391,1,0,0,0,389,391,3,64,32,
        0,390,385,1,0,0,0,390,389,1,0,0,0,391,61,1,0,0,0,392,393,5,37,0,
        0,393,396,6,31,-1,0,394,396,1,0,0,0,395,392,1,0,0,0,395,394,1,0,
        0,0,396,63,1,0,0,0,397,398,5,16,0,0,398,399,5,38,0,0,399,406,5,16,
        0,0,400,401,5,16,0,0,401,402,5,38,0,0,402,403,5,16,0,0,403,404,5,
        29,0,0,404,406,5,30,0,0,405,397,1,0,0,0,405,400,1,0,0,0,406,65,1,
        0,0,0,26,73,79,81,93,107,130,143,155,181,194,209,236,245,247,257,
        283,297,309,349,351,363,365,383,390,395,405
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



        self.archivo_tabla = open("tabla_de_simbolos.txt", "w")
        self.archivo_salida = open("salida.txt", "w")
        self.archivo_errores = open("errores.txt", "w")
        self.simbolos = tablasimbolos.TablaDeSimbolos(self.archivo_tabla)
        self.menos_menos = False
        self.listaVar = []
    def agregarEstructura(self, texto): {
        self.archivo_salida.write(texto)
    }

    def yyerror(self, texto): {
        self.archivo_errores.write(texto)
    }



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
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 71
                self.declaracion()
                pass

            elif la_ == 2:
                self.state = 72
                self.ejecucion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 79
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 75
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 76
                        self.declaracion()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.CuerpoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo)
                        self.state = 77
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 78
                        self.ejecucion()
                        pass

             
                self.state = 83
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
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.declaracion_var()

                self.agregarEstructura("DECLARACION VAR detectado")

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.declaracion_func()

                self.agregarEstructura("DECLARACION FUNCION detectado")

                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
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
            self.state = 95
            localctx._tipo = self.tipo()
            self.state = 96
            self.lista_variable()
            self.state = 97
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
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                localctx._ID = self.match(gramaticaprueba.ID)

                self.simbolos.addSimbolo((None if localctx._ID is None else localctx._ID.text))
                self.listaVar.append((None if localctx._ID is None else localctx._ID.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 103
                self.match(gramaticaprueba.SEMICOLON)
                self.state = 104
                self.lista_variable()

                self.simbolos.addSimbolo((None if localctx._ID is None else localctx._ID.text))
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

        def LEFT_PAREN(self):
            return self.getToken(gramaticaprueba.LEFT_PAREN, 0)

        def parametro(self):
            return self.getTypedRuleContext(gramaticaprueba.ParametroContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(gramaticaprueba.RIGHT_PAREN, 0)

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
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(gramaticaprueba.VOID)
                self.state = 110
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 111
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 112
                self.parametro()
                self.state = 113
                self.match(gramaticaprueba.RIGHT_PAREN)
                self.state = 114
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 115
                self.cuerpo_func()
                self.state = 116
                self.match(gramaticaprueba.RIGHT_BRACE)
                self.state = 117
                self.match(gramaticaprueba.COMMA)

                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text), "tipo", "func")

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(gramaticaprueba.VOID)
                self.state = 121
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 122
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 123
                self.match(gramaticaprueba.RIGHT_PAREN)
                self.state = 124
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 125
                self.cuerpo_func()
                self.state = 126
                self.match(gramaticaprueba.RIGHT_BRACE)
                self.state = 127
                self.match(gramaticaprueba.COMMA)

                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text), "tipo", "func")

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
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.tipo()
            self.state = 133
            self.match(gramaticaprueba.ID)
            #agregar el parametro a la tabla
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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.cuerpo(0)
                self.state = 137
                self.ejecucion_retorno()
                self.state = 138
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.ejecucion_retorno()
                self.state = 141
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
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.control_retorno()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.control_retorno()
                self.state = 147
                self.match(gramaticaprueba.COMMA)
                self.state = 148
                self.ejecucion_retorno()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.while_retorno()
                self.state = 151
                self.match(gramaticaprueba.COMMA)
                self.state = 152
                self.ejecucion_retorno()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
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
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.if_condicion()
                self.state = 158
                self.then_retorno()
                self.state = 159
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.if_condicion()
                self.state = 163
                self.then_retorno()
                self.state = 164
                self.match(gramaticaprueba.ELSE)
                self.state = 165
                self.bloque_control()
                self.state = 166
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.if_condicion()
                self.state = 170
                self.bloque_control()
                self.state = 171
                self.else_retorno()
                self.state = 172
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.if_condicion()
                self.state = 176
                self.then_retorno()
                self.state = 177
                self.else_retorno()
                self.state = 178
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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 184
                self.ejecucion_retorno()
                self.state = 185
                self.match(gramaticaprueba.COMMA)
                self.state = 186
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 189
                self.cuerpo_ejecucion(0)
                self.state = 190
                self.ejecucion_retorno()
                self.state = 191
                self.match(gramaticaprueba.COMMA)
                self.state = 192
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
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(gramaticaprueba.ELSE)
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
                self.match(gramaticaprueba.ELSE)
                self.state = 203
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 204
                self.cuerpo_ejecucion(0)
                self.state = 205
                self.ejecucion_retorno()
                self.state = 206
                self.match(gramaticaprueba.COMMA)
                self.state = 207
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
            self.state = 211
            self.match(gramaticaprueba.WHILE)
            self.state = 212
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 213
            self.condicion()
            self.state = 214
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 215
            self.match(gramaticaprueba.DO)
            self.state = 216
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 217
            self.cuerpo_ejecucion(0)
            self.state = 218
            self.match(gramaticaprueba.RETURN)
            self.state = 219
            self.match(gramaticaprueba.COMMA)
            self.state = 220
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
            self.state = 223
            self.match(gramaticaprueba.CLASS)
            self.state = 224
            localctx._ID = self.match(gramaticaprueba.ID)
            self.state = 225
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 226
            self.componentes_clase(0)
            self.state = 227
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.state = 228
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
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 232
                self.declaracion_var()
                pass

            elif la_ == 2:
                self.state = 233
                self.declaracion_func()
                pass

            elif la_ == 3:
                self.state = 234
                self.match(gramaticaprueba.ID)
                self.state = 235
                self.match(gramaticaprueba.COMMA)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 245
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 238
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 239
                        self.declaracion_var()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 240
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 241
                        self.declaracion_func()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 242
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 243
                        self.match(gramaticaprueba.ID)
                        self.state = 244
                        self.match(gramaticaprueba.COMMA)
                        pass

             
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
            self.state = 251
            self.ejecucion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaprueba.Cuerpo_ejecucionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo_ejecucion)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    self.ejecucion() 
                self.state = 259
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
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.asignacion()
                self.state = 261
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("ASIGNACION detectado")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.invocacion()
                self.state = 265
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("INVOCACION detectado")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.seleccion()
                self.state = 269
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.print_()
                self.state = 273
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("PRINT detectado")
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 276
                self.while_()
                self.state = 277
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("WHILE detectado")
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 280
                self.match(gramaticaprueba.ERROR)
                self.state = 281
                self.match(gramaticaprueba.COMMA)
                self.yyerror("ERROR detectado")
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
            self.state = 285
            self.match(gramaticaprueba.ID)
            self.state = 286
            self.match(gramaticaprueba.EQUALS)
            self.state = 287
            self.expresion(0)
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

        def ID(self):
            return self.getToken(gramaticaprueba.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(gramaticaprueba.LEFT_PAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaprueba.ExpresionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(gramaticaprueba.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_invocacion




    def invocacion(self):

        localctx = gramaticaprueba.InvocacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_invocacion)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(gramaticaprueba.ID)
                self.state = 290
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 291
                self.expresion(0)
                self.state = 292
                self.match(gramaticaprueba.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.match(gramaticaprueba.ID)
                self.state = 295
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 296
                self.match(gramaticaprueba.RIGHT_PAREN)
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
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.if_condicion()
                self.state = 300
                self.bloque_control()
                self.state = 301
                self.match(gramaticaprueba.END_IF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.if_condicion()
                self.state = 304
                self.bloque_control()
                self.state = 305
                self.match(gramaticaprueba.ELSE)
                self.state = 306
                self.bloque_control()
                self.state = 307
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
            self.state = 311
            self.match(gramaticaprueba.IF)
            self.state = 312
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 313
            self.condicion()
            self.state = 314
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
            self.state = 316
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 317
            self.cuerpo_ejecucion(0)
            self.state = 318
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
            self.state = 320
            self.expresion(0)
            self.state = 321
            self.comparador()
            self.state = 322
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
            self.state = 324
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
            self.state = 326
            self.match(gramaticaprueba.PRINT)
            self.state = 327
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 328
            self.match(gramaticaprueba.CADENA)
            self.state = 329
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
            self.state = 331
            self.match(gramaticaprueba.WHILE)
            self.state = 332
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 333
            self.condicion()
            self.state = 334
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 335
            self.match(gramaticaprueba.DO)
            self.state = 336
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66432) != 0)):
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
            self.state = 341
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 349
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 343
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 344
                        self.match(gramaticaprueba.PLUS)
                        self.state = 345
                        self.termino(0)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 346
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 347
                        self.match(gramaticaprueba.MINUS)
                        self.state = 348
                        self.termino(0)
                        pass

             
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 355
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 363
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 357
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 358
                        self.match(gramaticaprueba.MULTIPLY)
                        self.state = 359
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 360
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 361
                        self.match(gramaticaprueba.DIVIDE)
                        self.state = 362
                        self.factor()
                        pass

             
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.referencia()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.match(gramaticaprueba.MINUS)
                self.state = 370
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                key = (None if localctx._NUM_INT is None else localctx._NUM_INT.text)
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove[key]
                    else:
                        self.simbolos.reducirReferencia(key)
                # TODO chequear rango
                self.simbolos.addSimbolo("-" + (None if localctx._NUM_INT is None else localctx._NUM_INT.text))

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 372
                localctx._NUM_ULONG = self.match(gramaticaprueba.NUM_ULONG)

                self.simbolos.addSimbolo((None if localctx._NUM_ULONG is None else localctx._NUM_ULONG.text))

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 374
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                self.simbolos.addSimbolo((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 376
                self.match(gramaticaprueba.MINUS)
                self.state = 377
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                key = (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text)
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove[key]
                    else:
                        self.simbolos.reducirReferencia(key)
                # TODO chequear rango
                self.simbolos.addSimbolo("-" + (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 379
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                self.simbolos.addSimbolo((None if localctx._NUM_INT is None else localctx._NUM_INT.text))

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 381
                self.match(gramaticaprueba.ERROR)
                self.yyerror("se espera una cosntante o id")
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
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 386
                self.posible_guion_doble()

                self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
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

        def DOUBLE_MINUS(self):
            return self.getToken(gramaticaprueba.DOUBLE_MINUS, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_posible_guion_doble




    def posible_guion_doble(self):

        localctx = gramaticaprueba.Posible_guion_dobleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_posible_guion_doble)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(gramaticaprueba.DOUBLE_MINUS)

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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaprueba.ID)
            else:
                return self.getToken(gramaticaprueba.ID, i)

        def DOT(self):
            return self.getToken(gramaticaprueba.DOT, 0)

        def LEFT_PAREN(self):
            return self.getToken(gramaticaprueba.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(gramaticaprueba.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return gramaticaprueba.RULE_uso_clase




    def uso_clase(self):

        localctx = gramaticaprueba.Uso_claseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_uso_clase)
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(gramaticaprueba.ID)
                self.state = 398
                self.match(gramaticaprueba.DOT)
                self.state = 399
                self.match(gramaticaprueba.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.match(gramaticaprueba.ID)
                self.state = 401
                self.match(gramaticaprueba.DOT)
                self.state = 402
                self.match(gramaticaprueba.ID)
                self.state = 403
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 404
                self.match(gramaticaprueba.RIGHT_PAREN)
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
         




