class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = self.saude - self.fome

    def __repr__(self):
        return (f'Nome: {self.nome}\n'''
                f'Fome: {self.fome:.0f}\n'
                f'Saúde: {self.saude:.0f}\n'
                f'Idade: {self.idade:.0f}\n'
                f'Humor: {self.humor:.0f}\n')

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def retornaNome(self):
        return self.nome

    def alterarFome(self, comida):
        if self.fome < 1:
            print('Não é possível alimenta-lo, ele não está com fome!')
        elif self.fome < comida:
            print(f'Tem muita comida, a fome está menor que a quantidade de comida!!\n'
                  f'Fome: {self.fome}\n'
                  f'Quantidade de comida: {comida}')
        else:
            print(f'Estou com uma fome!!\n'
                  f'Fome: {self.fome:.0f}\n'
                  f'Hmmm!! Comida!!\n'
                  f'Comida: {comida}\n')
            self.fome = self.fome - comida
            self.humor = self.saude - self.fome
            print(f'Estava uma delicia! Obrigado amigo!\n'
                  f'Fome: {self.fome:.0f}\n')

    def retornaFome(self):
        return self.fome

    def brincar(self, tempo):
        print(f'Indo brincar por {tempo} minutos!!\n'
              f'Humor: {self.humor:.0f}\n')
        self.humor = self.humor + (tempo/10)  # A cada 10 minutos brincados, o humor aumenta 1
        self.fome = self.fome + (tempo/tempo)  # A cada tempo brincado, a fome aumenta 1
        print(f'Ufa, estou cansado e bateu uma fominha, brincamos muito!\n'
              f'Humor: {self.humor:.0f}\n'
              f'Fome: {self.fome:.0f}\n')
        return self.humor and self.fome

    def alterarSaude(self, dano):
        self.saude = self.saude - dano
        self.humor = self.saude - self.fome

    def retornaSaude(self):
        return self.saude

    def alterarIdade(self):
        self.idade = self.idade + 1
        print(f'Parabéns para mim!! Estou completando mais um ano de vida!')

    def retornaIdade(self):
        return self.idade


tamagushi = Tamagushi("Lilo", 40, 100, 5)
print(tamagushi)
tamagushi.brincar(20)
print(tamagushi)
tamagushi.alterarFome(25)
tamagushi.brincar(30)
print(tamagushi)
tamagushi.alterarIdade()
print(tamagushi)
