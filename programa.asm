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
cadena_14 db "then", 0


x_main_test_funcion DW ?
y_main_test_funcion DW ?
i_5 DW 5
i_1 DW 1
i_3 DW 3
@aux1 DW ?
@aux2 DW ?
.code
start:
JMP ErrorTYPE
MOV AX, i_5
MOV y_main_test_funcion, AX 
MOV BX,x_main_test_funcion
CMP y_main_test_funcion, BX
JGE TAG15
invoke MessageBox, NULL, addr cadena_14, addr Imp, MB_OK
TAG15:
MOV AX, y_main_test_funcion
SUB AX, i_1
MOV @aux1, AX
MOV AX, @aux1
MOV y_main_test_funcion, AX 
MOV AX, x_main_test_funcion
ADD AX, y_main_test_funcion
MOV @aux2, AX
MOV AX, @aux2
MOV x_main_test_funcion, AX 
retJMP FIN
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
