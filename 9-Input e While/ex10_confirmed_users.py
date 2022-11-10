# Para modificar uma lista enquanto trabalha com ela, utilize um laço while.
# Usar laços while com listas e dicionários permite coletar, armazenar e organizar muitas entradas
# A fim de analisá-las e apresentá-las posteriormente

# Transferindo itens de uma lista para outra
# Começa com os usuários que precisam ser verificados
# E com uma lista vazia para armazenar os usuários confirmados
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verifica cada usuário até que não haja mais usuários não confirmados
# Transfere cada usuário verificado para a lista de usuários confirmados
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Exibe todos os usuários confirmados
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
