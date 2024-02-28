##VERSAO 1##
from datetime import datetime

class Tarefa:
    def __init__(self, descricao):
        self.descricao= descricao
        self.feito= False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' concluida' if self.feito else ' nao foi concluida')

def main():
    casa=[]
    casa.append(Tarefa('passar roupa'))
    casa.append(Tarefa('lavar prato'))
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'lavar prato']
    for tarefa in casa:
        print(tarefa)

main()

##VERSAO 2##
from datetime import datetime

class projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome}({len(self.pendentes())}) tarefas pendentes'
        
class Tarefa:
    def __init__(self, descricao):
        self.descricao= descricao
        self.feito= False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' concluida' if self.feito else ' ')

def main():
    casa=projeto('tarefas de casa')
    casa.add('passar roupa')
    casa.add('lavar prato')
    print(casa)

    casa.procurar('lavar prato').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')
    print(casa)

    mercado = projeto('compras no mercado')
    mercado.add('frutas secas')
    mercado.add('carne')
    mercado.add('limpezas')
    print(mercado)
    comprar_carne = mercado.procurar('carne')
    comprar_carne.concluir()
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')

main()
