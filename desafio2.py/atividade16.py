quantidade = int(input("Digite a quantidade de sanduíches: "))

queijo_por_sanduiche = 2 * 50   # 2 fatias
presunto_por_sanduiche = 50
carne_por_sanduiche = 100

total_queijo = quantidade * queijo_por_sanduiche
total_presunto = quantidade * presunto_por_sanduiche
total_carne = quantidade * carne_por_sanduiche

total_queijo /= 1000
total_presunto /= 1000
total_carne /= 1000

print(f"Queijo: {total_queijo:.2f} kg")
print(f"Presunto: {total_presunto:.2f} kg")
print(f"Carne: {total_carne:.2f} kg")