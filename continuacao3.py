# Programa para classificar faixa etária
idade = int(input("Digite a idade: "))

if 0 <= idade <= 11:
    print(f"Idade {idade}: Criança")
elif 12 <= idade <= 17:
    print(f"Idade {idade}: Adolescente")
elif 18 <= idade <= 59:
    print(f"Idade {idade}: Adulto")
else:  # 60 ou mais
    print(f"Idade {idade}: Idoso")