# 1. CRIANDO AS LISTAS (Nossos gaveteiros de 12 espaços)
# Multiplicar por 12 cria uma lista com 12 espaços vazios ou zerados.
numero_voo = [0] * 12
origem = [""] * 12
destino = [""] * 12
lugares_disponiveis = [0] * 12

# Colocando dados no primeiro avião (posição 0) para a gente conseguir testar
numero_voo[0] = 1010
origem[0] = "Juiz de Fora"
destino[0] = "São Paulo"
lugares_disponiveis[0] = 50

# 2. O LOOP DO MENU PRINCIPAL
while True:
    print("\n==== COMPANHIA AÉREA ====")
    print("1 - Consultar")
    print("2 - Efetuar reserva")
    print("3 - Sair")
    
    # input() lê o que a pessoa digita. int() transforma esse texto em um número.
    opcao = int(input("Escolha uma opção: "))
    
    # 3. VERIFICANDO A OPÇÃO ESCOLHIDA (No Python usamos if, elif e else em vez de switch)
    if opcao == 1:
        print("\n--- CONSULTA ---")
        print("1 - Por número do vôo")
        print("2 - Por origem")
        print("3 - Por destino")
        
        op_consulta = int(input("Escolha o tipo de consulta: "))
        
        if op_consulta == 1:
            busca_numero = int(input("Digite o número do vôo: "))
            
            # O 'for' no Python é muito mais simples. 
            # range(12) significa que o 'i' vai de 0 até 11.
            for i in range(12):
                if numero_voo[i] == busca_numero:
                    print(f"Vôo: {numero_voo[i]} | De: {origem[i]} Para: {destino[i]} | Lugares: {lugares_disponiveis[i]}")
                    
    elif opcao == 2:
        voo_desejado = int(input("\nDigite o número do vôo que deseja viajar: "))
        encontrou_voo = False # Nossa bandeira indicando se achamos o voo
        
        for i in range(12):
            if numero_voo[i] == voo_desejado:
                encontrou_voo = True # Achamos o voo!
                
                # Verifica se tem lugar sobrando
                if lugares_disponiveis[i] > 0:
                    lugares_disponiveis[i] = lugares_disponiveis[i] - 1 # Dá baixa na passagem
                    print("Reserva confirmada!")
                else:
                    print("Vôo lotado.")
                
                break # Para de procurar nas outras gavetas
                
        # Se o loop terminar e a bandeira continuar False, o voo não existe
        if encontrou_voo == False:
            print("Vôo inexistente.")
            
    elif opcao == 3:
        print("Saindo do programa...")
        break # Esse comando quebra o "while True", encerrando tudo.
        
    else:
        print("Opção inválida. Tente novamente.")