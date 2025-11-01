# Arquivo: tests/test_restaurante.py

from components.restaurante import Restaurante
from components.avaliacao_restaurante import AvaliacaoRestaurante
from components.cardapio.prato import Prato # Importar Prato para testar 'adicionar_no_cardapio'
from tests.fixtures import restaurante_fixture, prato_fixture, restaurante_mock_data
import pytest

def teste_inicializacao_restaurante(restaurante_fixture, restaurante_mock_data):
    restaurante = restaurante_fixture
    
    # Verifica inicialização de atributos básicos
    assert restaurante._nome == "Restaurante Teste" # Verifica capitalização
    assert restaurante._categoria == "CHINESA" # Verifica uppercase
    assert not restaurante._ativo
    
    # Verifica inicialização do cardápio (assume que processar_cardapio funciona)
    assert len(restaurante._cardapio) == 1
    
    # Verifica inicialização das avaliações
    assert isinstance(restaurante._avaliacoes, AvaliacaoRestaurante)
    assert restaurante._avaliacoes.media == 4.0

def teste_ativo_propriedade_inativo(restaurante_fixture):
    restaurante = restaurante_fixture
    restaurante._ativo = False
    assert restaurante.ativo == '❌'

def teste_ativo_propriedade_ativo(restaurante_fixture):
    restaurante = restaurante_fixture
    restaurante._ativo = True
    assert restaurante.ativo == '✅'

def teste_calcular_media_avaliacoes_sucesso(restaurante_fixture):
    restaurante = restaurante_fixture
    # Média esperada: (5 + 3) / 2 = 4.0
    restaurante.calcular_media_avaliacoes()
    assert restaurante._avaliacoes.media == 4.0

def teste_alternar_estado_para_ativo(restaurante_fixture):
    restaurante = restaurante_fixture
    restaurante._ativo = False
    restaurante.alternar_estado()
    assert restaurante._ativo == True

def teste_alternar_estado_para_inativo(restaurante_fixture):
    restaurante = restaurante_fixture
    restaurante._ativo = True
    restaurante.alternar_estado()
    assert restaurante._ativo == False

def teste_adicionar_prato_no_cardapio(restaurante_fixture, prato_fixture):
    restaurante = restaurante_fixture
    cardapio_tamanho_inicial = len(restaurante._cardapio)
    
    restaurante.adicionar_no_cardapio(prato_fixture)
    
    assert len(restaurante._cardapio) == cardapio_tamanho_inicial + 1
    assert restaurante._cardapio[-1] == prato_fixture