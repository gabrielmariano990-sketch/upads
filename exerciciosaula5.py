# Programa para verificar se um número é positivo, negativo ou zero
numero = int(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número {numero} é zero.")