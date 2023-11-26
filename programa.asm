include \masm32\include\masm32rt.inc
.586
.model flat
option casemap :none
include \masm32\include\windows.inc
include \masm32\include\kernel32.inc
include \masm32\include\user32.inc
includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\user32.lib
.data
Error db "Error", 0
ErrorOvSF db "Error: overflow en un suma entre flotantes", 0
ErrorOvPE db "Error: overflow en una producto de enteros", 0
ErrorTYPE db "Error: Error tipos incomatibles entre operadores", 0
ErrorDIV0 db "Error: division por cero", 0
FINALIZO db "FINALIZO EL PROGRAMA", 0
Salida dt ?, 0
Imp db "Salida por pantalla", 0
@mem2byte dd ? ; 32 bits
MaxFLOAT dd 3.40282347E38 ; 32 bits 
cadena_10 db "then", 0
cadena_17 db "then", 0
cadena_29 db "else", 0
cadena_36 db "vale 5", 0
cadena_48 db "vale 4", 0
cadena_55 db "VALE 4 TODAVIA", 0
cadena_70 db "VALE 3 AHORA", 0
cadena_89 db "A, VALE 1 MENOS", 0
cadena_102 db "B, AUMENTANDOO", 0


clase_b STRUCT
    property1 DD ?     
    propertyc2 DD ?
clase_b ENDS


clase_c STRUCT
    property1 DD ?     
    propertyc2 DD ?     
    clase_b1 clase_b <?>
clase_c ENDS

c1_main clase_c <?>
b_main DW ?
a_main DW ?
i_6 DW 6
i_5 DW 5
i_1 DW 1
i_4 DW 4
i_3 DW 3
i_10 DW 10
@aux1 DW ?
@aux2 DW ?
@aux3 DW ?
@aux4 DW ?
@aux5 DW ?
.code
start:
MOV AX, i_6
MOV b_main, AX 
MOV BX,b_main
CMP i_6, BX
JNE TAG11
invoke MessageBox, NULL, addr cadena_10, addr Imp, MB_OK
TAG11:
MOV BX,b_main
CMP i_5, BX
JNE TAG20
invoke MessageBox, NULL, addr cadena_17, addr Imp, MB_OK
JMP TAG30
TAG20:
MOV AX, b_main
SUB AX, i_1
MOV @aux1, AX
MOV AX, @aux1
MOV b_main, AX 
MOV AX, b_main
MOV b_main, AX 
invoke MessageBox, NULL, addr cadena_29, addr Imp, MB_OK
TAG30:
MOV BX,b_main
CMP i_5, BX
JNE TAG37
invoke MessageBox, NULL, addr cadena_36, addr Imp, MB_OK
TAG37:
MOV AX, b_main
SUB AX, i_1
MOV @aux2, AX
MOV AX, @aux2
MOV b_main, AX 
MOV BX,b_main
CMP i_4, BX
JNE TAG49
invoke MessageBox, NULL, addr cadena_48, addr Imp, MB_OK
TAG49:
MOV BX,b_main
CMP i_4, BX
JNE TAG71
invoke MessageBox, NULL, addr cadena_55, addr Imp, MB_OK
MOV AX, b_main
SUB AX, i_1
MOV @aux3, AX
MOV AX, @aux3
MOV b_main, AX 
MOV AX, b_main
MOV b_main, AX 
MOV BX,b_main
CMP i_3, BX
JNE TAG71
invoke MessageBox, NULL, addr cadena_70, addr Imp, MB_OK
TAG71:
MOV AX, i_5
MOV a_main, AX 
TAG74:
MOV BX,a_main
CMP i_1, BX
JE FIN
MOV AX, a_main
SUB AX, i_1
MOV @aux4, AX
MOV AX, @aux4
MOV a_main, AX 
MOV AX, a_main
MOV a_main, AX 
invoke MessageBox, NULL, addr cadena_89, addr Imp, MB_OK
TAG90:
MOV BX,b_main
CMP i_10, BX
JE TAG105
MOV AX, b_main
ADD AX, i_1
MOV @aux5, AX
MOV AX, @aux5
MOV b_main, AX 
invoke MessageBox, NULL, addr cadena_102, addr Imp, MB_OK
JMP TAG90
TAG105:
JMP TAG74
JMP FIN
LabelErrorOvSF:
invoke MessageBox, NULL, addr ErrorOvSF, addr Error, MB_OK
invoke ExitProcess, 0
LabelErrorOvPE:
invoke MessageBox, NULL, addr ErrorOvPE, addr Error, MB_OK
invoke ExitProcess, 0
LabelErrorDIV0:
invoke MessageBox, NULL, addr ErrorDIV0, addr Error, MB_OK
invoke ExitProcess, 0
LabelErrorTYPE:
invoke MessageBox, NULL, addr ErrorTYPE, addr Error, MB_OK
invoke ExitProcess, 0
FIN:
invoke MessageBox, NULL, addr FINALIZO, addr Error, MB_OK
invoke ExitProcess, 0
end start
