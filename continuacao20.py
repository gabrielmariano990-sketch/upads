# Caixa Registradora

total = 0
quantidade = 0

while True:
    nome = input("Nome do produto (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    
    preco = float(input(f"Preço de {nome}: "))
    
    if preco <= 0:
        print("Preço inválido! Deve ser maior que zero.")
        continue
    
    total += preco
    quantidade += 1

# Cálculo da média
if quantidade > 0:
    media = total / quantidade
else:
    media = 0

# Aplicar desconto se necessário
if total > 200:
    desconto = total * 0.05
    total -= desconto
    print(f"\nDesconto aplicado: R$ {desconto:.2f}")

# Exibir resultados finais
print("\n--- Resumo da Compra ---")
print(f"Quantidade de itens: {quantidade}")
print(f"Valor total: R$ {total:.2f}")
print(f"Valor médio por item: R$ {media:.2f}")
