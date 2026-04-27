# Desenho de Triângulo

altura = int(input("Digite a altura do triângulo: "))

print("\nTriângulo alinhado à esquerda:")
for i in range(1, altura + 1):
    print("*" * i)

print("\nTriângulo centralizado:")
for i in range(1, altura + 1):
    # número de espaços antes
    espacos = altura - i
    # número de asteriscos (sempre ímpar)
    estrelas = 2 * i - 1
    print(" " * espacos + "*" * estrelas)
