# Programa de descontos da loja
valor_compra = float(input("Valor da compra (R$): "))

print(f"Valor original: R$ {valor_compra:.2f}")

if valor_compra <= 100.00:
    desconto_percentual = 0
    valor_desconto = 0
    valor_final = valor_compra
    
elif valor_compra <= 500.00:
    desconto_percentual = 10
    valor_desconto = valor_compra * 0.10
    valor_final = valor_compra - valor_desconto
    
else:
    desconto_percentual = 20
    valor_desconto = valor_compra * 0.20
    valor_final = valor_compra - valor_desconto

print(f"Desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}") 