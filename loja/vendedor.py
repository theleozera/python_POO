from .pessoa import Pessoa # importando do modulo pessoa a classe Pessoa, o ponto ali significa que estao na mesma pasta

class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario