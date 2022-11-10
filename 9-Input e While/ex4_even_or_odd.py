# Operador de módulo
# Operador de módulo (%), que divide um número por outro e devolve o resto
# Determinando se um número é par ou ímpar

number = input("Enter a number, add I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even.")

else:
    print(f"The number {number} is odd.")
