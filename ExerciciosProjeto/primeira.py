def nota_valida(nota):
    return 0 <= nota <= 10


def calcular_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)


while True:
    print("DESEMPENHO ESCOLAR")

    turma = input("Digite sua turma: ")
    disciplina = input("Digite sua disciplina: ")
    qtdalunos = int(input("Digite a quantidade de alunos: "))
    notas = []

    for i in range(qtdalunos):
        while True:
            nota = float(input(f"Digite a nota do aluno {i + 1}: "))
            if nota_valida(nota):
                notas.append(nota)
                break
            print("Nota inválida. Digite uma nota entre 0 e 10.")

    media = calcular_media(notas)

    if media >= 7:
        situacao = "Bem avaliada"
    elif media >= 5:
        situacao = "Em alerta"
    else:
        situacao = "Precisa de intervenção"

    print("\nRELATÓRIO DO DESEMPENHO ESCOLAR ")
    print(f"Turma: {turma}")
    print(f"Disciplina: {disciplina}")
    print(f"Quantidade de alunos: {qtdalunos}")
    print(f"Média da turma: {media:.2f}")
    print(f"Situação: {situacao}")

    reiniciar = input("Deseja cadastrar outra turma? (s/n): ").strip().lower()

    if reiniciar != "s":
        print("Encerrando o programa.")
        break