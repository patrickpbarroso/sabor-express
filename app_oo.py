from modelos.restaurante import Restaurante

mandalla = Restaurante('Mandalla Foods', 'Fast Food')

mandalla.alternar_estado()

mandalla.receber_avaliacao('André', 10)
mandalla.receber_avaliacao('Patrick', 8)
mandalla.receber_avaliacao('Mary', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()