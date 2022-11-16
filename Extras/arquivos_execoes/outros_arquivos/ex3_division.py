# Exceções
# Python usa objetos especiais chamados exceções para administrar erros,
# ao surgirem durante a execução de um programa
# Se a exceção não for tratada, o programa será interrompido e um traceback,
# que inclui uma informação sobre a exceção levantada, será exibido
# Com bloco try-except, os usuários verão mensagens de erro simpáticas escritas por você

print("=== Example: 1 ===")
# Tratando a exceção ZeroDivisionError
# Vamos observar um erro simples, que faz Python levantar uma exceção

# O erro informado no traceback, ZeroDivisionError, é um objeto exceção
# print(5/0)

# Diremos a Python o que fazer quando esse tipo de exceção ocorrer
# Usando blocos try-except

# Se o código no bloco try funcionar, Python ignorará o except
# Nesse exemplo, o código no bloco try gera um ZeroDivisionError,
# portanto Python procura um except que lhe diga como deve responder
try: 
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print()

print("=== Example: 2 ===")
# Usando exceções para evitar falhas
# Vamos observar um exemplo de como o programa segue em frente depois do erro
# Se o programa responder as entradas inválidas de modo apropriado, 
# ele poderá pedir mais entradas válidas em vez de causar uma falha

# Criando uma calculadora simples que faça apenas divisões
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    # Bloco else
    # Qualquer código que dependa do bloco try ter sucesso, deve ser coloco no bloco else
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)  
