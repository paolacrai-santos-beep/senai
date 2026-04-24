blusas = int(input("Quantidade de blusas: "))

metros_por_blusa = 120
metros_por_novelo = 125

novelos = (blusas * metros_por_blusa) / metros_por_novelo

print(f"Quantidade de novelos necessários: {novelos:.2f}")