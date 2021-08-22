class Professor:
    def __init__(self, nome, pontuacao):
        self.__nome = nome
        self.__pontuacao = pontuacao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao

JA DEI O PULL 
        
