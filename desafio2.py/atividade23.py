altura_pessoa = float(input("Sua altura (m): "))
sombra_pessoa = float(input("Comprimento da sua sombra (m): "))
sombra_predio = float(input("Comprimento da sombra do prédio (m): "))

altura_predio = (altura_pessoa * sombra_predio) / sombra_pessoa

print(f"Altura do prédio: {altura_predio:.2f} m")