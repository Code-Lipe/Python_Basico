# Escrevendo prompts claros
# Sempre que usar a função input(), inclua um prompt claro, facil de compreender

print("=== Example: 1 ===")
name = input("Please enter your name: ")
print(f"Hello, {name.title()}!")
print()

# Às vezes, você vai querer um prompt que seja maior que uma linha
# Você pode armazenar seu prompt em uma variável e passa-lá para a função input()
print("=== Example: 2 ===")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your fist name? "

name = input(prompt)
print(f"Hello, {name.title()}!")
