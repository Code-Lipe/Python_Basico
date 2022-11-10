# Usando int() para aceitar entradas numéricas
# Se usarmos a função input()
# Python interpretará tudo que o usuário fornecer como uma string
# Programa que determina se as pessoas têm altura sufuciente para a montanha-russa

height = input("How tall are you, in inches? ")
height = int(height) # int() converte para inteiro

if height >= 36:
    print("You're tall enough to ride!")

else:
    print("You'll be able to ride when you're a little older.")
