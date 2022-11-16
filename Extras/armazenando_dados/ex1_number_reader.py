import json

# Programa que use json.load() para ler a lista de volta para a memória:

file_name = 'Extras/armazenando_dados/numbers.json'

with open(file_name) as file_object:
    #json.load() para carregar as informações armazenadas em numbers.json, 
    # e as guardamos na variável numbers
    numbers = json.load(file_object)

print(numbers)
