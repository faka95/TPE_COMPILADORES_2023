from antlr4 import CommonTokenStream
from antlr4.CommonTokenFactory import CommonTokenFactory
from antlr4.Lexer import TokenSource, Lexer
from antlr4.tree.Trees import Trees

import AnalizadorLexico.Lexico as lexico
from antlr4.Token import Token

import AnalizadorLexico.Token as tokenLexico
from gramaticaprueba import gramaticaprueba


class CustomTokenSource(TokenSource):
    def __init__(self,contenido_str,archivo_errores,archivo_salida ):
        self.contenido_str = contenido_str
        self.lex = lexico.Lexico(contenido_str, archivo_errores)
        self.archivo_salida = archivo_salida
        self._factory = CommonTokenFactory.DEFAULT

    def nextToken(self):
        # Usa tu lexer personalizado para obtener el próximo token
        self.current_token = self.lex.yyLex()
        if self.current_token is not None:
            self.archivo_salida.write(str("LEXEMA: " + self.current_token.getLexema() + " - TOKEN: " + str(self.current_token.getToken()) + "\n"))
        token = Token()
        self._tokenFactorySourcePair = (None, None)
        if self.current_token.getLexema() != "FIN":
            t = self._factory.create(self._tokenFactorySourcePair, self.current_token.getToken(), self.current_token.getLexema(), Token.DEFAULT_CHANNEL,
                                     0,
                                     0, self.current_token.lineno, 0)
        else:
            t = self._factory.create(self._tokenFactorySourcePair, Token.EOF, None, Token.DEFAULT_CHANNEL,
                                     0,
                                     0, self.current_token.lineno, 0)

        return t
    def getSourceName(self):
        return "UNKNOWN"
"""La clase CustomTokenSource si bien no es lo mas efectivo es necesaria para poder trabajar con ANTLR ya que el parser utiliza su propia clase TOKEN """

class Sintactico:
    def __init__(self,contenido_str,archivo_errores):
        self.contenido_str = contenido_str
        self.archivo_errores = archivo_errores

    def start(self):
            archivo_salida = open("salida.txt", "w")
            token_source = CustomTokenSource(self.contenido_str,self.archivo_errores,archivo_salida)
            token_stream = CommonTokenStream(token_source)
            parser = gramaticaprueba(token_stream)
            tree = parser.programa()
            archivo_salida.close()
            print(tree.toStringTree(recog=parser))
            #print(tree.toStringTree(recog=parser))
