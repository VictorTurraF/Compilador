# -*- coding: utf-8 -*-

# classe do analizador lexico
from analizador_lexico import Tokenizador

# codigo fonte de entrada
codigo = """#include <stdio.h>
main()
{ 
  int Ab = 0, b = 5;
 
  if (b <=  10)
    a += 5;

  printf("Valores a = %d e b = %d", a, b);
}"""

# incilizacao objeto do analisador léxico
tokenizador = Tokenizador()
# chamada da função, retorna lista de tokens
tokens = tokenizador.getTokens( codigo )

print(tokens)