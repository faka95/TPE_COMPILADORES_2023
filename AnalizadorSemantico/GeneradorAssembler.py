from copy import copy

from AnalizadorSemantico.InformacionClase import InformacionClase


class DataGenerator:
    def __init__(self):
        self.classes = {}
        self.simboloClase = {}
        self.variables = {}
        self.functions = {}

    def procesar_linea(self, linea_texto):
        campos = {}
        partes = linea_texto.split(" - ")
        for parte in partes:
            if ": " in parte:
                clave, valor = parte.split(": ", 1)
                campos[clave.lower().replace(" ", "_")] = valor
        #print(campos)
        return InformacionClase(**campos)

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

    def setDatos(self,info: InformacionClase):
        if info.uso == "nombre de clase":
            self.simboloClase[info.simbolo] = info
        elif info.uso == "funcion":
            self.functions[info.simbolo] = info
        elif info.uso == "variable":
            self.variables[info.simbolo] = info
    def lookForProperty(self,propiedad) -> InformacionClase:
        aux = copy(self.variables.get(propiedad))
        return aux

    def lookForDeepProperty(self,clase: InformacionClase) -> []:
        list_c = []

        if clase.propiedades is not None:
            for item in clase.propiedades:
                list_c.append(self.lookForProperty(item))
        if clase.clase_herencia is not None:
            aux = self.lookForDeepProperty(copy(self.simboloClase.get(clase.clase_herencia)))
            if len(aux) != 0:
                list_c.extend(aux)
        return list_c

    def procesar_archivo(self,ruta_archivo):
        declaraciones_asm = []
        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                if linea.strip():  # Ignorar líneas vacías
                    infoclase = self.procesar_linea(linea)
                    self.setDatos(infoclase)

        for item in self.simboloClase.values():
                if item.simbolo not in self.classes:
                    new_struct = StructGen(item.simbolo)
                    if item.propiedades is not None:
                        for propiedad in item.propiedades:
                            prop = copy(self.lookForProperty(propiedad))
                            declaracion = self.generar_declaracion_asm(prop.simbolo,prop.tipo)
                            new_struct.addField(declaracion)

                    if item.clase_herencia is not None:
                        #print(item.clase_herencia)
                        list_clases = []
                        clase = copy(self.simboloClase.get(item.clase_herencia))
                        list_clases = self.lookForDeepProperty(clase)
                        print(list_clases)
                        for p in list_clases:

                            declaracion = self.generar_declaracion_asm(p.simbolo,p.tipo)
                            new_struct.addField(declaracion)
                    self.classes[item.simbolo] = new_struct

        for item in self.variables.values():
            if item.ultimo_ambito == "main":
                declaracion = self.generar_declaracion_asm(item.simbolo,item.tipo)
                declaraciones_asm.append(declaracion)
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
