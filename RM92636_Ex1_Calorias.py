soma = 0
alimentos = int(input("Digite quantos alimentos você comeu hoje: "))

for x in range(alimentos):
    total = float(input("Quantas calorias o alimento possuía? "))
    soma = soma + total

print("O total de calorias ingeridas é de {}".format(soma))
