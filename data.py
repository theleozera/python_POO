##VERSAO 1##
class Data: ##sempre com letra maiscula a classe
    def to_str(self): ##toda funcao dentro de uma classe recebe o parametro self primeiro, isso é obrigatorio
        return f'{self.dia}/{self.mes}/{self.ano}'
#objetos 
d1 = Data() #chamando a classe como funcão
d1.dia=5     #criando atributos
d1.mes=12    #criando atributos
d1.ano=2024  #criando atributos
print(d1.dia,'/', d1.mes,'/',d1.ano)
print(d1.to_str())

d2 = Data() #chamando a classe como funcão
d2.dia=4     #criando atributos
d2.mes=1    #criando atributos
d2.ano=2020  #criando atributos
print(d2.dia,'/', d2.mes,'/',d2.ano)
print(d2.to_str()) #aqui estou chamando o objeto e dizendo o nome da funcao que esta dentro da classe


##VERSAO 2##
class Data: ##sempre com letra maiscula a classe
    def __str__(self): #nesse caso aqui se eu usar __str__ eu nao preciso por a funcao junto ao objeto para chamalo
        return f'{self.dia}/{self.mes}/{self.ano}'
d3 = Data()
d3.dia= 1
d3.mes= 6
d3.ano = 2012
print(d3) #repare que aqui eu apenas botei o nome do objeto, nao usei o nome da funcao gracas ao __str__ usado la em cima


##VERSAO 3##
class Data:
    def __init__(self, dia, mes, ano): #criando um construtor
        self.dia=dia
        self.mes=mes
        self.ano=ano
    def __str__(self): 
        return f'{self.dia}/{self.mes}/{self.ano}'
d4=  Data(5,7,2023)
print(d4)


##VERSAO 4## com parametros nomeados
class Data:
    def __init__(self, dia=1, mes=1, ano=1970): #criando um construtor
        self.dia=dia
        self.mes=mes
        self.ano=ano
    def __str__(self): 
        return f'{self.dia}/{self.mes}/{self.ano}'
d5=  Data(ano =2000)# aqui se eu quiser eu posso nao mandar nenhum valor ja que os atributos tem um valor padrao, ou posso mandar só um se eu quiser por exemplo o ano = 2000
print(d5)