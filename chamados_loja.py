from datetime import datetime
from loja.cliente import Cliente
from loja.vendedor import Vendedor
from loja import Compra



def main():
    cliente = Cliente('maria', 44)
    vendedor = Vendedor('pedro', 36, 5000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra(cliente, datetime(2018,6,4),600)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    print(f'cliente: {cliente}, adulto ' if cliente.is_adult() else '')
    print(f'vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    quantidade_compras = len(cliente.compras)
    print(f'total {valor_total} em {quantidade_compras} compras')
    print(f'ultima compra {cliente.get_data_da_ultima_compra()} ')


main()
  