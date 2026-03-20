paes = float(input("quantos pães foram vendidos:"))
broas = float(input("quantas broas foram vendidas:"))

arrecadado = (paes * 0.12) + (broas * 1.50)
poupança = (arrecadado * 0.10)

print("total de vendas de pão e broa foi:", arrecadado)
print("quantidade de dinheiro que iria pra poupança:", poupança)