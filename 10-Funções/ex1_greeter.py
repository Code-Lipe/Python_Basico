# Definindo uma função
# Uma função simples que exibe uma saudação
# def, essa é a definição da função
# Parâmetro, uma informaçãp de que a função precisa para executar sua tarefa
# Argumentomé uma informação passada para a função em sua chamada

def greet_user(username): # username é um parâmetro
    """Exibe uma saudação simples.""" # Docstring, que descreve o que a função faz
    print(f"Hello, {username}!")


greet_user("Harry Potter") # Chamando a função e passando o argumento (Harry Potter)
