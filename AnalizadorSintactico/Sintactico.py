from antlr4 import CommonTokenStream
from AnalizadorSintactico.CustomANTLR import CustomTokenSource
from AnalizadorSintactico.CustomANTLR import CustomErrorStrategy
from AnalizadorSintactico.gramaticaprueba import gramaticaprueba


class Sintactico:
    def __init__(self,contenido_str,archivo_errores,archivo_salida):
        self.contenido_str = contenido_str
        self.archivo_errores = archivo_errores
        self.archivo_salida = archivo_salida

    def start(self):
            token_source = CustomTokenSource(self.contenido_str,self.archivo_errores,self.archivo_salida)
            token_stream = CommonTokenStream(token_source)
            parser = gramaticaprueba(token_stream)
            customErrorHandler = CustomErrorStrategy()
            customErrorHandler.setParserGen(parser)
            parser._errHandler = customErrorHandler
            tree = parser.programa()
            print("hola")
            print(parser.polacaInversa.referencias)
