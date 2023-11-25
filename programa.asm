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
@mem2byte dw ? ; 32 bits
MaxF32 dw 3.40282347E38 ; 32 bits 


clase_c STRUCT
    property1 DW ?     
    propertyc2 DD ?
clase_c ENDS

c2_main clase_c <?>
c1_main clase_c <?>
b_main DD ?
a_main DD ?
ul_0 DD 0
ul_5 DD 5
@aux1 DD ?
@aux2 DD ?
@aux3 DD ?
.code
start:
MOV EAX, ul_0
MOV a_main, EAX 
MOV EAX, ul_5
MOV b_main, EAX 
MOV EAX, a_main
ADD EAX, b_main
MOV @aux1, EAX
MOV EAX, @aux1
MOV b_main, EAX 
MOV EBX, a_main
MOV ECX, b_main
MUL EBX
MOV @aux2, ECX
JO LabelErrorOvPE
MOV EAX, @aux2
MOV b_main, EAX 
MOV EBX, b_main
CMP a_main, 0
JE LabelErrorDIV0
MOV ECX, EBX
DIV a_main
MOV @aux3, ECX
MOV EAX, @aux3
MOV b_main, EAX 
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
