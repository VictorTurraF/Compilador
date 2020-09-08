# -*- coding: utf-8 -*-
import re

PalavrasReservadas = ["asm", "auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "main", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]
Letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SimbolosEspeciais = [".", ",", ";", "(", ")", ":", "+", "-", "/", "*", "%", "<", ">", "{", "}", "[", "]", "="]
SimbolosCompostos = ["++", "--", ">=", "<=", "+=", "-=", "*=", "/=", "%=", "=="]

codigo = """#include <stdio.h>
main()
{ 
  int Ab = 0, b = 5;
 
  if (b <=  10)
    a += 5;

  printf("Valores a = %d e b = %d", a, b);
}"""

# tabela do resultado
tabela_analise = []

# Buffer para armazenar constantes de Strings
buffer = ""

# Buffer Flag, para indicar inicio e encerramento do buffer
buffer_flag = False

# Variavel Descrição do simbolo
simbolo = ""

# Remove espaços em branco desnecessario 
# ( dois ou mais espaços são convertidos para um espaço apenas )
codigo = re.sub("[ \t\r\f\v]{2,}", ' ', codigo)

# Quebra o codigo em linhas
result = re.split("\n", codigo )

# Para cada linha do codigo
for linha in range( len( result ) ):
  
  # Verifica se contem diretivas para ignorar a analise
  ignore = re.search( "^(//|#)(.*)", result[linha] )
  if ignore:
    token = ignore.group(1) 
    simbolo = "Diretiva: Ignore a linha"
    print( "\t", linha + 1, "\t", token, "\t\t", simbolo )
    continue

  # Quebra a linha em espaços e simbolos e simbolos compostos
  tokens = re.split("(\+\+|--|<=|>=|==|\+=|-=|\*=|/=|%=|\W)", result[linha])
  
  # print( tokens )
  for token in tokens:

    simbolo = ''

    if buffer_flag :
      if token == '"' :
        print( "\t", linha + 1, "\t", buffer, "\t\t", "String Constante" )
        buffer_flag = False
        buffer = ''
        simbolo = "Delimitador de String"
      else :
        buffer += token
        continue
    else :
      if token == '"' : # Caso seja inicio de string
        buffer_flag = True # inicia o buffer
        simbolo = "Delimitador de String"
    
    # Converte o token para minusculas
    token = token.lower()

    if token == '' or token == ' ' :
      continue

    elif token in SimbolosEspeciais:
      simbolo = "Simbolo especial"

    elif token in SimbolosCompostos:
      simbolo = "Simbolo Composto"

    elif token in PalavrasReservadas:
      simbolo = "Palavra Reservada"

    elif token.isdigit() :
      simbolo = "Contante inteira"

    else :
      simbolo = "Identificador"

    tabela_analise.append( [ linha, token, simbolo ] )
    print( "\t", linha + 1, "\t", token, "\t\t", simbolo )


# print(tabela_analise)