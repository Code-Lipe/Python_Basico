# Escrevendo dados em um arquivo vazio
# Para esrever um texto em um arquivo, chame open() com um segundo argumento,
# que diga a Python que você quer escrever dados no arquivo

# Atenção: o modo de escrita ('w') apaga todo o conteúdo do arquivo de texto já existente,
# então comente os exemplos que deseja evitar no momento,
# e execute esse programa para ver o resultado do exemplo desejado em programming.txt

file_name = 'Extras/arquivos_execoes/arquivos_texto/programming.txt'

# === Example: 1 ===
# Podemos abrir um arquivo em modo de:
# leitura ('r')
# escrita ('w')
# concatenação ('a')
# ler e escrever no arquivo ('r+')

with open(file_name, 'w') as file_object: # 'w' abre o arquivo em modo de escrita

    # O resultado você vê dentro do arquivo programming.txt
    file_object.write("I love programming.") # write() permite escrever no arquivo

# === Example: 2 ===
# Escrevendo várias linhas
# write() não acrescenta nenhuma quebra de linha ao texto que você escrever
# Portanto, se deseja escrever mais uma linha, utilize caractere de quebra de linha

with open(file_name, 'w') as file_object:

    # O resultado você vê dentro do arquivo programming.txt
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


# === Example: 3 ===
# Concatenando dados em um arquivo
# Se quiser acrescentar conteúdos em um arquivo em vez de sobrescrever o conteúdo existente,
# você pode abrir o arquivo em modo de concatenação
# Se o arquivo ainda não existe, Python criará um arquivo vazio para você

with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run it a browser.\n")
