import random

# Jogo de Adivinhação

secreto = random.randint(1, 50)
tentativas = 0
acertou = False

print("Tente adivinhar o número entre 1 e 50!")
print("Você tem 7 tentativas.\n")

while tentativas < 7:
    palpite = int(input(f"Tentativa {tentativas+1}: "))
    tentativas += 1
    
    if palpite == secreto:
        acertou = True
        break
    elif palpite > secreto:
        print("O número secreto é menor!")
    else:
        print("O número secreto é maior!")

# Classificação final
if acertou:
    print(f"\nParabéns! Você acertou o número {secreto} em {tentativas} tentativa(s).")
    if tentativas <= 3:
        print("Classificação: MESTRE!")
    elif tentativas <= 5:
        print("Classificação: Muito bom!")
    else:
        print("Classificação: Na hora certa!")
else:
    print(f"\nGame Over! O número secreto era {secreto}.")
