import random

print("BEM vindo ao simulador de Lutas Medievais")
print("Você é um guerreiro enfrentando um inimigo")

vida_jogador = 100
vida_inimigo = 100
dano_base = 15

while vida_jogador > 0 and vida_inimigo > 0:
    print(f"\n Sua vida é {vida_jogador} e a vida do inimigo é {vida_inimigo}")
    input("pressione Enter para atacar")

    dano_jogador = random.randint(dano_base - 5, dano_base + 5)
    vida_inimigo -= dano_jogador
    print(f"Você causou {dano_jogador}")

    if vida_inimigo <= 0:
        print("Você ganhou")
        break

    dano_inimigo = random.randint(dano_base - 5, dano_base + 5)
    vida_jogador -= dano_inimigo
    print(f"Inimigo causou {dano_inimigo}")

    if vida_jogador <= 0:
        print("Você perdeu")
        break