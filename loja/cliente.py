from .pessoa import Pessoa # importando do modulo pessoa a classe Pessoa, o ponto ali significa que estao na mesma pasta

def get_data(compra):
    return compra.data
    

class Cliente(Pessoa): # aqui cliente é uma classe que esta herdando da classe Pessoa, ou seja Pessoa é a super classe
    def __init__(self, nome, idade): #construtor
         super().__init__(nome, idade) #chamando construtor da classe pai (Pessoa)
         self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra) #passando compras para lista de compras ja que compra é uma lista

    def get_data_da_ultima_compra(self):
        return None if not self.compras else \
        sorted(self.compras, key=get_data)[-1].data #pega a data da compra, get_data e uma funcao feita la em cima que pega a compra e retorna a data dela e -1 é o ultimo item de compra da lista

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total = total + compra.valor
        return total