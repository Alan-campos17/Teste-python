investimentoInicial = float(input("Digite o valor do investimento inicial:"))
taxaDesconto = float(input("digite a taxa de desconto:"))
taxaPorcentagem = taxaDesconto / 100

contador = 1
qnFluxosCaixa = int(input("Digite a quantidade de fluxos de caixa:"))
valorPresenteLiquido = 0
while contador <= qnFluxosCaixa:
    faturamento = float(input("Digite o faturamento do ano {contador}:"))
    valorPresenteLiquido += faturamento / (1 + taxaPorcentagem) ** contador
    contador += 1

    if(valorPresenteLiquido - investimentoInicial) > 0:
        print( " O VPL é positivo, o investimento é viavel")
    else:
        print("O VPL é negativo, o investimento não é viavel")
