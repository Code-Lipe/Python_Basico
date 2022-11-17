import unittest
from ex2_survey import AnonymousSurvey

# Escreveremos um teste para verificar se uma resposta única à pergunta está armazenada de forma apropriada
# assertIn() será usado para conferir se a resposata está na lista de respostas depois que ela for armazenada
# Qualquer objeto criado no método setUp() estará disponível a todos os métodos de teste que você escrever

class TestAnonymousSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey"""

    def setUp(self):
        """Cria uma pesquisa e um conjunto de respostas que poderão ser usados em todos os métodos de teste"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Português']


    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)


    def test_store_three_responses(self):
        """Testa se três respostas individuais são armazenadas de forma apropriada."""

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
