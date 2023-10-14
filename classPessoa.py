class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def __repr__(self):
        return (f'Nome: {self.nome}\n'
                f'Idade: {self.idade} anos\n'
                f'Peso: {self.peso}kg\n'
                f'Altura: {self.altura}m')

    def crescer(self):
        if self.idade < 21:
            self.altura = self.altura + 0.05
        else:
            return self.altura

    def envelhecer(self):
        self.idade = self.idade + 1
        self.crescer()
        return self.idade

    def engordar(self, kilos):
        self.peso = self.peso + kilos
        return self.peso

    def emagrecer(self, quilos):
        self.peso = self.peso - quilos
        return self.peso


p1 = Pessoa('Thalles', 24, 60, 1.75)

print(f'{p1};\n'
      f'\n'
      f'{p1.nome} fez aniversário, agora ele tem {p1.envelhecer()} anos;\n'
      f'{p1.nome} subiu o peso para {p1.engordar(4)}kg;\n'
      f'{p1.nome} desceu o peso para {p1.emagrecer(2)}kg;\n'
      f'Altura: {p1.altura:.2f}')
