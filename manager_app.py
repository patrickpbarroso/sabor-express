import os

restaurantes = [{'nome':'Mandalla Foods', 'categoria':'Fast Food', 'ativo':False},
                {'nome':'Tijucana', 'categoria':'Comida mineira', 'ativo':True},
                {'nome':'Pizza Chic', 'categoria':'Comida italiana', 'ativo':False}]

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

def exibir_opcoes():
    ''' Mostra opções de ações do programa '''
    print('1. Cadastrar restaurante'
        + '\n2. Listar restaurantes'
        + '\n3. Alternar estado de restaurante'
        + '\n4. Sair')

def finalizar_app():
    ''' Encerra o programa '''
    exibir_subtitulo('...encerrando app')

def opcao_invalida():
    ''' Mostra que a opção digitada foi inválida '''
    print('Opção inválida.\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    ''' Redireciona ao menu principal '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(subtitulo):
    ''' Exibe o subtítulo seção do problema '''
    # os.system('clear')
    linha = '*' * len(subtitulo)
    print(linha + '\n' + subtitulo + '\n' + linha)
    print()

def cadastrar_novo_restaurante():
    ''' Cadastra novo restaurante no sistema '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')

    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes cadastrados no sistema '''
    exibir_subtitulo('Lista de restaurantes')

    print(f'{"Nome do restaurante".ljust(23)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o estado de um restaurante no sistema, que pode ser ativado ou desativado '''
    exibir_subtitulo('Alternar estado de restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] 
                        else f'O restaurante {nome_do_restaurante} foi desativado com sucesso')
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante não foi encontrado.')

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Lida com a opção selecionada e retorna a ação correspondente '''
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Método principal do sistema, onde a execução é iniciada '''
    # os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()