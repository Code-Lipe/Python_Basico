# Testando uma função
def get_formatted_name(fist, last, middle=''):
    """Formatando nome

    Args:
        fist (str): primeiro nome
        last (str): último nome
        middle (str, optional): nome do meio. Defaults to ''.

    Returns:
        str: nome completo formatado de modo elegante
    """
    if middle:
        fulll_name = f"{fist} {middle} {last}"
    else:
        fulll_name = f"{fist} {last}"
        
    return fulll_name.title()
