# Lendo um arquivo inteiro
# open() abre o arquivo para acessá-lo
# file_directory tem o caminho para que open() encontre o arquivo pi_digits.txt
# file_object recebe o objeto que representa pi_digits.txt
# read() lê todo o conteúdo do arquivo e armazenamos em contents

file_directory = 'Extras/arquivos_execoes/arquivos_texto/pi_digits.txt'
with open(file_directory) as file_object:
    contents = file_object.read()
    print(contents)
