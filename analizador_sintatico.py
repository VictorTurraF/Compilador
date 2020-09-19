class AnalizadorSintatico:

    __terminais = []

    __producoes = []

    __pilha_sintatica = []

    __cadeia = []

    def __init__( self, simbolos, producoes ) :
        if type( simbolos ) == list :
            self.__simbolos = simbolos

        if type( producoes ) == list :
            self.__producoes = producoes

    def verificar_sintaxe( tokens ) :
        





