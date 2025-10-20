MAX = 100
funcionarios = []  

def adicionar_funcionario():
    if len(funcionarios) >= MAX:
        print("Limite atingido!")
        return

    nome = input("Nome: ").strip()
    cargo = input("Cargo: ").strip()

    try:
        salario = float(input("Salário: ").strip())
    except ValueError:
        print("Valor de salário inválido!")
        return

    funcionario = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }

    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")


def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    print("\n=== Lista de Funcionários ===")
    for i, f in enumerate(funcionarios, start=1):
        print(f"{i}) {f['nome']} - {f['cargo']} - R$ {f['salario']:.2f}")

def buscar_funcionario():
    nome_busca = input("Nome do funcionário: ").strip()

    for f in funcionarios:
        if f["nome"].lower() == nome_busca.lower():
            print(f"Cargo: {f['cargo']} | Salário: R$ {f['salario']:.2f}")
            return

    print("Funcionário não encontrado.")

def main():
    while True:
        print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
        print("1 - Adicionar funcionário")
        print("2 - Listar funcionários")
        print("3 - Buscar funcionário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            buscar_funcionario()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
