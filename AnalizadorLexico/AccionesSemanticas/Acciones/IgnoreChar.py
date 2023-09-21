from AnalizadorLexico.AccionesSemanticas.Acciones_Semanticas import AccionSemantica
from AnalizadorLexico.Lexico import Lexico

class IgnoreChar(AccionSemantica):
    def __init__(self, lexico: Lexico):
        super().__init__(lexico)

    def ejecutar(self, buffer,caracterActual):
        buffer.clear()
