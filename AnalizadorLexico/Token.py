class Token:  # NUMEROS PROVISORIOS (cambian segun lo que asigne el parser)
    IF = 0
    ELSE = 1
    END_IF = 2
    PRINT = 3
    CLASS = 4
    VOID = 5
    INT = 6
    ULONG = 7
    FLOAT = 8
    WHILE = 9
    DO = 10
    MENORIGUAL = 11
    MAYORIGUAL = 12
    DISTINTO = 13
    ID = 14
    ERROR = 15
    CADENA = 16

    def getToken(self):
        lexema = self.lexema
        if lexema == 'FIN':
            return 200
        elif lexema == '+':
            return 43
        elif lexema == '-':
            return 45
        elif lexema == ',':
            return 44
        elif lexema == '/':
            return 43
        elif lexema == '*':
            return 43
        elif lexema == '(':
            return 43
        elif lexema == ')':
            return 43
        elif lexema == '<':
            return 43
        elif lexema == '>':
            return 43
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
        elif str(lexema).startswith("%") and str(lexema).endswith("%"):
            return self.CADENA
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
