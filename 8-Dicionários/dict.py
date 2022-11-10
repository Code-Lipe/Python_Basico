# Um dicionário simples
# Um par chave-valor é um conjunto de valores associados um ao outro
# Quando fornecemos uma chave, Python devolve o valor associado a essa chave
# Toda chave é associada a seu valor por meio de dois pontos
# Pares chave-valor individuais são separadas por vírgulas
print("=== Example: 1 ===")
alien_0 = {"color": "green", "points": 5} # Chaves: color e points, valores: green e 5
print(alien_0["color"]) # green
print(alien_0["points"]) # 5
print()

# Acessando valores em um dicionário
print("=== Example: 2 ===")
alien_0 = {"color": "green", "points": 5}
new_points = alien_0["points"]
print(f"You just earned {new_points} points!")
print()

# Adicionando novos pares chave-valor
print("=== Example: 3 ===")
alien_0 = {"color": "green", "points": 5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
print()

# Começando com um dicionário vazio
print("=== Example: 4 ===")
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)
print()

# Modificando valores em um dicionário
# Considere um alienígena que muda de verde para amarelo à medida que o jogo prossegue
print("=== Example: 5 ===")
alien_0 = {"color": "green"}
print(f"The alien is {alien_0['color']}.")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}.")

print("===========================")
# Um exemplo mais interessante, vamos monitorar a posição de um alienígena
# Ele pode se deslocar com velocidades diferentes
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original x_position: {alien_0['x_position']}")

if alien_0["speed"] == "slow":
    x_increment = 1

elif alien_0["speed"] == "medium":
    x_increment = 2

else:
    # Este deve ser um alienígena rápido
    x_increment = 3

# A nova posição é a posição antiga somada ao incremento
new_x_position = alien_0["x_position"] + x_increment
alien_0["x_position"] = new_x_position
print(f"New x_position: {alien_0['x_position']}")
print()

# Removendo pares chave-valor
# Tudo de que del precisa é do nome do dicionário e da chave que você deseja remover
print("=== Example: 6 ===")
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"] # O par chave-valor apagado é removido permanentemente
print(alien_0)
print()

# Um dicionário de objetos semelhantes
print("=== Example: 7 ===")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print(f"Sara's favorite language is {favorite_languages['sarah'].title()}.")
print()

# Percorrendo um dicionário com um laço
print("=== Example: 8 ===")
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

# Percorrendo todas as chaves de um dicionário com um laço
# O método keys() é conveniente quando não precisamos trabalhar com todos os valores
print("=== Example: 9 ===")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for name in favorite_languages.keys(): # Você pode optar por remover o keys()
    print(f"Name: {name.title()}")

    if name in favorite_languages:
        print(f"Hi {name.title()}! I see your favorite language is {favorite_languages[name].title()}\n")

# Percorrendo as chaves de um dicionário em ordem usando um laço
# Podemos usar a função sorted() para obter uma cópia ordenada das chaves
print("=== Example: 10 ===")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for talking the poll.")
print()

# Percorrendo todos os valores de um dicionário com um laço
# Se você estiver mais interessado nos valores, use o método values()
# Para ver cada linguagem escolhida sem repetições, use o conjunto (set)
print("=== Example: 11 ===")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
print()

# informações aninhadas
# Se quiser uma lista de itens como um valor em um dicionário, aninhe informações
# Uma lista de dicionários:
print("=== Example: 12 ===")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yelloww', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Usando range() para criar uma frota de 30 alienígenas:
print("==================================")
aliens = [] # Lista vazia para armazenar alienígenas

for alien_number in range(30): # Criar 30 alienígenas verdes
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]: # Mostrar os 5 primeiros alienígenas
    print(alien)
print(f"Total number of aliens: {len(aliens)}")
print()

# Uma lista em um dicionário
print("=== Example: 13 ===")
# Armazenando informações sobre uma pizza que está sendo pedida
pizza = {'crust': 'thick', 'toppings': ['murshrooms', 'extra cheese'],}

# Pedido
print(f"You ordered a {pizza['crust']} -crust pizza witch the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")
print()

# Um dicionário em um dicionário
# Podemos aninhar um dicionário em outro dicionário
# Mas o código poderá ficar complicado rapidamente se isso for feito
print("=== Example: 14 ===")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"Username {username}")
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print(f"Full name: {full_name.title()}")
    print(f"Location: {location.title()}\n")
