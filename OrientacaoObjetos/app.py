from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

mandalla = Restaurante('Mandalla Foods', 'Fast Food')
bebida = Bebida('Suco de Melancia', 5.0, 'Grande')
prato = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
mandalla.adicionar_no_cardapio(bebida)
mandalla.adicionar_no_cardapio(prato)
bebida.aplicar_desconto()
prato.aplicar_desconto()

def main():
    mandalla.exibir_cardapio

if __name__ == '__main__':
    main()