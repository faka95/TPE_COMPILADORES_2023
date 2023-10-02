from AnalizadorLexico.AccionesSemanticas.Acciones_Semanticas import AccionSemantica
from AnalizadorLexico.Lexico import Lexico

class DoubleConst(AccionSemantica):
    CONST_HIGHEXP = 38
    CONST_LOWEXP = -38
    CONST_LOWDEC = 1.17549435 * (10 ** CONST_LOWEXP)
    CONST_HIGHDEC = 3.40282347 * (10 ** CONST_HIGHEXP)

    def __init__(self, lexico: Lexico):
        super().__init__(lexico)

    def ejecutar(self, buffer,caracterActual):
        buffer += caracterActual
        exponente = 0
        entero_decimal = 0
        if "E" in buffer:
            numero = buffer.split("E")
            exponente = int(numero[1])
            entero_decimal = float(numero[0])
        elif "e" in buffer:
            numero = buffer.split("e")
            exponente = int(numero[1])
            entero_decimal = float(numero[0])
        else:
            entero_decimal = float(buffer)

        if (abs(exponente) > self.CONST_HIGHEXP):
            self.lexico.setTokenActual("error_yacc")
            self.lexico.escribirerror("Constante de tipo flotante FLOAT con exponente fuera de rango", buffer)
        else:
            exponencial = float(10 ** exponente)
            resultado = float(entero_decimal * exponencial)
            if (resultado == 0.0):
                self.lexico.setTokenActual(buffer)
            else:
                if (resultado <= self.CONST_LOWDEC):
                    self.lexico.setTokenActual("error_yacc")
                    self.lexico.escribirerror("Constante de tipo flotante FLOAT fuera de rango", buffer)
                elif (resultado >= self.CONST_HIGHDEC):
                    self.lexico.setTokenActual("error_yacc")
                    self.lexico.escribirerror("Constante de tipo flotante FLOAT fuera de rango", buffer)
                else:
                    self.lexico.setTokenActual(buffer)

