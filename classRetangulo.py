class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarLados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def retornaLados(self):
        return f'Base = {self.base}m; Altura = {self.altura}m'

    def calculoArea(self):
        area = self.base * self.altura
        return area

    def calculoPerim(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro

