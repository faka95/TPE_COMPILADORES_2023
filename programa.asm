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
cadena_18 db "b es 6.0, suma correcta", 0
cadena_30 db "b es 4.0, resta correcta", 0
cadena_42 db "b es 8.0, mult correcta", 0
cadena_54 db "b es 4.0, div correcta", 0


b_main DD ?
a_main DD ?
f2_0 DD 2.0
f4_0 DD 4.0
f6_0 DD 6.0
f8_0 DD 8.0
f3_40282346E38 DD 3.40282346e38
f10_0 DD 10.0
@aux1 DD ?
@aux2 DD ?
@aux3 DD ?
@aux4 DD ?
@aux5 DD ?
.code
start:
FLD f2_0
FSTP a_main
FLD f4_0
FSTP b_main
FLD dword ptr[a_main]
FADD dword ptr[b_main]
FCOM dword ptr[MaxFLOAT] 
FSTSW AX 
SAHF
JAE LabelErrorOvSF
FSTP dword ptr[@aux1]
FLD @aux1
FSTP b_main
FLD f6_0
FCOM b_main
FSTSW AX
SAHF
JNE TAG19
invoke MessageBox, NULL, addr cadena_18, addr Imp, MB_OK
TAG19:
FLD dword ptr[b_main]
FSUB dword ptr[a_main]
FSTP dword ptr[@aux2]
FLD @aux2
FSTP b_main
FLD f4_0
FCOM b_main
FSTSW AX
SAHF
JNE TAG31
invoke MessageBox, NULL, addr cadena_30, addr Imp, MB_OK
TAG31:
FLD dword ptr[a_main]
FMUL dword ptr[b_main]
FSTP dword ptr[@aux3]
FLD @aux3
FSTP b_main
FLD f8_0
FCOM b_main
FSTSW AX
SAHF
JNE TAG43
invoke MessageBox, NULL, addr cadena_42, addr Imp, MB_OK
TAG43:
FLDZ
FLD dword ptr[a_main]
FCOM
FSTSW AX 
SAHF
JE LabelErrorDIV0
FLD dword ptr[b_main]
FDIV a_main
FSTP dword ptr[@aux4]
FLD @aux4
FSTP b_main
FLD f4_0
FCOM b_main
FSTSW AX
SAHF
JNE TAG55
invoke MessageBox, NULL, addr cadena_54, addr Imp, MB_OK
TAG55:
FLD f3_40282346E38
FSTP b_main
FLD dword ptr[f10_0]
FADD dword ptr[b_main]
FCOM dword ptr[MaxFLOAT] 
FSTSW AX 
SAHF
JAE LabelErrorOvSF
FSTP dword ptr[@aux5]
FLD @aux5
FSTP b_main
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
