from AnalizadorLexico.Token import Token
import AnalizadorLexico.Lexico as lexico
from CodeReader import CodeReader
import sys
with open(sys.argv[1], 'r') as file:
    # python .\main.py "C:\\Users\\Tobias Romano\\Desktop\\archivo.txt" este es el formato
    contenido_str = file.read()
    archivo_salida = open("salida.txt", "w")
    archivo_errores = open("errores.txt", "w")
#print(contenido_str)

lex = lexico.Lexico(contenido_str, archivo_errores)
while True:
    token = lex.yyLex(contenido_str)
    if token is not None:
        archivo_salida.write(str("LEXEMA: " + token.getLexema() + " - Nro: " + str(token.getToken()) + "\n"))
    if token.getToken() == 200:
        break
archivo_salida.close()
archivo_errores.close()
print("Generacion de token finalizada")

