import AnalizadorLexico.AccionesSemanticas.AccionSemantica as accion
import AnalizadorLexico.Lexico


class DoubleError(accion.AccionSemantica):

    def __init__(self, lexico: AnalizadorLexico.Lexico.Lexico):
        super().__init__(lexico)

    def checkFloat(self, buffer):
        try:
            float(buffer)
            return True
        except ValueError:
            return False

    def ejecutar(self,caracterActual):
        if not (self.checkFloat(self.lexico.bufferLexema())):
            self.lexico.setTokenActual("error_yacc")
            self.lexico.escribirError("Contiene letras o no contiene digitos")
        else:
            if ("e" in self.lexico.bufferLexema() or "E" in self.lexico.bufferLexema()):
                if not ("+" in self.lexico.bufferLexema() or "-" in self.lexico.bufferLexema()):
                    self.lexico.setTokenActual("error_yacc")
                    self.lexico.escribirError("Contiene letras o no contiene digitos")

        self.lexico.bufferClear()

