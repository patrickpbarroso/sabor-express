from modelos.restaurante import Restaurante

mandalla = Restaurante('Mandalla Foods', 'Fast Food')

mandalla.alternar_estado()

mandalla.receber_avaliacao('André', 5)
mandalla.receber_avaliacao('Patrick', 3)
mandalla.receber_avaliacao('Mary', 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()