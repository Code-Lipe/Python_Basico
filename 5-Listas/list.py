# Em Python, colchetes ([]) indicam uma lista.
# Elementos individuais são separados por vírgulas
print("=== Example: 1 ===")
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print()

# Acessando elementos de uma lista
print("=== Example: 2 ===")
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles[0].title()) # Acessando e formatando o elemento "trek"
print(bicycles[2].title()) # Acessando e formatando o elemento "redline"
print(bicycles[-1]) # Acessando o último elemento da lista"
print()

# Usando valores individuais de uma lista
print("=== Example: 3 ===")
bicycles = ["trek", "cannondale", "redline", "specialized"]
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
print()

# Alterando, acrescentando e removendo elementos
print("=== Example: 4 ===")
motorcycles = [] # Lista vazia
motorcycles.append("honda") # Acrescentando
motorcycles.append("yamaha") # Acrescentando
motorcycles.append("suziki") # Acrescentando
print(motorcycles)
motorcycles[0] = "ducati" # Alterando
print(motorcycles)
motorcycles.insert(1, 'bmw') # Adicionando novo elemento em qualquer posição
print(motorcycles)
del motorcycles[0] # Removendo um elemento
print(motorcycles)
print()

# Removendo um item com o método pop()
print("=== Example: 5 ===")
# O método pop() remove o último item ou de qualquer posição de uma lista
# E permite que você trabalhe com esse item depois da remoção
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop(1) # Removendo um valor da lista e armazenando na variável
print(motorcycles)
print(popped_motorcycle)
print()

# Removendo um item de acordo com o valor (remove())
# O método remove() apaga apenas a primeira ocorrência do valor que você especificar
print("=== Example: 6 ===")
motorcycles = ["honda", "ducati", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati" # Eu sei qual item quero remover 
# Usando laço para remover valores repetidos
while too_expensive in motorcycles:
   motorcycles.remove(too_expensive)
print(motorcycles)
print("The " + too_expensive.title() + " was sold.")
print()

# Organizando uma lista
print("=== Example: 7 ===")
# Ordenando uma lista de forma permanente com o método sort()
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.sort() # Itens em ordem alfabética
print(cars) # Não podemos mais retornar à ordem original.
cars.sort(reverse=True) # Ordenando a lista em ordem alfabética inversa
print(cars)
# Ordenando uma lista temporariamente com a função sorted()
cars = ["bmw", "audi", "toyota", "subaru"]
print("===================================")
print("Here is the original list:")
print(cars)
print(sorted(cars))
print("Here is the original list again: ")
print(cars)
print()

# Exibindo uma lista em ordem inversa
print("=== Example: 8 ===")
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)
print()

# Descobrindo o tamanho de uma lista
print("=== Example: 9 ===")
cars = ["bmw", "audi", "toyota", "subaru"]
print("Number of cars:", len(cars))
print()

# Evitando erros de índice quando trabalhar com listas
print("=== Example: 10 ===")
# Exemplo de erro no índice:
motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles[3]) # IndexError: list index out of range
# Sempre que quiser acessar o último item de uma lista, você deve usar o índice -1
print(motorcycles[-1]) # Evitando o erro
# A única ocasião em que essa abordagem causará um erro
# É quando solicitamos o último item de uma lista vazia:
# Exemplo de erro com a lista vazia:
motorcycles = []
# print(motorcycles[-1]) # IndexError: list index out of range
