vogais = "aeiouAEIOU"

quantidade_vogais = 0
quantidade_consoantes = 0

while True:
    letra = input("Digite um caractere (ou '#' para encerrar): ")
    if letra == "#":
        break

    if letra in vogais:
        quantidade_vogais += 1
        print("a letra digitada é uma vogal")

    elif letra.isalpha():
        quantidade_consoantes += 1
        print("a letra digitada é uma consoante")

    else:
        print("a letra digitada não é uma letra do alfabeto")

print("\nRESULTADO FINAL")
print(f"Quantidade de vogais digitadas: {quantidade_vogais}")
print(f"Quantidade de consoantes digitadas: {quantidade_consoantes}")

if quantidade_vogais > quantidade_consoantes:
    print("Foram digitadas mais vogais do que consoantes.")

elif quantidade_consoantes > quantidade_vogais:
    print("Foram digitadas mais consoantes do que vogais.")

else:
    print("Foram digitadas a mesma quantidade de vogais e consoantes.")

