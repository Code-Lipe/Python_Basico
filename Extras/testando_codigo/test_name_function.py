import unittest
from ex1_name_function import get_formatted_name

# A sintaxe para criar um caso de teste exige um pouco de prática, 
# mas depois que você o configurar, será mais fácil adicionar outros casos de teste para suas funções.
# Para escrever um caso de teste para uma função, importe o módulo unittest e a função que você quer testar.
# Em seguida crie uma classe que herde de unittest.TestCase,
# e escreva uma série de métodos para testar diferentes aspectos do comportamento de sua função.

class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'.

    Args:
        unittest (module): modulo de teste
    """
    
    # Qualquer método que comece com test_ será executado de modo automático 
    def test_first_last_name(self):
        """Nomes como 'Harry Potter' funcionam? """

        formatted_name = get_formatted_name('harry', 'potter')

        # Métodos de asserção verificam se um resultado recebido é igual ao resutado que você esperava receber
        # diz o seguinte: “Compare o valor em formatted_name com a string 'Harry Potter'. 
        # Se forem iguais conforme esperado, tudo bem. Contudo, se não forem iguais, me avise!”.
        self.assertEqual(formatted_name, 'Harry Potter')

    
    # Adicionando novo teste
    def test_first_last_middle_name(self):
        """Nomes como 'Ginevra Molly Weasley' funcionam?"""
        
        formatted_name = get_formatted_name('ginevra','weasley', 'molly')
        self.assertEqual(formatted_name, 'Ginevra Molly Weasley')


# unittest.main() diz a Python para executar os testes desse arquivo
unittest.main()
