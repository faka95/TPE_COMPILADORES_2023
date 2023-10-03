import AnalizadorLexico.Lexico as lex
import AnalizadorLexico.AccionesSemanticas.Acciones.CharError as char

CONST_16BIT = 2 ** 15
SUFFIX_16BIT = "_i"
CONST_UNSIGNED_32BIT = 2 ** 32 - 1
SUFFIX_32BIT = "_ul"
buffer = "55555_"
CONST_HIGHEXP = 38
CONST_LOWEXP = -38
CONST_LOWDEC = 1.17549435 * (10 ** CONST_LOWEXP)
CONST_HIGHDEC = 3.40282347 * (10 ** CONST_HIGHEXP)

"""def rango_i(numero):
    if (numero >= (CONST_16BIT * (-1))) and (numero <= (CONST_16BIT - 1)):
        return True
    else:
        return False


def rango_ul(numero):
    if (numero >= 0) and (numero <= CONST_UNSIGNED_32BIT):
        return True
    else:
        return False


def ejecutar(buffer, caracterActual):
    buffer += caracterActual
    parte_numerica = ""
    if buffer[0] == "-":
        parte_numerica += buffer[0]
    for caracter in buffer:
        if caracter.isdigit():
            parte_numerica += caracter

    for letra in buffer:
        # Error si el sufijo contiene mayusculas
        if letra.isupper():
            print("error_yacc")
            print("Sufijo contiene mayusculas.")
            return

    if buffer.endswith(SUFFIX_16BIT):
        if not (rango_i(int(parte_numerica))):
            print("error_yacc");
            print("Constante entera INT fuera de rango", buffer)
            return
        else:
            print(buffer)

    elif buffer.endswith(SUFFIX_32BIT):
        if not (rango_ul(int(parte_numerica))):
            print("error_yacc");
            print("Constante entera ULONG fuera de rango", buffer)
            return
        else:
            print(buffer)

ejecutar(buffer,"ul")"""

"""
def ejecutar(buffer, caracterActual):
    buffer += caracterActual
    exponente = 0
    entero_decimal = 0
    if "E" in buffer:
        numero = buffer.split("E")
        exponente = int(numero[1])
        entero_decimal = float(numero[0])
    elif "e" in buffer:
        numero = buffer.split("e")
        exponente = int(numero[1])
        entero_decimal = float(numero[0])
    else:
        entero_decimal = float(buffer)

    if (abs(exponente) > CONST_HIGHEXP):
        print("error_yacc")
        print("Constante de tipo flotante FLOAT con exponente fuera de rango", buffer)
    else:
        exponencial = float(10 ** exponente)
        resultado = float(entero_decimal * exponencial)
        print(resultado)
        if (resultado == 0.0):
            print(buffer)
        else:
            if (resultado <= CONST_LOWDEC):
                print("error_yacc")
                print("Constante de tipo flotante FLOAT fuera de rango < lowdec", buffer)
            elif (resultado >= CONST_HIGHDEC):
                print("error_yacc")
                print("Constante de tipo flotante FLOAT fuera de rango > highdec", buffer)
            else:
                print(buffer)

cadena = "-0.16549426"
ejecutar(cadena,"8")
print(CONST_LOWDEC)
"""

lexico = lex.Lexico
error = char.CharError(lexico)
error.ejecutar("hola","+")

