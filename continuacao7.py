# Sistema de Notas com Frequência
print("=== SISTEMA DE NOTAS COM FREQUÊNCIA ===")

# Leitura dos dados
nota = float(input("Digite a nota final do aluno (0-10): "))
frequencia = float(input("Digite a frequência do aluno (%): "))

# Validações básicas
if nota < 0 or nota > 10:
    print("ERRO: Nota deve estar entre 0 e 10!")
elif frequencia < 0 or frequencia > 100:
    print("ERRO: Frequência deve estar entre 0 e 100%!")
else:
    # Determinação do status
    if nota >= 7.0 and frequencia >= 75:
        status = "APROVADO"
    elif nota < 7.0 and frequencia >= 75:
        status = "REPROVADO por nota"
    elif nota >= 7.0 and frequencia < 75:
        status = "REPROVADO por falta"
    else:  # nota < 7.0 e frequencia < 75
        status = "REPROVADO por nota e falta"
    
    # Exibição do resultado
    print(f"\n{'='*40}")
    print(f"Nota final: {nota:.1f}")
    print(f"Frequência: {frequencia:.1f}%")
    print(f"Status: {status}")
    print(f"{'='*40}")