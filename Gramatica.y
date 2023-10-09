%token IF ELSE END_IF PRINT CLASS VOID INT ULONG FLOAT WHILE DO MENORIGUAL MAYORIGUAL DISTINTO ID ERROR

%start programa

%%

programa:  { cuerpo }

cuerpo: declaracion
        | cuerpo declaracion
        | ejecucion
        | cuerpo ejecucion
;

declaracion: declaracion_var
            | declaracion_func
            | declaracion_clase
;

declaracion_var: tipo lista_variable ',' { "agregar al/los ids el tipo"}
;

lista_variable: ID { "agregar id a la tabla" }
                | ID ';' lista_variable { "agregar id a la tabla" }
                | ID lista_variable { error("falta ';'") }
                | ERROR ';' lista_variable { error ("se espera un id")}
;

declaracion_func: VOID ID '(' parametro ')' '{' cuerpo_func '}' { "agregar id a la tabla con tipo func" }
                  | VOID ID '(' ')' '{' cuerpo_func '}'

parametro: tipo ID {"agregar el parametro a la tabla"}
;

cuerpo_func: cuerpo ejecucuion_retorno
             | ejecucion_retorno //provisorio

ejecucion: asginacion ','
           | invocacion ','
           | seleccion ','
           | print ','
           | control ','
           | while ','
           | error ','
;

asignacion: ID expresion

invocacion: ID '(' expresion ')'
            | ID '(' ')'
;

selecion: IF '(' condicion ')' bloque_control ENDIF
          | IF '(' condicion ')' bloque_control ELSE bloque_control ENDIF
;

bloque_control: '{' cuerpo_control '}'
;

cuerpo_control: ejecucion
                | cuerpo_control ejecucion

condicion: expresion comparador expresion
;

comparador: '<'
            | '>'
            | '='
            | MENORIGUAL
            | MAYORIGUAL
            | DISTINTO
;

print: PRINT CADENA

//seguir acá


%%




