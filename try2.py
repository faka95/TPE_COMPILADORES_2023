from AnalizadorLexico.Token import Token
import AnalizadorLexico.Lexico as lexico
import TablaSimbolos as simbolos
from AnalizadorSintactico.Sintactico import Sintactico
from antlr4 import CommonTokenStream, FileStream
import sys
with open(sys.argv[1], 'r') as file:
    contenido_str = file.read()
    archivo_salida = open("salida.txt", "w")
    archivo_errores = open("errores.txt", "w")
    archivo_tabla = open("tabla_de_simbolos.txt", "w")

lex = lexico.Lexico(contenido_str, archivo_errores)
sintactico = Sintactico(contenido_str, archivo_errores, archivo_salida)
sintactico.start()

archivo_salida.close()
archivo_errores.close()
archivo_tabla.close()

print("Generacion de token finalizada")