def idade():
    solicite = int(input('Digite a sua idade: '))
    # condicionais
    crianca = solicite <= 12
    adolescente = 13 <= solicite <= 18
    adulto = 18 <= solicite <= 59

    if (crianca):
        print('Você é uma criança')
    elif (adolescente):
        print('Você é um(a) adolescente')
    elif (adulto):
        print('Você é um adulto')
    else:
        print('Você é um(a) idoso(a)')
idade()