contador = 1
soma = 0
while contador <= 5:
    salario = float(input(f"digite o salário do {contador} funcionário: "))
    contador += 1
    soma += salario
media = soma / 5
print ("a média dos salários dos 5 funcionários é: ", media)