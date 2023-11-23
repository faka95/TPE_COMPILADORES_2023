from copy import copy

from AnalizadorSemantico.InformacionClase import InformacionClase
from enum import Enum
from AnalizadorSemantico import PolacaInversa


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
        # print(campos)
        return InformacionClase(**campos)

    def generar_declaracion_asm(self, simbolo, tipo):
        tipos_asm = {"INT": "DD", "FLOAT": "DQ"}  # DD para INT, DQ para FLOAT en MASM32
        clase = None
        if (tipos_asm.get(tipo, None)) is None:
            if tipo in self.classes:
                clase = tipo
                return f"{simbolo} {clase} <>"
        else:
            return f"{simbolo} {tipos_asm.get(tipo)} ?"  # Pone '?' si el tipo no se reconoce

    def ifClass(self, simbolo: str):
        lexema = simbolo
        partes = lexema.split(':')
        if len(partes) > 2:
            return partes[-1]
        elif len(partes) == 2:
            return partes[1]
        else:
            return None

    def setDatos(self, info: InformacionClase):
        if info.uso == "nombre de clase":
            self.simboloClase[info.simbolo] = info
        elif info.uso == "funcion":
            self.functions[info.simbolo] = info
        elif info.uso == "variable":
            self.variables[info.simbolo] = info

    def lookForProperty(self, propiedad) -> InformacionClase:
        aux = copy(self.variables.get(propiedad))
        return aux

    def lookForDeepProperty(self, clase: InformacionClase) -> []:
        list_c = []

        if clase.propiedades is not None:
            for item in clase.propiedades:
                list_c.append(self.lookForProperty(item))
        if clase.clase_herencia is not None:
            aux = self.lookForDeepProperty(copy(self.simboloClase.get(clase.clase_herencia)))
            if len(aux) != 0:
                list_c.extend(aux)
        return list_c

    def procesar_archivo(self, ruta_archivo):
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
                        declaracion = self.generar_declaracion_asm(prop.simbolo, prop.tipo)
                        new_struct.addField(declaracion)

                if item.clase_herencia is not None:
                    # print(item.clase_herencia)
                    list_clases = []
                    clase = copy(self.simboloClase.get(item.clase_herencia))
                    list_clases = self.lookForDeepProperty(clase)
                    print(list_clases)
                    for p in list_clases:
                        declaracion = self.generar_declaracion_asm(p.simbolo, p.tipo)
                        new_struct.addField(declaracion)
                self.classes[item.simbolo] = new_struct

        for item in self.variables.values():
            if item.ultimo_ambito == "main":
                declaracion = self.generar_declaracion_asm(item.simbolo, item.tipo)
                declaraciones_asm.append(declaracion)
        return declaraciones_asm

    def getStruct(self):
        structures = []
        for a in self.classes.values():
            structures.append(a.toStr())
        return structures


class StructGen:
    def __init__(self, name):
        self.name = name + " STRUCT"
        self.fields = []
        self.end = name + " END"

    def addField(self, declaracion: str):
        self.fields.append(declaracion)

    def toStr(self):
        field = self.name
        espacios_indentacion = 4
        structs = "     \n".join(" " * espacios_indentacion + linea for linea in self.fields)
        return field + "\n" + structs + "\n" + self.end + "\n"


class Registros(Enum):
    EAX = 1
    EBX = 2
    ECX = 3
    EDX = 4


class CodeGenerator:
    def __init__(self, polaca: PolacaInversa):
        self.polaca = polaca
        self.celdaActual = 1
        self.operadores = ["+", "-", "*", "/", "BI", "BF", "FUNCION", "ret", "=", "<", "<=", ">=", "==", "=!",
                          "CALLFUNC", "PRINT"]
        self.codigo = ""
        self.pilaOperandos = []
        self.registrosDisponibles = {Registros.EAX: True, Registros.EBX: True, Registros.ECX: True, Registros.EDX: True}
        self.tira = polaca.referencias


    def getRegistroExterno(self, celdaActual):
        if self.registrosDisponibles[Registros.EAX]:
            return Registros.EAX
        elif self.registrosDisponibles[Registros.EDX]:
            return Registros.EDX
        else:
            self.liberar(Registros.EAX, celdaActual)
            return Registros.EAX

    def getRegistroInterno(self, celdaActual):
        if self.registrosDisponibles[Registros.EBX]:
            return Registros.EBX
        elif self.registrosDisponibles[Registros.ECX]:
            return Registros.ECX
        else:
            self.liberar(Registros.EBX, celdaActual)
            return Registros.EBX

    def liberar(self, registro, celdaAactual):
        aux = celdaAactual  # esto no va
        # TODO guardar el registro en un auxiliar y ponerle True el registroDisponible

    def sumaOResta(self, op):
        pass

    def multODiv(self, op):
        pass

    def generarCodigoAssembler(self):
        celda = self.tira[self.celdaActual]
        if celda in self.operadores:
            if celda == "+":
                self.sumaOResta(celda)
            elif celda == "-":
                self.sumaOResta(celda)
            elif celda == "*":
                self.multODiv(celda)
            elif celda == "/":
                self.multODiv(celda)
            elif celda == "BI":
                pass  # TODO
            elif celda == "BF":
                pass  # TODO
            elif celda == "FUNCION":
                pass  # TODO
            elif celda == "ret":
                pass  # TODO
            elif celda == "=":
                pass  # TODO
            elif celda == "<":
                pass  # TODO
            elif celda == "<=":
                pass  # TODO
            elif celda == ">=":
                pass  # TODO
            elif celda == "==":
                pass  # TODO
            elif celda == "=!":
                pass  # TODO
            elif celda == "CALLFUNC":
                pass  # TODO
            elif celda == "PRINT":
                pass  # TODO
        else:
            self.pilaOperandos.append(celda)
        self.celdaActual += 1


"""# Ruta al archivo de la tabla de símbolos
ruta_archivo = "tabla_de_simbolos.txt"
declaracion_asm = DataGenerator.procesar_archivo(ruta_archivo)

# Unir las declaraciones para formar la sección .data del código Assembler
codigo_asm_data = ".data\n" + "\n".join(declaracion_asm)
print(codigo_asm_data)"""
