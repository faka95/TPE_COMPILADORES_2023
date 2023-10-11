parser grammar gramaticaprueba;
options {
    tokenVocab = Lexico;
}

programa: '{' cuerpo '}'
;

cuerpo: cuerpo declaracion
        | cuerpo ejecucion
        | declaracion
        | ejecucion
;

declaracion: declaracion_var  {# agregarEstructura("DECLARACION VAR detectado")}
            | declaracion_func  {# agregarEstructura("DECLARACION FUNCION detectado")}
            | declaracion_clase  {# agregarEstructura("DECLARACION CLASE detectado")}
;

declaracion_var: tipo lista_variable ',' {#agregar al/los ids el tipo}
;

lista_variable: ID { #agregar id a la tabla }
                | ID ';' lista_variable {#agregar id a la tabla }
;

declaracion_func: VOID ID '(' parametro ')' '{' cuerpo_func '}' ',' {#agregar id a la tabla con tipo func }
                  | VOID ID '(' ')' '{' cuerpo_func '}' ','
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

control_retorno: if_condicion then_retorno END_IF {#agregarEstructura("IF detectado")}
                | if_condicion then_retorno ELSE bloque_control END_IF {#agregarEstructura("IF detectado")}
                | if_condicion bloque_control else_retorno END_IF {#agregarEstructura("IF detectado")}
                | if_condicion then_retorno else_retorno END_IF {#agregarEstructura("IF detectado")}
;

then_retorno:   '{' ejecucion_retorno ',' '}'
                | '{' cuerpo_ejecucion ejecucion_retorno ',' '}'
;

else_retorno:  ELSE '{' ejecucion_retorno ',' '}'
               | ELSE '{' cuerpo_ejecucion ejecucion_retorno ',' '}'
;

while_retorno: WHILE '(' condicion ')' DO '{' cuerpo_ejecucion RETURN ',' '}' {#agregarEstructura("WHILE detectado")}
;

declaracion_clase: CLASS ID '{' componentes_clase '}' ','
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

ejecucion: asignacion ','  {#agregarEstructura("ASIGNACION detectado")}
           | invocacion ',' {#agregarEstructura("INVOCACION detectado")}
           | seleccion ',' {#agregarEstructura("IF detectado")}
           | print ',' {#agregarEstructura("PRINT detectado")}
           | while ',' {#agregarEstructura("WHILE detectado")}
           | ERROR ',' {#yyerror("ERROR detectado")}
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
        | '-' NUM_INT
        | NUM_ULONG
        | NUM_FLOAT
        | '-' NUM_FLOAT
        | NUM_INT {#chequear rango en todos menos ULONG e ID}
        | ERROR {#error("se espera una cosntante o id")}
;

referencia: ID posible_guion_doble
            | uso_clase
;
posible_guion_doble: '--' {#/* acciones */ }
                  |
;
uso_clase: ID '.' ID
            | ID '.' ID '(' ')'
;
