palavra = "python"

letras_usuarios = []
chances = 7

ganhou = False

while True:
    # criar a nossa logica
 for letra in palavra:
    if letra in letras_usuarios:
       print(letra, end=" ")
    else:
       print("_",  end=" ")
       print("")
       break

if ganhou:
    print(f"parabens, você ganhou. A palavra era: {palavra} ")
else:
    print(f"Você perdeu! A palavra era {palavra}")