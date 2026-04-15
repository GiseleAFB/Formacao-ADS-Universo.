# 1. CRIANDO A NOSSA ESTRUTURA DE PILHA
class Pilha:
    # Quando criamos uma Pilha, ela começa como uma lista vazia e com um limite (capacidade)
    def __init__(self, capacidade):
        self.itens = []
        self.capacidade = capacidade

    # Função vazia: Retorna True se não tiver nada na lista
    def vazia(self):
        return len(self.itens) == 0

    # Função cheia: Retorna True se a lista atingiu o limite
    def cheia(self):
        return len(self.itens) >= self.capacidade

    # Função empilhar: Coloca um item no final da lista (no topo)
    def empilhar(self, item):
        if not self.cheia():
            self.itens.append(item)
        else:
            print("A pilha está cheia!")

    # Função desempilhar: Tira e retorna o último item da lista (o topo)
    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            return None

    # Função topo: Apenas olha quem está no topo, sem tirar ele de lá
    def topo(self):
        if not self.vazia():
            return self.itens[-1] # O índice -1 no Python pega o último elemento!
        else:
            return None


# 2. A FUNÇÃO DE CONTROLE DO DEPÓSITO
def chega_no_deposito(nova_caixa, pilha_A):
    # Criamos as pilhas auxiliares B e C com capacidade de sobra
    pilha_B = Pilha(20) # B é só para caixas de 5 toneladas
    pilha_C = Pilha(20) # C é só para caixas de 3 toneladas
    
    # PASSO A: Tirar as caixas menores do caminho
    # Enquanto a Pilha A não estiver vazia E a caixa no topo for mais leve que a nova...
    while not pilha_A.vazia() and pilha_A.topo() < nova_caixa:
        caixa_retirada = pilha_A.desempilhar() # Tiramos a caixa do caminho
        
        # Guardamos na pilha auxiliar certa
        if caixa_retirada == 5:
            pilha_B.empilhar(caixa_retirada)
        elif caixa_retirada == 3:
            pilha_C.empilhar(caixa_retirada)
            
    # PASSO B: O caminho está livre! Empilhamos a nova caixa pesada na Pilha A
    pilha_A.empilhar(nova_caixa)
    
    # PASSO C: Devolver as caixas menores para a Pilha A
    # Primeiro devolvemos as de 5 toneladas (Pilha B)
    while not pilha_B.vazia():
        pilha_A.empilhar(pilha_B.desempilhar())
        
    # Depois devolvemos as de 3 toneladas (Pilha C), para ficarem bem no topo
    while not pilha_C.vazia():
        pilha_A.empilhar(pilha_C.desempilhar())


# 3. TESTANDO O NOSSO PROGRAMA
# Vamos simular a chegada das caixas
pilha_principal = Pilha(20)

print("Chegou caixa de 5...")
chega_no_deposito(5, pilha_principal)
print("Estado da Pilha A:", pilha_principal.itens)

print("\nChegou caixa de 3...")
chega_no_deposito(3, pilha_principal)
print("Estado da Pilha A:", pilha_principal.itens)

# A MÁGICA ACONTECE AQUI:
print("\nChegou caixa de 7 (Essa é pesada, vai ter que remover a de 5 e a de 3 temporariamente)...")
chega_no_deposito(7, pilha_principal)
print("Estado da Pilha A:", pilha_principal.itens)

print("\nChegou caixa de 5...")
chega_no_deposito(5, pilha_principal)
print("Estado da Pilha A:", pilha_principal.itens)