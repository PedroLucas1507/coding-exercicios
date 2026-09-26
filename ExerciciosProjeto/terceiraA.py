posicao = int(input("Digite a posição da sequência de Fibonacci que deseja calcular: "))

if posicao <= 0:
    print("A posição deve ser um número inteiro positivo.")
elif posicao == 1 or posicao == 2:
    print(f"O número na posição {posicao} da sequência de Fibonacci é: 1")
else:
    fib_anterior = 1
    fib_atual = 1

    for i in range(3, posicao + 1):
        fib_proximo = fib_anterior + fib_atual
        fib_anterior = fib_atual
        fib_atual = fib_proximo

    print(f"O número na posição {posicao} da sequência de Fibonacci é: {fib_atual}")