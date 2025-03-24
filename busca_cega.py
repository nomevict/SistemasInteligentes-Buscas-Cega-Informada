from collections import deque

OBJETIVO = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Função para encontrar a posição do espaço vazio (0)
def encontrar_espaco(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                return i, j
    return -1, -1

# Função para comparar o estado atual com o estado objetivo
def comparativo(atual):
    return atual == OBJETIVO

# Movimentos possíveis: cima, baixo, esquerda, direita
movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Função para gerar novos estados a partir de um estado dado
def gerar_estados(atual):
    i, j = encontrar_espaco(atual)
    novos_estados = []
    for movimento in movimentos:
        novo_i, novo_j = i + movimento[0], j + movimento[1]
        if 0 <= novo_i < 3 and 0 <= novo_j < 3:
            novo_tabuleiro = [linha[:] for linha in atual]
            novo_tabuleiro[i][j], novo_tabuleiro[novo_i][novo_j] = novo_tabuleiro[novo_i][novo_j], novo_tabuleiro[i][j]
            novos_estados.append(novo_tabuleiro)
    return novos_estados

# Função de busca em largura (BFS)
def busca_largura(inicial):
    fila = deque([(inicial, [])])  # Fila com o estado e o caminho percorrido
    visitados = set()
    visitados.add(str(inicial))
    while fila:
        estado, caminho = fila.popleft()
        if comparativo(estado):
            return caminho
        for novo_estado in gerar_estados(estado):
            estado_str = str(novo_estado)
            if estado_str not in visitados:
                visitados.add(estado_str)
                fila.append((novo_estado, caminho + [novo_estado]))
    return None

# Estado inicial fornecido
inicial = [[8, 6, 0], [5, 4, 7], [2, 3, 1]]

# Executa a busca e imprime o resultado
resultado = busca_largura(inicial)
if resultado:
    print("Solução encontrada com {} movimentos: ".format(len(resultado)))
    for passo in resultado:
        for linha in passo:
            print(linha)
        print("-")
else:
    print("Nenhuma solução encontrada.")
