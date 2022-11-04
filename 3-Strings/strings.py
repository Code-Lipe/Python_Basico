# title() formata a primeira letra da palavra para maiúscula
print("=== title() ===")
name = "harry potter"
print(name.title())
print()

# upper() formata todos os caracteres para maiúsculas
# lower() formata todos os caracteres para minúsculas
print("=== upper(), lower() ===")
name = "Hermione Granger"
print(name.upper())
print(name.lower())
print()

# Combinando ou concatenando strings
print("=== Combinando Strings ===")
first_name = "albus"
last_name = "dumbledore"
full_name = first_name + " " + last_name
print(full_name)
message = "Hello, " + full_name.title() + "!"
print(message)
print()

# Tabulações ou quebras de linha
print("=== Tabulações - Quebras de linha ===")
message = "Enemy:\n\tLord Voldemort" # Tabulação (\t) e quebra de linha (\n)
print(message)
print()

# Removendo espaços em branco
print("=== Removendo espaços em branco ===")
name = "Dobby"
print(name.rstrip()) # Remove os espaços a direita
name = " Edwiges"
print(name.lstrip()) # Remove os espaços a esquerda
name = " Nagini "
print(name.strip()) # Remove os espaços a esqueda e direita
print()

# Evitando erros de sintaxe com strings
# ERRO: message = 'I'm fine'
message = "I'm fine" # Evitando o erro 
print(message)
