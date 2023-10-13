from AnalizadorLexico.Token import Token
import AnalizadorLexico.Lexico as lexico
import TablaSimbolos as simbolos
from AnalizadorSintactico.Sintactico import Sintactico
from antlr4 import CommonTokenStream, FileStream
import sys
with open(sys.argv[1], 'r') as file:
    contenido_str = file.read()
    archivo_errores = open("errores.txt", "w")
    archivo_tabla = open("tabla_de_simbolos.txt", "w")
lex = lexico.Lexico(contenido_str, archivo_errores)
"""while True:
    token = lex.yyLex(contenido_str)
    if token is not None:
        archivo_salida.write(str("LEXEMA: " + token.getLexema() + " - TOKEN: " + str(token.getToken()) + "\n"))
    if token.getToken() == 200:
        break
"""
sintactico = Sintactico(contenido_str, archivo_errores)
sintactico.start()


archivo_errores.close()
archivo_tabla.close()

print("Generacion de token finalizada")