# Sistema de Pedidos de Lanchonete

cardapio = {
    "Hambúrguer": {"preco": 25.00, "disponivel": True},
    "Pizza": {"preco": 35.00, "disponivel": True},
    "Suco": {"preco": 8.00, "disponivel": False},
    "Batata Frita": {"preco": 15.00, "disponivel": True},
    "Sorvete": {"preco": 12.00, "disponivel": False}
}

print("--- Cardápio ---")
for item, info in cardapio.items():
    status = "Disponível" if info["disponivel"] else "Indisponível"
    print(f"{item} - R$ {info['preco']:.2f} - {status}")

pedido = []
total = 0

while len(pedido) < 5:
    escolha = input("\nDigite o nome do item (ou 'cancelar' para encerrar): ")
    
    if escolha.lower() == "cancelar":
        print("\nPedido cancelado!")
        pedido = []
        total = 0
        break
    
    if escolha not in cardapio:
        print("Item não encontrado no cardápio.")
        continue
    
    if not cardapio[escolha]["disponivel"]:
        print(f"{escolha} está em falta. Escolha outro item.")
        continue
    
    pedido.append(escolha)
    total += cardapio[escolha]["preco"]
    print(f"{escolha} adicionado ao pedido.")

print("\n--- Resumo do Pedido ---")
if pedido:
    print("Itens pedidos:")
    for item in pedido:
        print(f"- {item} (R$ {cardapio[item]['preco']:.2f})")
    print(f"Quantidade de itens: {len(pedido)}")
    print(f"Valor total: R$ {total:.2f}")
else:
    print("Nenhum item foi pedido.")
