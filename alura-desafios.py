def eixo():
    x = float((input('Digite a coordenada x: ')))
    y = float((input('Digite a coordenada y: ')))
    # condicionais
    primeiro_quadrante = x > 0 and y > 0
    segundo_quadrante = x < 0 and y > 0
    terceiro_quadrante = x < 0 and y < 0
    quarto_quadrante = x > 0 and y < 0

    if (primeiro_quadrante):
        print(f'O ponto está no primeiro quadrante.')
    elif (segundo_quadrante):
        print('O ponto está no segundo quadrante.')
    elif (terceiro_quadrante):
        print('O ponto está no terceiro quadrante.')
    elif (quarto_quadrante):
        print('O ponto está no quarto quadrante.')
    else:
        print('O ponto está sobre um eixo ou na origem.')
eixo()