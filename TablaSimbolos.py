class TablaDeSimbolos:
    def __init__(self, archivo_tabla):
        self.simbolos = {}
        self.archivo_tabla = archivo_tabla

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
        self.archivo_tabla.write("Tabla de Simbolos: " + "\n")
        for lexema, id in self.simbolos.items():
            self.archivo_tabla.write("Lexema: {} ID: {}".format(lexema, id) + "\n")
"""
ts = TablaDeSimbolos()
ts.addSimbolo("+",3)
ts.addSimbolo("-",4)
ts.addSimbolo("/",5)
ts.addSimbolo("!!",6)
priSnt(ts.getSimbolo("+"))
"""