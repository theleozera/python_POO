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

##VERSAO 3## adicionando vencimento
from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas pendentes)'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('concluida')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('vencida')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'vence em {dias} dias')
        return f'{self.descricao} - {" ".join(status)}'


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas', datetime.now() + timedelta(days=3, minutes=12))
    mercado.add('Carne')
    mercado.add('Limpezas')
    print(mercado)
    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')


if __name__ == "__main__":
    main()

#VERSAO 4 USANDO HERANÇA

from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas pendentes)'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('concluida')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('vencida')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'vence em {dias} dias')
        return f'{self.descricao} - {" ".join(status)}'

class TarefaRecorrente(Tarefa):
    def __init__ (self, descricao, vencimento, dias = 7):
        super().__init__(descricao, vencimento)
        self.dias=dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
    
def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))
    casa.tarefas.append(TarefaRecorrente('troca lencois', datetime.now(), 7))
    casa.tarefas.append(casa.procurar('troca lencois').concluir())
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas', datetime.now() + timedelta(days=3, minutes=12))
    mercado.add('Carne')
    mercado.add('Limpezas')
    print(mercado)
    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')


if __name__ == "__main__":
    main()


    
 #versao 5 -----------------------------------------------------------------------------------------------#usando metodoss privados
from datetime import datetime, timedelta
class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def _add_tarefa(self, tarefa, **kwargs): #o underline significa que o metodo é privado no python
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento',None))) 

    def __iter__(self):
        return self.tarefas.__iter__()
        
    def add(self,tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)
        
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas pendentes)'

class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('concluida')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('vencida')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'vence em {dias} dias')
        return f'{self.descricao} - {" ".join(status)}'

class TarefaRecorrente(Tarefa):
    def __init__ (self, descricao, vencimento, dias = 7):
        super().__init__(descricao, vencimento)
        self.dias=dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
    
def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))
    casa.tarefas.append(TarefaRecorrente('troca lencois', datetime.now(), 7))
    casa.tarefas.append(casa.procurar('troca lencois').concluir())
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas', datetime.now() + timedelta(days=3, minutes=12))
    mercado.add('Carne')
    mercado.add('Limpezas')
    print(mercado)
    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')

if __name__ == "__main__":
    main()
#  ------versao 6------------------------

# sobrecarga de operadores

from datetime import datetime, timedelta
class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def _add_tarefa(self, tarefa, **kwargs): #o underline significa que o metodo é privado no python
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento',None))) 

    def __iter__(self):
        return self.tarefas.__iter__()
    
    #sobrecarga de operador +=
    #projeto += tarefa
    def __iadd__(self, tarefa):
        tarefa.dono=self
        self._add_tarefa(tarefa)
        return self
        
    def add(self,tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)
        
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas pendentes)'

class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('concluida')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('vencida')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'vence em {dias} dias')
        return f'{self.descricao} - {" ".join(status)}'

class TarefaRecorrente(Tarefa):
    def __init__ (self, descricao, vencimento, dias = 7):
        super().__init__(descricao, vencimento)
        self.dias=dias
        self.donodono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa
    
def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))
    casa += TarefaRecorrente('troca lencois', datetime.now(), 7)
    casa.procurar('troca lencois').concluir()
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas', datetime.now() + timedelta(days=3, minutes=12))
    mercado.add('Carne')
    mercado.add('Limpezas')
    print(mercado)
    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')

if __name__ == "__main__":
    main()

# ----------------------versao 7-----------------------
#tratamento de exceções


from datetime import datetime, timedelta

class TarefaNaoEncontrada(Exception):  # Define uma exceção para quando uma tarefa não é encontrada
    pass

