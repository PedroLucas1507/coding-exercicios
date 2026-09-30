pontos = 0

gabarito = ["b", "a", "d"]

for i in range(3):
    resposta = input(f"Digite a resposta da questão {i + 1}: ").lower()

    if resposta == gabarito[i]:
        pontos += 1

print(f"Pontuação final: {pontos}")