# Verificador de Primos

num = int(input("Digite um número inteiro positivo: "))

if num <= 1:
    print(f"{num} não é primo (números menores ou iguais a 1 não são considerados primos).")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            divisor = i
            break

    if primo:
        print(f"{num} é primo!")
    else:
        print(f"{num} não é primo. É divisível por {divisor}.")
