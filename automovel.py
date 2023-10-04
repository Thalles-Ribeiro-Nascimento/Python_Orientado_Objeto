class Automovel:

    def __init__(self, placa = None):
        print('Executando o construtor...')
        self.set_placa(placa)


    def get_placa(self):
        return self.__placa

    def set_placa(self, placa):
        if len(placa) < 5:
            print('A placa não tem dígitos suficientes')
            self.__placa = None
        else:
            self.__placa = placa

    def dirigir(self, velocidade):
            print('Estou dirigindo a %d km/h' % velocidade)

fusca = Automovel('KMA-2234')
corola = Automovel('KS2')

print(fusca.get_placa())
print(corola.get_placa())