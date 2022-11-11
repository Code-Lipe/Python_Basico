# Modificando uma lista em uma função
# Quando passamos uma lista a uma função, ela pode ser modificada

print("=== Example: 1 ===")
# Começa com alguns designs que devem ser impressos
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
complete_models = []

# Simula a impressão de cada design, até que não haja mais nenhum
# Trasfere cada design para completed_models após a impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simula a criação de uma impressão 3D a partir do design
    print(f"Printing model: {current_design}")
    complete_models.append(current_design)


# Exibe todos os modelos finalizados
print("\nThe following models have been printed:")
for completed_model in complete_models:
    print(completed_model)
print()

# Podemos reorganizar esse código escrevendo duas funções
print("=== Example: 2 ===")
def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.

    Args:
        unprinted_design (str, list): lista de design para serem impressos
        completed_models (str, list): lista de design impressos
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Mostra todos os modelos impressos.

    Args:
        completed_models (str, list): modelos impressos
    """
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Evitando que uma função modifique uma lista
# Às vezes, você vai querer evitar que uma função modifique uma lista
# Nesse caso, podemos tratar esse problema passando uma cópia da lista para função
# Qualquer alteração que a função fizer na lista afetará apenas a cópia
# A notação de fatia [:] cria uma cópia da lista para ser enviada à função

# exemplo:
# nome_da_função(nome_da_lista[:])
