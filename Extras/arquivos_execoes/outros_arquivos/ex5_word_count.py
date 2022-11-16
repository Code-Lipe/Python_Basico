# Trabalhando com vários arquivos
def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo.

    Args:
        filename (txt): arquivo de texto
    """
    try:
    
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        
        # Falhando silenciosamente 
        # Você pode usar o 'pass' que diz para não fazer nada e o programa continua como se nada tivesse acontecido
        message = f"Sorry, the file {filename} does not exist."
        print(message)

    else: 
        # Conta o número aproximado de palavras no arquivo

        words = contents.split()
        num_words = len(words)
        print(f"The file {filename}: \nhas about {num_words} words.")


file_alice = 'Extras/arquivos_execoes/arquivos_texto/alice.txt'
file_programming_error = 'programming.txt'
file_programming = 'Extras/arquivos_execoes/arquivos_texto/programming.txt'

file_names = [file_alice, file_programming_error, file_programming]
for file_name in file_names:
    print()
    count_words(file_name)
