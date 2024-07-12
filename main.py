# Variables and commentaries
name_inter = "Daniel Sam"

type_int = 11

print(type(name_inter))
print(type(type_int))

# CONSTANTS

VARIABLE_CONTANTE_NAME = "Daniel Alencar"
print(VARIABLE_CONTANTE_NAME)
VARIABLE_CONTANTE_NAME = "Alterada pq não existe, ah boas praticas"
print(VARIABLE_CONTANTE_NAME)

# Booleans first character Uppercase

var_true = True
var_false = False

# Float

var_float = 5.5

# Operation mathematics

print(4 + 5)
print(6  - 7)
print(3 * 9)
print( 8 / 4)

# Use value var type_int and multiple
print(type_int * 3)

# Comparison operators
print(4 > 5)
print(5 == 5)
print(6 < 7)
print(4 <= 7)
print(9 >= 4)
print(5 != 5)

# Logical Operators

# IF (not) negation operator
print(not(5 > 5))
# If one condition == true
print((4 != 3) or (56 < 44))
# If every statement is true
print((2 == 2) and (4 > 2))

# Condition Structures
age = 17
if age > 18 and age <= 59:
    print("Adulto")
elif age >= 60:
    print("Ansião")
else:
    print("Adolecente")

# Repeating Structures
# range(init, value, increment)
for i in range(0, 10, 2):
    print(i)
else:
    print("Teste realizado com sucesso do for!")

# While
quantity = 1

while quantity <= 5:
    print("numero:", quantity)
    quantity += 1
