class ContaBancaria():
    def __init__(self, titular='', saldo=0.0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        print(f'{'Nome do Titular'.ljust(25)} | {'Saldo da conta'.ljust(25)} | {'Status'}')
        return f'{self._titular.ljust(25)} | {str(self._saldo).ljust(25)} | {self.ativar_conta}'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativar_conta(self):
        return 'Ativo' if self._ativo else 'Desativado'

    
tiago_conta_bancaria = ContaBancaria('Tiago', 720.0)
ana_conta_bancaria = ContaBancaria('Tiago', 820.0)

print(tiago_conta_bancaria)




   

        
       
        

