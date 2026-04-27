# Somatório Interativo

soma = 0
quantidade = 0

while True:
    numero = float(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero
    quantidade += 1

# Cálculo da média
if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

# Exibição dos resultados
print(f"Soma: {soma}")
print(f"Quantidade de números digitados: {quantidade}")
print(f"Média: {media}")
