# Tabuada Completa (1 a 10)

# Cabeçalho
print("     ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()

# Corpo da tabela
for linha in range(1, 11):
    print(f"{linha:2}:", end="")
    for coluna in range(1, 11):
        print(f"{linha * coluna:4}", end="")
    print()
