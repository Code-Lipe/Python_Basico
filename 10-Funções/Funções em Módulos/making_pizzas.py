# Você pode importar quantas funções quiser de um módulo,
# separando o nome de cada função com uma vírgula

# ATENÇÃO: A melhor abordagem é importar a função ou as funções que você quiser,
# ou importar o módulo todo e usar a notação de ponto. 
# Isso resulta em um código claro, mais fácil de ler e de entender.

# Exemplo 1
# import pizza (para importar todo módulo, usa notação de ponto)

# import pizza 
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Exemplo 2
# from pizza import make_pizza as mp (a palavra resevada 'as' renomeia a função para mp neste programa)

# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(16, 'mushrooms', 'green peppers', 'extra cheese')

# Exemplo 2
# Importando funções específicas

from pizza import make_pizza 
make_pizza(16, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Exemplo 3
# Também podemos fornecer um 'as' para um nome de módulo.

# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Exemplo 4
# Importando todas as funções de um módulo
# Podemos dizer a Python para importar todas as funções de um módulo,
# usando o operador asterisco (*)
# Como todas as funções são importadas, podemos chamar qualquer função pelo nome, 
# sem usar a notação de ponto.

# from pizza import *
# make_pizza(16, 'pepperoni')
# make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
