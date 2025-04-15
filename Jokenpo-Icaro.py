import random



total_partidas_geral = 0
total_partidas_hxh = 0
total_partidas_hxm = 0
total_partidas_mxm = 0
vitorias_j1 = 0
vitorias_j2 = 0
vitorias_maquina_hxm = 0
vitorias_j1_hxm = 0
vitorias_maquina_mxm_1 = 0
vitorias_maquina_mxm_2 = 0
empates = 0
empates_hxh = 0
empates_hxm = 0
empates_mxm = 0

while True:
    print('\n--- MENU ---')
    print('modo 1: humano X humano')
    print('modo 2: humano X máquina')
    print('modo 3: máquina X máquina')
    print('modo 4: ver estatísticas gerais')
    print('modo 5: ver estatísticas do modo hxh')
    print('modo 6: ver estatísticas do modo hxm')
    print('modo 7: ver estatísticas do modo mxm')
    print('modo 8: sair\n')

    while True:
        modo_jogo = int(input('Digite o modo de jogo (1-8): '))

        if modo_jogo == 1 or modo_jogo == 2 or modo_jogo == 3 or modo_jogo == 4 or modo_jogo == 5 or modo_jogo == 6 or modo_jogo == 7 or modo_jogo == 8:
            break
        else:
            print('Digite números apenas de 1 à 8!')
            break

    if modo_jogo == 8:
        break

    if modo_jogo == 4:
        if total_partidas_geral == 0:
            print("Nenhuma partida jogada ainda.")
        else:
            print("\n--- ESTATÍSTICAS GERAIS ---")
            print(f"Total de partidas: {total_partidas_geral}")
            print(f"Vitórias do jogador 1: {vitorias_j1} ({(vitorias_j1 / total_partidas_geral) * 100:.2f}%)")
            print(f"Vitórias do jogador 2: {vitorias_j2} ({(vitorias_j2 / total_partidas_geral) * 100:.2f}%)")
            print(f"Vitórias do jogador 1 no hxm: {vitorias_j1_hxm} ({(vitorias_j1_hxm / total_partidas_hxm) * 100:.2f}%)")
            print(f"Vitórias da máquina no hxm: {vitorias_maquina_hxm} ({(vitorias_maquina_hxm / total_partidas_hxm) * 100:.2f}%)")
            print(f"Vitórias da máquina 1: {vitorias_maquina_mxm_1} ({(vitorias_maquina_mxm_1 / total_partidas_mxm) * 100:.2f}%)")
            print(f"Vitórias da máquina 2: {vitorias_maquina_mxm_2} ({(vitorias_maquina_mxm_2 / total_partidas_mxm) * 100:.2f}%)")
            print(f"Empates: {empates} ({(empates / total_partidas_geral) * 100:.2f}%)")
            print("---------------------\n")
            
    if modo_jogo == 5:
        
            print('\n--- ESTÁTÍSTICAS hxh ---')
            print(f"Total de partidas: {total_partidas_hxh}")
            print(f"Vitórias do jogador 1: {vitorias_j1} ({(vitorias_j1 / total_partidas_hxh) * 100:.2f}%)")
            print(f"Vitórias do jogador 2: {vitorias_j2} ({(vitorias_j2 / total_partidas_hxh) * 100:.2f}%)")
            print(f"Empates: {empates_hxh} ({(empates_hxh / total_partidas_hxh) * 100:.2f}%)")
            print("---------------------\n")
            
    if modo_jogo == 6:
        
            print('\n--- ESTÁTÍSTICAS hxm ---')
            print(f"Total de partidas: {total_partidas_hxm}")
            print(f"Vitórias do jogador 1 no hxm: {vitorias_j1_hxm} ({(vitorias_j1_hxm / total_partidas_hxm) * 100:.2f}%)")
            print(f"Vitórias da máquina: {vitorias_maquina_hxm} ({(vitorias_maquina_hxm / total_partidas_hxm) * 100:.2f}%)")
            print(f"Empates: {empates_hxm} ({(empates_hxm / total_partidas_hxm) * 100:.2f}%)")
            print("---------------------\n")
            
    if modo_jogo == 7:
        
            print('\n--- ESTÁTÍSTICAS mxm ---')
            print(f"Total de partidas: {total_partidas_mxm}")
            print(f"Vitórias da máquina 1: {vitorias_maquina_mxm_1} ({(vitorias_maquina_mxm_1 / total_partidas_mxm) * 100:.2f}%)")
            print(f"Vitórias da máquina 2: {vitorias_maquina_mxm_2} ({(vitorias_maquina_mxm_2 / total_partidas_mxm) * 100:.2f}%)")
            print(f"Empates: {empates_mxm} ({(empates_mxm / total_partidas_mxm) * 100:.2f}%)")
            print("---------------------\n")

    while True:
        if modo_jogo == 1:
            while modo_jogo == 1:
                escolha_jogador_1 = int(input('Escolha do 1º jogador: 1-Pedra, 2-Papel, 3-Tesoura?'))
                break
            while modo_jogo == 1:    
                escolha_jogador_2 = int(input('Escolha do 2º jogador: 1-Pedra, 2-Papel, 3-Tesoura?'))
                break
            total_partidas_geral += 1
            total_partidas_hxh += 1
            if escolha_jogador_1 == escolha_jogador_2:
                print('Empate!')
                empates += 1
                empates_hxh += 1 
            elif (escolha_jogador_1 == 1 and escolha_jogador_2 == 3) or (escolha_jogador_1 == 2 and escolha_jogador_2 == 1) or (escolha_jogador_1 == 3 and escolha_jogador_2 == 2): 
                print("Vitória do jogador 1")
                vitorias_j1 += 1
            else:
                print("Vitória do jogador 2")
                vitorias_j2 += 1

        elif modo_jogo == 2:
            while modo_jogo == 2:
                escolha_jogador_1 = int(input('Escolha do 1º jogador: 1-Pedra, 2-Papel, 3-Tesoura?'))
                break
            escolha_maquina_hxm = random.randint(1,3)
            print("A máquina 2 escolheu", escolha_maquina_hxm)
            total_partidas_geral += 1
            total_partidas_hxm += 1
            if escolha_jogador_1 == escolha_maquina_hxm:
                print('Empate!')
                empates += 1
                empates_hxm += 1
            elif (escolha_jogador_1 == 1 and escolha_maquina_hxm == 3) or (escolha_jogador_1 == 2 and escolha_maquina_hxm == 1) or (escolha_jogador_1 == 3 and escolha_maquina_hxm == 2): 
                print("Vitória do jogador 1")
                vitorias_j1_hxm += 1
            else:
                print("Vitória da máquina")
                vitorias_maquina_hxm += 1
                

        elif modo_jogo == 3:
            escolha_maquina_mxm_1 = random.randint(1,3)
            print("A máquina 1 escolheu", escolha_maquina_mxm_1)
            escolha_maquina_mxm_2 = random.randint(1,3)
            print("A máquina 2 escolheu", escolha_maquina_mxm_2)
            total_partidas_geral += 1
            total_partidas_mxm += 1
            if escolha_maquina_mxm_1 == escolha_maquina_mxm_2:
                print('Empate!')
                empates += 1
                empates_mxm += 1
            elif (escolha_maquina_mxm_1 == 1 and escolha_maquina_mxm_2 == 3) or (escolha_maquina_mxm_1 == 2 and escolha_maquina_mxm_2 == 1) or (escolha_maquina_mxm_1 == 3 and escolha_maquina_mxm_2 == 2): 
                print("Vitória da máquina 1")
                vitorias_maquina_mxm_1 += 1
            else:
                print("Vitória da máquina 2")
                vitorias_maquina_mxm_2 += 1

        while True:
            continuar = int(input("Digite 1 para jogar novamente e digite 2 para ir ao menu inicial: "))
            if continuar in [1,2]:
                break

        if continuar == 2:
            break




