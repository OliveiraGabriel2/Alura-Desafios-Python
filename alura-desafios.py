class Pessoa():
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    @property
    def saudacao(self):
        if (self.profissao):
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}'
        else:
            return f'Olá, eu sou {self.nome}'
        
    def aniversario(self):
        self.idade += 1

tiago = Pessoa('Tiago', 25, 'Programador')

print("Informações Iniciais:")
print(tiago)
print()
tiago.aniversario()
print()
print(tiago.saudacao)



   

        
       
        

