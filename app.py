from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_VilaPizza = Restaurante('Vila Pizza', 'Pizza')
bebida_suco = Bebida('Suco de Abacaxi', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_pizza = Prato('Pizza', 10.0, 'A melhor pizza da cidade')
prato_pizza.aplicar_desconto()
restaurante_VilaPizza.adicionar_no_cardapio(bebida_suco)
restaurante_VilaPizza.adicionar_no_cardapio(prato_pizza)

def main():
    restaurante_VilaPizza.exibir_cardapio

if __name__ == '__main__':
    main()