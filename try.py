import AnalizadorSemantico.PolacaInversa as Polaca
from AnalizadorSemantico.GeneradorAssembler import DataGenerator

p = Polaca.ExpresionPolacaInversa()
"""
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

"""def ifClass(simbolo):
    partes = simbolo.split(':')
    # Si el token tiene más de dos partes, la última parte es el ámbito real.
    if len(partes) > 2:
        return partes[-1]
    # Si el token tiene solo dos partes, el ámbito es el segundo elemento.
    elif len(partes) == 2:
        return partes[1]
    else:
        # Si el token no tiene el formato esperado, devolver None o un error.
        return None

print(ifClass("hola:main"))"""
# Ruta al archivo de la tabla de símbolos
ruta_archivo = "tabla_de_simbolos.txt"
data = DataGenerator()
declaracion_asm = data.procesar_archivo(ruta_archivo)

# Unir las declaraciones para formar la sección .data del código Assembler
codigo_asm_data = ".data\n" + "\n".join("\n" + linea for linea in data.getStruct()) + "\n" +  "\n".join(declaracion_asm)
#espacios_indentacion = 4

# Crear la sección .data con indentación para cada línea
#codigo_asm_data = ".data\n" + "\n".join(" " * espacios_indentacion + linea for linea in data.getStruct()) + "\n" + "\n".join(declaracion_asm)
nombre_archivo = "programa.asm"
with open(nombre_archivo, "w") as archivo:
    archivo.write(codigo_asm_data)
#print(codigo_asm_data)
print(data.classes)