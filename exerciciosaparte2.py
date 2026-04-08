# Sistema de login com 3 tentativas
SENHA_CORRETA = "python123"
tentativas = 3

while tentativas > 0:
    senha = input(f"Digite a senha ({tentativas} tentativa(s) restante(s)): ")
    
    if senha == SENHA_CORRETA:
        print("✅ Acesso liberado!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"❌ Senha incorreta! {tentativas} tentativa(s) restante(s).")
        else:
            print("🚫 Conta bloqueada!") 