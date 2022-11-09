# Expressões booleanas
# Uma expressão booleana é apenas outro nome para um teste condicional.
# Um valor booleano é True ou False: game_active = True ou can_edit = False

# Um exemplo simples
print("=== Example: 1 ===")
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    # Python usa os valores True e False
    # E assim decide se o código em uma instrução if deve ser executado
    if car == "bmw": # Se for True
        print(car.upper())

    else: # Se for False
        print(car.title())
print()

# Verificando a igualdade
print("=== Example: 2 ===")

car = "bmw"
print(car == "bmw") # True
print(car == "audi") # False
print()

# Ignorando as diferenças entre maiúsculas e minúsculas na igualdade
print("=== Example: 3 ===")
# Testes de igualdade difenciam maiúsculas de minúsculas em Python
car = "Audi"
print(car == "audi") # False
print(car.lower() == "audi") # True
print()

# Verificando a difereça
print("=== Example: 4 ===")
# Se quiser determinar se dois valores não são iguais
# Você pode usar ponto de exclamação e um sinal de igualdade (!=)
requested_topping = "mushrooms"
if requested_topping != "anchovies": # True, são diferentes
    print("Hold the anchovies!")
print()

# Comparações numéricas
print("=== Example: 5 ===")
age = 19
# <: menor, <=: menor ou igual
# >: maior, >=: maior ou igual
print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False
print()

# Usando "and" para testar várias condições
# and: retorna True se as duas condições passarem no teste
print("=== Example: 6 ===")
age_0 = 22
age_1 = 18
# Uso dos parênteses em torno dos testes para melhor legibilidade: print(() and ())
print((age_0 >= 21) and (age_1 >= 21)) # False

age_1 = 22
print((age_0 >= 21) and (age_1 >= 21)) # True
print()

# Usando "or" para testar várias condições
# or: retorna True se UMA das duas condições passarem no teste
print("=== Example: 7 ===")
age_0 = 22
age_1 = 18
# Uso dos parênteses em torno dos testes para melhor legibilidade: print(() and ())
print((age_0 >= 21) or (age_1 >= 21)) # True

age_0 = 18
print((age_0 >= 21) or (age_1 >= 21)) # False
print()

# Verificando se um valor está em uma lista
# Para descobrir se um valor em particular já está em um lista
# Utilize a palavra reservada "in"
print("=== Example: 8 ===")
requested_topping = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_topping) # True
print("pepperoni" in requested_topping) # False
print()

# Verificando se um valor não está em uma lista
# Para descobrir se um valor em particular não está em um lista
# Utilize a palavra reservada "not"
print("=== Example: 9 ===")
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
print()
