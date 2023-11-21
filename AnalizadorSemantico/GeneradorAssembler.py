class DataGenerator:
    def __init__(self):
        self.classes = {}

    def procesar_linea(self, linea):
        try:
            partes = linea.split(" - ")
            parte_simbolo = partes[0]
            parte_tipo = partes[1]
            simbolo = parte_simbolo.split(": ")[1]
            tipo = parte_tipo.split(": ")[2]

            return simbolo, tipo
        except IndexError:
            # Devolver None si no se encuentra el formato esperado
            return None, None
    def generar_declaracion_asm(self,simbolo, tipo):
        tipos_asm = {"INT": "DD", "FLOAT": "DQ"}  # DD para INT, DQ para FLOAT en MASM32
        clase = None
        if (tipos_asm.get(tipo,None)) is None:
            if tipo in self.classes:
                clase = tipo
                return f"{simbolo} {clase} <>"
        else:
            return f"{simbolo} {tipos_asm.get(tipo)} ?"  # Pone '?' si el tipo no se reconoce
    def ifClass(self,simbolo:str):
        lexema = simbolo
        partes = lexema.split(':')
        if len(partes) > 2:
            return partes[-1]
        elif len(partes) == 2:
            return partes[1]
        else:
            return None


    def procesar_archivo(self,ruta_archivo):
        declaraciones_asm = []
        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                if linea.strip():  # Ignorar líneas vacías
                    simbolo, tipo = self.procesar_linea(linea)
                    if tipo != "func" and tipo != "clase":
                        clase = self.ifClass(str(simbolo))
                        #print(clase)
                        declaracion = self.generar_declaracion_asm(simbolo, tipo)
                        print(declaracion)
                        if (clase is not None) and (clase != "main"):
                            if clase in self.classes:
                                self.classes[clase].addField(declaracion)
                            else:
                                new_struct = StructGen(clase)
                                self.classes[clase] = new_struct
                        elif clase == "Main" or clase == "main":
                            declaraciones_asm.append(declaracion)
        #print(declaraciones_asm)
        return declaraciones_asm
    def getStruct(self):
        structures = []
        for a in self.classes.values():
            structures.append(a.toStr())
        return structures

class StructGen:
    def __init__(self,name):
        self.name = name + " STRUCT"
        self.fields = []
        self.end = name + " END"

    def addField(self,declaracion:str):
        self.fields.append(declaracion)
    def toStr(self):
        field = self.name
        espacios_indentacion = 4
        structs = "     \n".join(" " * espacios_indentacion + linea for linea in self.fields)
        return field + "\n" + structs + "\n" + self.end + "\n"
#class CodeGenerator:


"""# Ruta al archivo de la tabla de símbolos
ruta_archivo = "tabla_de_simbolos.txt"
declaracion_asm = DataGenerator.procesar_archivo(ruta_archivo)

# Unir las declaraciones para formar la sección .data del código Assembler
codigo_asm_data = ".data\n" + "\n".join(declaracion_asm)
print(codigo_asm_data)"""