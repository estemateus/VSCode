class Veiculo:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade  # Velocidade em km/h

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano, 0)
        self.potencia = potencia  # Potência em cavalos (HP)
    
    def acelerar(self, incremento):
# Carros podem acelerar mais rápido
        self.velocidade += incremento + self.potencia

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano, 0)
        self.tipo = tipo  # Tipo de bicicleta (ex: mountain bike, estrada)

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo}, Velocidade: {self.velocidade} km/h"

# Criando objetos
carro1 = Carro("Toyota", "Corolla", 2022, 150)
bicicleta1 = Bicicleta("Trek", "Mountain Bike", 2021, "MTB")

# Acelerando os veículos, pois se não indicarmos este valor, a velocidade permanecerá 0
carro1.acelerar(10)      # Vai somar 10 + 150 = 160
bicicleta1.acelerar(5)   # Vai somar 5

# Exibindo o status dos veículos
print("Status do Carro:")
print(carro1.status())

print("\nStatus da Bicicleta:")
print(bicicleta1.status())