class Funcionario:
    def __init__(self, id_func, name_func, sal_func, department_func):
        self.id = id_func
        self.nome = name_func
        self.salario = sal_func
        self.departamento = department_func

    def calHoraExtra(self, salario, horas_trabalhadas):
        if horas_trabalhadas > 50:
            print(f"O funcionário {self.nome} trabalhou {horas_trabalhadas}hrs a mais!")
            hora_extra = horas_trabalhadas - 50
            valor = hora_extra * (salario/50)
            self.salario = self.salario + valor
            print(f"Ganho adicional por hora extra foi de: R${valor:.2f}\n")
            return self.salario
        else:
            print(f"Para cálculo de horas extras é necessário ter trabalhado mais de 50hrs\n")
            return self.salario

    def alterarDepartment(self, novo_departamento):
        print(f"O funcionário {self.nome} está indo para um novo departamento!")
        self.departamento = novo_departamento
        print(f"Novo departamento: {self.departamento}\n")
        return self.departamento

    def detalhesFunc(self):
        print(f'Informações do funcionário {self.nome}:\n'
              f'ID: {self.id}\n'
              f'Nome: {self.nome}\n'
              f'Salário: R${self.salario:.2f}\n'
              f'Departamento: {self.departamento}\n')


func = Funcionario(1335, 'Thalles', 900, 'Tecnologia da Informação')
func.detalhesFunc()
func.alterarDepartment("Recursos Humanos")
func.calHoraExtra(900, 60)
func.detalhesFunc()
func2 = Funcionario(1299, "Bruno", 5450, "Professor")
func2.detalhesFunc()
