import math

# Fórmula de Bhaskara: (-b +- sqrt(b² - 4ac)) / (2a)

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print('\nValor de x1: {0}'.format(x1))
    print('Valor de x2: {0}'.format(x2))
    print(f"O x1 é {x1} e o x2 é {x2}")
else:
    print("O delta é negativo, não existem raízes reais.")
