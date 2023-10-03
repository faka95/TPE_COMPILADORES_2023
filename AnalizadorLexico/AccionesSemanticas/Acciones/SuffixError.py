import AnalizadorLexico.AccionesSemanticas.AccionSemantica as accion
import AnalizadorLexico.Lexico


class SuffixError(accion.AccionSemantica):
    SUFFIX_16BIT = "_i"
    SUFFIX_32BIT = "_ul"
    def __init__(self, lexico: AnalizadorLexico.Lexico.Lexico):
        super().__init__(lexico)

    def ejecutar(self, buffer, caracterActual):
        if not (buffer.endswith(self.SUFFIX_32BIT) or buffer.endswith(self.SUFFIX_16BIT)):
            self.lexico.setTokenActual("error_yacc")
            self.lexico.escribirError("Entero no contiene Sufijo")

        buffer = ""
