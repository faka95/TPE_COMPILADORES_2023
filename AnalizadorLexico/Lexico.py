import importlib

class Lexico:
    FINAL = 99
    ERROR = 100
    termino = False
    erroresLex = 0
    # escribirError
    matrizDeTransiciones = [
        # letra digito    /      *      +      -     =      <       >      {      }      (      )      ,      ;      .     %      _      u      i     e/E     !   Blc/tab   nl    otro   #estado
        [1, 9, FINAL, 3, FINAL, FINAL, 7, 5, 6, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, 12, 2, 1, 1, 1, 1, 8, 0, 0,
         ERROR],  # 0
        [1, 1, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,
         1, 2, 2, 2, 2, 2, 2, ERROR],  # 1
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, FINAL, 2, 2, 2, 2, 2, 2, 2, ERROR],  # 2
        [FINAL, FINAL, FINAL, 4, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,
         FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, ERROR],  # 3
        [FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,
         FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, 4, ERROR],  # 4
        [FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,
         FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, ERROR],  # 5
        [FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,
         FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, ERROR],  # 6
        [FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,
         FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, ERROR],  # 7
        [ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR,
         ERROR, ERROR, ERROR, ERROR, ERROR, FINAL, ERROR, ERROR, ERROR],  # 8
        [ERROR, 9, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, 13, ERROR,
         10, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR],  # 9
        [ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR,
         ERROR, ERROR, 11, FINAL, ERROR, ERROR, ERROR, ERROR, ERROR],  # 10
        [ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR,
         ERROR, ERROR, ERROR, FINAL, ERROR, ERROR, ERROR, ERROR, ERROR],  # 11
        [ERROR, 13, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR,
         ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR],  # 12
        [FINAL, 13, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,
         FINAL, FINAL, FINAL, FINAL, 14, FINAL, FINAL, FINAL, ERROR],  # 13
        [ERROR, ERROR, ERROR, ERROR, 15, 15, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR,
         ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR],  # 14
        [ERROR, 16, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR,
         ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR],  # 15
        [FINAL, 16, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,
         FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL],  # 16
    ]

    columna = {
        '/': 2,
        '*': 3,
        '+': 4,
        '-': 5,
        '=': 6,
        '<': 7,
        '>': 8,
        '{': 9,
        '}': 10,
        '(': 11,
        ')': 12,
        ',': 13,
        ';': 14,
        '.': 15,
        '%': 16,
        '_': 17,
        '!': 21,
    }

    # habria que ver como funcionaría con tab nl y espacio
    def getColumna(self, caracter):
        ascii = ord(caracter)
        if ascii == 69 | ascii == 101:  # e/E
            return 20
        elif ascii == 117:  # u
            return 18
        elif ascii == 105:  # i
            return 19
        elif ascii > 64 & ascii < 91 | ascii > 96 & ascii < 123:  # letras restantes
            return 0
        elif ascii > 47 & ascii < 58:  # numeros
            return 1
        elif ascii == 32 | ascii == 9:  # espacio/tab
            return 22
        elif ascii == 10 | ascii == 13:  # new line/carriage return
            return 23
        else:
            return self.columna.get(caracter, 24)  # resto de simbolos

    def __init__(self, programa):
        self._programa = programa
        self._tokenActual = None
        self._indice = [0]
        self._nroLinea = 1
        self._bufferLexema = ""

    @property
    def tokenActual(self):
        return self._tokenActual

    @tokenActual.setter
    def tokenActual(self, value):
        self._tokenActual = value

    @property
    def nroLinea(self):
        return self._nroLinea

    @nroLinea.setter
    def nroLinea(self, value):
        self._nroLinea = value

    @property
    def indice(self):
        return self._indice

    @indice.setter
    def indice(self, value):
        self._indice = value

    @property
    def bufferLexema(self):
        return self._bufferLexema

    @bufferLexema.setter
    def bufferLexema(self, value):
        self._bufferLexema = value

    def yyLex(self, programa):
        if self._indice[0] == len(programa)+1:
            return "Fin"
        estado = 0
        token_actual = None
        while token_actual is None:
            caracter_actual = programa[self._indice[0]]
            if caracter_actual == 13:
                self._indice[0] += 1
                caracter_actual = programa[self._indice[0]]
            if caracter_actual == 10:
                self.nroLinea += 1
            estado_sig = self.matrizDeTransiciones[estado][self.getColumna(caracter_actual)]
            print(estado_sig)
            acciones_mod = importlib.import_module('AccionesSemanticas.Acciones_Semanticas')
            acciones = getattr(acciones_mod,"AccionesSemanticas")
            accion = acciones.AccionesSemanticas.getAccion(estado, self.getColumna(caracter_actual))
            accion.ejecutar(self.bufferLexema, caracter_actual)
            estado = estado_sig
            self._indice[0] += 1
            if self._indice[0] >= len(programa):
                return "FIN"
            if estado_sig == self.FINAL:
                break
        print("TokenActual: " + str(token_actual))
        return token_actual
