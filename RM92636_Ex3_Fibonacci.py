x = 0
y = 1
z = 1

n = int(input("Digite um número inteiro: "))

if n == 0 or n == 1:
    print("O número {} pertence a sequência de Fibonacci".format(n))
else:
    while x < n:
        x = y + z
        z = y
        y = x
    if x == n:
        print("O número {} pertence a sequência de Fibonacci".format(n))
    else:
        print("O número não pertence a sequência de Fibonacci")
