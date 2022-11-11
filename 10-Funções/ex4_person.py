# Devolvendo um dicionário
# Uma função pode devolver qualquer tipo de valor necessário
# Incluindo estruturas de dados complexos como listas e dicionários

def build_person(first_name, last_name, age=''):
    """Devolve um dicionário com informações sobre uma pessoa.

    Args:
        first_name (str): primeiro nome
        last_name (str): último nome
        age (int, optional): idade. Defaults to ''.

    Returns:
        str, int: dicionário
    """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


wizard = build_person('hermione', 'granger', age=27)
print(wizard)