from mod_rh import cadastrar_colaborador, exibir_colaboradores

colaboradores = []

while True:
    print("\nSistema de RH")
    print("1 - Cadastrar colaborador")
    print("2 - Listar colaboradores")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        while True:
            try:
                salario = float(input("Salario: ").replace(",", "."))
                break
            except ValueError:
                print("Valor inválido. Digite um número (ex: 3500.00).")
        colaborador = cadastrar_colaborador(nome, cargo, salario)
        colaboradores.append(colaborador)
        print("Colaborador '{nome}' cadastrado com sucesso!")

    elif opcao == "2":
        exibir_colaboradores(colaboradores)
    elif opcao == "0":
        print("Sistema encerrado.")
        break
    else:
        print("Opcao invalida.")
