contador = 1
soma_notas = 0

while contador <= 4:
    nota = float(input(f"digite a nota do { contador } bimestre"))
    if notas < 0 or notas > 10:
        print("nota inválida. a nota deve estar entre 0 e 10")
        continue 
    contador += 1
    soma_notas += notas

media = soma_notas / 4 
print("a média de notas é: ", media)

if media >= 7:
        print("o aluno está aprovado")
if media >=5:
        print("o aluno está em recuperação")
else:
       print("o aluno está reprovado")