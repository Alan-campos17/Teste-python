while True:
    valorC1apital= int(input("Digite o valor do seu capital:"))
    print("vamos considerar uma selic de 13,25 por cento e ver quanto renderá seu capital:")
    rentabilidadedeBruto = valorCapital * 1.1325
    print(f"Se investir seu dinheiro na Selic no fim do ano você tera: \n {rentabilidadedeBruto}")
   
    faturamento = int(input("Digite o faturamento do seu negocio em um ano"))

    lucroLiquido = faturamento * 0.15

    if (lucroLiquido < rentabilidadedeBruto):
    print(f"O negocio não é viavel")
    print(f"O seu lucro liquido é {lucroLiquido}")
    break
    
else:
    print(f"O seu negocio é viavel")
    print(f"O seu lucro liquido é {lucroLiquido}")
    break