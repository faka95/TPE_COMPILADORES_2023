from AnalizadorLexico.Token import Token
from CodeReader import CodeReader
import sys

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

token = Token("IF")
token.print()
token.lexema = "ELSE"
token.print()
