# 1. CRIANDO AS NOSSAS ESTRUTURAS
pilha_alunos = [] # O último a entrar fica no final da lista (topo)
fila_notas = []   # O primeiro a entrar fica no começo da lista (início)

numero_gerado = 1 # O número do aluno começa no 1 e vai aumentando sozinho

# 2. O MENU PRINCIPAL
while True:
    print("\n==== SISTEMA ESCOLAR ====")
    print("1 - Cadastrar aluno")
    print("2 - Cadastrar nota")
    print("3 - Calcular a média de um aluno")
    print("4 - Listar os nomes dos alunos sem notas")
    print("5 - Excluir aluno (Regra de Pilha)")
    print("6 - Excluir nota (Regra de Fila)")
    print("7 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    # OPÇÃO 1: Cadastrar aluno na Pilha
    if opcao == 1:
        nome_aluno = input("Digite o nome do aluno: ")
        # Criamos um "dicionário" para guardar o número e o nome juntos
        novo_aluno = {"numero": numero_gerado, "nome": nome_aluno}
        
        pilha_alunos.append(novo_aluno) # append() coloca no topo da pilha
        print(f"Aluno {nome_aluno} cadastrado com o número {numero_gerado}!")
        
        numero_gerado += 1 # Aumenta 1 para o próximo aluno que for cadastrado
        
    # OPÇÃO 2: Cadastrar nota na Fila
    elif opcao == 2:
        numero_busca = int(input("Digite o número do aluno: "))
        
        # Primeiro, vamos ver se esse aluno existe na pilha
        aluno_existe = False
        for aluno in pilha_alunos:
            if aluno["numero"] == numero_busca:
                aluno_existe = True
                break
                
        if aluno_existe:
            nota = float(input("Digite a nota (entre 0 e 10): "))
            # Validação da nota
            if 0 <= nota <= 10:
                nova_nota = {"numero_aluno": numero_busca, "valor": nota}
                fila_notas.append(nova_nota) # append() coloca no final da fila
                print("Nota cadastrada com sucesso!")
            else:
                print("Erro: A nota precisa estar entre 0 e 10.")
        else:
            print("Erro: Aluno não cadastrado.")
            
    # OPÇÃO 3: Calcular média
    elif opcao == 3:
        numero_busca = int(input("Digite o número do aluno para ver a média: "))
        
        # Procurar o nome do aluno
        nome_encontrado = ""
        for aluno in pilha_alunos:
            if aluno["numero"] == numero_busca:
                nome_encontrado = aluno["nome"]
                break
                
        if nome_encontrado == "":
            print("Aviso: Aluno não encontrado.")
        else:
            soma_notas = 0.0
            quantidade_notas = 0
            
            # Percorrer a fila de notas procurando as notas desse aluno
            for nota in fila_notas:
                if nota["numero_aluno"] == numero_busca:
                    soma_notas += nota["valor"]
                    quantidade_notas += 1
                    
            if quantidade_notas > 0:
                media = soma_notas / quantidade_notas
                print(f"Aluno: {nome_encontrado} | Média: {media:.2f}")
            else:
                print(f"Aviso: O aluno {nome_encontrado} não possui notas cadastradas.")

    # OPÇÃO 4: Alunos sem notas
    elif opcao == 4:
        print("\n--- Alunos sem notas ---")
        encontrou_algum = False
        
        for aluno in pilha_alunos:
            tem_nota = False
            for nota in fila_notas:
                if nota["numero_aluno"] == aluno["numero"]:
                    tem_nota = True
                    break
                    
            if not tem_nota:
                print(f"- {aluno['nome']} (Número: {aluno['numero']})")
                encontrou_algum = True
                
        if not encontrou_algum:
            print("Todos os alunos cadastrados possuem notas.")

    # OPÇÃO 5: Excluir Aluno (Pilha)
    elif opcao == 5:
        if len(pilha_alunos) == 0:
            print("A pilha de alunos está vazia.")
        else:
            aluno_topo = pilha_alunos[-1] # Olha quem está no topo (o último da lista)
            
            # Verificar se ele tem notas na fila
            tem_nota = False
            for nota in fila_notas:
                if nota["numero_aluno"] == aluno_topo["numero"]:
                    tem_nota = True
                    break
                    
            if tem_nota:
                print(f"Erro: O aluno do topo ({aluno_topo['nome']}) possui notas e não pode ser excluído.")
            else:
                aluno_removido = pilha_alunos.pop() # .pop() tira do TOPO da pilha
                print(f"Aluno {aluno_removido['nome']} excluído com sucesso (saiu do topo da pilha).")

    # OPÇÃO 6: Excluir Nota (Fila)
    elif opcao == 6:
        if len(fila_notas) == 0:
            print("A fila de notas está vazia.")
        else:
            nota_removida = fila_notas.pop(0) # .pop(0) tira do INÍCIO da fila
            print(f"Nota {nota_removida['valor']} do aluno {nota_removida['numero_aluno']} excluída com sucesso (saiu do início da fila).")

    # OPÇÃO 7: Sair
    elif opcao == 7:
        print("Encerrando o sistema...")
        break
        
    else:
        print("Opção inválida.")