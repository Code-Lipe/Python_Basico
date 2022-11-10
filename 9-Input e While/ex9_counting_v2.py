# Usando continue em um laço
# Em vez de sair totalmente de um laço sem executar o restante de seu código
# Podemos usar a instrução continue para retornar ao início, com base no resultado de um teste condicional
# Programa que considera um laço que conte de 1 a 10 mas apresente os números ímpares desse intervalo

print("=== Example: 1 ===")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
print()

# Evitando loops infinitos
print("=== Example: 2 ===")
x = 1
while x <= 5:
    print(x)
    
    # Se omitir essa liha, o laço executará para sempre
    x += 1 
