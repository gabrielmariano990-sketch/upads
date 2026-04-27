# Calculadora Simples

# Leitura dos dados
num1 = float(input("Primeiro número: "))
operador = input("Operador (+, -, *, /): ")
num2 = float(input("Segundo número: "))

# Realização da operação
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 == 0:
        resultado = "Erro: divisão por zero não permitida."
    else:
        resultado = num1 / num2
else:
    resultado = "Operador inválido."

# Exibição do resultado
print(f"{num1} {operador} {num2} = {resultado}")
