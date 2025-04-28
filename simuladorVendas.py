#1 - Perguntar ao usuario o investimento inicial
#2 - Perguntar ao usuario a taxa de desconto
#3 - Perguntar o faturamento do ano 1, 2, 3, 4,e 5
#4 - calcular o VPL de cada ano seguindo a formula
#5 - faturamento1 / (1 + taxa) ^t
#6 - Somar os 4 VPLs e diminuir o Investimento inicial

faturamento1 = float(input("digite o faturamento do ano 1:"))
faturamento2 = float(input("digite o faturamento do ano 2:"))
faturamento3 = float(input("digite o faturamento do ano 3:"))
faturamento4 = float(input("digite o faturamento do ano 4:"))
faturamento5 = float(input("digite o faturamento do ano 5:"))
                     
investimento = float(input("digite o investimento inicial:"))
taxa = float(input("digite a taxa de desconto:") /100)

ano1 = faturamento1 / (1 + 20) **1
ano2 = faturamento2 / (1 + 20) **2
ano3 = faturamento3 / (1 + 20) **3
ano4 = faturamento4 / (1 + 20) **4
ano5 = faturamento5 / (1 + 20) **5
vpl = ano1 + ano2 + ano3 + ano4 + ano5 - investimento
print("O VPL é de R$ %.2f" % vpl)
if vpl > 0:
    print("O VPL é positivo, o investimento é viavel")
else:
    print("O VPL é negativo o investimento não é viavel")