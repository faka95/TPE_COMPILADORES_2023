from antlr4 import CommonTokenStream

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
        token_source = CustomTokenSource(self.contenido_str,self.archivo_errores)
        token_stream = CommonTokenStream(token_source)
        parser = gramaticaprueba(token_stream)
        tree = parser.start_()


 """       while True:
            token = self.lex.yyLex(self.contenido_str)
            if token is not None:
                archivo_salida.write(str("LEXEMA: " + token.getLexema() + " - TOKEN: " + str(token.getToken()) + "\n"))
            if token.getToken() == 200:
                break"""