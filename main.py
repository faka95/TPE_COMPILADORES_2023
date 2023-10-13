import sys

import AnalizadorLexico.Lexico as lexico
from AnalizadorSintactico.Sintactico import Sintactico

with open(sys.argv[1], 'r') as file:
    contenido_str = file.read()
    archivo_salida = open("salida.txt", "w")
    archivo_errores = open("errores.txt", "w")
    archivo_tabla = open("tabla_de_simbolos.txt", "w")

lex = lexico.Lexico(contenido_str, archivo_errores)
sintactico = Sintactico(contenido_str, archivo_errores)
sintactico.start()
"""while True:
    token = lex.yyLex()
    if token is not None:
        archivo_salida.write(str("LEXEMA: " + token.getLexema() + " - TOKEN: " + str(token.getToken()) + "\n"))
    if token.getToken() == 400:
        break
"""
archivo_salida.close()
archivo_errores.close()
archivo_tabla.close()
print("Generacion de token finalizada")
