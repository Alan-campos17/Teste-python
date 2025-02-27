print("****************************")
print("Bem vindo ao jogo da forca")
print("****************************")

palavra = "python"

enforcou = False
ganhou = False

letras_usuarios = []
chances = 7

while(not enforcou and not acertou ):
   chute = input("qual a letra?")
   chute = chute.strip()

   index = 0
   for letra in palavra_secreta:
      if(chute == letra):
         print( f"Encontrei a letra {letra} na posição{index}")
         index = index + 1
   print("jogando....")
   print("fim de jogo")

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