num1 = float(input("Digite um valor: "))
num2 = float(input("Digite outro valor: "))

print("Escolha a Operação")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Escolha a op: ")

match opcao:
    case "1":
        resultado = num1 + num2
        print(f"Resultado da soma: {resultado}")
    case "2":
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")
    case "3":
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")
    case "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro: Não é possível dividir por zero!")
    case _:
        print("Opção inválida! Escolha um número de 1 a 4.")