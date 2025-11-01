# Arquivo: tests/test_sabor_express.py

from components.sabor_express import SaborExpress
from components.restaurantes import Restaurantes
from tests.fixtures import sabor_express_object_fixture, restaurantes_data_mock
import pytest
from unittest.mock import patch, MagicMock

# ... (Seu código existente de teste_escolher_restaurante e teste_escolher_pedido) ...

# Teste para SaborExpress.obter_restaurantes (requer mock de arquivo)
@patch('builtins.open')
@patch('json.load')
def teste_obter_restaurantes_carrega_dados_mock(mock_json_load, mock_open, restaurantes_data_mock):
    # Configura o mock do json.load para retornar nossos dados de mock
    mock_json_load.return_value = restaurantes_data_mock
    
    sabor_express = SaborExpress()
    sabor_express.obter_restaurantes()
    
    # Verifica se o método open foi chamado com o caminho correto
    mock_open.assert_called_with("data/restaurants_db.json")
    
    # Verifica se o _restaurantes foi inicializado corretamente
    assert isinstance(sabor_express._restaurantes, Restaurantes)
    assert len(sabor_express._restaurantes._lista_de_restaurantes) == 2

# Teste para SaborExpress.calcular_preco com e sem desconto
@patch('builtins.print') # Mock para capturar a saída do print
def teste_calcular_preco_com_desconto(mock_print):
    sabor_express = SaborExpress()
    
    # Cria um mock para o pedido_escolhido
    pedido_mock = MagicMock()
    pedido_mock._preco = 100.00
    
    sabor_express.calcular_preco(pedido_mock, "S")
    
    # Verifica se aplicar_desconto foi chamado
    pedido_mock.aplicar_desconto.assert_called_once()
    
    # Verifica se o preço foi impresso (usando o mock_print)
    # Assumindo que o desconto alterou o preço para, digamos, 85.00
    # O teste abaixo verifica a formatação. Se o mock não alterar o preço,
    # ele imprimirá 100.00
    mock_print.assert_called_with(f"O pedido ficou por {pedido_mock._preco:.2f}")

@patch('builtins.print') # Mock para capturar a saída do print
def teste_calcular_preco_sem_desconto(mock_print):
    sabor_express = SaborExpress()
    
    # Cria um mock para o pedido_escolhido
    pedido_mock = MagicMock()
    pedido_mock._preco = 100.00
    
    sabor_express.calcular_preco(pedido_mock, "N")
    
    # Verifica se aplicar_desconto NÃO foi chamado
    pedido_mock.aplicar_desconto.assert_not_called()
    
    # Verifica se o preço foi impresso
    mock_print.assert_called_with(f"O pedido ficou por {pedido_mock._preco:.2f}")