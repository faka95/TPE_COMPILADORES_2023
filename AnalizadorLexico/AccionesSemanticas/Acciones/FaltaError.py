import AnalizadorLexico.AccionesSemanticas.AccionSemantica as accion
import AnalizadorLexico.Lexico


class FaltaError(accion.AccionSemantica):

    def __init__(self, lexico: AnalizadorLexico.Lexico.Lexico):
        super().__init__(lexico)

    def ejecutar(self, buffer, caracterActual):
        if not (caracterActual == "!"):
            self.lexico.setTokenActual("error_yacc")
            self.lexico.escribirError("Falta !")
        buffer = ""

