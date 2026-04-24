
preco_p = 10
preco_m = 12
preco_g = 15

qtd_p = int(input("Quantidade de camisetas pequenas: "))
qtd_m = int(input("Quantidade de camisetas médias: "))
qtd_g = int(input("Quantidade de camisetas grandes: "))

total = (qtd_p * preco_p) + (qtd_m * preco_m) + (qtd_g * preco_g)

print(f"Valor arrecadado: R$ {total:.2f}")