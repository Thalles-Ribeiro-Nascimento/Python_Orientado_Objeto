class ContaInvestimentos:
    def __init__(self, num_conta, nome_correntista, taxa_juros=0, saldo=0):
        self.conta = num_conta
        self.correntista = nome_correntista
        self.saldo = saldo
        self.juros = taxa_juros

    def __repr__(self):
        return (f'Saldo: R$ {self.saldo:.2f}\n'
                f'Nome: {self.correntista}\n')

    def depositoSaque(self, funcao, valor):
        if funcao == 'Depositar' or funcao == 'depositar':
            if valor < 1:
                return 'Não será possível realizar o deposita!'
            else:
                print(f'Seu saldo disponível: R$ {self.saldo:.2f}\n'
                    f'Valor para depósito: R$ {valor:.2f}\n')
                self.saldo = self.saldo + valor
                print(f'Seu novo saldo: R$ {self.saldo:.2f}')

        elif funcao == 'Saque' or funcao == 'saque':
            if self.saldo < valor or valor < 1:
                return 'Não é possível realizar o saque!!'
            else:
                print(f'Valor para o saque: R$ {valor:.2f}')
                self.saldo = self.saldo - valor
                print(f'Seu novo saldo é: R$ {self.saldo:.2f}')

    def adcJuros(self):
        self.saldo = self.saldo + (self.saldo * 10 / 100)
        print(f'Seus ganhos: R$ {self.saldo:.2f}')

