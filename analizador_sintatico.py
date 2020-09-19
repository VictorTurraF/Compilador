class AnalizadorSintatico:

    __terminais = []

    __producoes = []

    __pilha_sintatica = []

    def __init__( self, simbolos, tabela_sintatica ){

        if type( simbolos ) == list :
            self.__simbolos = simbolos

        if type( tabela_sintatica ) == list :
            self.__tabela_sintatica = tabela_sintatica
    }

    def analizar_sintaxe( tokens ) : bool




