class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        nova = self.velocidade_atual + delta if self.velocidade_atual + delta <= self.velocidade_maxima else self.velocidade_maxima
        self.velocidade_atual = nova
        return nova

    def frear(self, delta=5):
        nova = self.velocidade_atual - delta if self.velocidade_atual - delta >= 0 else 0
        self.velocidade_atual = nova
        return nova
    
carro1= Carro(180)

for _ in range(25):
    print(carro1.acelerar(8))
    
for _ in range(10):
    print(carro1.frear(20))   
       

