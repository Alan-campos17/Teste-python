import time
import os

def cronometro(segundos: int) -> str:
    """Executa um cronômetro regressivo no terminal."""
    for s in range(segundos, 0, -1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"⏳ Tempo restante: {s} segundos")
        time.sleep(1)
    print("🚨 Tempo esgotado!")
    return f"Cronômetro de {segundos} segundos finalizado!"
