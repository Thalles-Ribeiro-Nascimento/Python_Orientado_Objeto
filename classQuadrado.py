class Quadrado:
    def __init__(self, tamanho_lado):
        self.lado = tamanho_lado

    def mudaValorLado(self, novo_lado):
        self.lado = novo_lado

    def retornarLado(self):
        return self.lado

    def calculaArea(self):
        area = self.lado**2
        return area


quadrado = Quadrado(2)
quadrado.mudaValorLado(4)
print(f"Valor: {quadrado.retornarLado()}cm; Área: {quadrado.calculaArea()}cm")
