import AnalizadorLexico.AccionesSemanticas.AccionSemantica as accion
import AnalizadorLexico.Lexico

""" Identificadores cuyos nombres pueden tener hasta 20 caracteres de longitud. El primer puede ser una letra o ‟_‟, y
el resto pueden ser letras, dígitos y “_”. Los identificadores con longitud mayor serán truncados y esto se
informará como Warning. Las letras utilizadas en los nombres de identificador sólo pueden ser minúsculas. """

class IdConsumeLast(accion.AccionSemantica):
    def __init__(self, lexico: AnalizadorLexico.Lexico.Lexico):
        super().__init__(lexico)

    def ejecutar(self, caracterActual):
        self.lexico.bufferAdd(caracterActual)
        for letra in self.lexico.bufferLexema():
            if letra.isupper():
                self.lexico.setTokenActual("error_yacc");
                self.lexico.escribirError("Identificador contiene mayusculas.")
                return
        if len(self.lexico.bufferLexema()) <= 20: #Esperar respuesta de paula a ver que hago con las letras mayusculas
            self.lexico.setTokenActual(self.lexico.bufferLexema())
        else:
            self.lexico.setTokenActual(self.lexico.bufferLexema()[:20])  # Se trunca el lexema
            self.lexico.escribirError("Lexema supera el tamaño máximo de 20")