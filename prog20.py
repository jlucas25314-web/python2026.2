cargo = input("Digite o cargo (caixa, vendedor ou gerente): ").upper()

if cargo == "CAIXA":
    salario_base = 1500
elif cargo == "VENDEDOR":
    salario_base = 2400
elif cargo == "GERENTE":
    salario_base = 4000
else:
    salario_base = 0
    print("Cargo inválido! Rode o programa novamente.")

if salario_base > 0:
    
    inss = salario_base * 0.12
    
    if salario_base > 2000:
        irrf = salario_base * 0.14
    else:
        irrf = salario_base * 0.08
         
    salario_final = salario_base - irrf - inss

print(f"Salário Base: R$ {salario_base:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IRRF: R$ {irrf:.2f}")
print(f"Salário Final Líquido: R$ {salario_final:.2f}")