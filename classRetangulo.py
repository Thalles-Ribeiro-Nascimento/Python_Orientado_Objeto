class Retangulo:
    def __init__(self, b, h):
        self.base = b
        self.altura = h

    def setLados(self):
        base = input("Insira um novo valor para base: ")
        self.base = base
        altura = input("Insira um novo valor para altura: ")
        self.altura = altura
        return self.base and self.altura

    def Area(self):
        return self.base * self.altura

    def Perimetro(self):
        return 2*(self.base + self.altura)

retan = Retangulo(4, 5)

print(f'Base: {retan.base} cm; Altura: {retan.altura} cm; Área: {retan.Area()} cm; Perímetro: {retan.Perimetro()} cm')
