# Deixando o usuário decidir quando quer sair

prompt = "\nTell me sometihing, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
