palavra = input("Digite uma palvra ou frase:").lower().replace("","")
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("É um palindromo!")
else:
    print("Não é um palindromo")
