"""Uma classe que pode ser usada para representar um carro."""
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
        self.odometer_reading = 0

    
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

    
    def update_odometer(self, mileage):
        """
        Define o valor de leitura do hodômetro com o valor especificado
        Rejeita a alteração se for tentativa de definir um valor menor para o hodômetro
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    
    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.odometer_reading += miles


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
        