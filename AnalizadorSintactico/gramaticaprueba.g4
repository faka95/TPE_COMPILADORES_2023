parser grammar gramaticaprueba;
options {
    tokenVocab = Lexico;
}
@parser::header {
import TablaSimbolos as tablasimbolos
from antlr4.Token import Token
import AnalizadorSemantico.PolacaInversa as Polaca
}
@parser::members {
    self.archivo_tabla = open("tabla_de_simbolos.txt", "a")
    self.archivo_salida = open("salida.txt", "a")
    self.archivo_errores = open("errores.txt", "a")
    self.simbolos = tablasimbolos.TablaDeSimbolos(self.archivo_tabla)
    self.menos_menos = False
    self.listaVar = []
    self.text = ""
    self.polacaInversa = Polaca.ExpresionPolacaInversa()
    self.aux = 1
    self.elseaux = False
def agregarEstructura(self, texto):
    self.archivo_salida.write(str(texto+"\n"))

def yyerror(self, texto, linea):
    self.archivo_errores.write(str("ERROR DE SINTAXIS: " + texto + " En la linea " + str(linea) + "\n"))

def getValor(self, texto):
    valor = ""
    for caracter in texto:
        if caracter.isdigit() or caracter in [".","E","e"]:
            valor += caracter
    return valor
}

programa: '{' cuerpo '}' {
self.simbolos.imprimirTabla()
self.archivo_tabla.close()
}
;

cuerpo: cuerpo declaracion
        | cuerpo ejecucion
        | declaracion
        | ejecucion
;

declaracion: declaracion_var  {
self.agregarEstructura("DECLARACION VAR detectado")
}
            | declaracion_func
            | declaracion_clase  {
self.agregarEstructura("DECLARACION CLASE detectado")
}
;

declaracion_var: tipo lista_variable ',' {
for key in self.listaVar:
    self.simbolos.addCaracteristica(key, "tipo", $tipo.text)
self.listaVar = []
}
;

lista_variable: ID {
self.listaVar.append($ID.text)
}
                | ID ';' lista_variable {
self.listaVar.append($ID.text)
}
;

declaracion_func: VOID ID {self.polacaInversa.addElemento(('FUNCION' + ' ' + $ID.text))} parametro '{' cuerpo_func '}' ',' {
self.simbolos.addCaracteristica($ID.text, "tipo", "func")
self.agregarEstructura("DECLARACION FUNCION detectado")
}
                  | VOID ID '(' ')' '{' cuerpo_func '}' ',' {
self.simbolos.addCaracteristica($ID.text, "tipo", "func")
self.agregarEstructura("DECLARACION FUNCION detectado")
}
;

parametro: '(' ')'
            | '(' tipo ID ')' {
self.simbolos.addCaracteristica($ID.text, "tipo", $tipo.text)
}
;

cuerpo_func: cuerpo ejecucion_retorno ','
             | ejecucion_retorno ','
;

ejecucion_retorno: control_retorno //Hacer lo mismo que el if
                    | control_retorno ',' ejecucion_retorno
                    | while_retorno
                    | while_retorno ',' ejecucion_retorno
                    | RETURN {self.polacaInversa.addElemento("ret")}  //Agrego BI y una celda vacia. Pero antes de hacer esto esperar respuesta de Paula por multiples cintas.
;

control_retorno: if_condicion then_retorno END_IF {self.agregarEstructura("IF detectado")}
                | if_condicion then_retorno ELSE bloque_control END_IF {self.agregarEstructura("IF detectado")}
                | if_condicion bloque_control else_retorno END_IF {self.agregarEstructura("IF detectado")}
                | if_condicion then_retorno else_retorno END_IF {self.agregarEstructura("IF detectado")}
;

then_retorno:   '{' ejecucion_retorno ',' '}'
                | '{' cuerpo_ejecucion ejecucion_retorno ',' '}'
;

else_retorno:  ELSE '{' ejecucion_retorno ',' '}'
               | ELSE '{' cuerpo_ejecucion ejecucion_retorno ',' '}'
