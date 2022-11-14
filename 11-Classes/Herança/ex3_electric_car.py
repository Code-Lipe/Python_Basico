# Método __init__() de uma classe-filha
# A primeira tarefa de Python ao criar uma instância de uma classe-filha éatribuir valores a todos os atributos da classe-pai. 
# Para isso, o método__init__() de uma classe-filha precisa da ajuda de sua classe-pai.
# Qualquer método da classe-pai que não se enquadre no que você estiver,
# tentando modelar com a classe-filha pode ser sobrescrito.
# Para isso, defina um método na classe-filha com o mesmo nome do método da classe-pai que você deseja sobrescrever.
class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Devolve a descrição completa e formatada

        Returns:
            str: descrição do carro
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


# Instâncias como atributos
# Ao modelar algo do mundo real no código você poderá perceber que está,
# adicionando cada vez mais detalhes em uma classe
# Nessas situações, talvez você perceba que parte de uma classe pode ser escrita como uma classe separada
class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""

    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print(f"This car has a {self.battery_size} -KWh battery")

    
    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de pecorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f"This car can go approximately {range}"
        message += " miles on a full charge."
        print(message)


class EletricCar(Car): # Classe-filha
    """Representa aspectos específicos de veículos elétricos."""

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai.

        Args:
            make (str): marca do carro
            model (str): modelo do carro
            year (int): ano do carro
        """

        # A função super() ajuda Python a criar conexões entre a classe-pai  e a filha
        super().__init__(make, model, year)

        # Atributo que cria uma nova instância de Battery
        self.battery = Battery()
        

my_tesla = EletricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
