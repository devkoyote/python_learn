from animal import Animal
from interface_animal import Interface_Animal
from dono import Dono

class Gato(Animal, Interface_Animal):


    def __init__(self, nome, idade, cor, dono = Dono()):
        # extends Animal
        super().__init__(nome, idade, cor)
        self.__dono = dono

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono

    # function action
    def fazer_barulho(self):
        return "Miauu"

    def brincar(self):
        return "O gato está pulando no telhado"
