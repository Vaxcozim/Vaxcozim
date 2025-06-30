
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

while True:
    print("\nCalculadora")
    print("Selecione uma das operações abaixo:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "5":
        print("Saindo da calculadora...")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Por favor, selecione uma opção válida.")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite apenas números.")
        continue

    match opcao: 
        case "1":
            resultado = soma(num1, num2)
            print(f"O resultado da soma é: {resultado}")
        case "2":
            resultado = subtracao(num1, num2)
            print(f"O resultado da subtração é: {resultado}")
        case "3":
            resultado = multiplicacao(num1, num2)
            print(f"O resultado da multiplicação é: {resultado}")
        case "4":
            resultado = divisao(num1, num2)
            print(f"O resultado da divisão é: {resultado}")
        case _:
            print("Opção inválida. Por favor, selecione uma opção válida.")

