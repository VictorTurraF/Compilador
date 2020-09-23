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
  id * ( id + num )
"""

#Analizador lexico

print("Tokens: ")
# incilizacao objeto do analisador léxico
tokenizador = Tokenizador()

# chamada da função, retorna lista de tokens
tokens = tokenizador.getTokens( codigo )

# Analizador sintatico
print("\nSintaxe:")

# OBSERVAÇÃO: A lista de terminais é organizada de forma a indexar a
# lista de regras de determinada produção, ou seja, 
# o indice de determinada regra de uma produção faz referencia à posição
# onde se encontra o terminal ao qual pertençe a regra de produção
 
terminais = [ "+", "-", "*", "/", "id", "num", "(", ")", "$" ]

producoes = [
  { 
    "producao": "E", 
    "regras" : [ 0, 0, 0, 0, ["T", "S"], ["T", "S"], ["T", "S" ], 0, 0]
  },
  { 
    "producao": "T", 
    "regras" : [ 0, 0, 0, 0, ["F", "G"], ["F", "G"], ["F", "G" ], 0, 0]
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

# inicia um analizador sintatico
sintetizador = AnalizadorSintatico( terminais, producoes )

# realiza a verificação da sintaxe, retorna se é valido ou não (boolean)
sintaxe_valida = sintetizador.verificar_sintaxe( tokens )

if( sintaxe_valida ) :
  print("Sintaxe válida")
else: 
  print("Sintaxe invalida")