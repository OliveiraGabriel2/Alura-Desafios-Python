class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

verificacao = 'Está ativo' if restaurante_praca.ativo == True else 'Está inativo'
print(verificacao)

