# -*- coding: utf-8 -*-

# classe do analizador lexico
from analizador_lexico import Tokenizador
from analizador_sintatico import AnalizadorSintatico

# codigo fonte de entrada
# codigo = """#include <stdio.h>
# main()
# { 
#   int Ab = 0, b = 5;
 
#   if (b <=  10)
#     a += 5;

#   printf("Valores a = %d e b = %d", a, b);
# }"""

codigo = """
  a + b * ( c + d )
"""

#Analizador lexico

# incilizacao objeto do analisador léxico
tokenizador = Tokenizador()

# chamada da função, retorna lista de tokens
tokens = tokenizador.getTokens( codigo )

print(tokens)


#Analizador sintatico

terminais = [ "+", "-", "*", "/". "id", "num", "(", ")", "" ]

producoes = [
  { 
    "producao": "E", 
    "regras" : [ 0, 0, 0, 0, ["T", "S"], ["T", "S"], ["T", "S" ]]
  },
  { 
    "producao": "T", 
    "regras" : [ 0, 0, 0, 0, ["F", "G"], ["F", "G"], ["F", "G" ]]
  },
  { 
    "producao": "S", 
    "regras" : [ ["+", "T", "S"], ["-", "T", "S"], 0, 0, 0, 0, 0, [""], [""]]
  },
  { 
    "producao": "G", 
    "regras" : [ [""], [""], ["*", "F", "G"], ["/", "F", "G"], 0, 0, 0, [""], [""]]
  },
  { 
    "producao": "F", 
    "regras" : [ 0, 0, 0, 0, ["id"], ["num"], ["(", "E", ")"], 0, 0 ]
  },
]

sintetizador = AnalizadorSintatico( terminais, )
