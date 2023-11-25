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
MaxFLOAT dw 3.40282347E38 ; 32 bits 
cadena_18 db "b es 6.0, suma correcta", 0
cadena_30 db "b es 4.0, resta correcta", 0
cadena_42 db "b es 8.0, mult correcta", 0
cadena_54 db "b es 4.0, div correcta", 0


b_main DD ?
a_main DD ?
2.0 DD 2.0
4.0 DD 4.0
6.0 DD 6.0
8.0 DD 8.0
@aux1 DD ?
@aux2 DD ?
@aux3 DD ?
@aux4 DD ?
.code
start:
FLD 2.0
FSTP a_main
FLD 4.0
FSTP b_main
FLD dword ptr[a_main]
FADD dword ptr[b_main]
FCOM dword ptr[MaxFLOAT] 
FSTSW @mem2byte 
MOV EAX , @mem2byte
SAHF
JGE LabelErrorOvSF
FSTP dword ptr[@aux1]
FLD @aux1
FSTP b_main
FLD 6.0
FCOM b_main
FSTSW @mem2byte
MOV EAX , @mem2byte
SAHF
JNE TAG19
invoke MessageBox, NULL, addr cadena_18, addr Imp, MB_OK
TAG19:
FLD dword ptr[a_main]
FSUB dword ptr[b_main]
FSTP dword ptr[@aux2]
FLD @aux2
FSTP b_main
FLD 4.0
FCOM b_main
FSTSW @mem2byte
MOV EAX , @mem2byte
SAHF
JNE TAG31
invoke MessageBox, NULL, addr cadena_30, addr Imp, MB_OK
TAG31:
FLD dword ptr[a_main]
FMUL dword ptr[b_main]
FSTP dword ptr[@aux3]
FLD @aux3
FSTP b_main
FLD 8.0
FCOM b_main
FSTSW @mem2byte
MOV EAX , @mem2byte
SAHF
JNE TAG43
invoke MessageBox, NULL, addr cadena_42, addr Imp, MB_OK
TAG43:
FLDZ
FLD dword ptr[b_main]
FCOM
FSTSW @mem2byte 
MOV EAX , @mem2byte
SAHF
JE LabelErrorDIV0
FLD dword ptr[a_main]
FDIV a_main
FSTP dword ptr[@aux4]
FLD @aux4
FSTP b_main
FLD 4.0
FCOM b_main
FSTSW @mem2byte
MOV EAX , @mem2byte
SAHF
JNE FIN
invoke MessageBox, NULL, addr cadena_54, addr Imp, MB_OK
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
