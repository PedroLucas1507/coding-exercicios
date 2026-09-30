print("===== CONFIGURAÇÃO DO CAMPO MINADO =====")

# Cadastro do administrador
nome_admin = input("Digite o nome do administrador: ")
senha_admin = input("Digite a senha do administrador: ")

print("\nAdministrador cadastrado com sucesso!")

# Login do administrador
tentativas = 0
login_realizado = False

while tentativas < 3:

    senha = input("Digite a senha do administrador: ")

    if senha == senha_admin:
        login_realizado = True
        print("Login realizado com sucesso!")
        break

    tentativas += 1
    print(f"Senha incorreta. Tentativa {tentativas} de 3.")


if not login_realizado:
    print("Número máximo de tentativas atingido.")
    print("Programa encerrado.")

else:

    # Escolha da dificuldade
    while True:

        print("\n===== DIFICULDADE =====")
        print("1 - Fácil (3 bombas)")
        print("2 - Difícil (5 bombas)")

        dificuldade = input("Escolha a dificuldade: ")

        if dificuldade == "1":
            quantidade_bombas = 3
            break

        elif dificuldade == "2":
            quantidade_bombas = 5
            break

        else:
            print("Opção inválida.")

    # Cadastro das bombas
    bombas = []

    print(f"\nDigite a posição das {quantidade_bombas} bombas.")

    while len(bombas) < quantidade_bombas:

        posicao = int(input("Digite uma posição entre 1 e 15: "))

        if posicao < 1 or posicao > 15:
            print("Posição inválida!")
            continue

        if posicao in bombas:
            print("Essa posição já possui uma bomba!")
            continue

        bombas.append(posicao)

    # Limpar a tela
    print("\n" * 50)

    print("Configuração concluída!")

    # Cadastro dos jogadores
    jogador1 = input("Digite o nome do Jogador 1: ")
    jogador2 = input("Digite o nome do Jogador 2: ")

    pontos_jogador1 = 0
    pontos_jogador2 = 0

    # Controle de turno
    turno = 1

    jogo_terminou = False
    vencedor = ""
    motivo_vitoria = ""

    total_palpite = 0

    while not jogo_terminou:

        if turno == 1:

            jogador_atual = jogador1

        else:

            jogador_atual = jogador2

        print("\n==============================")
        print(f"É a vez de {jogador_atual}")
        print("==============================")

        posicao = int(input("Digite uma posição entre 1 e 15: "))

        if posicao < 1 or posicao > 15:
            print("Posição inválida. Tente novamente.")
            continue

        total_palpite += 1

        # Verificar se acertou uma bomba
        if posicao in bombas:

            print("\n💥 BOOM!")
            print(f"{jogador_atual} acertou uma bomba!")

            if turno == 1:
                vencedor = jogador2
            else:
                vencedor = jogador1

            motivo_vitoria = "porque o adversário explodiu."
            jogo_terminou = True

        else:

            print("Palpite seguro!")

            # Verificar se está perto de uma bomba
            perto_de_bomba = False

            for bomba in bombas:

                if abs(posicao - bomba) == 1:
                    perto_de_bomba = True
                    break

            if perto_de_bomba:
                print("Cuidado, você está perto de uma bomba!")

            # Contabilizar ponto
            if turno == 1:

                pontos_jogador1 += 1

                print(
                    f"{jogador1} possui "
                    f"{pontos_jogador1} palpites seguros."
                )

                if pontos_jogador1 == 3:
                    vencedor = jogador1
                    motivo_vitoria = "por atingir 3 palpites seguros."
                    jogo_terminou = True

            else:

                pontos_jogador2 += 1

                print(
                    f"{jogador2} possui "
                    f"{pontos_jogador2} palpites seguros."
                )

                if pontos_jogador2 == 3:
                    vencedor = jogador2
                    motivo_vitoria = "por atingir 3 palpites seguros."
                    jogo_terminou = True

            # Alternar jogador
            if not jogo_terminou:

                if turno == 1:
                    turno = 2
                else:
                    turno = 1

    # Relatório final
    print("\n================================")
    print("         FIM DA PARTIDA")
    print("================================")

    print(f"Vencedor: {vencedor}")
    print(f"Motivo: {motivo_vitoria}")
    print(f"Total de palpites: {total_palpite}")