from AnalizadorLexico.AccionesSemanticas.Acciones_Semanticas import AccionSemantica
from AnalizadorLexico.Lexico import Lexico


class SimpleChar(AccionSemantica):
    def __init__(self, lexico: Lexico):
        super().__init__(lexico)

    def ejecutar(self, buffer, caracterActual):
        buffer.clear()
        buffer.append(caracterActual)
        self.lexico.setTokenActual(buffer)
        buffer.clear()
