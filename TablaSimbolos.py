class TablaDeSimbolos:
    def __init__(self, archivo_tabla):
        self.simbolos = {}
        self.archivo_tabla = archivo_tabla

    def addSimbolo(self, lexema):
        if lexema not in self.simbolos:
            self.simbolos[lexema] = {"referencias": 1}
        else:
            self.simbolos[lexema]["referencias"] = self.simbolos[lexema]["referencias"] + 1

    def addCaracteristica(self, lexema, caracteristica, valor):
        if lexema not in self.simbolos:
            self.simbolos[lexema] = {caracteristica: valor, "referencias": 1}
        else:
            self.simbolos[lexema][caracteristica] = valor

    def aumentarReferencia(self, lexema):
        if lexema in self.simbolos:
            self.simbolos[lexema]["referencias"] = self.simbolos[lexema]["referencias"] + 1

    def reducirReferencia(self, lexema):
        if lexema in self.simbolos:
            self.simbolos[lexema]["referencias"] = self.simbolos[lexema]["referencias"] - 1

    def getSimbolo(self, lexema):
        return self.simbolos.get(lexema)  # retorna el mapa de caracteristicas de ese simbolo

    def getCaracteristica(self, lexema, caracteristica):
        if caracteristica in self.simbolos.keys():
            return self.simbolos[lexema][caracteristica]
        else:
            print("ERROR: no existe columna ", caracteristica, ", en el lexema ", lexema)

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