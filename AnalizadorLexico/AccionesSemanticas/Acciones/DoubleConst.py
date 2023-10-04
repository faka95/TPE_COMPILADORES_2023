import AnalizadorLexico.AccionesSemanticas.AccionSemantica as accion
import AnalizadorLexico.Lexico

class DoubleConst(accion.AccionSemantica):
    CONST_HIGHEXP = 38
    CONST_LOWEXP = -38
    CONST_LOWDEC = 1.17549435 * (10 ** CONST_LOWEXP)
    CONST_HIGHDEC = 3.40282347 * (10 ** CONST_HIGHEXP)

    def __init__(self, lexico: AnalizadorLexico.Lexico.Lexico):
        super().__init__(lexico)

    def ejecutar(self, caracterActual):
        self.lexico.bufferAdd(caracterActual)
        exponente = 0
        entero_decimal = 0
        if "E" in self.lexico.bufferLexema():
            numero = self.lexico.bufferLexema().split("E")
            exponente = int(numero[1])
            entero_decimal = float(numero[0])
        elif "e" in self.lexico.bufferLexema():
            numero = self.lexico.bufferLexema().split("e")
            exponente = int(numero[1])
            entero_decimal = float(numero[0])
        else:
            entero_decimal = float(self.lexico.bufferLexema())

        if (abs(exponente) > self.CONST_HIGHEXP):
            self.lexico.setTokenActual("error_yacc")
            self.lexico.escribirerror("Constante de tipo flotante FLOAT con exponente fuera de rango", self.lexico.bufferLexema())
        else:
            exponencial = float(10 ** exponente)
            resultado = float(entero_decimal * exponencial)
            if (resultado == 0.0):
                self.lexico.setTokenActual(self.lexico.bufferLexema())
            else:
                if (resultado <= self.CONST_LOWDEC):
                    self.lexico.setTokenActual("error_yacc")
                    self.lexico.escribirerror("Constante de tipo flotante FLOAT fuera de rango", self.lexico.bufferLexema())
                elif (resultado >= self.CONST_HIGHDEC):
                    self.lexico.setTokenActual("error_yacc")
                    self.lexico.escribirerror("Constante de tipo flotante FLOAT fuera de rango", self.lexico.bufferLexema())
                else:
                    #print(buffer)
                    self.lexico.setTokenActual(self.lexico.bufferLexema())

