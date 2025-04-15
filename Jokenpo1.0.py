import random

# Variáveis para estatísticas
estatisticas_hvh = {'partidas': 0, 'jogador1': 0, 'jogador2': 0, 'empates': 0}
estatisticas_hvm = {'partidas': 0, 'humano': 0, 'maquina': 0, 'empates': 0}
estatisticas_mvm = {'partidas': 0, 'maquina1': 0, 'maquina2': 0, 'empates': 0}

print("Bem-vindo ao Jokenpô!")

while True:
    print("\nMenu:")
    print("1 - Humano vs Humano")
    print("2 - Humano vs Máquina")
    print("3 - Máquina vs Máquina")
    print("4 - Ver Estatísticas")
    print("5 - Sair")

    # Seleção de modo
    while True:
        try:
            opcao = int(input("Escolha: "))
            if 1 <= opcao <= 5:
                break
            print("Digite 1, 2, 3, 4 ou 5")
        except:
            print("Entrada inválida. Digite um número")

    if opcao == 5:
        break

    if opcao == 4:
        # Mostrar estatísticas
        print("\n--- Estatísticas ---")

        # Estatísticas Humano vs Humano
        print("\nHumano vs Humano:")
        if estatisticas_hvh['partidas'] > 0:
            total = estatisticas_hvh['partidas']
            print(f"Partidas: {total}")
            print(f"Jogador 1: {estatisticas_hvh['jogador1']} vitórias ({(estatisticas_hvh['jogador1']/total)*100:.1f}%)")
            print(f"Jogador 2: {estatisticas_hvh['jogador2']} vitórias ({(estatisticas_hvh['jogador2']/total)*100:.1f}%)")
            print(f"Empates: {estatisticas_hvh['empates']} ({(estatisticas_hvh['empates']/total)*100:.1f}%)")
        else:
            print("Nenhuma partida jogada")

        # Estatísticas Humano vs Máquina
        print("\nHumano vs Máquina:")
        if estatisticas_hvm['partidas'] > 0:
            total = estatisticas_hvm['partidas']
            print(f"Partidas: {total}")
            print(f"Humano: {estatisticas_hvm['humano']} vitórias ({(estatisticas_hvm['humano']/total)*100:.1f}%)")
            print(f"Máquina: {estatisticas_hvm['maquina']} vitórias ({(estatisticas_hvm['maquina']/total)*100:.1f}%)")
            print(f"Empates: {estatisticas_hvm['empates']} ({(estatisticas_hvm['empates']/total)*100:.1f}%)")
        else:
            print("Nenhuma partida jogada")

        # Estatísticas Máquina vs Máquina
        print("\nMáquina vs Máquina:")
        if estatisticas_mvm['partidas'] > 0:
            total = estatisticas_mvm['partidas']
            print(f"Partidas: {total}")
            print(f"Máquina 1: {estatisticas_mvm['maquina1']} vitórias ({(estatisticas_mvm['maquina1']/total)*100:.1f}%)")
            print(f"Máquina 2: {estatisticas_mvm['maquina2']} vitórias ({(estatisticas_mvm['maquina2']/total)*100:.1f}%)")
            print(f"Empates: {estatisticas_mvm['empates']} ({(estatisticas_mvm['empates']/total)*100:.1f}%)")
        else:
            print("Nenhuma partida jogada")

        continue

    # Jogar uma partida
    while True:
        if opcao == 1:
            # Modo Humano vs Humano
            print("\nModo: Humano vs Humano")

            # Jogador 1
            while True:
                try:
                    j1 = int(input("Jogador 1 (1-Pedra, 2-Papel, 3-Tesoura): "))
                    if 1 <= j1 <= 3:
                        break
                    print("Digite 1, 2 ou 3")
                except:
                    print("Entrada inválida. Digite um número")

            # Jogador 2
            while True:
                try:
                    j2 = int(input("Jogador 2 (1-Pedra, 2-Papel, 3-Tesoura): "))
                    if 1 <= j2 <= 3:
                        break
                    print("Digite 1, 2 ou 3")
                except:
                    print("Entrada inválida. Digite um número")

            estatisticas_hvh['partidas'] += 1

            # Determinar vencedor
            if j1 == j2:
                print("\nEmpate!")
                estatisticas_hvh['empates'] += 1
            elif (j1 == 1 and j2 == 3) or (j1 == 2 and j2 == 1) or (j1 == 3 and j2 == 2):
                print("\nJogador 1 venceu!")
                estatisticas_hvh['jogador1'] += 1
            else:
                print("\nJogador 2 venceu!")
                estatisticas_hvh['jogador2'] += 1

        elif opcao == 2:
            # Modo Humano vs Máquina
            print("\nModo: Humano vs Máquina")

            # Jogador humano
            while True:
                try:
                    j1 = int(input("Sua jogada (1-Pedra, 2-Papel, 3-Tesoura): "))
                    if 1 <= j1 <= 3:
                        break
                    print("Digite 1, 2 ou 3")
                except:
                    print("Entrada inválida. Digite um número")

            # Máquina
            j2 = random.randint(1, 3)
            print(f"Máquina jogou: {['Pedra', 'Papel', 'Tesoura'][j2-1]}")

            estatisticas_hvm['partidas'] += 1

            # Determinar vencedor
            if j1 == j2:
                print("\nEmpate!")
                estatisticas_hvm['empates'] += 1
            elif (j1 == 1 and j2 == 3) or (j1 == 2 and j2 == 1) or (j1 == 3 and j2 == 2):
                print("\nVocê venceu!")
                estatisticas_hvm['humano'] += 1
            else:
                print("\nMáquina venceu!")
                estatisticas_hvm['maquina'] += 1

        elif opcao == 3:
            # Modo Máquina vs Máquina
            print("\nModo: Máquina vs Máquina")

            # Máquina 1
            j1 = random.randint(1, 3)
            print(f"Máquina 1 jogou: {['Pedra', 'Papel', 'Tesoura'][j1-1]}")

            # Máquina 2
            j2 = random.randint(1, 3)
            print(f"Máquina 2 jogou: {['Pedra', 'Papel', 'Tesoura'][j2-1]}")

            estatisticas_mvm['partidas'] += 1

            # Determinar vencedor
            if j1 == j2:
                print("\nEmpate!")
                estatisticas_mvm['empates'] += 1
            elif (j1 == 1 and j2 == 3) or (j1 == 2 and j2 == 1) or (j1 == 3 and j2 == 2):
                print("\nMáquina 1 venceu!")
                estatisticas_mvm['maquina1'] += 1
            else:
                print("\nMáquina 2 venceu!")
                estatisticas_mvm['maquina2'] += 1



print("\nObrigado por jogar!")