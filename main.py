import matplotlib.pyplot as plt
import random

# Configuração do tabuleiro
ROWS, COLS = 30, 30  # Número de linhas e colunas
GRID_SIZE = 600 // COLS  # Tamanho dos quadrados do tabuleiro (unidade de distância no gráfico)

# Definição do número mínimo e máximo de obstáculos
total_cells = ROWS * COLS
min_obstacles = 0  
max_obstacles = total_cells - 2  # O número máximo de obstáculos é o total de células menos os pontos inicial e final
num_obstacles = 0  # Começando com 0 obstáculos

# Lista de todas as células disponíveis (excluindo início e fim)
start = (0, 0)  # Ponto inicial
end = (ROWS - 1, COLS - 1)  # Ponto final
all_available_cells = [(r, c) for r in range(ROWS) for c in range(COLS) if (r, c) != start and (r, c) != end]
random.shuffle(all_available_cells)

# Lista para manter ordem dos obstáculos adicionados
obstacles = []

def get_neighbors(cell):
    """Retorna todas as células vizinhas que compartilham pelo menos um vértice"""
    row, col = cell
    neighbors = []
    
    # Verificar células que compartilham vértices nos 4 lados
    directions = [
        (row-1, col), (row+1, col),  # Norte e Sul
        (row, col-1), (row, col+1),  # Oeste e Leste
        (row-1, col-1), (row-1, col+1),  # Noroeste e Nordeste
        (row+1, col-1), (row+1, col+1)   # Sudoeste e Sudeste
    ]
    
    # Filtrar apenas células válidas dentro do tabuleiro
    for r, c in directions:
        if 0 <= r < ROWS and 0 <= c < COLS:
            neighbors.append((r, c))
            
    return neighbors

def add_obstacle():
    """Adiciona um novo obstáculo sem compartilhar vértices com os existentes"""
    global obstacles, all_available_cells
    
    # Obtém todas as células que já são obstáculos ou são vizinhas de obstáculos
    invalid_cells = set(obstacles)
    for obstacle in obstacles:
        invalid_cells.update(get_neighbors(obstacle))
    
    # Filtra células disponíveis que não são inválidas
    valid_cells = [cell for cell in all_available_cells 
                  if cell not in invalid_cells 
                  and cell != start and cell != end]
    
    if valid_cells:
        # Escolhe uma célula aleatória das disponíveis
        new_obstacle = random.choice(valid_cells)
        obstacles.append(new_obstacle)
        return True
    return False

def regenerate_obstacles():
    """Regenera obstáculos sem compartilhar vértices, até o máximo possível"""
    global obstacles, all_available_cells
    
    # Reseta a lista de obstáculos
    obstacles = []
    
    # Reseta a lista de células disponíveis e embaralha
    all_available_cells = [(r, c) for r in range(ROWS) for c in range(COLS) 
                          if (r, c) != start and (r, c) != end]
    random.shuffle(all_available_cells)
    
    # Adiciona obstáculos um por um, respeitando a restrição de vértices
    while add_obstacle():
        if len(obstacles) >= max_obstacles:
            break  # Para quando atingir o máximo possível de obstáculos

def plot_board():
    """Plota o tabuleiro com obstáculos"""
    fig, ax = plt.subplots(figsize=(12, 12))  # Aumenta o tamanho do gráfico

    # Desenha os quadrados do tabuleiro
    for row in range(ROWS):
        for col in range(COLS):
            ax.add_patch(plt.Rectangle((col, row), GRID_SIZE, GRID_SIZE, edgecolor='gray', facecolor='white'))

    # Desenha os obstáculos como quadrados vermelhos, com tamanho ajustado
    for row, col in obstacles:
        ax.add_patch(plt.Rectangle((col + 0.1, row + 0.1), 0.8, 0.8, edgecolor='red', facecolor='red'))  # Ajusta o tamanho e o espaçamento dos obstáculos

    # Desenha o ponto inicial sobre o vértice
    ax.add_patch(plt.Circle((start[1], start[0]), 0.4, color='green'))  # O ponto inicial é no vértice (0, 0)

    # Desenha o ponto final sobre o vértice da última célula (canto inferior direito)
    ax.add_patch(plt.Circle((end[1], end[0]), 0.4, color='blue'))  # O ponto final é no vértice (ROWS-1, COLS-1)

    # Ajusta os limites e o grid
    ax.set_xlim(0, COLS)
    ax.set_ylim(0, ROWS)
    
    # Ajuste os vértices para que fiquem nas bordas (extremos das células)
    ax.set_xticks([x for x in range(COLS + 1)])  # Coloca os números nas bordas dos quadrados
    ax.set_yticks([y for y in range(ROWS + 1)])  # Coloca os números nas bordas dos quadrados
    ax.set_aspect('equal')
    ax.invert_yaxis()  # Inverte o eixo Y para que (0, 0) fique no canto superior esquerdo

    # Exibe o gráfico
    plt.grid(True)
    
    # Ajuste dinâmico para os valores dos eixos
    ax.set_xticklabels(range(COLS + 1), fontsize=8)  # Ajusta para que as labels comecem de 0 a COLS
    ax.set_yticklabels(range(ROWS + 1), fontsize=8, rotation=0, verticalalignment='center', horizontalalignment='right')  # Ajusta para que as labels comecem de 0 a ROWS

    plt.show()

# Regenerar o máximo de obstáculos possível respeitando as restrições
regenerate_obstacles()

# Plotar o tabuleiro
plot_board()
