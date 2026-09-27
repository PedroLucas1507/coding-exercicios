numero1 = int(input("insira o primeiro número inteiro: "))
numero2 = int(input("insira o segundo número inteiro: "))

resto = numero1

while resto >= numero2:
    resto -= numero2

print(f"O resto da divisão de {numero1} por {numero2} é: {resto}")