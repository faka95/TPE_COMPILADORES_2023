class Lexico:
    FINAL = 99
    ERROR = 100
    nroLinea = 1
    indice = []
    termino = False
    erroresLex = 0
    lexema = ""
    # matrizDeAcciones semanticas
    # tokenActual
    # escribirError
    matriz = [[1,2,3],
              [2,3,4],
              [1,3,2]]
    matrizDeTransiciones = [
    #letra digito  /      *       +      -     =      <    >      {      }      (      )       ,     ;      .    :      _      D      '  Blanco-tab  nl      !    otro   #estado
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 0
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 1
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 2
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 3
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 4
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 5
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 6
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 7
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 8
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 9
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 10
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 11
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 12
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 13
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 14
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 15
    [11   ,1    , FINAL, FINAL, FINAL, FINAL,   10,    6,    9, FINAL, FINAL, FINAL, FINAL, FINAL, FINAL,   5, FINAL, ERROR, ERROR,   12,         0,    0, ERROR, ERROR],  # 16
    ]