;

while_retorno: WHILE '(' condicion ')' DO '{' cuerpo_ejecucion RETURN ',' '}' {
self.agregarEstructura("WHILE detectado")
{self.polacaInversa.addElemento("ret")}
}
;

declaracion_clase: CLASS ID '{' componentes_clase '}' ',' {
self.simbolos.addCaracteristica($ID.text, "tipo", "clase")
}
;

componentes_clase: declaracion_var
                    | declaracion_func
                    | ID ','
                    | componentes_clase declaracion_var
                    | componentes_clase declaracion_func
                    | componentes_clase ID ','
;

cuerpo_ejecucion: cuerpo_ejecucion ejecucion
                  | ejecucion
;

ejecucion: asignacion ','  {self.agregarEstructura("ASIGNACION detectado")}
           | invocacion ',' {self.agregarEstructura("INVOCACION detectado")}
           | seleccion ',' {self.agregarEstructura("IF detectado")}
           | print ',' {self.agregarEstructura("PRINT detectado")}
           | while ',' {self.agregarEstructura("WHILE detectado")}
           | ERROR ',' {self.yyerror(str("ERROR en sentencia ejecutable en linea: {}"),$ERROR.line)}
;

asignacion: ID '=' expresion {
self.simbolos.aumentarReferencia($ID.text)
self.polacaInversa.addElemento($ID.text)
self.polacaInversa.addElemento("=")
}
;

invocacion: ID '(' expresion ')' {
self.simbolos.aumentarReferencia($ID.text)
aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + $ID.text)
self.polacaInversa.addElemento(aux)
self.polacaInversa.addElemento("CALLFUNC")
}
            | ID '(' ')' {
self.simbolos.aumentarReferencia($ID.text)
aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + $ID.text)
self.polacaInversa.addElemento(aux)
self.polacaInversa.addElemento("CALLFUNC")
}
            | clase=ID '.' funcion=ID '(' ')' {
self.simbolos.aumentarReferencia($clase.text)
self.simbolos.aumentarReferencia($funcion.text)
aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + $funcion.text)
self.polacaInversa.addElemento(aux)
self.polacaInversa.addElemento("CALLFUNC")
}
            | clase=ID '.' funcion=ID '(' expresion ')' {
self.simbolos.aumentarReferencia($clase.text)
self.simbolos.aumentarReferencia($funcion.text)
aux = self.polacaInversa.getReferenciaOp('FUNCION' + ' ' + $funcion.text)
self.polacaInversa.addElemento(aux)
self.polacaInversa.addElemento("CALLFUNC")
}
;

seleccion: if_condicion bloque_control posible_else END_IF {
if self.elseaux is False:
    number = self.polacaInversa.getLastPendingStep()
    self.polacaInversa.setElemento(number)
else:
    self.elseaux = False
} //Agrego valor que sigue de la cinta en la celdad el tope de la Pila. Y desapilo
;
posible_else: else bloque_control {
number = self.polacaInversa.getLastPendingStep()
self.polacaInversa.setElemento(number)
} //Agrego valor que sigue de la cinta en la celda del tope de la pila. Y desapilo
             |
;
else: ELSE {
self.elseaux = True
number = self.polacaInversa.getLastPendingStep()
self.polacaInversa.addPendingStep(self.polacaInversa.reference_counter)
self.polacaInversa.addElemento(" ")
self.polacaInversa.addElemento("BI")
self.polacaInversa.setElemento(number)
} // agrego celda vacia(y agrego en la pila) y BI
;

if_condicion: IF '(' condicion ')' {
self.polacaInversa.addPendingStep(self.polacaInversa.reference_counter)
self.polacaInversa.addElemento(" ")
self.polacaInversa.addElemento("BF")
} //Agrego celda vacia, apilo, y agrego BF
;

bloque_control: '{' cuerpo_ejecucion '}'
;

