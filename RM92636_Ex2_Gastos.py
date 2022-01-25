soma = 0
media = 0

transacoes = int(input("Quantas transações você realizou hoje?: "))

for x in range(0, transacoes):
    valores = float(input("Digite o valor de cada uma das transações: "))

    soma = soma + valores
    media = soma / transacoes

print("O total foi de {}$".format(soma))
print("A média das transações foi de {:.2f}$".format(media))
