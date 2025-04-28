ValorCompra = float(input("Digite o valor de compra: "))
ValorVenda = float(input("Digite o valor de venda: "))

Lucro = ValorVenda - ValorCompra

if Lucro > 0:
    print("O lucro é de R$ %.2f" % Lucro)
elif Lucro < 0:
    print("O prejuízo é de R$ %.2f" % abs(Lucro))
else:
    print("Não houve lucro nem prejuízo.")