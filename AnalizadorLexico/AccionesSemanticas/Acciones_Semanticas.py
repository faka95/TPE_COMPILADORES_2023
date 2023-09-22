from abc import ABC,abstractmethod
import AnalizadorLexico.Lexico as Lexico
class AccionSemantica(ABC):
    def __init__(self, lexico: Lexico):
        self.lexico = lexico

    @abstractmethod
    def ejecutar(self, buffer,caracterActual):
        pass


class AccionesSemanticas:
    def __init__(self, lexico):
        self.lexico = lexico
        self.AS0 = None
        self.AS1 = None
        self.AS2 = None
        self.AS3 = None
        self.AS4 = None
        self.AS5 = None
        self.AS6 = None
        self.AS7 = None
        self.AS8 = None
        self.E1 = None
        self.E2 = None
        self.E3 = None
        self.E4 = None
        self.matrizAccionesSemanticas = [
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
