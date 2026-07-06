idade = int(input("Digite a idade do candidato: "))
genero = input("Digite o gênero do candidato (masculino/femenino): ")

if idade >=18 and genero == "masculino":
    print ("O Candidato está APTO para o alistamento")    
else:
    print("O Candidato NÃO ESTÁ APTO para o alistamento")