def calculadora(num1, num2, operacao):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "Erro: Números devem ser inteiros ou flutuantes!"

    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Erro: Operação inválida!"

def main():
    print("Calculadora")
    print("-----------")

    while True:
        try:
            num1 = input("Digite o primeiro número: ")
            num1 = float(num1)  # converte a entrada para float
            break
        except ValueError:
            print("Erro: Número deve ser inteiro ou flutuante!")

    while True:
        try:
            num2 = input("Digite o segundo número: ")
            num2 = float(num2)  # converte a entrada para float
            break
        except ValueError:
            print("Erro: Número deve ser inteiro ou flutuante!")

    while True:
        operacao = input("Digite a operação (+, -, *, /): ")
        operacao = operacao.lower()  # converte para minúscula
        if operacao in ("+", "-", "*", "/"):
            break
        else:
            print("Erro: Operação inválida!")

    resultado = calculadora(num1, num2, operacao)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()