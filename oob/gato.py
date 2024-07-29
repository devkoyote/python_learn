from animal import Animal
from interface_animal import InterfaceAnimal
from dono import Dono


class Gato(Animal, InterfaceAnimal):

    def __init__(self, nome, idade, cor, qtd_brinquedos_gato, dono=Dono()):
        self.__dono = dono
        self.__qtd_brinquedos_gato = qtd_brinquedos_gato
        # extends Animal
        super().__init__(nome, idade, cor)

        # Overwrite method

    def __str__(self):
        return f"O nome do gato é: {self.nome}. A idade é: {self.idade}. A cor é: {self.cor}" \
               f" A quantidade de brinquedos: {self.__qtd_brinquedos_gato}"

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
