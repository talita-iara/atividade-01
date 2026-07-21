import csv
nome_arquivo = "dados_atividade01.csv"
with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
print("Arquivo CSV criado!")

matricula = "12345"
senha = "teste"

h_inicio = 0
h_intervalo_inicio = 0
h_intervalo_final = 0
h_final = 0

padrao_inicio = "08:00"
padrao_intervalo_inicio = "12:00"
padrao_intervalo_final = "13:00"
padrao_final = "17:00"

matricula_usuario = input("Digite sua matrícula: ")
senha_usuario = input("Digite sua senha: ")

if matricula_usuario == matricula and senha_usuario == senha:

    while True:

        menu = int(input(
"======== MENU ======== \n"
"0 - Sair \n"
"1 - Início da jornada \n"
"2 - Início do intervalo \n"
"3 - Fim do intervalo \n"
"4 - Fim da jornada \n"
"5 - Exibir registros \n"
"Digite a opção: "))

        if menu == 1:
            h_inicio = input("Digite o horário de início da jornada: ")
            if h_inicio >= "06:00" and h_inicio <= "10:00":
                print("Horário registrado com sucesso!")
            else:
                print("Você passou do horário de tolerância, favor dirija-se ao RH para realizar o registro e justificativa.")

        elif menu == 2:
            if h_inicio != 0:
                h_intervalo_inicio = input("Digite o horário de início do intervalo: ")
                print("Horário registrado com sucesso!")
            else:
                print("Primeiro registre o início da jornada.")

        elif menu == 3:
            if h_intervalo_inicio != 0:
                h_intervalo_final = input("Digite o horário de fim do intervalo: ")
                print("Horário registrado com sucesso!")
            else:
                print("Primeiro registre o início do intervalo.")

        elif menu == 4:
            if h_intervalo_final != 0 or (h_intervalo_inicio == 0 and h_intervalo_final == 0):
                h_final = input("Digite o horário de fim da jornada: ")
                if h_final >= "15:00" and h_final <= "19:00":
                    print("Horário registrado com sucesso!")
                else:
                    print("Você passou do horário de tolerância, favor dirija-se ao RH para realizar o registro e justificativa.")
            else:
                print("Marcações inválidas, verifique os registros.")

        elif menu == 5:
            print("\n===== REGISTROS =====")
            print("Início da jornada:", h_inicio)
            print("Início do intervalo:", h_intervalo_inicio)
            print("Fim do intervalo:", h_intervalo_final)
            print("Fim da jornada:", h_final)

        elif menu == 0:
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")

else:
    print("Matrícula ou senha inválidas.")