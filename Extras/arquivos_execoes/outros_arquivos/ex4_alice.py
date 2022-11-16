# Tratando a exceção FileNotFoundError
# Um problema comum ao trabalhar com arquivos é o tratamento de arquivos ausentes
# O arquivo pode estar em outro lugar, nome incorreto ou arquivo não exista
# Podemos tratar todas essas situações de um modo simples com um bloco try-except

# Lendo um arquivo que não existe. O programa a seguir tenta ler o conteúdo de alice.txt,
# mas não salvei o arquivo no mesmo diretório em que está ex4_alice.py

# Movi o arquivo alice.txt para o diretório correto, portanto o bloco try funcionará
file_name = 'Extras/arquivos_execoes/arquivos_texto/alice.txt'

try:
    
    with open(file_name) as file_object:

        # Python não é capaz de ler um arquivo ausente, portanto uma exceção poderá ser levantada se tal arquivo for ausente
        contents = file_object.read()

except FileNotFoundError:
    message = f"Sorry, the file {file_name} does not exist."
    print(message)

else: # Conta o número aproximado de palavras no arquivo

    # Analisando textos
    # Podemos analisar arquivos- texto que contenham blocos inteiros
    # split() separa uma string em partes sempre que encontra um espaço,
    # e armazena todas as partes em uma lista

    words = contents.split()
    num_words = len(words)
    print(f"The file {file_name} has about {num_words} words.")
