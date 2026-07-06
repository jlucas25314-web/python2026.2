opcao = int(input("Digite uma opção "))

match opcao:
    case 1:
     print("Você escolheu a opção 1: Ver saldo")
    case 2:
     print("Voce escolheu a opção 2: Fazer saque")
    case 3:
     print("Voce escolheu a opção 3: Falar com atentendente.")
    case _:
     print("Opção inválida! Escolha um numero de 1 a 3.") 
    