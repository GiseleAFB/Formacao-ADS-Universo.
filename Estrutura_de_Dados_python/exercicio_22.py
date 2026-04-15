# 1. CRIANDO AS LISTAS (10 posições cada)
codigos = [0] * 10
saldos = [0.0] * 10

# Vamos cadastrar três contas iniciais para a gente conseguir testar o programa
codigos[0] = 123
saldos[0] = 500.0   # A conta 123 tem R$ 500,00

codigos[1] = 456
saldos[1] = 1000.0  # A conta 456 tem R$ 1000,00

codigos[2] = 789
saldos[2] = 50.0    # A conta 789 tem R$ 50,00

# 2. O MENU PRINCIPAL
# O programa só termina quando for digitada a opção 4[cite: 40].
while True:
    print("\n==== CONTROLE BANCÁRIO ====")
    print("1. Efetuar depósito")
    print("2. Efetuar saque")
    print("3. Consultar o ativo bancário")
    print("4. Finalizar o programa")
    
    opcao = int(input("Escolha uma opção: "))
    
    # 3. LÓGICA DO DEPÓSITO
    if opcao == 1:
        conta_deposito = int(input("Digite o código da conta para depósito: "))
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        encontrou_conta = False
        
        # Procurando a conta na lista
        for i in range(10):
            if codigos[i] == conta_deposito:
                saldos[i] = saldos[i] + valor_deposito # Atualiza o saldo [cite: 31]
                print(f"Depósito realizado! Novo saldo: R$ {saldos[i]:.2f}")
                encontrou_conta = True
                break
                
        if encontrou_conta == False:
            print("Conta não encontrada.") [cite: 30]

    # 4. LÓGICA DO SAQUE
    elif opcao == 2:
        conta_saque = int(input("Digite o código da conta para saque: "))
        valor_saque = float(input("Digite o valor a ser sacado: "))
        encontrou_conta = False
        
        for i in range(10):
            if codigos[i] == conta_saque:
                encontrou_conta = True
                # Verifica se o saldo é suficiente para cobrir o saque [cite: 34]
                if saldos[i] >= valor_saque:
                    saldos[i] = saldos[i] - valor_saque # Realiza o saque [cite: 36]
                    print(f"Saque realizado! Novo saldo: R$ {saldos[i]:.2f}")
                else:
                    print("Saldo insuficiente.") [cite: 37]
                break
                
        if encontrou_conta == False:
            print("Conta não encontrada.") [cite: 33]

    # 5. LÓGICA DO ATIVO BANCÁRIO
    elif opcao == 3:
        # Para consultar o ativo, somamos o saldo de todas as contas [cite: 38]
        soma_total = 0.0
        for i in range(10):
            soma_total = soma_total + saldos[i]
            
        print(f"O ativo bancário total (soma de todos os saldos) é: R$ {soma_total:.2f}")

    # 6. FINALIZAR
    elif opcao == 4:
        print("Finalizando o programa bancário...")
        break
        
    else:
        print("Opção inválida. Escolha um número de 1 a 4.")