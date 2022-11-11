# Valores de retorno
# Uma função nem sempre precisa exibir sua saída diretamente
# Ela pode processar alguns dados e então devolver um valor ou um conjunto de valores
# O valor devolvido pela função é chamado de valor de retorno (return)

# Devolvendo um valor simples
print("=== Example: 1 ===")
def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante.

    Args:
        first_name (str): primeito nome
        last_name (str): último nome

    Returns:
        str: nome completo e formatado
    """

    full_name = f"{first_name} {last_name}"
    return full_name.title()


wizard = get_formatted_name('harry', 'potter')
print(wizard)
print()

# Deixando um argumento opcional
# Valores default podem ser usados para deixar um argumento opcional

print("=== Example: 2 ===")
def get_formatted_name(first_name, last_name, middle_name=''):
    """Devolve um nome completo formatado de modo elegante.

    Args:
        first_name (str): primeito nome
        last_name (str): último nome
        middle_name (str, optional): nome do meio. Defaults to ''.

    Returns:
        str: nome completo ou nome inicial com o final
    """

    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