'''
while True:
        entrada = input("Escolha: ")
        if entrada == "1" or entrada == "2" or entrada == "3" or entrada == "4" or entrada == "5":
            opcao = int(entrada)
            break
        print("Entrada inválida. Digite 1, 2, 3, 4 ou 5.")

    if opcao == 5:
        break

    # Mostrar estatísticas
    if opcao == 4:
        print("\n--- Estatísticas ---")

        # Humano vs Humano
        print("\nHumano vs Humano:")
        total = estatisticas_hvh['partidas']
        if total > 0:
            print("Partidas:", total)
            print("Jogador 1:", estatisticas_hvh['jogador1'], "vitórias", f"({(estatisticas_hvh['jogador1']*100)//total}%)")
            print("Jogador 2:", estatisticas_hvh['jogador2'], "vitórias", f"({(estatisticas_hvh['jogador2']*100)//total}%)")
            print("Empates:", estatisticas_hvh['empates'], f"({(estatisticas_hvh['empates']*100)//total}%)")
        else:
            print("Nenhuma partida jogada.")

        # Humano vs Máquina
        print("\nHumano vs Máquina:")
        total = estatisticas_hvm['partidas']
        if total > 0:
            print("Partidas:", total)
            print("Humano:", estatisticas_hvm['humano'], "vitórias", f"({(estatisticas_hvm['humano']*100)//total}%)")
            print("Máquina:", estatisticas_hvm['maquina'], "vitórias", f"({(estatisticas_hvm['maquina']*100)//total}%)")
            print("Empates:", estatisticas_hvm['empates'], f"({(estatisticas_hvm['empates']*100)//total}%)")
        else:
            print("Nenhuma partida jogada.")

        # Máquina vs Máquina
        print("\nMáquina vs Máquina:")
        total = estatisticas_mvm['partidas']
        if total > 0:
            print("Partidas:", total)
            print("Máquina 1:", estatisticas_mvm['maquina1'], "vitórias", f"({(estatisticas_mvm['maquina1']*100)//total}%)")
            print("Máquina 2:", estatisticas_mvm['maquina2'], "vitórias", f"({(estatisticas_mvm['maquina2']*100)//total}%)")
            print("Empates:", estatisticas_mvm['empates'], f"({(estatisticas_mvm['empates']*100)//total}%)")
        else:
            print("Nenhuma partida jogada.")

        continue
'''