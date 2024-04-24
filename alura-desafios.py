class Musica:
    nome = ''
    artista = ''
    duracao = float

musica_gospel = Musica()
musica_gospel.nome = 'Quero Exaltar'
musica_gospel.artista = 'Lorena Oliveira'
musica_gospel.duracao = 3.35

musica_trap = Musica()
musica_trap.nome = 'Diz ai Qual é o Plano?'
musica_trap.artista = 'MC Ig'
musica_trap.duracao = 11.43

print(vars(musica_gospel), vars(musica_trap))