assinatura = (input("Qual o seu tipo de assinatura?: "))
faturamento = int(input("Digite o seu faturamento: "))

if assinatura == "Basic":
    bonusB = 30 * faturamento / 100
    print(bonusB)

elif assinatura == "Silver":
    bonusS = 20 * faturamento / 100
    print(bonusS)

elif assinatura == "Gold":
    bonusG = 10 * faturamento / 100
    print(bonusG)

elif assinatura == "Platinum":
    bonusP = 5 * faturamento / 100
    print(bonusP)