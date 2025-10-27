import math

def calcular_volume_cilindro(raio, altura):
    volume = math.pi * (raio ** 2) * altura
    return volume

raio = float(input("Digite o raio do cilindro em cm³: "))
altura = float(input("Digite a altura do cilindro em cm³: "))

volume = calcular_volume_cilindro(raio, altura)
print(f"O volume do cilindro é: {volume:.2f} cm³")

