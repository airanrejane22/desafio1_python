# Lista para armazenar registros de estudantes (cada estudante é um dicionário)
registros = []

# Função para adicionar um novo registro de estudante
def adicionar_estudante():
    nome, estudante_id, notas = input("Digite o nome, ID e notas do estudante (separados por espaço): ").split()
    notas = [float(nota) for nota in notas.split()]
    registro = {"Nome": nome, "ID": estudante_id, "Notas": notas}
    registros.append(registro)
    print("Registro de estudante adicionado com sucesso.")

# Função para exibir todos os registros de estudantes
def exibir_registros():
    for registro in registros:
        print("Nome: " + registro["Nome"])
        print("ID: " + registro["ID"])
        print("Notas: " + ", ".join(map(str, registro["Notas"]))
        print()

# Função para procurar um estudante pelo ID
def procurar_por_id():
    estudante_id = input("Digite o ID do estudante que deseja procurar: ")
    for registro in registros:
        if registro["ID"] == estudante_id:
            print("Registro encontrado:")
            print("Nome: " + registro["Nome"])
            print("ID: " + registro["ID"])
            print("Notas: " + ", ".join(map(str, registro["Notas"]))
            break
    else:
        print("ID não encontrado.")

# Função para calcular e exibir a média de notas de todos os estudantes
def calcular_media_notas():
    if not registros:
        print("Nenhum registro de estudante disponível.")
    else:
        todas_notas = [nota for registro in registros for nota in registro["Notas"]]
        media = sum(todas_notas) / len(todas_notas)
        print(f"A média de notas de todos os estudantes é: {media:.2f}")

# Função para salvar registros de estudantes em um arquivo de texto
def salvar_em_arquivo():
    formato = input("Escolha o formato de salvamento (por exemplo, CSV): ")
    with open("registros_estudantes.txt", "w") as arquivo:
        for registro in registros:
            if formato.lower() == "csv":
                linha = f"{registro['Nome']},{registro['ID']},{','.join(map(str, registro['Notas']))}\n"
            else:
                linha = f"{registro['Nome']} {registro['ID']} {' '.join(map(str, registro['Notas']))}\n"
            arquivo.write(linha)
    print("Registros salvos em arquivo.")

# Função para carregar registros de estudantes de um arquivo de texto
def carregar_de_arquivo():
    formato = input("Escolha o formato de carregamento (por exemplo, CSV): ")
    registros.clear()
    with open("registros_estudantes.txt", "r") as arquivo:
        for linha in arquivo:
            if formato.lower() == "csv":
                dados = linha.strip().split(',')
            else:
                dados = linha.strip().split()
            nome, estudante_id, notas = dados[0], dados[1], list(map(float, dados[2:]))
            registro = {"Nome": nome, "ID": estudante_id, "Notas": notas}
            registros.append(registro)
    print("Registros carregados do arquivo.")

# Loop principal para o programa
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar novo registro de estudante")
    print("2. Exibir registros de estudantes")
    print("3. Procurar estudante por ID")
    print("4. Calcular média de notas de estudantes")
    print("5. Salvar registros em arquivo")
    print("6. Carregar registros de arquivo")
    print("0. Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        adicionar_estudante()
    elif escolha == "2":
        exibir_registros()
    elif escolha == "3":
        procurar_por_id()
    elif escolha == "4":
        calcular_media_notas()
    elif escolha == "5":
        salvar_em_arquivo()
    elif escolha == "6":
        carregar_de_arquivo()
    elif escolha == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")
