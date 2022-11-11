# Passando uma lista para uma função
# Com frequência, você achará útil passar uma lista para função
# Seja uma lista de nomes, números ou de objetos mais complexos
# Se passarmos uma lista a uma função, ela terá acesso direto ao conteúdo da lista
def greet_users(names):
    """Exibe uma saudação simples a cada usúario da lista.

    Args:
        names (str): lista de nomes
    """
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)


usernames = ['hanna', 'ty', 'margot']
greet_users(usernames)
