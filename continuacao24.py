# Calculadora de Média da Turma

notas = []
aprovados = 0
recuperacao = 0
reprovados = 0

while True:
    nota = float(input("Digite a nota do aluno (-1 para encerrar): "))
    if nota == -1:
        break
    if nota < 0 or nota > 10:
        print("Nota inválida! Digite um valor entre 0 e 10.")
        continue
    
    notas.append(nota)
    
    if nota >= 7:
        aprovados += 1
    elif nota >= 5:
        recuperacao += 1
    else:
        reprovados += 1

# Processamento final
quantidade = len(notas)

if quantidade > 0:
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / quantidade
    percentual_aprovacao = (aprovados / quantidade) * 100
else:
    maior = menor = media = percentual_aprovacao = 0

# Exibição dos resultados
print("\n--- Relatório da Turma ---")
print(f"Quantidade de alunos: {quantidade}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média da turma: {media:.2f}")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
print(f"Percentual de aprovação: {percentual_aprovacao:.2f}%")
