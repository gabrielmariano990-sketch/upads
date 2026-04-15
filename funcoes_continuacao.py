def linha(tamanho):
    """Imprime linha de = com tamanho especificado"""
    print("=" * tamanho)

def cabecalho(titulo, tamanho=30):
    """Cabeçalho com título centralizado"""
    linha(tamanho)
    espacos = (tamanho - len(titulo)) // 2
    print(" " * espacos + titulo)
    linha(tamanho)
    print()  # Linha em branco

# Exemplos de uso
cabecalho("Relatório de Notas", 30)
cabecalho("Vendas 2024", 25)
cabecalho("Boletim Escolar")  # Usa padrão 30