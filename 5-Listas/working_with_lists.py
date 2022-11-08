# Trabalhando com listas
# Percorrendo uma lista inteira com um laço
print("=== Example: 1 ===")
witches = ["Harry", "Hermione", "Ron"]
for witch in witches:
    print(f"Name: {witch}") # Formatando com f-strings (f"")
print("Welcome to Hogwarts!")
print()

# Criando listas numéricas
# Usando a função range()
print("=== Example: 2 ===")
for value in range(1, 5): # range() de Python facilita gerar uma série de números
    print(value) # A saída não conterá o valor final, que seria 5
print()

# Usando range() para criar uma lista de números
print("=== Example: 3 ===")
numbers = list(range(1, 6)) # range() para de contar no último valor, sem incluir ele
print(numbers) # A saída não conterá o valor final, que seria 6

# Usando range() para ignorar alguns números em um dado intervalo
print("=================")
even_numbers = list(range(2, 11, 2)) # Listar os números pares entre 1 e 10
print(even_numbers)

# Em Python, dois asteriscos (**) representam exponenciais
print("=================")
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
print()

# Estatísticas simples com uma lista de números
print("=== Example: 4 ===")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # Valor mínimo
print(max(digits)) # Valor máximo
print(sum(digits)) # Soma de uma lista de números
print()

# List comprehensions (abrangência de lista)
# Permite gerar lista com apenas uma linha de código
print("=== Example: 5 ===")
squares = [value**2 for value in range(1, 11)]
print(squares)
print()

# Fatiamento em uma lista
print("=== Example: 6 ===")
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3]) # De 0 a 3, os elementos 0, 1 e 2 serão devolvidos
print(players[1:4]) # De 1 a 4, os elementos 1, 2, 3  serão devolvidos
print(players[:4]) # De 0 a 4, os elementos 0, 1, 2, 3  serão devolvidos
print(players[2:]) # De 2 a 4, os elementos 2, 3, 4  serão devolvidos
print(players[-3:]) # Exibe os nomes dos três últimos jogadores
print("===============================")

# Percorrendo uma fatia com um laço
players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
print()

# Copiando uma lista
print("=== Example: 6 ===")
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:] # Fatiando( e armazenando) todos os elementos da lista 
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorite foods are: ")
print(my_foods)
print("My friend's favorite foods are: ")
print(friend_foods)
