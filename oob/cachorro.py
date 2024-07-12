from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, cor, qtd_ossos):
        self.__qtd_ossos = qtd_ossos
        # Extends generic class
        super().__init__(nome, idade, cor)


    # Methods Access [GET | SETTER ]
    @property
    def qtd_ossos(self):
        return self.__qtd_ossos

    @qtd_ossos.setter
    def qtd_ossos(self, qtd_ossos):
        self.__qtd_ossos = qtd_ossos


        # Function action
    def fazer_barulho(self):
        return "Au au"