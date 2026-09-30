total = 0

quantidade = 0

while True:
    valor = (float(input("Digite um valor (ou 0 para encerrar): ")))
    if valor == 0:
        break

    elif valor < 0:
        print("Valor inválido. Digite um número positivo.")

    else:
        total += float(valor)
        quantidade += 1

print(f"Total de valores digitados:{total:.2f}")
print(f"Quantidade de valores digitados:{quantidade}")
