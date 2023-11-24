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
        self.variablesPolaca = {}

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
        tipos_asm = {"INT": "DW", "FLOAT": "DD", "ULONG": "DD"}  # DD para INT, DQ para FLOAT en MASM32
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
            self.variablesPolaca[info.raw_simbolo] = info

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
                    print(infoclase)
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
                declaracion = self.generar_declaracion_asm(item.raw_simbolo, item.tipo)
                declaraciones_asm.append(declaracion)
            elif item.ultimo_ambito in self.functions:
                declaracion = self.generar_declaracion_asm(item.raw_simbolo,item.tipo)
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
        self.numAux = 1
        self.header= ""

        self.ruta_archivo = "tabla_de_simbolos.txt"
        self.data = DataGenerator() #Si queres ver si existe una variable,el tipo el ambito, etc. Esta variable tiene 4 diccionarios con clases, funciones, variablesPolaca etc.
                                    #Si buscas una variable dada por la polaca, busca en variablesPolaca, por ejemplo, variable.raw_simbolo, que es el simbolo
                                    #Es el simbolo asi: simbolo_main_clase_b
        self.declaracion_asm = self.data.procesar_archivo(self.ruta_archivo)


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
        # TODO chequear tipo y si es flotante madnarlo a otra funcion
        op1 = self.pilaOperandos.pop(0)
        op2 = self.pilaOperandos.pop(0)
        registro = self.getRegistroExterno(self.celdaActual)
        if registro == Registros.EAX:
            registro = "EAX"
        else:
            registro = "EDX"
        self.codigo += "MOV " + registro + ", " + op1, "\n"
        if op == "+":
            self.codigo += "ADD " + registro + ", " + op2 + "\n"
        else:
            self.codigo += "SUB " + registro + ", " + op2 + "\n"


    def multODiv(self, op):
        op1 = self.pilaOperandos.pop(0)
        op2 = self.pilaOperandos.pop(0)
        if self.data.variablesPolaca.get(op1).tipo != self.data.variablesPolaca.get(op2).tipo:
            # TODO poner error
        else:

            if not self.registrosDisponibles[Registros.EBX]:
                self.liberar(Registros.EBX, self.celdaActual)
            if self.data.variablesPolaca.get(op1).tipo == "INT":
                self.codigo += "MOV EBX, " + op1, "\n"
                self.codigo += "CWD\n"
            elif self.data.variablesPolaca.get(op1).tipo == "ULONG":
                self.codigo += "MOV EBX, " + op1, "\n"
                self.codigo += "CWDE\n"
                self.codigo += "CDQ\n"
            if op == "*":
                self.codigo += "MUL " + op2 + "\n"
                if (not self.registrosDisponibles[Registros.ECX]):
                    self.liberar(Registros.ECX,self.celdaActual)
                self.codigo += "JO LabelErrorOvPE\n"
            else:
                if (not self.registrosDisponibles[Registros.ECX]):
                    self.liberar(Registros.ECX, self.celdaActual)
                if self.data.variablesPolaca.get(op2).tipo == "INT":
                    self.codigo += "MOV ECX, " + op2, "\n"
                    self.codigo += "CWD\n"
                elif self.data.variablesPolaca.get(op2).tipo == "ULONG":
                    self.codigo += "MOV ECX, " + op2, "\n"
                    self.codigo += "CWDE\n"
                    self.codigo += "CDQ\n"

                self.codigo += "JE LabelErrorDIV0\n"
                self.codigo += "DIV " + op2 + "\n";

        self.registrosDisponibles[Registros.EBX] = True
        #terceto.setRegistro(registros.EAX.name()); esto estaba aca.
    def operacionFlotante(self, op1, op2, op):
        if op == "+":
            self.codigo += "FLD " + op1 + "\n"
            self.codigo += "FADD " + op2 + "\n"
            # ErrorOverflow
        elif op == "-":
            self.codigo += "FLD " + op1 + "\n"
            self.codigo += "FSUB " + op2 + "\n"
        elif op == "*":
            self.codigo += "FLD " + op1 + "\n"
            self.codigo += "FMUL " + op2 + "\n"
            self.codigo += "FCOM MaxF32 \n"
            self.codigo += "FSTSW @mem2byte\n"
            if self.registrosDisponibles[Registros.EAX]:
                self.liberar(Registros.EAX, self.celdaActual)
            self.codigo += "MOV EAX , @mem2byte\n"
            self.codigo += "SAHF\n"
        elif op == "/":
            # error division por 0
            self.codigo += "FLD " + op2 + "\n"
            self.codigo += "FDIVR " + op1 + "\n"
        elif op == "=":
            self.codigo += "FLD " + op2 + "\n"
            self.codigo += "FSTP " + op1 + "\n"
        if op != "=":
            self.codigo += "FSTP @aux" + str(self.numAux) + "\n"
            self.numAux += 1


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

    def setHeader(self):
        self.header += "include \\masm32\\include\\masm32rt.inc\n"
        self.header += ".386\n"
        self.header += ".model flat\n"
        self.header += "option casemap :none\n"
        self.header += "include \\masm32\\include\\windows.inc\n"
        self.header += "include \\masm32\\include\\kernel32.inc\n"
        self.header += "include \\masm32\\include\\user32.inc\n"
        self.header += "includelib \\masm32\\lib\\kernel32.lib\n"
        self.header += "includelib \\masm32\\lib\\user32.lib\n"
        self.header += ".data\n"
        self.header += "Error db \"Error\", 0\n"
        self.header += "ErrorOvSF db \"Error: overflow en un suma entre flotantes\", 0\n"
        self.header += "ErrorOvPE db \"Error: overflow en una producto de enteros\", 0\n"
        self.header += "ErrorTYPE db \"Error: Error tipos incomatibles entre operadores\", 0\n"
        self.header += "ErrorDIV0 db \"Error: division por cero\", 0\n"
        self.header += "Salida dt ?, 0\n"
        self.header += "Imp db \"Salida por pantalla\", 0\n"
        self.header += "@mem2byte dw ? ; 32 bits\n"
        self.header += "MaxF32 dw 3.40282347E38 ; 32 bits \n"
