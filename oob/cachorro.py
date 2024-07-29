from animal import Animal
from interface_animal import InterfaceAnimal
from dono import Dono


class Cachorro(Animal, InterfaceAnimal):

    # Assigns object to class -> dono = Dono()
    def __init__(self, nome, idade, cor, qtd_ossos, dono=Dono()):
        self.__qtd_ossos = qtd_ossos
        self.__dono = dono
        # Extends generic class
        super().__init__(nome, idade, cor)

    # Overwrite method
    def __str__(self):
        return f"O nome do cachorro é: ${self.nome}. A idade é: ${self.idade}. A cor é: ${self.cor}" \
               f" A quantidade de ossos é: ${self.qtd_ossos}"

    # Methods Access [GET | SETTER ]
    @property
    def qtd_ossos(self):
        return self.__qtd_ossos

    @qtd_ossos.setter
    def qtd_ossos(self, qtd_ossos):
        self.__qtd_ossos = qtd_ossos

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono

        # Function action

    def fazer_barulho(self):
        return "Au au"

    def brincar(self):
        return "O cachorro está roendo o osso"