condicion: expresion comparador expresion {
self.polacaInversa.addElemento($comparador.text)}
;

comparador: '<'
            | '>'
            | MENORIGUAL
            | MAYORIGUAL
            | DISTINTO
            | COMPIGUAL
;

print: PRINT '(' CADENA ')'{
self.polacaInversa.addElemento($CADENA.text)
self.polacaInversa.addElemento("PRINT")
}
;
while: while_condicion bloque_control {
number = self.polacaInversa.getLastPendingStep()
self.polacaInversa.addElemento(self.aux)
self.polacaInversa.addElemento("BI")
self.polacaInversa.setElemento(number)
}

;

while_condicion:{self.aux = self.polacaInversa.reference_counter} WHILE '(' condicion ')' DO{
self.polacaInversa.addPendingStep(self.polacaInversa.reference_counter)
self.polacaInversa.addElemento(" ")
self.polacaInversa.addElemento("BF")
}

;

tipo: INT
       | ULONG
       | FLOAT
       | ID {
self.simbolos.aumentarReferencia($ID.text)
}
;

expresion:  expresion '+' termino {self.polacaInversa.addElemento("+")}
            | expresion '-' termino {self.polacaInversa.addElemento("-")}
            | termino
;

termino: termino '*' factor {self.polacaInversa.addElemento("*")}
        | termino '/' factor {self.polacaInversa.addElemento("/")}
        | factor
;

factor: referencia
        | '-' NUM_INT {
key = $NUM_INT.text
if key in self.simbolos.keys():
    if self.simbolos.getCaracteristica(key, "referencias") == 1:
        self.simbolos.remove(key)
    else:
        self.simbolos.reducirReferencia(key)
# TODO chequear rango
self.simbolos.addSimbolo("-" + $NUM_INT.text)
self.polacaInversa.addElemento($NUM_INT.text)
}
        | NUM_ULONG {
self.simbolos.addCaracteristica($NUM_ULONG.text, "tipo", "ULONG")
self.polacaInversa.addElemento($NUM_ULONG.text)
}
        | NUM_FLOAT {
self.simbolos.addCaracteristica($NUM_FLOAT.text, "tipo", "FLOAT")
self.polacaInversa.addElemento($NUM_FLOAT.text)
}
        | '-' NUM_FLOAT {
key = $NUM_FLOAT.text
if key in self.simbolos.keys():
    if self.simbolos.getCaracteristica(key, "referencias") == 1:
        self.simbolos.remove(key)
    else:
        self.simbolos.reducirReferencia(key)
self.simbolos.addSimbolo("-" + $NUM_FLOAT.text)
self.polacaInversa.addElemento($NUM_FLOAT.text)
}
        | NUM_INT {
if $NUM_INT.text == "32768_i":
    self.yyerror("INT fuera de rango",$NUM_INT.line)
else:
    self.simbolos.addCaracteristica($NUM_INT.text, "tipo", "INT")
    texto = $NUM_INT.text
    self.simbolos.addCaracteristica(texto, "valor", self.getValor(texto))
    self.polacaInversa.addElemento($NUM_INT.text)
}
        | ERROR {self.yyerror("se espera una constante o id",$ERROR.line)}
;

referencia: ID {self.polacaInversa.addElemento($ID.text)} posible_guion_doble {
self.simbolos.aumentarReferencia($ID.text)
if (self.menos_menos is True):
    self.polacaInversa.addElemento($ID.text)
    self.polacaInversa.addElemento('=')
    self.menos_menos = False
}
            | uso_clase
;
posible_guion_doble: '-' '-' {
self.menos_menos = True
self.polacaInversa.addElemento('1_i')
self.polacaInversa.addElemento("-")

}
                  |
;
uso_clase: clase=ID '.' atributo=ID {
self.simbolos.aumentarReferencia($clase.text)
self.simbolos.aumentarReferencia($atributo.text)
clase = $clase.text + "." + $atributo.text
self.polacaInversa.addElemento(str(clase))
}
;
