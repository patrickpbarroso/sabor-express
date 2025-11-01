# Arquivo: tests/fixtures.py

from components.cardapio.sobremesa import Sobremesa
from components.restaurantes import Restaurantes
from components.sabor_express import SaborExpress
from components.restaurante import Restaurante
from components.avaliacao_restaurante import AvaliacaoRestaurante
# O import de Prato era necessário para as novas fixtures de Restaurante
from components.cardapio.prato import Prato 

import pytest

# --- FIXTURES ORIGINAIS DO USUÁRIO ---
@pytest.fixture
def sabor_express_object_fixture():
    sabor_express_mock = SaborExpress()
    sabor_express_mock._restaurantes = Restaurantes({
            "restaurants": [
                {
                    "name": "restaurante 1",
                    "category": "tradicional",
                    "menu": [
                        {
                            "Item": "Item 1",
                            "Price": 5,
                            "Description": "An item 1"
                        },
                        {
                            "Item": "Item 2",
                            "Price": 10,
                            "Description": "An item 2"
                        },
                        {
                            "Item": "Item 1",
                            "Price": 6,
                            "Description": "An item 3"
                        }
                    ],
                    "ratings": {
                        "average": 3,
                        "individual_ratings": [
                            {
                                "rating": 3,
                                "description": "Don't like it that much"
                            }
                        ]
                    }
                },
                {
                    "name": "restaurante 2",
                    "category": "tradicional",
                    "menu": [
                        {
                            "Item": "Item 1",
                            "Price": 5,
                            "Description": "An item 1"
                        },
                        {
                            "Item": "Item 2",
                            "Price": 10,
                            "Description": "An item 2"
                        },
                        {
                            "Item": "Item 1",
                            "Price": 6,
                            "Description": "An item 3"
                        }
                    ],
                    "ratings": {
                        "average": 3,
                        "individual_ratings": [
                            {
                                "rating": 3,
                                "description": "Don't like it that much"
                            }
                        ]
                    }
                }
            ]
        })
    
    return sabor_express_mock

@pytest.fixture
def sobremesa_fixture():
    return Sobremesa(
        nome="Sorvete",
        preco=100,
        tipo="Gelados",
        tamanho="500ml"
    )

# --- NOVAS FIXTURES ADICIONADAS PARA OS TESTES DE RESTAURANTE E RESTAURANTES ---

@pytest.fixture
def restaurante_mock_data():
    """ Dados de mock para inicializar uma instância de Restaurante. """
    return {
        "nome": "restaurante teste",
        "categoria": "chinesa",
        "cardapio": [
            {
                "Item": "Prato Teste",
                "Price": 50.00,
                "Description": "Um delicioso prato para teste"
            }
        ],
        "avaliacoes": {
            "average": 4.0,
            "individual_ratings": [
                {"rating": 5, "description": "Excelente!"},
                {"rating": 3, "description": "Razoável."}
            ]
        }
    }

@pytest.fixture
def restaurante_fixture(restaurante_mock_data):
    """ Retorna uma instância de Restaurante para testes. """
    return Restaurante(
        nome=restaurante_mock_data["nome"],
        categoria=restaurante_mock_data["categoria"],
        cardapio=restaurante_mock_data["cardapio"],
        avaliacoes=restaurante_mock_data["avaliacoes"]
    )

@pytest.fixture
def prato_fixture():
    """ Retorna uma instância de Prato para testes. """
    # Nota: Assumindo que a classe Prato existe e tem estes atributos
    return Prato(
        nome="Prato de Teste",
        preco=25.00,
        descricao="Descricao do Prato de Teste"
    )

@pytest.fixture
def restaurantes_data_mock():
    """ Dados de mock para inicializar uma instância de Restaurantes. """
    return {
        "restaurants": [
            {
                "name": "Restaurante A",
                "category": "Italiana",
                "menu": [],
                "ratings": {"average": 0, "individual_ratings": []}
            },
            {
                "name": "Restaurante B",
                "category": "Japonesa",
                "menu": [],
                "ratings": {"average": 0, "individual_ratings": []}
            }
        ]
    }