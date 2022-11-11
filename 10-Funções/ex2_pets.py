# Os argumentos podem ser passados para as funções de várias maneiras
# Podemos usar argumentos posicionais
# Argumentos posicionais devem estar na mesma ordem em que os parâmetros

# Argumentos posicionais
# Considere a função que apresente informações sobre animais de estimação
# A função informa o tipo de cada animal e o nome dele
print("=== Example: 1 ===")
def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação.

    Args:
        animal_type (str): tipo do animal
        pet_name (str): nome do animal
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Várias chamadas de função
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
print()

# Argumentos nomeados
# Um argumento nomeado (keyword argument) é um par nome-valor passado para uma função
# Associamos diretamente o nome e o valor no próprio argumento
# Para que não haja confução quando ele for passado para a função
print("=== Example: 2 ===")
def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação.

    Args:
        animal_type (str): tipo do animal
        pet_name (str): nome do animal
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Quando Python lê a chamada da função:
# Ele sabe que deve armazenar o argumento 'cat no parâmetro animal_type
# Ele sabe que deve armazenar o argumento 'doby no parâmetro pet_name
describe_pet(animal_type='cat', pet_name='doby') # Argumentos nomeados

# Valores default
# Se um argumento para um parâmetro não for especificado na chamada da função
# O valor default do parâmetro será utilizado
print("=== Example: 3 ===")
def describe_pet(pet_name, animal_type='dog'):
    """Exibe informações sobre um animal de estimação.

    Args:
        pet_name (str): nome do animal
        animal_type (str, optional): tipo do animal. Defaults to ''.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('willie')
# Como um argumento explícito para o animal_type foi especificado
# Python ignorará o valor default do parâmetro
describe_pet('harry', 'hamster')
