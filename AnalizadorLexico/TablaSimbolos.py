class TablaDeSimbolos:
    def __init__(self):
        self.simbolos = {}

    def addSimbolo(self, lexema, id):
        if lexema not in self.simbolos:
            self.simbolos[lexema] = id

    def getSimbolo(self, lexema):
        return self.simbolos.get(lexema)

    def removerSimbolo(self, lexema):
        del self.simbolos[lexema]

    def isKey(self, lexema):
        return lexema in self.simbolos

    def imprimirTabla(self):
        print("Tabla de Simbolos: ")
        for lexema, id in self.simbolos.items():
            print("Lexema: {} ID: {}".format(lexema, id))
"""
ts = TablaDeSimbolos()
ts.addSimbolo("+",3)
ts.addSimbolo("-",4)
ts.addSimbolo("/",5)
ts.addSimbolo("!!",6)
priSnt(ts.getSimbolo("+"))
"""