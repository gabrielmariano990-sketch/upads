# Loop for - Percorrendo Strings
nome = input("Digite seu nome: ")
print(f"\nLetras de '{nome}':")
for letra in nome:
    print(f" -> {letra}")

# Contar vogais
vogais = "aeiouAEIOU"
contagem = 0
for letra in nome:
    if letra in vogais:
        contagem += 1

print(f"'{nome}' tem {contagem} vogal(is).")