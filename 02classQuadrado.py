class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def setLado(self):
        tamanho_lado = input("Insira um novo valor do lado: ")
        self.lado = tamanho_lado
        return self.getLado()

    def getLado(self):
        return self.lado

    def calcArea(self):
        return self.lado**2

quadrado = Quadrado(2)

print(f"Lado do quadrado = {quadrado.getLado()}; Sua área é {quadrado.calcArea()}")

