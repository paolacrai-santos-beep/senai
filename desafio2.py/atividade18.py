horas_normais = float(input("Horas normais trabalhadas: "))
horas_extras = float(input("Horas extras trabalhadas: "))

salario_bruto = (horas_normais * 10) + (horas_extras * 15)
salario_liquido = salario_bruto * 0.9

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")