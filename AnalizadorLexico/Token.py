import numbers


class Token:  # NUMEROS PROVISORIOS (cambian segun lo que asigne el parser)
    IF = 300
    ELSE = 301
    END_IF = 302
    PRINT = 303
    CLASS = 304
    VOID = 305
    INT = 306
    ULONG = 307
    FLOAT = 308
    WHILE = 309
    DO = 310
    MENORIGUAL = 311
    MAYORIGUAL = 312
    DISTINTO = 313
    ID = 314
    ERROR = 315
    CADENA = 316
    NUM_INT = 317
    NUM_ULONG = 318
    NUM_FLOAT = 319
    RETURN = 320
    COMPIGUAL = 321

    def getToken(self):
        lexema = self.lexema
        if lexema == 'FIN':
            return 400
        elif lexema == '+':
            return 43
        elif lexema == '-':
            return 45
        elif lexema == ',':
            return 44
        elif lexema == '/':
            return 47
        elif lexema == '*':
            return 42
        elif lexema == '(':
            return 40
        elif lexema == ')':
            return 41
        elif lexema == '<':
            return 60
        elif lexema == '>':
            return 62
        elif lexema == '{':
            return 123
        elif lexema == '}':
            return 125
        elif lexema == ';':
            return 59
        elif lexema == '=':
            return 61
        elif lexema == '<=':
            return self.MENORIGUAL
        elif lexema == '>=':
            return self.MAYORIGUAL
        elif lexema == '!!':
            return self.DISTINTO
        elif lexema == '==':
            return self.COMPIGUAL
        elif lexema == 'IF':
            return self.IF
        elif lexema == 'ELSE':
            return self.ELSE
        elif lexema == 'END_IF':
            return self.END_IF
        elif lexema == 'PRINT':
            return self.PRINT
        elif lexema == 'CLASS':
            return self.CLASS
        elif lexema == 'VOID':
            return self.VOID
        elif lexema == 'INT':
            return self.INT
        elif lexema == 'ULONG':
            return self.ULONG
        elif lexema == 'FLOAT':
            return self.FLOAT
        elif lexema == 'error_yacc':
            return self.ERROR
        elif lexema == 'WHILE':
            return self.WHILE
        elif lexema == 'DO':
            return self.DO
        elif lexema == "RETURN":
            return self.RETURN
        elif str(lexema).startswith("%") and str(lexema).endswith("%"):
            return self.CADENA
        elif str(lexema).endswith("_i"):
            return self.NUM_INT
        elif str(lexema).endswith("_ul"):
            return self.NUM_ULONG
        elif str(lexema).__contains__("."):
            return self.NUM_FLOAT
        else:
            return self.ID

    def __init__(self, lexema, nrolinea):
        self._lineno = nrolinea
        self._lexema = lexema
        self._nro = self.getToken()

    @property
    def lexema(self):
        return self._lexema

    @property
    def value(self):
        return self._lexema

    @property
    def lineno(self):
        return self._lineno

    @lineno.setter
    def lineno(self, nro):
        self.lineno = nro

    @lexema.setter
    def lexema(self, value):
        self._lexema = value
        self._nro = self.getToken()

    @property
    def type(self):
        return self.getToken()

    def getLexema(self):
        return self._lexema

    def print(self):
        print("Token [lexema: '" + str(self.lexema) + "' , nro= " + str(self._nro) + "]")
