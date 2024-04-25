class Carro():
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

carro_ferrari = Carro('Ferrari', 'Vermelha', '2024')
print(carro_ferrari)

