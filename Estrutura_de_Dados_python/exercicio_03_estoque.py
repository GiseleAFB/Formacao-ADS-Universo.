# 1. CRIANDO AS LISTAS (10 posições cada) 
codigos_produtos = [0] * 10
estoque_produtos = [0] * 10

# Vamos cadastrar dois produtos para facilitar os testes
codigos_produtos[0] = 555
estoque_produtos[0] = 20  # O produto 555 tem 20 unidades

codigos_produtos[1] = 777
estoque_produtos[1] = 5   # O produto 777 tem 5 unidades

print("==== SISTEMA DE CONTROLE DE ESTOQUE ====")
print("Dica: Para encerrar o sistema, digite 0 no Código do Cliente.\n")

# 2. O LAÇO DE PEDIDOS [cite: 80]
while True:
    codigo_cliente = int(input("\nDigite o código do cliente (ou 0 para sair): "))
    
    # Condição de parada: se for 0, quebra o laço 
    if codigo_cliente == 0:
        print("Encerrando as vendas...\n")
        break
        
    codigo_produto = int(input("Digite o código do produto: "))
    quantidade_pedida = int(input("Digite a quantidade desejada: "))
    
    encontrou_produto = False
    
    # 3. VERIFICANDO O PRODUTO E O ESTOQUE
    for i in range(10):
        # Se achou o produto na lista 
        if codigos_produtos[i] == codigo_produto:
            encontrou_produto = True
            
            # Verifica se tem estoque suficiente para atender integralmente 
            if estoque_produtos[i] >= quantidade_pedida:
                # Atualiza o estoque 
                estoque_produtos[i] = estoque_produtos[i] - quantidade_pedida
                print("Pedido atendido. Obrigado e volte sempre.") # 
            else:
                print("Não temos estoque suficiente desta mercadoria.") # 
                
            break # Já achou e resolveu, pode parar de procurar na lista
            
    # Se o laço for terminou e a bandeira continuar False 
    if encontrou_produto == False:
        print("Código inexistente.") # 


# 4. RELATÓRIO FINAL 
print("==== RELATÓRIO FINAL DE ESTOQUE ====")
for i in range(10):
    # Imprime apenas os produtos que foram cadastrados (código diferente de 0)
    if codigos_produtos[i] != 0:
        print(f"Produto Código: {codigos_produtos[i]} | Estoque Atualizado: {estoque_produtos[i]}") #