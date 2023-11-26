include \masm32\include\masm32rt.inc
.386
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
cadena_13 db "then", 0
cadena_20 db "then", 0
cadena_32 db "else", 0
cadena_39 db "vale 5", 0
cadena_51 db "vale 4", 0
cadena_58 db "VALE 4 TODAVIA", 0
cadena_73 db "VALE 3 AHORA", 0
cadena_92 db "A, VALE 1 MENOS", 0
cadena_105 db "B, AUMENTANDOO", 0


clase_b STRUCT
    property1 DW ?     
    propertyc2 DD ?
clase_b ENDS


clase_c STRUCT
    property1 DW ?     
    propertyc2 DD ?     
    clase_b_ clase_b <?>
clase_c ENDS

c1_main clase_c <?>
b_main DW ?
a_main DW ?
i_6 DW 6
i_1 DW 1
i_5 DW 5
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
JMP ErrorTYPE
MOV BX,b_main
CMP i_6, BX
JNE TAG14
invoke MessageBox, NULL, addr cadena_13, addr Imp, MB_OK
TAG14:
MOV BX,b_main
CMP i_5, BX
JNE TAG23
invoke MessageBox, NULL, addr cadena_20, addr Imp, MB_OK
JMP TAG33
TAG23:
MOV AX, b_main
SUB AX, i_1
MOV @aux1, AX
MOV AX, @aux1
MOV b_main, AX 
MOV AX, b_main
MOV b_main, AX 
invoke MessageBox, NULL, addr cadena_32, addr Imp, MB_OK
TAG33:
MOV BX,b_main
CMP i_5, BX
JNE TAG40
invoke MessageBox, NULL, addr cadena_39, addr Imp, MB_OK
TAG40:
MOV AX, b_main
SUB AX, i_1
MOV @aux2, AX
MOV AX, @aux2
MOV b_main, AX 
MOV BX,b_main
CMP i_4, BX
JNE TAG52
invoke MessageBox, NULL, addr cadena_51, addr Imp, MB_OK
TAG52:
MOV BX,b_main
CMP i_4, BX
JNE TAG74
invoke MessageBox, NULL, addr cadena_58, addr Imp, MB_OK
MOV AX, b_main
SUB AX, i_1
MOV @aux3, AX
MOV AX, @aux3
MOV b_main, AX 
MOV AX, b_main
MOV b_main, AX 
MOV BX,b_main
CMP i_3, BX
JNE TAG74
invoke MessageBox, NULL, addr cadena_73, addr Imp, MB_OK
TAG74:
MOV AX, i_5
MOV a_main, AX 
TAG77:
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
invoke MessageBox, NULL, addr cadena_92, addr Imp, MB_OK
TAG93:
MOV BX,b_main
CMP i_10, BX
JE TAG108
MOV AX, b_main
ADD AX, i_1
MOV @aux5, AX
MOV AX, @aux5
MOV b_main, AX 
invoke MessageBox, NULL, addr cadena_105, addr Imp, MB_OK
JMP TAG93
TAG108:
JMP TAG77
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
