# Potência sem Operador **

base = int(input("Base: "))
expoente = int(input("Expoente (inteiro positivo): "))

resultado = 1
for i in range(expoente):
    resultado *= base

print(f"{base} ^ {expoente} = {resultado}")
