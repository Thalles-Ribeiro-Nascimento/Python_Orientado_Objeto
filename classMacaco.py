class Macaco:
    def __init__(self, nome, bucho=None):
        self.nome = nome
        self.bucho = bucho

    def comer(self, comida):
        # Crie uma lista para poder retirar o alimento da lista, através do função pop(), no método digerir
        estomago = [comida]

        if comida == self or comida == jack:
            print('Não é possível comer esse tipo de alimento!')
        else:
            print(f'{self.nome} está comendo {comida}.')
            self.bucho = estomago

    def verBucho(self):
        print(f'Estômago do {self.nome}: {self.bucho}\n')

    def digerir(self):
        if not self.bucho:
            print('Seu macaco está com fome!')
        else:
            self.bucho.pop()
            print(f'O alimento foi digerido.\n'
                  f'Estômago: {self.bucho}\n'
                  f'')


jack = Macaco('Jackson')
jack.comer('Maçã')
jack.verBucho()
jack.digerir()
jack.comer('Banana')
jack.verBucho()
jack.digerir()
jack.comer('Tangerina')
jack.verBucho()
jack.digerir()

bob = Macaco('Bob')
bob.comer('Banana')
bob.verBucho()
bob.digerir()
bob.comer('Maçã')
bob.verBucho()
bob.digerir()
bob.comer(jack)
bob.verBucho()
bob.comer('Manga')
bob.verBucho()
