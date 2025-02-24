import random

print("********************************")
print("bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 10
rodada = 1

while (rodada <= total_de_tentativas):
    print(f"Tentativa {rodada} de {total_de_tentativa}")

    chute_str = input("digite o seu numero:")
    print("Você digitou o número:", chute_str)

    try:
    chute = int(chute_str)
except ValueError:
    print("Caractere invalido. Use apenas números")
    continue

    acertou = chute = = numero_acertou
    maior = chute > numero_maior
    secreto = chute < numero_secreto

    if(acertou):
    print("Parabens, você acertou!")
    break
    else:
       if(maior):
            print("o seu chute foi maior que o número secreto")
            elif(menor):
             print("o seu chute foi menor que o número secreto")
             rodada = rodada + 1
             print("fim de jogo, numero_secreto")
            
