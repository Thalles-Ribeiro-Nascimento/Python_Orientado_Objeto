class Funcionario:
    def __init__(self, nome=None, salario=None):
        self.nome = nome
        self.salario = salario

    def __repr__(self):
        return (f"Nome: {self.nome}\n"
                f"Salário: R$ {self.salario:.2f}\n")

    def colocarNome(self, nome):
        self.nome = nome
        return self.nome

    def colocarSalario(self, salario):
        self.salario = salario
        return self.salario

    def aumentoSal(self, perc):
        if not self.salario and not self.nome:
            print('Funcionário não existe!!!')
        elif not self.salario:
            print('Funcionário sem salário')
        else:
            print(f'O funcionário {self.nome} ganhará um aumento de {perc}% no salário!')
            self.salario = self.salario + (self.salario * perc/100)
            print(f'Salário: R$ {self.salario:.2f}')


