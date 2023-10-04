class Veiculo:
    # Class Attribute;
    color = "White"

    # __init__ Construtor e privado; Self é uma referência ao Objeto instânciado e dentro do construtor passamos métodos
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"A capacidade da(o) {self.name} é de {capacity} passageiros"

# Classe do ônibus
class Onibus(Veiculo):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)

# Classe da moto
class Moto(Veiculo):
    def seating_capacity(self, capacity = 2):
        return super().seating_capacity(capacity = 2)

# Instância Moto
xre = Moto("Xre", 180, 20)
print(xre.seating_capacity())
print(f"{xre.name} é {xre.color}")

# Instância Ônibus
bus = Onibus("Escolar", 180, 125503)
print(bus.seating_capacity())
print(f"{bus.name} é {bus.color}")



