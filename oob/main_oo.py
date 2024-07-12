from cachorro import Cachorro
from gato import Gato
from dono import Dono


ca1 = Cachorro("Spike", 11, "Branco", 3, dono=Dono('Tiago'))

print(ca1.nome)
print(ca1.dono.nome)
print(ca1.idade)
print(ca1.cor)
print(ca1.qtd_ossos)
print(ca1.fazer_barulho())
print(ca1.brincar())

ga1 = Gato("Trunks", 2, "Cinza", dono=Dono('Felipe'))

print(ga1.nome)
print(ga1.dono.nome)
print(ga1.idade)
print(ga1.cor)
print(ga1.fazer_barulho())
print(ga1.brincar())