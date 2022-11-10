# Usando break para sair de um laço
# Para sair de um laço whike de imediato, sem executar qualquer código restante no laço
# Utilize a instrução break
# Este programa pergunta ao usuário os nomes de lugares que ele já visitou

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
