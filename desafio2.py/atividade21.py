
latas = int(input("Quantidade de latas (350 ml): "))
garrafas_600 = int(input("Quantidade de garrafas (600 ml): "))
garrafas_2l = int(input("Quantidade de garrafas (2L): "))

total_litros = (latas * 0.35) + (garrafas_600 * 0.6) + (garrafas_2l * 2)

print(f"Total de litros: {total_litros:.2f} L")