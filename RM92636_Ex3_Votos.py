Seg = int(input("Digite o número de votos de Segunda-Feira: "))
Ter = int(input("Digite o número de votos de Terça-Feira:"))
Qua = int(input("Digite o número de votos de Quarta-Feira: "))
Qui = int(input("Digite o número de votos de Quinta-Feira:"))
Sex = int(input("Digite o número de votos de Sexta-Feira: "))

if (Seg > Ter) and (Seg > Qua) and (Seg > Qui) and (Seg > Sex):
    print("Segunda-Feira é o dia mais votado, com {} votos.".format(Seg))

if (Ter > Seg) and (Ter > Qua) and (Ter > Qui) and (Ter > Sex):
    print("Terça-Feira é o dia mais votado, com {} votos.".format(Ter))

if (Qua > Seg) and (Qua > Ter) and (Qua > Qui) and (Qua > Sex):
    print("Quarta-Feira é o dia mais votado, com {} votos.".format(Qua))

if (Qui > Seg) and (Qui > Qua) and (Qui > Qua) and (Qua > Sex):
    print("Terça-Feira é o dia mais votado, com {} votos.".format(Qua))

if (Sex > Seg) and (Sex > Qua) and (Sex > Qui) and (Sex > Ter):
    print("Sexta-Feira é o dia mais votado, com {} votos.".format(Sex))

