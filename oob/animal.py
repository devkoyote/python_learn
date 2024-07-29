#====IMPORTS===========

class Animal:

    def __init__(self, nome, idade, cor):
        self.__nome = nome
        self.__idade = idade
        self.__cor = cor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor



