numero = int(input("Digite um número inteiro: "))

if numero == 0 or numero == 1:
    print(f"O número {numero} não é primo.")

elif numero == 2:
    print(f"O número {numero} é primo.")
elif numero % 2 == 0:
    print(f"O número {numero} não é primo.")

else:
    primo = True

    divisor = 3

    while divisor <= numero:
        if numero % divisor == 0:
            primo = False
            break
        divisor += 2

    if primo:
        print(f"O número {numero} é primo.")    

    else:
        print(f"O número {numero} não é primo.")