import json
from components.restaurantes import Restaurantes


def exibir_nome_do_programa():
    ''' Exibe o nome do programa '''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def obter_restaurantes():
    with open("data/restaurants_db.json") as file:
        restaurants_data = json.load(file)

    restaurantes = Restaurantes(restaurants_data)

    return restaurantes

def escolher_restaurante(restaurantes):
    print("Digite o número do restaurante no qual deseja fazer o pedido.")
    
    for idx, restaurante in enumerate(restaurantes._lista_de_restaurantes):
        print(f"{idx + 1}" + f" - {restaurante._nome}" )

    restaurante_escolhido_index = int(input("Restaurante escolhido: "))
    restaurante_escolhido = restaurantes._lista_de_restaurantes[restaurante_escolhido_index - 1]

    return restaurante_escolhido, restaurante_escolhido_index

def escolher_pedido(restaurante_escolhido):
    print("\nDigite o número do item que deseja pedir.")
    restaurante_escolhido.exibir_cardapio

    pedido_escolhido = int(input("Pedido escolhido: "))
    return restaurante_escolhido._cardapio[pedido_escolhido - 1]

def calcular_preco(pedido_escolhido):
    tem_desconto = input("Você tem cupom de desconto? (S/N)")
    if tem_desconto == "S":
        pedido_escolhido.aplicar_desconto()

    print(f"O pedido ficou por {pedido_escolhido._preco:.2f}")

def avaliar_pedido(restaurantes, idx):
    deseja_avaliar = input("Deseja fazer uma avaliação? (S/N)")

    if deseja_avaliar == "S":
        nota_avaliacao = int(input("Nota (1 a 5):"))
        descricao_avaliacao = input("Comentário:")

        restaurantes._lista_de_restaurantes[idx]._avaliacoes.avaliacoes_individuais.append({
            "rating": nota_avaliacao,
            "description": descricao_avaliacao
        })

        restaurantes._lista_de_restaurantes[idx].calcular_media_avaliacoes

        # save json
        nova_avaliacao = {
            "average": restaurantes._lista_de_restaurantes[idx]._avaliacoes.media,
            "individual_ratings": restaurantes._lista_de_restaurantes[idx]._avaliacoes.avaliacoes_individuais,
        }

        with open("nova_avaliacao.json", "w", encoding="utf-8") as file:
            json.dump({f"{restaurantes._lista_de_restaurantes[idx]._nome}": nova_avaliacao}, file, ensure_ascii=False, indent=4)


        print("\nObrigado pela avaliação!")

    

def iniciar_interface_de_pedidos(restaurantes):
    restaurante_escolhido, idx = escolher_restaurante(restaurantes)

    pedido_escolhido = escolher_pedido(restaurante_escolhido)

    calcular_preco(pedido_escolhido)

    avaliar_pedido(restaurantes, idx)

    print("\nPedido finalizado.")

# mandalla = Restaurante('Mandalla Foods', 'Fast Food')
# bebida = Bebida('Suco de Melancia', 5.0, 'Grande')
# prato = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
# mandalla.adicionar_no_cardapio(bebida)
# mandalla.adicionar_no_cardapio(prato)
# bebida.aplicar_desconto()
# prato.aplicar_desconto()

def main():
    exibir_nome_do_programa()
    restaurantes = obter_restaurantes()

    interface_de_pedidos = iniciar_interface_de_pedidos(restaurantes)


if __name__ == '__main__':
    main()