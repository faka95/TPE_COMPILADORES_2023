from antlr4 import CommonTokenStream
from antlr4.tree.Trees import Trees

import AnalizadorLexico.Lexico as lexico
from antlr4.Token import Token
import AnalizadorLexico.Token as tokenLexico
from gramaticaprueba import gramaticaprueba


class CustomTokenSource:
    def __init__(self,contenido_str,archivo_errores):
        self.contenido_str = contenido_str
        self.lex = lexico.Lexico(contenido_str, archivo_errores)

    def nextToken(self):
        # Usa tu lexer personalizado para obtener el próximo token
        self.current_token = self.lex.yyLex()
        token = Token()
        token.type = self.current_token.getToken()
        token.text = self.current_token.getLexema()
        token.line = self.current_token.lineno
        return token
"""La clase CustomTokenSource si bien no es lo mas efectivo es necesaria para poder trabajar con ANTLR ya que el parser utiliza su propia clase TOKEN """

class Sintactico:
    def __init__(self,contenido_str,archivo_errores):
        self.contenido_str = contenido_str
        self.archivo_errores = archivo_errores

    def start(self):
        while True:
            token_source = CustomTokenSource(self.contenido_str,self.archivo_errores)
            token_stream = CommonTokenStream(token_source)
            print("hola")
            parser = gramaticaprueba(token_stream)
            print("hola2")
            tree = parser.programa()
            print("hola3")
            print(Trees.toStringTree(tree, None, parser))
            print(tree.toStringTree(recog=parser))