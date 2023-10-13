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
        4,1,39,409,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,75,8,1,1,1,1,1,1,1,1,1,5,1,81,8,
        1,10,1,12,1,84,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,95,8,
        2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,109,8,4,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,3,5,132,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,3,7,145,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,
        8,157,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,183,8,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,196,8,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,
        211,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,
        1,14,3,14,238,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,247,8,
        14,10,14,12,14,250,9,14,1,15,1,15,1,15,1,15,1,15,5,15,257,8,15,10,
        15,12,15,260,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,3,16,285,8,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,3,18,299,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,3,19,311,8,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,
        21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,5,27,351,8,27,10,27,12,27,354,9,27,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,365,8,28,10,28,12,28,
        368,9,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,3,29,385,8,29,1,30,1,30,1,30,1,30,1,30,3,30,
        392,8,30,1,31,1,31,1,31,3,31,397,8,31,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,3,32,407,8,32,1,32,0,5,2,28,30,54,56,33,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,0,2,3,0,13,15,22,22,31,32,2,0,7,9,16,16,417,0,66,
        1,0,0,0,2,74,1,0,0,0,4,94,1,0,0,0,6,96,1,0,0,0,8,108,1,0,0,0,10,
        131,1,0,0,0,12,133,1,0,0,0,14,144,1,0,0,0,16,156,1,0,0,0,18,182,
        1,0,0,0,20,195,1,0,0,0,22,210,1,0,0,0,24,212,1,0,0,0,26,224,1,0,
        0,0,28,237,1,0,0,0,30,251,1,0,0,0,32,284,1,0,0,0,34,286,1,0,0,0,
        36,298,1,0,0,0,38,310,1,0,0,0,40,312,1,0,0,0,42,317,1,0,0,0,44,321,
        1,0,0,0,46,325,1,0,0,0,48,327,1,0,0,0,50,332,1,0,0,0,52,339,1,0,
        0,0,54,341,1,0,0,0,56,355,1,0,0,0,58,384,1,0,0,0,60,391,1,0,0,0,
        62,396,1,0,0,0,64,406,1,0,0,0,66,67,5,35,0,0,67,68,3,2,1,0,68,69,
        5,36,0,0,69,70,6,0,-1,0,70,1,1,0,0,0,71,72,6,1,-1,0,72,75,3,4,2,
        0,73,75,3,32,16,0,74,71,1,0,0,0,74,73,1,0,0,0,75,82,1,0,0,0,76,77,
        10,4,0,0,77,81,3,4,2,0,78,79,10,3,0,0,79,81,3,32,16,0,80,76,1,0,
        0,0,80,78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,3,
        1,0,0,0,84,82,1,0,0,0,85,86,3,6,3,0,86,87,6,2,-1,0,87,95,1,0,0,0,
        88,89,3,10,5,0,89,90,6,2,-1,0,90,95,1,0,0,0,91,92,3,26,13,0,92,93,
        6,2,-1,0,93,95,1,0,0,0,94,85,1,0,0,0,94,88,1,0,0,0,94,91,1,0,0,0,
        95,5,1,0,0,0,96,97,3,52,26,0,97,98,3,8,4,0,98,99,5,26,0,0,99,100,
        6,3,-1,0,100,7,1,0,0,0,101,102,5,16,0,0,102,109,6,4,-1,0,103,104,
        5,16,0,0,104,105,5,33,0,0,105,106,3,8,4,0,106,107,6,4,-1,0,107,109,
        1,0,0,0,108,101,1,0,0,0,108,103,1,0,0,0,109,9,1,0,0,0,110,111,5,
        6,0,0,111,112,5,16,0,0,112,113,5,29,0,0,113,114,3,12,6,0,114,115,
        5,30,0,0,115,116,5,35,0,0,116,117,3,14,7,0,117,118,5,36,0,0,118,
        119,5,26,0,0,119,120,6,5,-1,0,120,132,1,0,0,0,121,122,5,6,0,0,122,
        123,5,16,0,0,123,124,5,29,0,0,124,125,5,30,0,0,125,126,5,35,0,0,
        126,127,3,14,7,0,127,128,5,36,0,0,128,129,5,26,0,0,129,130,6,5,-1,
        0,130,132,1,0,0,0,131,110,1,0,0,0,131,121,1,0,0,0,132,11,1,0,0,0,
        133,134,3,52,26,0,134,135,5,16,0,0,135,136,6,6,-1,0,136,13,1,0,0,
        0,137,138,3,2,1,0,138,139,3,16,8,0,139,140,5,26,0,0,140,145,1,0,
        0,0,141,142,3,16,8,0,142,143,5,26,0,0,143,145,1,0,0,0,144,137,1,
        0,0,0,144,141,1,0,0,0,145,15,1,0,0,0,146,157,3,18,9,0,147,148,3,
        18,9,0,148,149,5,26,0,0,149,150,3,16,8,0,150,157,1,0,0,0,151,152,
        3,24,12,0,152,153,5,26,0,0,153,154,3,16,8,0,154,157,1,0,0,0,155,
        157,5,12,0,0,156,146,1,0,0,0,156,147,1,0,0,0,156,151,1,0,0,0,156,
        155,1,0,0,0,157,17,1,0,0,0,158,159,3,40,20,0,159,160,3,20,10,0,160,
        161,5,3,0,0,161,162,6,9,-1,0,162,183,1,0,0,0,163,164,3,40,20,0,164,
        165,3,20,10,0,165,166,5,2,0,0,166,167,3,42,21,0,167,168,5,3,0,0,
        168,169,6,9,-1,0,169,183,1,0,0,0,170,171,3,40,20,0,171,172,3,42,
        21,0,172,173,3,22,11,0,173,174,5,3,0,0,174,175,6,9,-1,0,175,183,
        1,0,0,0,176,177,3,40,20,0,177,178,3,20,10,0,178,179,3,22,11,0,179,
        180,5,3,0,0,180,181,6,9,-1,0,181,183,1,0,0,0,182,158,1,0,0,0,182,
        163,1,0,0,0,182,170,1,0,0,0,182,176,1,0,0,0,183,19,1,0,0,0,184,185,
        5,35,0,0,185,186,3,16,8,0,186,187,5,26,0,0,187,188,5,36,0,0,188,
        196,1,0,0,0,189,190,5,35,0,0,190,191,3,30,15,0,191,192,3,16,8,0,
        192,193,5,26,0,0,193,194,5,36,0,0,194,196,1,0,0,0,195,184,1,0,0,
        0,195,189,1,0,0,0,196,21,1,0,0,0,197,198,5,2,0,0,198,199,5,35,0,
        0,199,200,3,16,8,0,200,201,5,26,0,0,201,202,5,36,0,0,202,211,1,0,
        0,0,203,204,5,2,0,0,204,205,5,35,0,0,205,206,3,30,15,0,206,207,3,
        16,8,0,207,208,5,26,0,0,208,209,5,36,0,0,209,211,1,0,0,0,210,197,
        1,0,0,0,210,203,1,0,0,0,211,23,1,0,0,0,212,213,5,10,0,0,213,214,
        5,29,0,0,214,215,3,44,22,0,215,216,5,30,0,0,216,217,5,11,0,0,217,
        218,5,35,0,0,218,219,3,30,15,0,219,220,5,12,0,0,220,221,5,26,0,0,
        221,222,5,36,0,0,222,223,6,12,-1,0,223,25,1,0,0,0,224,225,5,5,0,
        0,225,226,5,16,0,0,226,227,5,35,0,0,227,228,3,28,14,0,228,229,5,
        36,0,0,229,230,5,26,0,0,230,231,6,13,-1,0,231,27,1,0,0,0,232,233,
        6,14,-1,0,233,238,3,6,3,0,234,238,3,10,5,0,235,236,5,16,0,0,236,
        238,5,26,0,0,237,232,1,0,0,0,237,234,1,0,0,0,237,235,1,0,0,0,238,
        248,1,0,0,0,239,240,10,3,0,0,240,247,3,6,3,0,241,242,10,2,0,0,242,
        247,3,10,5,0,243,244,10,1,0,0,244,245,5,16,0,0,245,247,5,26,0,0,
        246,239,1,0,0,0,246,241,1,0,0,0,246,243,1,0,0,0,247,250,1,0,0,0,
        248,246,1,0,0,0,248,249,1,0,0,0,249,29,1,0,0,0,250,248,1,0,0,0,251,
        252,6,15,-1,0,252,253,3,32,16,0,253,258,1,0,0,0,254,255,10,2,0,0,
        255,257,3,32,16,0,256,254,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,
        0,258,259,1,0,0,0,259,31,1,0,0,0,260,258,1,0,0,0,261,262,3,34,17,
        0,262,263,5,26,0,0,263,264,6,16,-1,0,264,285,1,0,0,0,265,266,3,36,
        18,0,266,267,5,26,0,0,267,268,6,16,-1,0,268,285,1,0,0,0,269,270,
        3,38,19,0,270,271,5,26,0,0,271,272,6,16,-1,0,272,285,1,0,0,0,273,
        274,3,48,24,0,274,275,5,26,0,0,275,276,6,16,-1,0,276,285,1,0,0,0,
        277,278,3,50,25,0,278,279,5,26,0,0,279,280,6,16,-1,0,280,285,1,0,
        0,0,281,282,5,17,0,0,282,283,5,26,0,0,283,285,6,16,-1,0,284,261,
        1,0,0,0,284,265,1,0,0,0,284,269,1,0,0,0,284,273,1,0,0,0,284,277,
        1,0,0,0,284,281,1,0,0,0,285,33,1,0,0,0,286,287,5,16,0,0,287,288,
        5,34,0,0,288,289,3,54,27,0,289,35,1,0,0,0,290,291,5,16,0,0,291,292,
        5,29,0,0,292,293,3,54,27,0,293,294,5,30,0,0,294,299,1,0,0,0,295,
        296,5,16,0,0,296,297,5,29,0,0,297,299,5,30,0,0,298,290,1,0,0,0,298,
        295,1,0,0,0,299,37,1,0,0,0,300,301,3,40,20,0,301,302,3,42,21,0,302,
        303,5,3,0,0,303,311,1,0,0,0,304,305,3,40,20,0,305,306,3,42,21,0,
        306,307,5,2,0,0,307,308,3,42,21,0,308,309,5,3,0,0,309,311,1,0,0,
        0,310,300,1,0,0,0,310,304,1,0,0,0,311,39,1,0,0,0,312,313,5,1,0,0,
        313,314,5,29,0,0,314,315,3,44,22,0,315,316,5,30,0,0,316,41,1,0,0,
        0,317,318,5,35,0,0,318,319,3,30,15,0,319,320,5,36,0,0,320,43,1,0,
        0,0,321,322,3,54,27,0,322,323,3,46,23,0,323,324,3,54,27,0,324,45,
        1,0,0,0,325,326,7,0,0,0,326,47,1,0,0,0,327,328,5,4,0,0,328,329,5,
        29,0,0,329,330,5,21,0,0,330,331,5,30,0,0,331,49,1,0,0,0,332,333,
        5,10,0,0,333,334,5,29,0,0,334,335,3,44,22,0,335,336,5,30,0,0,336,
        337,5,11,0,0,337,338,3,42,21,0,338,51,1,0,0,0,339,340,7,1,0,0,340,
        53,1,0,0,0,341,342,6,27,-1,0,342,343,3,56,28,0,343,352,1,0,0,0,344,
        345,10,3,0,0,345,346,5,24,0,0,346,351,3,56,28,0,347,348,10,2,0,0,
        348,349,5,25,0,0,349,351,3,56,28,0,350,344,1,0,0,0,350,347,1,0,0,
        0,351,354,1,0,0,0,352,350,1,0,0,0,352,353,1,0,0,0,353,55,1,0,0,0,
        354,352,1,0,0,0,355,356,6,28,-1,0,356,357,3,58,29,0,357,366,1,0,
        0,0,358,359,10,3,0,0,359,360,5,28,0,0,360,365,3,58,29,0,361,362,
        10,2,0,0,362,363,5,27,0,0,363,365,3,58,29,0,364,358,1,0,0,0,364,
        361,1,0,0,0,365,368,1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,367,
        57,1,0,0,0,368,366,1,0,0,0,369,385,3,60,30,0,370,371,5,25,0,0,371,
        372,5,18,0,0,372,385,6,29,-1,0,373,374,5,19,0,0,374,385,6,29,-1,
        0,375,376,5,20,0,0,376,385,6,29,-1,0,377,378,5,25,0,0,378,379,5,
        20,0,0,379,385,6,29,-1,0,380,381,5,18,0,0,381,385,6,29,-1,0,382,
        383,5,17,0,0,383,385,6,29,-1,0,384,369,1,0,0,0,384,370,1,0,0,0,384,
        373,1,0,0,0,384,375,1,0,0,0,384,377,1,0,0,0,384,380,1,0,0,0,384,
        382,1,0,0,0,385,59,1,0,0,0,386,387,5,16,0,0,387,388,3,62,31,0,388,
        389,6,30,-1,0,389,392,1,0,0,0,390,392,3,64,32,0,391,386,1,0,0,0,
        391,390,1,0,0,0,392,61,1,0,0,0,393,394,5,37,0,0,394,397,6,31,-1,
        0,395,397,1,0,0,0,396,393,1,0,0,0,396,395,1,0,0,0,397,63,1,0,0,0,
        398,399,5,16,0,0,399,400,5,38,0,0,400,407,5,16,0,0,401,402,5,16,
        0,0,402,403,5,38,0,0,403,404,5,16,0,0,404,405,5,29,0,0,405,407,5,
        30,0,0,406,398,1,0,0,0,406,401,1,0,0,0,407,65,1,0,0,0,26,74,80,82,
        94,108,131,144,156,182,195,210,237,246,248,258,284,298,310,350,352,
        364,366,384,391,396,406
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

    def yyerror(self, texto):
        self.archivo_errores.write(str(texto+"\n"))



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
            self.state = 94
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

                self.agregarEstructura("DECLARACION FUNCION detectado")

                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
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
            self.state = 96
            localctx._tipo = self.tipo()
            self.state = 97
            self.lista_variable()
            self.state = 98
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
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                localctx._ID = self.match(gramaticaprueba.ID)

                self.simbolos.addSimbolo((None if localctx._ID is None else localctx._ID.text))
                self.listaVar.append((None if localctx._ID is None else localctx._ID.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 104
                self.match(gramaticaprueba.SEMICOLON)
                self.state = 105
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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(gramaticaprueba.VOID)
                self.state = 111
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 112
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 113
                self.parametro()
                self.state = 114
                self.match(gramaticaprueba.RIGHT_PAREN)
                self.state = 115
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 116
                self.cuerpo_func()
                self.state = 117
                self.match(gramaticaprueba.RIGHT_BRACE)
                self.state = 118
                self.match(gramaticaprueba.COMMA)

                self.simbolos.addCaracteristica((None if localctx._ID is None else localctx._ID.text), "tipo", "func")

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(gramaticaprueba.VOID)
                self.state = 122
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 123
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 124
                self.match(gramaticaprueba.RIGHT_PAREN)
                self.state = 125
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 126
                self.cuerpo_func()
                self.state = 127
                self.match(gramaticaprueba.RIGHT_BRACE)
                self.state = 128
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
            self.state = 133
            self.tipo()
            self.state = 134
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
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.cuerpo(0)
                self.state = 138
                self.ejecucion_retorno()
                self.state = 139
                self.match(gramaticaprueba.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.ejecucion_retorno()
                self.state = 142
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
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.control_retorno()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.control_retorno()
                self.state = 148
                self.match(gramaticaprueba.COMMA)
                self.state = 149
                self.ejecucion_retorno()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.while_retorno()
                self.state = 152
                self.match(gramaticaprueba.COMMA)
                self.state = 153
                self.ejecucion_retorno()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 155
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
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.if_condicion()
                self.state = 159
                self.then_retorno()
                self.state = 160
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.if_condicion()
                self.state = 164
                self.then_retorno()
                self.state = 165
                self.match(gramaticaprueba.ELSE)
                self.state = 166
                self.bloque_control()
                self.state = 167
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.if_condicion()
                self.state = 171
                self.bloque_control()
                self.state = 172
                self.else_retorno()
                self.state = 173
                self.match(gramaticaprueba.END_IF)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 176
                self.if_condicion()
                self.state = 177
                self.then_retorno()
                self.state = 178
                self.else_retorno()
                self.state = 179
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
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 185
                self.ejecucion_retorno()
                self.state = 186
                self.match(gramaticaprueba.COMMA)
                self.state = 187
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 190
                self.cuerpo_ejecucion(0)
                self.state = 191
                self.ejecucion_retorno()
                self.state = 192
                self.match(gramaticaprueba.COMMA)
                self.state = 193
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
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(gramaticaprueba.ELSE)
                self.state = 198
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 199
                self.ejecucion_retorno()
                self.state = 200
                self.match(gramaticaprueba.COMMA)
                self.state = 201
                self.match(gramaticaprueba.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(gramaticaprueba.ELSE)
                self.state = 204
                self.match(gramaticaprueba.LEFT_BRACE)
                self.state = 205
                self.cuerpo_ejecucion(0)
                self.state = 206
                self.ejecucion_retorno()
                self.state = 207
                self.match(gramaticaprueba.COMMA)
                self.state = 208
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
            self.state = 212
            self.match(gramaticaprueba.WHILE)
            self.state = 213
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 214
            self.condicion()
            self.state = 215
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 216
            self.match(gramaticaprueba.DO)
            self.state = 217
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 218
            self.cuerpo_ejecucion(0)
            self.state = 219
            self.match(gramaticaprueba.RETURN)
            self.state = 220
            self.match(gramaticaprueba.COMMA)
            self.state = 221
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
            self.state = 224
            self.match(gramaticaprueba.CLASS)
            self.state = 225
            localctx._ID = self.match(gramaticaprueba.ID)
            self.state = 226
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 227
            self.componentes_clase(0)
            self.state = 228
            self.match(gramaticaprueba.RIGHT_BRACE)
            self.state = 229
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
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 233
                self.declaracion_var()
                pass

            elif la_ == 2:
                self.state = 234
                self.declaracion_func()
                pass

            elif la_ == 3:
                self.state = 235
                self.match(gramaticaprueba.ID)
                self.state = 236
                self.match(gramaticaprueba.COMMA)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 246
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 239
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 240
                        self.declaracion_var()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 241
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 242
                        self.declaracion_func()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaprueba.Componentes_claseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_componentes_clase)
                        self.state = 243
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 244
                        self.match(gramaticaprueba.ID)
                        self.state = 245
                        self.match(gramaticaprueba.COMMA)
                        pass

             
                self.state = 250
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
            self.state = 252
            self.ejecucion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaprueba.Cuerpo_ejecucionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_cuerpo_ejecucion)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    self.ejecucion() 
                self.state = 260
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
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.asignacion()
                self.state = 262
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("ASIGNACION detectado")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.invocacion()
                self.state = 266
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("INVOCACION detectado")
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.seleccion()
                self.state = 270
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("IF detectado")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 273
                self.print_()
                self.state = 274
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("PRINT detectado")
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 277
                self.while_()
                self.state = 278
                self.match(gramaticaprueba.COMMA)
                self.agregarEstructura("WHILE detectado")
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 281
                self.match(gramaticaprueba.ERROR)
                self.state = 282
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
            self.state = 286
            self.match(gramaticaprueba.ID)
            self.state = 287
            self.match(gramaticaprueba.EQUALS)
            self.state = 288
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
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(gramaticaprueba.ID)
                self.state = 291
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 292
                self.expresion(0)
                self.state = 293
                self.match(gramaticaprueba.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(gramaticaprueba.ID)
                self.state = 296
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 297
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
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.if_condicion()
                self.state = 301
                self.bloque_control()
                self.state = 302
                self.match(gramaticaprueba.END_IF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.if_condicion()
                self.state = 305
                self.bloque_control()
                self.state = 306
                self.match(gramaticaprueba.ELSE)
                self.state = 307
                self.bloque_control()
                self.state = 308
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
            self.state = 312
            self.match(gramaticaprueba.IF)
            self.state = 313
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 314
            self.condicion()
            self.state = 315
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
            self.state = 317
            self.match(gramaticaprueba.LEFT_BRACE)
            self.state = 318
            self.cuerpo_ejecucion(0)
            self.state = 319
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
            self.state = 321
            self.expresion(0)
            self.state = 322
            self.comparador()
            self.state = 323
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
            self.state = 325
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
            self.state = 327
            self.match(gramaticaprueba.PRINT)
            self.state = 328
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 329
            self.match(gramaticaprueba.CADENA)
            self.state = 330
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
            self.state = 332
            self.match(gramaticaprueba.WHILE)
            self.state = 333
            self.match(gramaticaprueba.LEFT_PAREN)
            self.state = 334
            self.condicion()
            self.state = 335
            self.match(gramaticaprueba.RIGHT_PAREN)
            self.state = 336
            self.match(gramaticaprueba.DO)
            self.state = 337
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
            self.state = 339
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
            self.state = 342
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 350
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 344
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 345
                        self.match(gramaticaprueba.PLUS)
                        self.state = 346
                        self.termino(0)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 347
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 348
                        self.match(gramaticaprueba.MINUS)
                        self.state = 349
                        self.termino(0)
                        pass

             
                self.state = 354
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
            self.state = 356
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 364
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 358
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 359
                        self.match(gramaticaprueba.MULTIPLY)
                        self.state = 360
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaprueba.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 361
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 362
                        self.match(gramaticaprueba.DIVIDE)
                        self.state = 363
                        self.factor()
                        pass

             
                self.state = 368
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
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.referencia()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(gramaticaprueba.MINUS)
                self.state = 371
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
                self.state = 373
                localctx._NUM_ULONG = self.match(gramaticaprueba.NUM_ULONG)

                self.simbolos.addSimbolo((None if localctx._NUM_ULONG is None else localctx._NUM_ULONG.text))

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 375
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                self.simbolos.addSimbolo((None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 377
                self.match(gramaticaprueba.MINUS)
                self.state = 378
                localctx._NUM_FLOAT = self.match(gramaticaprueba.NUM_FLOAT)

                key = (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text)
                if key in self.simbolos.keys():
                    if self.simbolos.getCaracteristica(key, "referencias") == 1:
                        self.simbolos.remove(key)
                    else:
                        self.simbolos.reducirReferencia(key)
                # TODO chequear rango
                self.simbolos.addSimbolo("-" + (None if localctx._NUM_FLOAT is None else localctx._NUM_FLOAT.text))

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 380
                localctx._NUM_INT = self.match(gramaticaprueba.NUM_INT)

                self.simbolos.addSimbolo((None if localctx._NUM_INT is None else localctx._NUM_INT.text))

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 382
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
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                localctx._ID = self.match(gramaticaprueba.ID)
                self.state = 387
                self.posible_guion_doble()

                self.simbolos.aumentarReferencia((None if localctx._ID is None else localctx._ID.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
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
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
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
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(gramaticaprueba.ID)
                self.state = 399
                self.match(gramaticaprueba.DOT)
                self.state = 400
                self.match(gramaticaprueba.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.match(gramaticaprueba.ID)
                self.state = 402
                self.match(gramaticaprueba.DOT)
                self.state = 403
                self.match(gramaticaprueba.ID)
                self.state = 404
                self.match(gramaticaprueba.LEFT_PAREN)
                self.state = 405
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
         




