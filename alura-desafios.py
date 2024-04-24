numero = 10

def decrescente():
    global numero
    for numero in range(numero, 0, -1):
        print(f'{numero}')

decrescente()