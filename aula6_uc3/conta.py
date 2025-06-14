class ContaCorrente:

    def __init__ (self, nome_cliente, num_conta, senha, saldo = 0.0):
        self.nome_cliente = nome_cliente
        self.num_conta = num_conta
        # self.agencia = agencia
        self.saldo = saldo
        self.senha = senha
        # self.cheque_especial = cheque_especial
        # self.cartao_credito = cartao_credito
        # self.financiamento = financiamento

    def mostrar_saldo(self):

        print(f'o saldo de {self.nome_cliente} dispomível é {self.saldo}')

    
    def sacar(self, valor):

        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print (f' saque realizado. \nNovo saldo: {self.saldo}')
        else:
            print ('saldo insuficiente')


    def depositar(self, valor):

        if valor > 0:
            self.saldo += valor
            print (f'depósito  realizado com successo. \nNovo saldo: {self.saldo}')
        else:
            print ('incapaz de depositar valores negatvos. ')


    def transferir(self, valor, destinatario): 

        if self.num_conta != destinatario.num_conta:
            ContaCorrente.sacar(self, valor)
            ContaCorrente.depositar(destinatario, valor)
        else:
            print('Mão pode ser feita a transferencia.')