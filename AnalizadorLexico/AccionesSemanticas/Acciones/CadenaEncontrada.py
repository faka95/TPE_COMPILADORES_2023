import AnalizadorLexico.AccionesSemanticas.AccionSemantica as accion
import AnalizadorLexico.Lexico

class CadenaEncontrada(accion.AccionSemantica):
    def __init__(self, lexico: AnalizadorLexico.Lexico.Lexico):
        super().__init__(lexico)

    def ejecutar(self, buffer,caracterActual):
        buffer += caracterActual
        self.lexico.setTokenActual(buffer)
        buffer = ""

