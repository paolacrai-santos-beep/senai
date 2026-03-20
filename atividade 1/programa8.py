nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade > 120:
    print("Idade inválida! por favor, digite uma idade igual ou menor que 120")

dias = (idade * 365)

print(nome,"você já viveu", dias,"dias")
