peso = input ("Digite o seu peso: ")
altura = input("Digite a sua altura em metros: ")
imc = float(peso) / (float(altura) ** 2)
if imc < 16:
	print("O seu IMC é {:.2f}, e está na categoria Baixo peso grau 3".format(imc))
elif imc <= 16.99:
	print("O seu IMC é {:.2f}, e está na categoria Baixo peso grau 2".format(imc))
elif imc <= 18.49:
	print("O seu IMC é {:.2f}, e está na categoria Baixo peso grau 1".format(imc))
elif imc <= 24.99:
	print("O seu IMC é {:.2f}, e está no peso ideal".format(imc))
elif imc <= 29.99:
	print("O seu IMC é {:.2f}, e você está com Sobrepeso".format(imc))
elif imc <= 34.99:
	print("O seu IMC é {:.2f}, e está na categoria de Obesidade grau 1".format(imc))
elif imc <= 39.99:
	print("O seu IMC é {:.2f}, e está na categoria de Obesidade grau 2".format(imc))
elif imc >= 40:
	print("O seu IMC é {:.2f}, e está na categoria de Obesidade grau 3".format(imc))