print("=== Inteiro (int) ===")
print(2 + 3) # Somar (+)
print(3 - 2) # Subtrair (-)
print(2 * 3) # Multiplicar (*)
print(3 / 2) # Dividir (/)

# Ordem das Operações
print("=== Ordem das Operações ===")
print(2 + 3 * 4) # Resultado: 14
print((2 + 3) * 4) # Resultado: 20

# Flutuante (float)
print("=== Flutuante (float) ===")
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)

# Evitando erros de tipo com a função str()
print("=== Extra: Função str() ===")
age = 25
message = "Happy " + str(age) + "rd Birthday"
print(message)
