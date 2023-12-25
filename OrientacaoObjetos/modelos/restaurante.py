from modelos.avaliacao import Avaliacao

class Restaurante:
    """ Representa um restaurante e suas características. """
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        """
        Inicializa uma instância da classe Restaurante.

        Entrada:
        - nome (str): Nome do restaurante criado
        - categoria (str): Categoria do restaurante criado
        """
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """ Retorna uma representação textual da instância """
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """ Lista restaurantes cadastrados """
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |' 
                  + f' {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        """ Retorna um símbolo verda de verificação se restaurante ativo e um x vermelho se não """
        return '✅' if self._ativo else '❌'
    
    @property
    def media_avaliacoes(self):
        """ Calcula e retorna a média de avaliações de um restaurante"""
        if not self._avaliacoes:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_avaliacoes = len(self._avaliacoes)
        media = round(soma_das_notas/quantidade_de_avaliacoes, 1)

        return media
    
    def alternar_estado(self):
        """ Altera estado de um restaurando de ativo para desativado ou vice-versa """
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        """ 
        Recebe avaliação de um restaurante por um cliente
        
        Entrada:
        - cliente (str): cliente que está realizando a avaliação
        - nota (float): nota atribuída ao restaurante na avaliação
        """
        if nota < 0 or nota > 5:
            print(f'Avaliação inválida do cliente {cliente} inválida')
        else:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
    
    