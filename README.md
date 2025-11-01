# ☕ Sabor Express - Testes Unitários

Este repositório contém o projeto "Sabor Express" com a implementação de testes unitários básicos, conforme solicitado para a atividade.

## 👥 Dupla Responsável

* **Daniel Rodrigues**
* **Thais Daniela**

## ✅ Implementação dos Testes Unitários

A implementação dos testes foi realizada utilizando o framework **Pytest**. O foco foi garantir a funcionalidade essencial de seleção de itens e o comportamento da classe `Sobremesa`.

### Arquivos de Teste Implementados

Os testes unitários foram organizados nos seguintes arquivos:

| Arquivo de Teste | Classe Principal Testada | Funcionalidades Cobertas |
| :--- | :--- | :--- |
| **`tests/test_sabor_express.py`** | `SaborExpress` | Seleção de restaurante e pedido, e o fluxo de cálculo de preço (com/sem desconto). |
| **`tests/test_restaurantes.py`** | `Restaurantes` | Inicialização correta da lista de objetos `Restaurante` a partir dos dados de *mock*. |
| **`tests/test_restaurante.py`** | `Restaurante` | Inicialização da classe, propriedades de estado (`ativo`) e lógica de avaliações. |
| **`tests/test_sobremesa.py`** | `Sobremesa` | Aplicação correta da regra de desconto na sobremesa. |
| **`tests/fixtures.py`** | *Fixtures* | Criação de dados de *mock* e instâncias de classes para isolar os testes. |

---

### 🚀 Como Executar os Testes

Para executar a bateria de testes, certifique-se de estar com o ambiente virtual ativado e com o pacote `pytest` instalado.

1.  Acesse o diretório raiz do projeto.
2.  Execute o comando no terminal:
    ```bash
    pytest -v
    ```