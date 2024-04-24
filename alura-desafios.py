def login():
    user = (input('Digite o seu usuário: '))
    senha = (input('Digite a sua senha: '))
    # condicionais
    user_do_app = user == 'GabrielOliveira22'
    senha_do_app = senha == 'SenhaTeste123'


    if (user_do_app and senha_do_app):
        print(f'Seja bem vindo, {user}!')
    elif (user_do_app and not senha_do_app):
        print('Senha errada!')
    elif (senha_do_app and not user_do_app):
        print('Usuário errado!')
    else:
        print('Senha ou usuário errado!')
login()