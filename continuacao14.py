# Contagem Regressiva Personalizada

inicio = int(input("Número inicial: "))
passo = int(input("Passo: "))

valor = inicio
while valor > 0:
    print(valor, end=" ")
    valor -= passo

print("\nFim da contagem!")
