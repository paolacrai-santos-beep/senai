m1 = int(input("Moedas de 1 centavo: "))
m5 = int(input("Moedas de 5 centavos: "))
m10 = int(input("Moedas de 10 centavos: "))
m25 = int(input("Moedas de 25 centavos: "))
m50 = int(input("Moedas de 50 centavos: "))
m1r = int(input("Moedas de 1 real: "))

total = (m1*0.01 + m5*0.05 + m10*0.10 + m25*0.25 + m50*0.50 + m1r*1)

print(f"Total economizado: R$ {total:.2f}")