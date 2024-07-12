import abc


#Every interface has methods without defined behavior

class Interface_Animal(abc.ABC):

    @abc.abstractmethod
    def fazer_barulho(self):
        pass

    @abc.abstractmethod
    def brincar(self):
        pass
