import json

# Carrega o nome do usuário se foi armazenado anteriormente
# Caso contrário, pede que o usuário forneça o nome e armazena essa informação

def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível.

    Returns:
        txt: arquivo de texto com o nome
    """
    file_name = 'Extras/armazenando_dados/username.json'
    try:
        with open(file_name) as file_object:
            user_name = json.load(file_object)

    except:
        return None
    else:
        return user_name
        

def get_new_username():
    """Pede um novo nome de usuário.

    Returns:
        str: nome de usuário
    """
    user_name = input("What is your name? ")
    file_name = 'Extras/armazenando_dados/username.json'
    with open(file_name, 'w') as file_object:
        json.dump(user_name, file_object)
    return user_name


def greet_user():
    """Saúda o usuário pelo nome."""
    user_name = get_stored_username()
    if user_name:
        print(f"Welcome back, {user_name.title()}!")
    else:
        user_name = get_new_username()
        print(f"We'll remember you when yoy come back, {user_name.title()}!")


greet_user()
