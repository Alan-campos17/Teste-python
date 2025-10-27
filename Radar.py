import time

distancia_metragem = 10

inicio = time.perf_counter()
input("Pressione Enter quando o objeto passar pelo ponto inicial...")
tempo_inicial = time.perf_counter()

input("Pressione Enter quando o objeto passar pelo ponto final...")
tempo_final = time.perf_counter()

tempo_decorrido = tempo_final - tempo_inicial

velocidade_ms = distancia_metragem / tempo_decorrido
velocidade_kmh = velocidade_ms * 3.6 

limite_velocidade = 60 
if velocidade_kmh > limite_velocidade:
    print(f"Você passou a {velocidade_kmh:.2f} km/h. Limite: {limite_velocidade} km/h. Multado!")
else:
    print(f"Você passou a {velocidade_kmh:.2f} km/h dentro do limite.")