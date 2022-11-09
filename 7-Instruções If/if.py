# Há vários tipos de instruções if
# E a escolha dependerá do número de condições que devem ser testadas

# Instruções if simples:
# Se o teste condicional for avaliado como True
# Python executará o código após a instrução if 
# Se o teste for avaliado como False
# Python ignorará o código depois da instrução if
print("=== Example: 1 ===")
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
print()

# Instruções if-else
print("=== Example: 2 ===")
age = 17
if age >= 18: # True
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

else: # False
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
print()

# Sintaxe if-elif-else
print("=== Example: 3 ===")
age = 12
if age < 4: # if: se...
    price = 0
elif age < 18: # elif: se não, se...
    price = 5
else: # else: se não...
    price = 10
print(f"Your admission cost is ${price}.")
print()

# Usando vários blocos elif
# Podemos usar quantos blocos elif quisermos em nosso código
# Python não exige um bloco else no final de uma cadeia if-elif
print("=== Example: 4 ===")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65: 
    price = 5
print(f"Your admission cost is ${price}.")
print()

# Testando várias condições
# A cadeia if-elif-else é eficaz 
# Mas é apropriada somente quando você quiser que apenas um teste passe.
# Às vezes, porém, é importante verificar todas as condições de interesse.
# Você deve usar uma série de instruções if simples, sem blocos elif ou else.
# Essa técnica faz sentido quando mais de uma condição pode ser True 
# E você quer atuar em todas as condições que sejam verdadeiras.
print("=== Example: 5 ===")
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!")
print()

# Usando instruções if com listas
# E se a pizza ficasse sem green peppers?
print("=== Example: 6 ===")
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!")
print()

# Verificando se uma lista não está vazia
print("=== Example: 7 ===")
requested_toppings = []
if requested_toppings: # True, se tiver ao menos um item na lista
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("Finished making your pizza!")

else: # False
    print("Are you sure you want a plain pizza?")
print()

# Usando várias listas
print("=== Example: 8 ===")
avaliable_toppings = [
    "mushrooms", 
    "olives", 
    "green peppers",
    "pepperoni", 
    "pineapple", 
    "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("Finished making your pizza!")
