# Passando um número arbitrário de argumentos
# Às vezes, você não saberá com antecedência quantos argumentos uma função terá
# Python permite que uma função receba um número arbitrário de argumentos
# O asterisco no nome do parâmetro diz a Python para criar uma tupla vazia
print("=== Example: 1 ===")
def make_pizza(*toppings):
    """Apresenta a pizza que estamos prestes a preparar"""
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green pappers', 'extra cheese')
print()

# Misturando argumentos posicionais e arbitrários
print("=== Example: 2 ===")
def make_pizza(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar"""
    print(f"\nMaking a {size} -inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green pappers', 'extra cheese')

