# Usando argumentos nomeados arbitrários
# Às vezes, você vai querer aceitar um número arbitrário de argumentos, 
# mas não saberá com antecedência qual tipo de informação será passado para a função.
# Os asteriscos duplos ** antes do parâmetro fazem Python criar um dicionário vazio
# E coloca quaisquer pares nome-valor recebidos nesse dicionário.
def build_profile(first, last, **user_info):
    """_summary_

    Args:
        first (str): primeiro nome
        last (str): último nome

    Returns:
        dict: retorna um dicionário
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    
    return profile


user_profile = build_profile(
    'albert', 
    'einster', 
    location='princeton', 
    field='physics'
)

print(user_profile)
