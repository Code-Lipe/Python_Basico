# Lendo um arquivo inteiro
# open() abre o arquivo para acessá-lo
# file_directory tem o caminho para que open() encontre o arquivo pi_digits.txt
# file_object recebe o objeto que representa pi_digits.txt
# read() lê todo o conteúdo do arquivo e armazenamos em contents

file_directory = 'Extras/arquivos_excecoes/arquivos_texto/pi_digits.txt'

print("=== Example: 1 ===")
with open(file_directory) as file_object:
    contents = file_object.read()
    print(contents)
print()

print("=== Example: 2 ===")
# Lendo dados linha a linha
# Podemos usar um laço for no objeto arquivo para nalisar cada uma das suas linhas

with open(file_directory) as file_object:
    for line in file_object:
        print(line.rstrip()) # rstrip() elimina linhas em branco extras
print()

print("=== Example: 3 ===")
# Criando uma lista de linhas de um arquivo
# Se quiser preservar o acesso ao conteúdo de um arquivo fora do bloco with,
# você pode armazenar as linhas do arquivo em uma lista dentro do bloco,
# e então trabalhar com essa lista

with open(file_directory) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print()

print("=== Example: 4 ===")
# Trabalhando com o conteúdo de um arquivo
# Depois de ler um arquivo em memória, você poderá fazer o que quiser com esses dados

# Criando uma única string contendo todos os dígitos do arquivo, sem espaços em branco
with open(file_directory) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
