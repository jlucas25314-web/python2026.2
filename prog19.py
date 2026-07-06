idade = int(input("Digite a idade: "))
ingresso = input("Tem ingresso? (sim/não) ").upper()

if idade >=12 and ingresso == "SIM":
    print("Acesso Liberado! Divirta-se no Brinquedo.")
elif ingresso == "SIM" and idade < 12:
    print("Você tem ingresso,mas não tem idade mínima de 12 anos.")
else:
    print("Acesso negado. Você precisa de um ingresso.")