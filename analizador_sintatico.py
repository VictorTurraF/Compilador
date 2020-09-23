# Analisador sintatico
class AnalizadorSintatico:

    # Contem em sequencia os terminais pertencentes a esta gramatica
    __terminais = []

    # Contem a tabela com as regras de produção
    __producoes = []

    # Aqui será empilhada toda a sequencia de produções
    __pilha_sintatica = []

    # Contem a cadeia de tokens a serem consumidos
    __cadeia = []

    # Construtor, para instanciar é necessário fornecer a sequencia de terminais
    # e a tabela de produções da gramática
    def __init__( self, terminais, producoes ) :
        if type( terminais ) == list :
            self.__terminais = terminais
        if type( producoes ) == list :
            self.__producoes = producoes

    def verificar_sintaxe( self, tokens ) :
        # mota a cadeia de tokens
        for token in tokens :
            self.__cadeia.append( token[1] )
        # $ para identificar o fim da cadeia
        self.__cadeia.append("$")

        # inicia a pilha sintatica, com simbolo inicial
        self.__pilha_sintatica.append("E")

        # enquanto pilha nao estiver vazia
        while self.__pilha_sintatica != [] :
            print( self.__pilha_sintatica, self.__cadeia )
            
            # desempilha o item do topo
            letra = self.__pilha_sintatica.pop()
            
            # obtem o primeiro token da cadeia (token de entrada)
            terminal = ''
            if self.__cadeia != [] :
                terminal = self.__cadeia[0]

            # caso a regra desempilhada seja vazia
            if letra == '' :
                # faz nada, prox iteração
                continue

            # caso foi desempilhado um terminal
            elif letra in self.__terminais :
                # verifica se corresponde com a token de entrada da cadeia
                if letra == terminal :
                    # consome o token da cadeia
                    del self.__cadeia[0]
                    # prox iteração
                    continue
                #senao Erro
                else :
                    return False

            # senão (então foi desempilhada uma regra), empilhar producao (invertida)
            else:
                # 1 - busca o indice do token de entrada (terminal) na lista
                indice_terminal = self.__terminais.index( terminal )

                # 2 - busca na tabela a producao que devera ser usada
                producao = 0
                for p in self.__producoes :
                    if p["producao"] == letra :
                                              # aqui usa o indice
                        producao = p["regras"][indice_terminal]
                        break
                if producao == 0 :
                    print("Produção não encontrada")
                    return False

                # 3 - Inverte a produção (ABC -> CBA)
                prod_copy = producao.copy()
                prod_copy.reverse()

                # 4 - Empilha produção invertida
                self.__pilha_sintatica = self.__pilha_sintatica + prod_copy
            

        return True






