import json

numbers = [2, 3, 5, 7, 11, 13]

# É comum usar a extensão de arquivo .json para indicar que os dados do arquivo estão armazenados em formato JSON.
file_name = 'Extras/armazenando_dados/numbers.json'

with open(file_name, 'w') as file_object:
    # json.dump() para armazenar a lista numbers no arquivo numbers.json
    json.dump(numbers, file_object)


