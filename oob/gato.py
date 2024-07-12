from animal import Animal

class Gato(Animal):

    def __init__(self, nome, idade, cor):
        # extends Animal
        super().__init__(nome, idade, cor)

    # function action
    def fazer_barulho(self):
        return "Miauu"
