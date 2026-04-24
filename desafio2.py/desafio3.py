import time
tempo_resfriamento = 10

print("Iniciando tempo de resfriamento...\n")

for segundos in range(tempo_resfriamento, 0, -1):
    print(f"Tempo restante: {segundos} segundos")
    time.sleep(1)  

print("\nTempo finalizado! A prensa pode ser aberta.")