def cadastrar_colaborador(nome: str, cargo: str, salario: float) -> dict:
    return {
        "nome": nome,
        "cargo": cargo,
        "salario": salario,
    }
def exibir_colaboradores(lista_colaboradores: list) -> None:
    if not lista_colaboradores:
        print("Nenhum colaborador cadastrado.")
        return
    print("\nLista de Colaboradores")
    for i, colaborador in enumerate(lista_colaboradores, start=1):
        print(f"{i}. Nome: {colaborador['nome']}")
        print(f"Cargo: {colaborador['cargo']}")
        print(f"Salario: R$ {colaborador['salario']:.2f}")
    print("\n")
