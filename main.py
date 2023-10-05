from AnalizadorLexico.Token import Token
import AnalizadorLexico.Lexico as lexico
from CodeReader import CodeReader
import sys
with open(sys.argv[1], 'r') as file:
    # python .\main.py "C:\\Users\\Tobias Romano\\Desktop\\archivo.txt" este es el formato
    contenido_str = file.read()
#print(contenido_str)

lex = lexico.Lexico(contenido_str)
while True:
    token = lex.yyLex(contenido_str)
    if token is not None:
        print("LEXEMA: ", token.getLexema(), " - Nro: ", token.getToken())
    if token.getToken() == 200:
        break
print("Generacion de token finalizada")

