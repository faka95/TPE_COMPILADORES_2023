from AnalizadorLexico.AccionesSemanticas.Acciones_Semanticas import AccionSemantica
from AnalizadorLexico.Lexico import Lexico

""" Identificadores cuyos nombres pueden tener hasta 20 caracteres de longitud. El primer puede ser una letra o ‟_‟, y
el resto pueden ser letras, dígitos y “_”. Los identificadores con longitud mayor serán truncados y esto se
informará como Warning. Las letras utilizadas en los nombres de identificador sólo pueden ser minúsculas. """

class IdReturnLast(AccionSemantica):
    def __init__(self, lexico: Lexico):
        super().__init__(lexico)

    def ejecutar(self, buffer,caracterActual):
        if len(buffer) <= 20: #Esperar respuesta de paula a ver que hago con las letras mayusculas
            self.lexico.setTokenActual(buffer)
        else:
            self.lexico.setTokenActual(buffer[:20])  # Se trunca el lexema
            self.lexico.escribirError("Lexema supera el tamaño máximo de 20")