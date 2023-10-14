class ContaCorrente:
    def __init__(self, num_conta, nome_correntista, nome, saldo=0):
        self.conta = num_conta
        self.correntista = nome_correntista
        self.saldo = saldo
        self.completo = nome

    def alterarNome(self, novo_nome):
        self.correntista = novo_nome
        return self.correntista

    def depositoSaque(self, funcao, valor):
        if funcao == 'Depositar' or funcao == 'depositar':
            if valor < 1:
                return 'Não será possível realizar o deposita!'
            else:
                print(f'Seu saldo disponível: R$ {self.saldo:.2f}\n'
                    f'Valor para depósito: R$ {valor:.2f}')
                self.saldo = self.saldo + valor
                print(f'Seu novo saldo: R$ {self.saldo:.2f}')

        elif funcao == 'Saque' or funcao == 'saque':
            if self.saldo < valor or valor < 1:
                return 'Não é possível realizar o saque!!'
            else:
                print(f'Valor para o saque: R$ {valor:.2f}')
                self.saldo = self.saldo - valor
                print(f'Seu novo saldo é: R$ {self.saldo:.2f}')


nu = ContaCorrente(1000, 'Thalles Ribeiro Nascimento', 'Thalles')
nu.depositoSaque('Depositar', 1500)
nu.depositoSaque("Saque", 100)
