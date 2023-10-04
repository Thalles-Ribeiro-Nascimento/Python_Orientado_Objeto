class Funcionario:
    def __init__(self):
        self.__salario = None
        self.__nome = None

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getSalario(self):
        return self.__salario

    def setSalario(self, salario):
        self.__salario = salario


thalles = Funcionario()
thalles.setNome('Thalles Nascimento')
thalles.setSalario(2500)
print(thalles.getNome())
print(thalles.getSalario())
