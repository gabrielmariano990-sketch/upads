#ler 5 notas e calcular media 
total = 0 # acumulador 
aprovados = 0 # contador 

for i in range(1, 6):
    nota = float(input(f"nota {i}:"))
    nota += nota      # acumula
    if nota >=7.0:
        aprovados += 1 # conta
        
media = total / 5 
print(f"\nmedia da turma: {media:.2f}")
print(f"aprovados: {aprovados} de 5")