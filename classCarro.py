class Veiculo:
    def __init__(self, modelo, consumo, tanque=0):
        self.modelo = modelo
        self.consumo = consumo
        self.qtd_combustivel = tanque

    def __repr__(self):
        return (f'Modelo: {self.modelo}\n'
                f'Consumo: {self.consumo}Km/L\n')


    def abastecer(self, litro):
        if litro < 1 or self.qtd_combustivel == 100:
            print('Não é possível abastecer!!')
        else:
            print(f'Seu tanque possuia {self.qtd_combustivel}L de combustível\n'
                  f'Será adicionado {litro}L ao tanque!\n')
            self.qtd_combustivel = self.qtd_combustivel + litro
            print(f'Tanque: {self.qtd_combustivel}L')

    def obterGasolina(self):
        return f'Tanque: {self.qtd_combustivel}L'

    def andar(self, km):
        print(f'Andou {km}Km\n')
        self.qtd_combustivel = self.qtd_combustivel - (km/self.consumo)
        if self.qtd_combustivel < 1:
            print('Não é possível realizar esse calculo!')
        else:
            print(f'Quantidade consumida: {km/self.consumo:.2f}L')
            print(f'Combustível restante no tanque: {self.qtd_combustivel:.2f}L')


palio = Veiculo(str(input('Insira o modelo do veículo: ')), float(input(f'Insira o consumo: ')))
print(palio)
palio.abastecer(int(input('Insira a quantidade de combustível abastecido: ')))
palio.obterGasolina()
palio.andar(int(input("Insira quantos KM você viajou: ")))
