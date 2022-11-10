# Usando uma flag
# Se o programa deva executar somente enquanto MUITAS condições forem verdadeiras
# Podemos definir uma váriavel que determina se o programa com um todo deve estar ativo
# Essa variável, chamada de flag atua como um sinal para o programa

prompt = "\nTell me sometihing, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    
    else:
        print(message)
