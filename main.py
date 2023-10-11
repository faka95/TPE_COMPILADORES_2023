from AnalizadorLexico.Token import Token
import AnalizadorLexico.Lexico as lexico
#import AnalizadorSintactico.yacc as sintactico
from CodeReader import CodeReader
import sys
with open(sys.argv[1], 'r') as file:
    # python .\main.py "C:\\Users\\Tobias Romano\\Desktop\\archivo.txt" este es el formato
    contenido_str = file.read()
    archivo_salida = open("salida.txt", "w")
    archivo_errores = open("errores.txt", "w")
    archivo_tabla = open("tabla_de_simbolos.txt", "w")
#print(contenido_str)

lex = lexico.Lexico(contenido_str, archivo_errores)
#analizador_sintactico = sintactico.yacc()
token = lex.yyLex()
print(token.getLexema())
token = lex.yyLex()
print(token.getLexema())
token = lex.yyLex()
print(token.getLexema())
while True:
    token = lex.yyLex()
    if token is not None:
        archivo_salida.write(str("LEXEMA: " + token.getLexema() + " - TOKEN: " + str(token.getToken()) + "\n"))
    if token.getToken() == 400:
        break
archivo_salida.close()
archivo_errores.close()
archivo_tabla.close()
print("Generacion de token finalizada")

