# Arquivo: tests/test_restaurantes.py

from components.restaurantes import Restaurantes
from components.restaurante import Restaurante
from tests.fixtures import restaurantes_data_mock
import pytest

def teste_inicializacao_restaurantes_lista_correta(restaurantes_data_mock):
    restaurantes_obj = Restaurantes(restaurantes_data_mock)
    
    # Verifica se a lista foi criada
    assert isinstance(restaurantes_obj._lista_de_restaurantes, list)
    
    # Verifica o número de restaurantes
    assert len(restaurantes_obj._lista_de_restaurantes) == 2
    
    # Verifica o tipo dos itens na lista
    assert isinstance(restaurantes_obj._lista_de_restaurantes[0], Restaurante)
    
    # Verifica se o nome foi processado corretamente (capitalizado)
    assert restaurantes_obj._lista_de_restaurantes[0]._nome == "Restaurante A"