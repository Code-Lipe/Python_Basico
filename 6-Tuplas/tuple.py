# Lista são mutáveis
# Ao necessitar de uma lista IMUTÁVEL, as tuplas permitem isso.
# Definindo uma tupla
print("=== Example: 1 ===")
dimensions = (200, 50) # Tuplas usam parênteses no lugar de colchetes ([])
# dimensions[0] = 200 # Erro! Tuplas são imutáveis
print(dimensions[0])
print(dimensions[1])
print()

# Percorrendo todos os valores de tuplas com um laço
print("=== Example: 2 ===")
dimensions = (400, 100) # Sobrescrevendo uma tupla
for dimension in dimensions:
    print(dimension)
print()

print("=================")
names = ("harry", "hermione", "ron")
# names = "dobby" # Vai substituir todos os nomes da lista por cada caractere do nome "dobby"
for name in names:
    print(f"Welcome: {name.title()}")
