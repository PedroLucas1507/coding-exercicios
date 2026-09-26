def fibonacci(posicao):
    if posicao == 1 or posicao == 2:
        return 1

    return  fibonacci(posicao - 1) + fibonacci(posicao - 2)

posicao = int(input("Digite a posição da sequência de Fibonacci que deseja calcular: "))

if posicao <= 0:
    print("A posição deve ser um número inteiro positivo.")
else:
    resultado = fibonacci(posicao)
    print(f"O número na posição {posicao} da sequência de Fibonacci é: {resultado}")