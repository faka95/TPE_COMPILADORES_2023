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
        self.E2 = None
        self.matrizAccionesSemanticas = None
