parser grammar gramaticaprueba;
options {
    tokenVocab = Lexico;
}
@parser::header {
import TablaSimbolos as tablasimbolos
from antlr4.Token import Token
}
@parser::members {
    self.archivo_tabla = open("tabla_de_simbolos.txt", "w")
    self.archivo_salida = open("salida.txt", "w")
    self.archivo_errores = open("errores.txt", "w")
    self.simbolos = tablasimbolos.TablaDeSimbolos(self.archivo_tabla)
    self.menos_menos = False
    self.listaVar = []
def agregarEstructura(self, texto): {
    self.archivo_salida.write(texto)
}

def yyerror(self, texto): {
    self.archivo_errores.write(texto)
}
}


programa: '{' cuerpo '}'
;

cuerpo: cuerpo declaracion
        | cuerpo ejecucion
        | declaracion
        | ejecucion
;

declaracion:
declaracion_var  {
self.agregarEstructura("DECLARACION VAR detectado")
}
| declaracion_func  {
self.agregarEstructura("DECLARACION FUNCION detectado")
}
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
self.simbolos.addSimbolo($ID.text)
self.listaVar.append($ID.text)
}
                | ID ';' lista_variable {
self.simbolos.addSimbolo($ID.text)
self.listaVar.append($ID.text)
}
;

declaracion_func: VOID ID '(' parametro ')' '{' cuerpo_func '}' ',' {
self.simbolos.addCaracteristica($ID.text, "tipo", "func")
}
                  | VOID ID '(' ')' '{' cuerpo_func '}' ',' {
self.simbolos.addCaracteristica($ID.text, "tipo", "func")
}
;

parametro: tipo ID {#agregar el parametro a la tabla}
;

cuerpo_func: cuerpo ejecucion_retorno ','
             | ejecucion_retorno ','
;

ejecucion_retorno: control_retorno
                    | control_retorno ',' ejecucion_retorno
                    | while_retorno ',' ejecucion_retorno
                    | RETURN
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

while_retorno: WHILE '(' condicion ')' DO '{' cuerpo_ejecucion RETURN ',' '}' {self.agregarEstructura("WHILE detectado")}
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
           | ERROR ',' {self.yyerror("ERROR detectado")}
;

asignacion: ID '=' expresion
;

invocacion: ID '(' expresion ')'
            | ID '(' ')'
;

seleccion: if_condicion bloque_control END_IF
          | if_condicion bloque_control ELSE bloque_control END_IF
;

if_condicion: IF '(' condicion ')'
;

bloque_control: '{' cuerpo_ejecucion '}'
;

condicion: expresion comparador expresion
;

comparador: '<'
            | '>'
            | MENORIGUAL
            | MAYORIGUAL
            | DISTINTO
            | COMPIGUAL
;

print: PRINT '(' CADENA ')'
;

while: WHILE '(' condicion ')' DO bloque_control
;

tipo: INT
       | ULONG
       | FLOAT
       | ID
;

expresion:  expresion '+' termino
            | expresion '-' termino
            | termino
;

termino: termino '*' factor
        | termino '/' factor
        | factor
;

factor: referencia
        | '-' NUM_INT {
key = $NUM_INT.text
if key in self.simbolos.keys():
    if self.simbolos.getCaracteristica(key, "referencias") == 1:
        self.simbolos.remove[key]
    else:
        self.simbolos.reducirReferencia(key)
# TODO chequear rango
self.simbolos.addSimbolo("-" + $NUM_INT.text)
}
        | NUM_ULONG {
self.simbolos.addSimbolo($NUM_ULONG.text)
}
        | NUM_FLOAT {
self.simbolos.addSimbolo($NUM_FLOAT.text)
}
        | '-' NUM_FLOAT {
key = $NUM_FLOAT.text
if key in self.simbolos.keys():
    if self.simbolos.getCaracteristica(key, "referencias") == 1:
        self.simbolos.remove[key]
    else:
        self.simbolos.reducirReferencia(key)
# TODO chequear rango
self.simbolos.addSimbolo("-" + $NUM_FLOAT.text)
}
        | NUM_INT {
self.simbolos.addSimbolo($NUM_INT.text)
}
        | ERROR {self.yyerror("se espera una cosntante o id")}
;

referencia: ID posible_guion_doble {
self.simbolos.aumentarReferencia($ID.text)
}
            | uso_clase
;
posible_guion_doble: '--' {
self.menos_menos = True
}
                  |
;
uso_clase: ID '.' ID
            | ID '.' ID '(' ')'
;
