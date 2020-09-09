import re

# Analizador Lexico

class Tokenizador:

  ## Propriedades ##

  # Const Palavras reservadas da linguagem
  __palavras_reservadas = [
    "asm", "auto", "break", 
    "case", "char", "const", 
    "continue", "default", "do", 
    "double", "else", "enum", 
    "extern", "float", "for", 
    "goto", "if", "int", 
    "long", "main", "register", 
    "return", "short", "signed", 
    "sizeof", "static", "struct", 
    "switch", "typedef", "union", 
    "unsigned", "void", "volatile", 
    "while",
  ]

  # Const. Simbolos especiais da linguagem
  __simbolos_especiais = [
    ".", ",", ";", 
    "(", ")", ":", 
    "+", "-", "/", 
    "*", "%", "<", 
    ">", "{", "}", 
    "[", "]", "=",
  ]

  # Const. Operadores compostos da linguagem
  __simbolos_compostos = [
    "++", "--", ">=", 
    "<=", "+=", "-=", 
    "*=", "/=", "%=", 
    "==",
  ]

  # tabela do resultado
  __lista_tokens = []

  # Buffer para armazenar constantes de Strings
  __buffer = ""

  # Buffer Flag, para indicar inicio e encerramento do buffer
  __buffer_flag = False

  # Código
  __codigo = ""

  # Array de linhas do codigo
  __linhas = []




  ## Metodos da Classe ##

  # Remove espaços em branco desnecessario 
  # ( dois ou mais espaços são convertidos para um espaço apenas )
  def __remover_espacos(self, cod):
    return re.sub("[ \t\r\f\v]{2,}", " ", cod)

  # Retorna um array com as linhas do codigo
  def __quebrar_linhas(self, cod):
    return re.split("\n", cod )

  # Retorna um array com os tokens
  def __quebrar_simbolos( self, linha ):
    return re.split("(\+\+|--|<=|>=|==|\+=|-=|\*=|/=|%=|\W)", linha)

  # Encontra diretivas de compilação
  def __buscar_diretivas( self, linha ):
    return re.search( "^(//|#)(.*)", linha )

  def __gerar_tokens(self):

    # Remove os espaços desnecessários
    self.__codigo = self.__remover_espacos( self.__codigo )

    # Quebra o codigo em linhas
    self.__linhas = self.__quebrar_linhas( self.__codigo )

    # percorre as linhas
    for i, linha in enumerate( self.__linhas ) :

      # Busca por diretivas para ignorar a analise
      diretivas = self.__buscar_diretivas( linha )

      # se existir alguma diretiva
      if diretivas:
        token = diretivas.group(1) 
        desc_simbolo = "Diretiva: Ignore a linha"
        print( i + 1, "\t", token, "\t\t", desc_simbolo )
        continue
      
      # Quebra a linha em espaços e simbolos e simbolos compostos
      tokens = self.__quebrar_simbolos( linha ) 

      #percorre os tokens
      for token in tokens:

        desc_simbolo = ""
   
        # Verifica a existencia de cadeias
        if self.__buffer_flag :
          if token == '"' :
            print( i + 1, "\t", self.__buffer, "\t\t", "String Constante" )
            self.__buffer_flag = False
            self.__buffer = ""
            desc_simbolo = "Delimitador de String"
          else :
            self.__buffer += token
            continue
        else :
          if token == '"' : # Caso seja inicio de string
            self.__buffer_flag = True # inicia o buffer

        # Converte o token para minusculas
        token = token.lower()

        # Verifica os tokens
        if token == "" or token == " " :
          continue
        
        elif token == "\"":
          desc_simbolo = "Delimitador de String"

        elif token in self.__simbolos_especiais:
          desc_simbolo = "Simbolo especial"

        elif token in self.__simbolos_compostos:
          desc_simbolo = "Simbolo Composto"

        elif token in self.__palavras_reservadas:
          desc_simbolo = "Palavra Reservada"
    
        elif token.isdigit() :
          desc_simbolo = "Contante inteira"

        else :
          desc_simbolo = "Identificador"

        print( i + 1, "\t", token, "\t\t", desc_simbolo )

        self.__lista_tokens.append( [ i, token, desc_simbolo ] )




  ## Metodos publicos ##

  def getTokens( self, codigo ):

    # atribuição do código
    self.__codigo = codigo

    # geração dos tokens
    self.__gerar_tokens()

    return self.__lista_tokens