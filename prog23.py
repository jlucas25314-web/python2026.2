codigo = int(input("Digite o código: "))
match codigo:
    case 200:
        print("Sucesso! Tudo certo a sua requisição.")
    case 400:
        print ("Erro do cliente: Requisição malformada.")
    case 401 | 403:
        print("Erro de permissão: Você não tem acesso a esta pagina")
    case 404:
        print("Erro: Pagina nao encostrada")
    case 500 | 503:
        print("Erro no servidor: Nosso sistema esta instavel no momento")
    case _:
        print("codigo HTTP {codigo_status} desconhecido")
        