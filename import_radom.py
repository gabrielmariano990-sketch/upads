import random

secreto = random.randint(1, 100)
tentativas = 0
print("pensei num numero de 1 a 100. tente adivinhar! ")

while True:
    palpite = int(input("seu palpite:"))
    tentativas += 1

    if palpite < secreto:
        print("maior! tente um outro numero mais alto.")
    elif palpite > secreto:
         print("menor! tente um outro numero mais baixo.")

    else:
        print(f"parabens! acertou em {tentativas} tentativas(s)!")
        break