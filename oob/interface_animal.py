import abc


#Every interface has methods without defined behavior

class InterfaceAnimal(abc.ABC):

    @abc.abstractmethod
    def fazer_barulho(self):
        pass

    @abc.abstractmethod
    def brincar(self):
        pass
