def columna(caracterActual):
    pass

class Lexico:
    FINAL = 99
    ERROR = 100
    nroLinea = 1  # inicia en la primera linea
    indice = [0]
    termino = False
    erroresLex = 0
    lexema = ""
    programa = ""
    # matrizDeAcciones semanticas
    # tokenActual
    # escribirError
    matrizDeTransiciones = [
    #letra digito    /      *      +      -     =      <       >      {      }      (      )      ,      ;      .     %      _      u      i     e/E     !   Blc/tab   nl    otro   #estado
    [    1,     9, FINAL,     3, FINAL, FINAL,     7,     5,     6, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,    12,     2,     1,     1,     1,     1,     8,     0,     0, ERROR],  # 0
    [    1,     1, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,     1,     2,     2,     2,     2,     2,     2, ERROR],  # 1
    [    1,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2,     2, FINAL,     2,     2,     2,     2,     2,     2,     2, ERROR],  # 2
    [FINAL, FINAL, FINAL,     4, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, ERROR],  # 3
    [FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,     4, ERROR],  # 4
    [FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, ERROR],  # 5
    [FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, ERROR],  # 6
    [FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, ERROR],  # 7
    [ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, FINAL, ERROR, ERROR, ERROR],  # 8
    [ERROR,     9, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR,    13, ERROR,    10, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR],  # 9
    [ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR,    11, FINAL, ERROR, ERROR, ERROR, ERROR, ERROR],  # 10
    [ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, FINAL, ERROR, ERROR, ERROR, ERROR, ERROR],  # 11
    [ERROR,    13, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR],  # 12
    [FINAL,    13, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,    14, FINAL, FINAL, FINAL, ERROR],  # 13
    [ERROR, ERROR, ERROR, ERROR,    15,    15, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR],  # 14
    [ERROR,    16, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR],  # 15
    [FINAL,    16, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL],  # 16
    ]

    def __init__(self, programa):
        self.programa = programa
    def yyLex(self, programa):
        if self.indice[0] == len(programa):
            return "Fin"
        estado = 0
        tokenActual = None
        while tokenActual is None:
            caracterActual = self.indice[0]
            if programa[caracterActual] == 13:
                self.indice[0] += 1
                caracterActual = programa[self.indice[0]]
            if caracterActual == 10:
                self.nroLinea += 1
            estadoSig = self.matrizDeTransiciones[estado][columna(caracterActual)]
            #AccionSemantica accion = accionesSemanticas.getAccion(estado,paridad(c));
            #accion.ejecutar(bufferLexema,indice,c);
            estado = estadoSig
            self.indice[0] += 1
            if self.indice[0] >= len(programa):
                return "TokenFin"
            if estadoSig == self.FINAL:
                break
        print("TokenActual")
        return "TokenActual"

    # faltan cosas del Lexico de java
