class Bola:
#     Construtor
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, color):
        self.cor = color

    def mostraCor(self):
        return self.cor


adidas = Bola('Azul', 35, "Poliuretano")
adidas.trocaCor("Preta")
print(f'Cor da bola: {adidas.mostraCor()}; Circunferência: {adidas.circunferencia}cm; Material: {adidas.material}')
