# Lista inicial de jantaNormal
jantaNormal = ["salsicha", "X-bacon", "Miojo", "Coca-cola", "Pizza-Doce"]

# Adicionando novos itens à lista
jantaNormal.append("torresmo")
jantaNormal.append("hamburguer")
jantaNormal.append("batata frita")
jantaNormal.append("salada")
jantaNormal.append("suco")

# Removendo os últimos 3 itens adicionados, se existirem
for _ in range(3):
    if jantaNormal:  # Verifica se a lista não está vazia
        jantaNormal.pop()

# Imprimindo a lista final
print(jantaNormal)