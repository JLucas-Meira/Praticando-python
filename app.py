from modelos.restaurante import Restaurante

restaurante_Silva = Restaurante('Silva Food', 'Comidas Tipícas')
restaurante_Silva.alternar_estado()
restaurante_Silva.receber_avaliacao('Pablo', 4)
restaurante_Silva.receber_avaliacao('Natiele', 5)
restaurante_Silva.receber_avaliacao('Jose', 2)
restaurante_Silva.receber_avaliacao('Livia', 3)

restaurante_VilaPizza = Restaurante('Vila Pizza', 'Pizza')
restaurante_VilaPizza.alternar_estado()
restaurante_VilaPizza.receber_avaliacao('Alfredo', 3)
restaurante_VilaPizza.receber_avaliacao('Esther', 5)
restaurante_VilaPizza.receber_avaliacao('Carina', 3)

restaurante_ChurrascariaBiz = Restaurante('Churrascaria Biz', 'Churrascaria')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()