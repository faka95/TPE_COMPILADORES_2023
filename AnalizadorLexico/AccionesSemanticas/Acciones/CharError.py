import AnalizadorLexico.AccionesSemanticas.AccionSemantica as accion
import AnalizadorLexico.Lexico


class CharError(accion.AccionSemantica):

    def __init__(self, lexico: AnalizadorLexico.Lexico.Lexico):
        super().__init__(lexico)

    def ejecutar(self,caracterActual):
        if (not caracterActual.isalpha()) and not (caracterActual in self.lexico.columna.keys()):
            self.lexico.setTokenActual("error_yacc")
            self.lexico.escribirError("Caractero no soportado")
        self.lexico.bufferClear()

