from cachorro import Cachorro
from gato import Gato

ca1 = Cachorro("Spike", 11, "Branco", 3)

print(ca1.nome)
print(ca1.idade)
print(ca1.cor)
print(ca1.qtd_ossos)
print(ca1.fazer_barulho())
print(ca1.brincar())

ga1 = Gato("Trunks", 2, "Cinza")

print(ga1.nome)
print(ga1.idade)
print(ga1.cor)
print(ga1.fazer_barulho())
print(ga1.brincar())