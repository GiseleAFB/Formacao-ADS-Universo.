# 1. CRIANDO AS LISTAS DE POLTRONAS (24 espaços cada)
# Tudo começa com 0 (todas as poltronas desocupadas)
janela = [0] * 24
corredor = [0] * 24

# 2. O MENU DE VENDAS
while True:
    print("\n==== VIAÇÃO UNIVERSO ====")
    print("1 - Comprar passagem na Janela")
    print("2 - Comprar passagem no Corredor")
    print("3 - Sair")
    
    # Primeiro, vamos checar se o ônibus está completamente cheio
    # Se a soma de todas as janelas (24) + todos os corredores (24) der 48, lotou!
    if sum(janela) + sum(corredor) == 48:
        print("Atenção: O ônibus está COMPLETAMENTE CHEIO!") # Avisa que lotou
    
    opcao = int(input("Escolha uma opção: "))
    
    # 3. COMPRANDO JANELA
    if opcao == 1:
        # Verifica se todas as janelas estão ocupadas (soma igual a 24)
        if sum(janela) == 24:
            print("Não existem poltronas livres nas janelas.")
        else:
            print("\nPoltronas disponíveis na JANELA:")
            # Mostra apenas as que têm o valor 0
            for i in range(24):
                if janela[i] == 0:
                    # Coloco i + 1 para o cliente ver a poltrona "1" em vez de "0"
                    print(f"Poltrona {i + 1}")
            
            escolha = int(input("Digite o número da poltrona que deseja: "))
            
            # Como mostramos i+1, temos que subtrair 1 para achar a "gaveta" certa na lista
            indice = escolha - 1
            
            # Verifica se o cliente digitou um número válido e se está vazia
            if 0 <= indice < 24 and janela[indice] == 0:
                janela[indice] = 1 # Muda para 1 (Ocupada)
                print("Passagem comprada com sucesso!")
            else:
                print("Poltrona inválida ou já ocupada.")

    # 4. COMPRANDO CORREDOR
    elif opcao == 2:
        # Verifica se todos os corredores estão ocupados
        if sum(corredor) == 24:
            print("Não existem poltronas livres no corredor.")
        else:
            print("\nPoltronas disponíveis no CORREDOR:")
            for i in range(24):
                if corredor[i] == 0:
                    print(f"Poltrona {i + 1}")
            
            escolha = int(input("Digite o número da poltrona que deseja: "))
            indice = escolha - 1
            
            if 0 <= indice < 24 and corredor[indice] == 0:
                corredor[indice] = 1 # Ocupa a poltrona
                print("Passagem comprada com sucesso!")
            else:
                print("Poltrona inválida ou já ocupada.")
                
    # 5. SAIR
    elif opcao == 3:
        print("Encerrando o sistema de vendas...")
        break
        
    else:
        print("Opção inválida.")