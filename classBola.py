class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circun = circunferencia
        self.material = material

    def mostraCor(self):
        return self.cor

    def trocaCor(self):
        color = input("Insira a nova cor: ")
        self.cor = color
        return self.cor


adidas = Bola("Azul", 38, 'Couro')
adidas.trocaCor()

print(f"Cor da bola: {adidas.mostraCor()}; Circuferência da bola: {adidas.circun}cm; Material da bola: {adidas.material}")
