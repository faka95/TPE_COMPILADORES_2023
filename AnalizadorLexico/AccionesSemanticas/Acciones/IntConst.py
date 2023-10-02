from AnalizadorLexico.AccionesSemanticas.Acciones_Semanticas import AccionSemantica
from AnalizadorLexico.Lexico import Lexico

class IntConst(AccionSemantica):
    CONST_16BIT = 2**15
    SUFFIX_16BIT = "_i"
    CONST_UNSIGNED_32BIT = 2**32 - 1
    SUFFIX_32BIT = "_ul"
    def __init__(self, lexico: Lexico):
        super().__init__(lexico)
    def rango_i(self,numero):
        if (numero >= (self.CONST_16BIT * (-1))) and (numero <= (self.CONST_16BIT - 1)):
            return True
        else: return False

    def rango_ul(self, numero):
        if (numero >= 0) and (numero <= self.CONST_UNSIGNED_32BIT):
            return True
        else: return False

    def ejecutar(self, buffer,caracterActual):
        buffer += caracterActual
        parte_numerica = ""

        if buffer[0] == "-":
            parte_numerica += buffer[0]

        for caracter in buffer:
            if caracter.isdigit():
                parte_numerica += caracter

        for letra in buffer:
            #Error si el sufijo contiene mayusculas
            if letra.isupper():
                self.lexico.setTokenActual("error_yacc")
                self.lexico.escribirError("Sufijo contiene mayusculas.")
                return

        if buffer.endswith(self.SUFFIX_16BIT):
            if not (self.rango_i(int(parte_numerica))):
                self.lexico.setTokenActual("error_yacc")
                self.lexico.escribirerror("Constante entera INT fuera de rango", buffer)
                return
            else:
                self.lexico.setTokenActual(buffer)

        elif buffer.endswith(self.SUFFIX_32BIT):
            if not (self.rango_ul(int(parte_numerica))):
                self.lexico.setTokenActual("error_yacc")
                self.lexico.escribirerror("Constante entera ULONG fuera de rango", buffer)
                return
            else:
                self.lexico.setTokenActual(buffer)





