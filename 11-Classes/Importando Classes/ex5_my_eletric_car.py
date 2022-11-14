from modulo_car import EletricCar

# Criando carro elétrico
my_testa = EletricCar('teste', 'model s', 2016)
print(my_testa.get_descriptive_name())
my_testa.battery.describe_battery()
my_testa.battery.get_range()
