total_dias = int(input("Digite o total de dias: "))

anos = total_dias // 360
resto = total_dias % 360

meses = resto // 30
dias = resto % 30

print(f"{anos} ano(s), {meses} mês(es) e {dias} dia(s)")