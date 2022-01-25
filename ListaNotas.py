notas = []

opcao = -1
while opcao != 4:
    print("1 - Informar notas \n 2 - Exibir notas \n 3 - Calcular média da sala \n 4 - Sair")
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        notas.append(float(input("Digite as notas: ")))

    elif opcao == 2:
        for x in notas:
            print(x)

    elif opcao == 3:
        media = (sum(notas)/len(notas))
        print("A média da sala é {:.2f}".format(media))

