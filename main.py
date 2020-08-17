import re

PalavrasReservadas = ["asm", "auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "main", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]
Letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SimbolosEspeciais = [".", ",", ";", "(", ")", ":", "+", "-", "/", "*", "%", "<", ">", "{", "}", "[", "]", "="]
SimbolosCompostos = ["++", "--", ">=", "<=", "+=", "-=", "*=", "/=", "%=", "=="]

codigo = """#include <stdio.h>
main()
{ 
  int a = 0, b = 5;
 
  if (b <=  10)
    a += 5;

  printf(“Valores a = %d e b = %d”, a, b);
}"""

# tabela do resultado
tabela_analise = []

# Buffer para encontrar Simbolos Compostos
buffer = ""

# Variavel Descrição do simbolo
simbolo = ""

# Converte para letras minusculas
codigo = codigo.lower()

# Remove espaços em branco desnecessario 
# ( dois ou mais espaços são convertidos para um espaço apenas )
codigo = re.sub("[ \t\r\f\v]{2,}", ' ', codigo)

# Quebra o codigo em linhas
result = re.split("\n", codigo )

# Para cada linha do codigo
for linha in range( len( result ) ):
  # print("linha " + str(linha + 1) + ":\t " + str(result[linha]))
  
  # Verifica se contem diretivas para ignorar a analise
  ignore = re.search( "^(//|#)(.*)", result[linha] )
  if ignore:
    token = ignore.group(1) 
    simbolo = "Diretiva: Ignore a linha"
    print( "\t", linha + 1, "\t", token, "\t\t", simbolo )
    continue

  # Quebra a linha em espaços e simbolos
  tokens = re.split("(\W)", result[linha])
  # print( tokens )
  for token in tokens:
    if token == '':
      continue
    else:
      simbolo = ''
      if token in SimbolosEspeciais:
        simbolo = "Simbolo especial"
      print( "\t", linha + 1, "\t", token, "\t\t", simbolo )


print(tabela_analise)

  



