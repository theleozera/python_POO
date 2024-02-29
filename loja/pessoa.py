
class Pessoa:

    def __init__(self,nome, idade): #construtor
        self.nome=nome
        self.idade = idade

    def __str__(self) :
       if not self.idade: # se nao mandar idade vai só o nome
           return self.nome
       return f'{self.nome}({self.idade}) anos' # senao retorna os dois mesmo

    def is_adult(self): # vendo se é maior de idade
        return(self.idade or 0)>18
       
        
        
