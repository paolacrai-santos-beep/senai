numero = int(input("Digite um número inteiro (até 3 dígitos): "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print(f"CENTENA = {centena}")
print(f"DEZENA = {dezena}")
print(f"UNIDADE = {unidade}")