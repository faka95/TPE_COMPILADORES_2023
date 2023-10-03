from abc import ABC,abstractmethod
import AnalizadorLexico.Lexico
import AnalizadorLexico.AccionesSemanticas.Acciones.AddChar as Addchar
import AnalizadorLexico.AccionesSemanticas.Acciones.IgnoreChar as IgnoreChar
import AnalizadorLexico.AccionesSemanticas.Acciones.InitBuffer as InitBuffer
import AnalizadorLexico.AccionesSemanticas.Acciones.SimpleChar as SimpleChar
import AnalizadorLexico.AccionesSemanticas.Acciones.CadenaEncontrada as CadenaEncontrada
import AnalizadorLexico.AccionesSemanticas.Acciones.DoubleConst as DoubleConst
import AnalizadorLexico.AccionesSemanticas.Acciones.IdConsumeLast as IdConsumeLast
import AnalizadorLexico.AccionesSemanticas.Acciones.IdReturnLast as IdReturnLast
import AnalizadorLexico.AccionesSemanticas.Acciones.IntConst as IntConst
import AnalizadorLexico.AccionesSemanticas.Acciones.CharError as CharError
import AnalizadorLexico.AccionesSemanticas.Acciones.DoubleError as DoubleError
import AnalizadorLexico.AccionesSemanticas.Acciones.FaltaError as FaltaError
import AnalizadorLexico.AccionesSemanticas.Acciones.SuffixError as SuffixError
class AccionesSemanticas:
    def __init__(self, lexico: AnalizadorLexico.Lexico.Lexico):
        self.lexico = lexico
        self.AS0 = IgnoreChar.IgnoreChar(self.lexico)
        self.AS1 = InitBuffer.InitBuffer(self.lexico)
        self.AS2 = Addchar.AddChar(self.lexico)
        self.AS3 = IdReturnLast.IdReturnLast(self.lexico)
        self.AS4 = IdConsumeLast.IdConsumeLast(self.lexico)
        self.AS5 = IntConst.IntConst(self.lexico)
        self.AS6 = DoubleConst.DoubleConst(self.lexico)
        self.AS7 = CadenaEncontrada.CadenaEncontrada(self.lexico)
        self.AS8 = SimpleChar.SimpleChar(self.lexico)
        self.E1 = SuffixError.SuffixError(self.lexico)
        self.E2 = CharError.CharError(self.lexico)
        self.E3 = FaltaError.FaltaError(self.lexico)
        self.E4 = DoubleError.DoubleError(self.lexico)
        self._matrizAccionesSemanticas = [
    #   letra       digito          /          *           +           -            =          <           >           {            }         (          )           ,               ;       .             %           _           u          i          e/E          !        Blc/tab       nl         otro   #estado
    [  self.AS1,   self.AS1,   self.AS8,   self.AS1,   self.AS8,   self.AS8,   self.AS1,   self.AS1,   self.AS1,   self.AS8,   self.AS8,   self.AS8,   self.AS8,   self.AS8,   self.AS8,   self.AS1,   self.AS1,   self.AS1,   self.AS1,   self.AS1,   self.AS1,   self.AS1,   self.AS0,   self.AS0, self.E2],  # 0
    [  self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS7,   self.AS1,   self.AS1,   self.AS1,   self.AS1,   self.AS1,   self.AS0,   self.AS0, self.E2],  # 1
    [  self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS4,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3, self.E2],  # 2
    [  self.AS3,   self.AS3,   self.AS3,   self.AS2,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3, self.E2],  # 3
    [  self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS2,   self.AS4, self.E2],  # 4
    [  self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS4,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3, self.E2],  # 5
    [  self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS4,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3, self.E2],  # 6
    [  self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS4,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3,   self.AS3, self.E2],  # 6
    [   self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,    self.E3,   self.AS4,    self.E3,    self.E3, self.E2],  # 8
    [   self.E1,    self.E1,   self.AS2,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,   self.AS2,    self.E1,   self.AS2,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1, self.E2],  # 9
    [   self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,   self.AS2,   self.AS5,    self.E1,    self.E1,    self.E1,    self.E1, self.E2],  # 10
    [   self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,    self.E1,   self.AS5,    self.E1,    self.E1,    self.E1,    self.E1, self.E2],  # 11
    [   self.E1,    self.E4,   self.AS2,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4, self.E2],  # 12
    [  self.AS6,   self.AS2,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS2,   self.AS6,   self.AS6,   self.AS6, self.E2],  # 13
    [   self.E4,    self.E4,    self.E4,    self.E4,   self.AS2,   self.AS2,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4, self.E2],  # 14
    [   self.E4,   self.AS2,    self.E4,    self.E4,   self.AS2,   self.AS2,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4,    self.E4, self.E2],  # 15
    [  self.AS6,   self.AS2,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS6,   self.AS2,   self.AS6,   self.AS6,   self.AS6, self.E2],  # 13
    ]

    @property
    def matrizAccionesSemanticas(self):
        return self._matrizAccionesSemanticas

    @classmethod
    def getAccion(cls, fila, columna):
        return cls.matrizAccionesSemanticas[fila][columna]
