from AnalizadorLexico.Token import Token
import AnalizadorLexico.Lexico as lexico
from CodeReader import CodeReader
import sys
with open(sys.argv[1], 'r') as file:
    # python .\main.py "C:\\Users\\Tobias Romano\\Desktop\\archivo.txt" este es el formato
    contenido_str = file.read()
print(contenido_str)
"""codigo = CodeReader(sys.argv[1])
generador = codigo.getchar()
for caracter in generador:
    if caracter == " ":
        print("espacio")
    elif caracter == "\n":
        print("salto")
    else:
        print(caracter)
print(codigo.getLast())"""
lex = lexico.Lexico(contenido_str)
lex.yyLex(contenido_str)

"""
token = Token("IF")
token.print()
token.lexema = "ELSE"
token.print()
"""