from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, cor, qtd_ossos):
        self.qtd_ossos = qtd_ossos
        # Extends generic class
        super().__init__(nome, idade, cor)
        # Function action
    def latir(self):
        return "Au au"