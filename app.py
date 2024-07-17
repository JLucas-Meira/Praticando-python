from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_VilaPizza = Restaurante('Vila Pizza', 'Pizza')
bebida_suco = Bebida('Suco de Abacaxi', 5.0, 'Grande')
Pizza = Prato('Pizza', 10.0, 'A melhor pizza da cidade')
restaurante_VilaPizza.adicionar_no_cardapio(bebida_suco)
restaurante_VilaPizza.adiconar_no_cardapio(Pizza)

def main():
    print(bebida_suco)
    print(Pizza)

if __name__ == '__main__':
    main()