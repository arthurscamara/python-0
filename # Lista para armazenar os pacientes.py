
paciente_nome = ""
paciente_telefone = ""

while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar paciente")
    print("2 - Ver paciente")
    print("3 - Enviar lembrete")
    print("4 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        paciente_nome = input("Digite o nome do paciente: ")
        paciente_telefone = input("Digite o telefone do paciente: ")
        print("Paciente cadastrado com sucesso!")

    elif opcao == "2":
        if paciente_nome != "":
            print("Nome do paciente:", paciente_nome)
            print("Telefone:", paciente_telefone)
        else:
            print("Nenhum paciente cadastrado.")

    elif opcao == "3":
        if paciente_nome != "":
            print("Lembrete enviado para", paciente_nome)
        else:
            print("Nenhum paciente para enviar lembrete.")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
