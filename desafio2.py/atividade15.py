conta = float(input("Digite o valor total da conta: R$ "))

parte = conta / 3

carlos = int(parte)
andre = int(parte)

felipe = conta - (carlos + andre)

print(f"Carlos paga: R$ {carlos:.2f}")
print(f"André paga: R$ {andre:.2f}")
print(f"Felipe paga: R$ {felipe:.2f}")