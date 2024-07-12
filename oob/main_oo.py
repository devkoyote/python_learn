from cachorro import Cachorro
from gato import Gato

ca1 = Cachorro("Spike", 11, "Branco")

print(ca1.nome)
print(ca1.idade)
print(ca1.cor)
print(ca1.latir())

ga1 = Gato("Trunks", 2, "Cinza")

print(ga1.nome)
print(ga1.idade)
print(ga1.cor)
print(ga1.miar())