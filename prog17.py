temperatura = float(input("Digite a temperatura atual: "))

if temperatura < 18:
    print("Está Frio.")
elif temperatura >= 18 and temperatura < 30:
    print("Está agradável.")
else:
    print("Está calor")
