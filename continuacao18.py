# Maior e Menor de N números

n = int(input("Quantos números você deseja digitar? "))

soma = 0
maior = None
menor = None

for i in range(n):
    num = float(input(f"Digite o {i+1}º número: "))
    soma += num
    
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

media = soma / n

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média dos valores: {media}")
