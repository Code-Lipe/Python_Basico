# Criando e usando uma classe
class Dog(): # Definindo a classe

    # Uma função que faz parte de uma classe é um método
    # __init__() é um método especial que o Python executa automaticamente,
    # sempre que criamos uma nova instância baseada na classe Dog
    def __init__(self, name, age): # self é uma referência à própria instância
        """Uma tentativa simples de modelar um cachorro.

        Args:
            name (str): nome do cachorro
            age (int): idade do cachorro
        """
        # Qualquer variável prefixada com self está disponível a todos os métodos da classe
        self.name = name
        self.age = age

    
    def sit(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(f"{self.name.title()} is now sitting.")


    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(f"{self.name.title()} rolled over!")


# Criando uma instância a partir de uma classe
# Pense em uma classe como um conjunto de instruções para criar uma instância
my_dog = Dog('willie', 6) # Criando o objeto(instânciando)

print("=== Example: 1 ===")
# Acessando atributos
# Para acessar os atributos de uma instância utilize a notação de ponto
print(f"My dog's name is {my_dog.name.title()}.") 
print(f"My dog is {my_dog.age} years old.")
print()

print("=== Example: 2 ===")
# Chamando métodos
my_dog.sit()
my_dog.roll_over()
print()

print("=== Example: 3 ===")
# Criando várias instâncias
your_dog = Dog('lucy', 3)

# my_dog
print(f"My dog's name is {my_dog.name.title()}.") 
print(f"My dog is {my_dog.age} years old.")

# your_ dog
print(f"My dog's name is {your_dog.name.title()}.") 
print(f"My dog is {your_dog.age} years old.")
print()