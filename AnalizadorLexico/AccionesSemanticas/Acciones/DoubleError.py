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

    def ejecutar(self, buffer, caracterActual):
        if not (self.checkFloat(buffer)):
            self.lexico.setTokenActual("error_yacc")
            self.lexico.escribirError("Contiene letras o no contiene digitos")
        else:
            if ("e" in buffer or "E" in buffer):
                if not ("+" in buffer or "-" in buffer):
                    self.lexico.setTokenActual("error_yacc")
                    self.lexico.escribirError("Contiene letras o no contiene digitos")

        buffer = ""

