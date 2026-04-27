# Análise de Senha

senha = input("Digite sua senha: ")

tem_maiuscula = False
tem_numero = False

# Verificar cada caractere
for ch in senha:
    if ch.isupper():
        tem_maiuscula = True
    if ch.isdigit():
        tem_numero = True

# Verificar comprimento
tem_tamanho = len(senha) >= 8

# Resultado final
print("\n--- Resultado da Análise ---")
print(f"Tem pelo menos 8 caracteres? {'Sim' if tem_tamanho else 'Não'}")
print(f"Contém letra maiúscula? {'Sim' if tem_maiuscula else 'Não'}")
print(f"Contém número? {'Sim' if tem_numero else 'Não'}")

if tem_tamanho and tem_maiuscula and tem_numero:
    print("Senha forte!")
else:
    print("Senha fraca!")
