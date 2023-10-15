class BombaCombustivel:
    def __init__(self, tipo, valor, quantidade):
        self.tipoCombustivel = tipo
        self.valorLitro = valor
        self.qtd_Combustivel = quantidade

    def abastecerValor(self, price):
        if price >= self.valorLitro:
            print(f'A quantidade de litros colocada pagando R$ {price:.2f} foi de {price/self.valorLitro:.2f}L')
            self.qtd_Combustivel = self.qtd_Combustivel - (price / self.valorLitro)
            print(f'Quantidade de litros restante na bomba: {self.qtd_Combustivel:.2f}L')
        else:
            print('Não é possível abastecer!!')

    def abastecerLitro(self, litro):
        if litro <= self.qtd_Combustivel:
            print(f'{litro}L de gasolina deu R$ {litro * self.valorLitro:.2f}')
            self.qtd_Combustivel = self.qtd_Combustivel - litro
            print(f'Quantidade de litros restante na bomba: {self.qtd_Combustivel:.2f}L')
        else:
            print('Não é possível abastecer!!')

    def alteraValor(self, novo_valor):
        self.valorLitro = novo_valor
        return self.valorLitro

    def alteraCombustivel(self, novo_tipo):
        self.tipoCombustivel = novo_tipo
        return self.tipoCombustivel

    def alteraQuantidade(self, nova_qtd):
        self.qtd_Combustivel = nova_qtd
        print(f'Quantidade de litros: {self.qtd_Combustivel}')
        return self.qtd_Combustivel


shell = BombaCombustivel('Gasolina Comum', 5.75, 100)
shell.abastecerValor(50)
shell.abastecerLitro(50)
ipiranga = BombaCombustivel('Etanol', 4.75, 100)
ipiranga.abastecerLitro(10)
ipiranga.alteraValor(5)
ipiranga.abastecerLitro(10)
ipiranga.alteraQuantidade(100)
ipiranga.alteraValor(5)
ipiranga.abastecerLitro(10)
