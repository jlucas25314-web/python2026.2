anoat = int(input("Digite o ano atual "))
anon = int(input("Digite o ano de nascimento "))

idade = anoat - anon
print(f"sua idade é {idade}")
if idade >=18:
    print("Maior de idade")
else:
    print("Menor de idade")