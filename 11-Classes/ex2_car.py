# Trabalhado com classes e instâncias
# Podemos modificar os atributos de uma instância diretamente,
# ou escrever métodos que atualizem os atributos de formas específicas
class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro.

        Args:
            make (str): marca do carro
            model (str): modelo do carro
            year (int): ano do carro
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Valor default'

    
    def get_descriptive_name(self):
        """Devolve um nome descritivo

        Returns:
            str: Devolve um nome descritivo, formatado de modo elegante
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print(f"This car has {self.odometer_reading} miles on it.")

    
    def update_odometer(self, mileage): # Atualizando o valor do atributo pelo método
        """
        Define o valor de leitura do hodômetro com o valor especificado
        Rejeita a alteração se for tentativa de definir um valor menor para o hodômetro
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    
    def increment_odometer(self, miles): # incrementando valor de um atributo
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.odometer_reading += miles


print("=== Example: 1 ===")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
print()

print("=== Example: 2 ===")
#Definindo um valor default para um atributo
my_new_car.read_odometer()
print()

print("=== Example: 3 ===")
# Modificando valores de atributos
# A maneira mais simples de modificar o valor de um atributo é acessá-lo,
# diretamente por meio de uma instância
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print("============================")
# Pode ser mais conveniente ter métodos que atualizem determinados atributos para você
my_new_car.update_odometer(23)
my_new_car.read_odometer()
print()

print("=== Example: 4 ===")
# Às vezes, você vai querer incrementar o valor de um atributo de determinada quantidade,
# em vez de definir um valor totalmente novo
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
