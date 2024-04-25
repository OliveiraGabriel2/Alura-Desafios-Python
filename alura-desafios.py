class Restaurante():
    def __init__(self, nome, categoria, prato_principal, valor_entrada):
        self.nome = nome
        self.categoria = categoria
        self.prato_principal = prato_principal
        self.valor_entrada = valor_entrada

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Prato-principal: {self.prato_principal} | Valor da entrada: R${self.valor_entrada} reais'

restaurante_gourmet = Restaurante('Vitrini', 'Gourmet', 'Risoto de cogumelos selvagens com trufas', int('30'))
print(restaurante_gourmet) 

