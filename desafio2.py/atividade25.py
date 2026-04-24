import math

raio = float(input("Raio da base: "))
altura = float(input("Altura: "))

volume = math.pi * (raio ** 2) * altura

print(f"Volume: {volume:.2f}")