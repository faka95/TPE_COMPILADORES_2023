import AnalizadorSemantico.PolacaInversa as Polaca

p = Polaca.ExpresionPolacaInversa()

example = "x = 3 + 4 * 5 + ( 7 + 8 )"
p.addElemento(3)
p.addElemento("+")
p.addElemento(4)
p.addElemento("*")
p.addElemento(5)
p.addElemento("+")
p.addElemento("(")
p.addElemento(7)
p.addElemento("+")
p.addElemento(8)
p.addElemento(")")
print(p.referencias)
p.setElemento(7)
print(p.referencias)
a = True
if a is True:
    print("hola")
else:
    a = 3 + 4

"""
def lookRef(self, elemento):
    with open("tabla_de_simbolos.txt", 'r') as file:
        for linea in file:
            if f"Simbolo: {elemento} -" in linea:
                partes = linea.split('-')
                for parte in partes:
                    if "referencias:" in parte:
                        referencia = parte.split(':')[-1].strip()
                        return int(referencia)
    return None
print(p.getAllOperando())
"""