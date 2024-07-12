from animal import Animal
from interface_animal import Interface_Animal


class Gato(Animal, Interface_Animal):


    def __init__(self, nome, idade, cor):
        # extends Animal
        super().__init__(nome, idade, cor)

    # function action
    def fazer_barulho(self):
        return "Miauu"

    def brincar(self):
        return "O gato está pulando no telhado"