class Projeto:
    def __init__(self, nome):  # Inicializa um projeto com um nome
        self.nome = nome
        self.tarefas = []  # Inicializa a lista de tarefas do projeto como vazia

    def _add_tarefa(self, tarefa, **kwargs):  # Método privado para adicionar uma tarefa existente ao projeto
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):  # Método privado para adicionar uma nova tarefa ao projeto
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None))) 

    def __iter__(self):  # Permite iterar sobre as tarefas do projeto
        return self.tarefas.__iter__()

    # Sobrecarga do operador +=
    # projeto += tarefa
    def __iadd__(self, tarefa):  # Sobrecarga do operador += para adicionar uma tarefa diretamente ao projeto
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self
        
    def add(self, tarefa, vencimento=None, **kwargs):  # Adiciona uma nova tarefa ao projeto
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)
        
    def pendentes(self):  # Retorna uma lista de tarefas pendentes dentro do projeto
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):  # Procura por uma tarefa específica dentro do projeto
        try:
            return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))

    def __str__(self):  # Retorna uma representação em string do projeto
        return f'{self.nome} ({len(self.pendentes())} tarefas pendentes)'

class Tarefa:
    def __init__(self, descricao, vencimento=None):  # Inicializa uma tarefa com uma descrição e uma data de vencimento opcional
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()  # Registra o momento de criação da tarefa
        self.vencimento = vencimento  # Define a data de vencimento da tarefa

    def concluir(self):  # Marca a tarefa como concluída
        self.feito = True

    def __str__(self):  # Retorna uma representação em string da tarefa
        status = []
        if self.feito:
            status.append('concluída')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('vencida')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'vence em {dias} dias')
        return f'{self.descricao} - {" ".join(status)}'

class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):  # Inicializa uma tarefa recorrente com uma descrição, data de vencimento e intervalo de dias
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):  # Marca a tarefa recorrente como concluída e cria uma nova tarefa recorrente
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa

def main():
    casa = Projeto('Tarefas de casa')  # Cria um novo projeto para tarefas de casa
    casa.add('Passar roupa', datetime.now())  # Adiciona uma tarefa ao projeto de casa
    casa.add('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))  # Adiciona outra tarefa ao projeto de casa
    casa += TarefaRecorrente('troca lencois', datetime.now(), 7)  # Adiciona uma tarefa recorrente ao projeto de casa
    casa.procurar('troca lencois').concluir()  # Conclui a tarefa recorrente encontrada no projeto de casa
    print(casa)  # Imprime o projeto de casa

    try:
        casa.procurar('lavar prato - ERRO').concluir()  # Procura e tenta concluir uma tarefa inexistente no projeto de casa
    except TarefaNaoEncontrada as e:
        print(f'A causa do erro foi: {str(e)}')  # Captura e imprime a exceção de tarefa não encontrada
    
    casa.procurar('Lavar prato').concluir()  # Conclui a tarefa de lavar prato no projeto de casa
    for tarefa in casa.tarefas:  # Itera sobre as tarefas do projeto de casa
        print(f'- {tarefa}')  # Imprime cada tarefa do projeto de casa
    print(casa)  # Imprime novamente o projeto de casa

    mercado = Projeto('Compras no mercado')  # Cria um novo projeto para compras no mercado
    mercado.add('Frutas secas', datetime.now() + timedelta(days=3, minutes=12))  # Adiciona uma tarefa ao projeto de mercado
    mercado.add('Carne')  # Adiciona outra tarefa ao projeto de mercado
    mercado.add('Limpezas')  # Adiciona outra tarefa ao projeto de mercado
    print(mercado)  # Imprime o projeto de mercado
    comprar_carne = mercado.procurar('Carne')  # Procura a tarefa de comprar carne no projeto de mercado
    comprar_carne.concluir()  # Conclui a tarefa de comprar carne no projeto de mercado
    for tarefa in mercado.tarefas:  # Itera sobre as tarefas do projeto de mercado
        print(f'- {tarefa}')  # Imprime cada tarefa do projeto de mercado

if __name__ == "__main__":
    main()  # Chama a função principal quando o script é executado diretamente  
