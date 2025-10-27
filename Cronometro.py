import time
import os

class Cronometro:
    def __init__(self, segundos: int):
        self.segundos = segundos

    def iniciar(self):
        """Roda um cronômetro regressivo no terminal"""
        for s in range(self.segundos, 0, -1):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"⏳ Tempo restante: {s} segundos")
            time.sleep(1)
        print("🚨 Tempo esgotado!")


if __name__ == "__main__":
    print("=== Cronômetro ===")
    tempo = int(input("Digite o tempo do cronômetro em segundos: "))
    c = Cronometro(tempo)
    c.iniciar()
