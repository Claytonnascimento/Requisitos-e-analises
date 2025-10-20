notas = {}
lista_nomes = []

def adicionar_aluno():
    nome = input("Nome do aluno: ").strip()
    try:
        nota = float(input("Nota final: ").strip())
    except ValueError:
        print("Valor inválido! Digite um número para a nota.")
        return

    notas[nome] = nota
    lista_nomes.append(nome)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    if not lista_nomes:
        print("Nenhum aluno cadastrado.")
        return

    print("\n Lista de Alunos")
    for nome in lista_nomes:
        print(f"- {nome} | Nota: {notas[nome]:.2f}")

def buscar_nota():
    nome = input("Nome do aluno: ").strip()
    if nome in notas:
        print(f"Nota de {nome}: {notas[nome]:.2f}")
    else:
        print("Aluno não encontrado.")

def main():
    while True:
        print("\n SISTEMA DE ALUNOS")
        print("1 - Adicionar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar nota")
        print("0 - Sair")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_nota()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
