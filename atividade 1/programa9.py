nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
while True:
    if idade > 120 or idade < 0:
        print("Idade inválida! por favor, digite uma idade igual ou menor que 120")
        idade = int(input("Digite sua idade: "))
    else:
        break 

dias = (idade * 365)
print(f"Olá {nome}, você já viveu cerca de:  {dias} dias")