dia=input("Digite o dia da semana: ")
match dia:
  case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":
     print("Dia de semana. Dia de progamar!")
  case "Sábado" | "Domingo":
     print("Fim de semana! Hora de descansar.")
  case _:
     print("Dia inválido.")
