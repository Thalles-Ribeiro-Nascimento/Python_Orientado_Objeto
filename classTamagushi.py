class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = self.saude - self.fome

    def __repr__(self):
        return (f'Nome: {self.nome}\n'
                f'Fome: {self.fome}\n'
                f'Saúde: {self.saude}\n'
                f'Idade: {self.idade}\n'
                f'Humor: {self.humor}')

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def retornaNome(self):
        return self.nome

    def alterarFome(self, comida):
        self.fome = self.fome - comida
        self.humor = self.saude - self.fome

    def retornaFome(self):
        return self.fome

    def alterarSaude(self, dano):
        self.saude = self.saude - dano
        self.humor = self.saude - self.fome

    def retornaSaude(self):
        return self.saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornaIdade(self):
        return self.idade


bicho = Tamagushi("Lilo", 50, 100, 5)
bicho.alterarFome(10)
bicho.alterarSaude(25)
print(bicho)

