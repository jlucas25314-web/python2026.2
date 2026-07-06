peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso/(altura*altura)
print(f"Sendo sua altura {altura} e o seu peso sendo {peso} kg, seu indice de massa corporal é: {imc:.2f}")