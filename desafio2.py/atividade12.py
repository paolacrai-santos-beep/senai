salario = float(input("Digite o salário: R$ "))

aumento = salario * 0.15
salario_com_aumento = salario + aumento

imposto = salario_com_aumento * 0.08
salario_final = salario_com_aumento - imposto

print(f"Salário inicial: R$ {salario:.2f}")
print(f"Salário com aumento: R$ {salario_com_aumento:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")