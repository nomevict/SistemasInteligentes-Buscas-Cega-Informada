import pygame
import random

# Configuração do tabuleiro
WIDTH, HEIGHT = 800, 800  # Tamanho da tela
ROWS, COLS = 8, 8
GRID_SIZE = 600 // COLS  # Tamanho dos quadrados do tabuleiro
MARGIN = 50  # Margem ao redor do tabuleiro
INFO_AREA_WIDTH = 200  # Largura da área de informações

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)     # Verde mais escuro para o ponto inicial
BLUE = (25, 25, 112)      # Azul marinho para o ponto final
RED = (220, 20, 60)       # Vermelho crimson para obstáculos
GRAY = (180, 180, 180)    # Grade - um pouco mais suave
DARK_GRAY = (105, 105, 105)  # Cor para detalhes

# Inicializa pygame
pygame.init()
win = pygame.display.set_mode((WIDTH + INFO_AREA_WIDTH, HEIGHT))
pygame.display.set_caption("Tabuleiro com Obstáculos Incrementais")

# Fontes
title_font = pygame.font.SysFont('Arial', 24, bold=True)
info_font = pygame.font.SysFont('Arial', 20)
counter_font = pygame.font.SysFont('Arial', 22, bold=True)

# Criando a grade de pontos (vértices nas interseções)
points = [(row, col) for row in range(ROWS) for col in range(COLS)]

# Define o ponto inicial e final
start = (0, 0)  # Canto superior esquerdo
end = (ROWS - 1, COLS - 1)  # Canto inferior direito

# Definição do número mínimo e máximo de obstáculos
total_cells = ROWS * COLS
min_obstacles = 0  
max_obstacles = int(total_cells * 0.25)  
num_obstacles = 0  # Começando com 0 obstáculos

# Lista de todas as células disponíveis (excluindo início e fim)
all_available_cells = [(r, c) for r in range(ROWS) for c in range(COLS) 
                      if (r, c) != start and (r, c) != end]
random.shuffle(all_available_cells)

# Lista para manter ordem dos obstáculos adicionados
obstacles = []

def get_neighbors(cell):
    """Retorna todas as células vizinhas que compartilham pelo menos um vértice"""
    row, col = cell
    neighbors = []
    
    # Verificar células que compartilham vértices nos 4 lados
    # Norte, Sul, Leste, Oeste
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

def remove_obstacle():
    """Remove o último obstáculo adicionado"""
    global obstacles
    
    if obstacles:
        obstacles.pop()
        return True
    return False

def regenerate_obstacles(num):
    """Regenera todos os obstáculos sem compartilhar vértices"""
    global obstacles, all_available_cells
    
    # Reseta a lista de obstáculos
    obstacles = []
    
    # Reseta a lista de células disponíveis e embaralha
    all_available_cells = [(r, c) for r in range(ROWS) for c in range(COLS) 
                          if (r, c) != start and (r, c) != end]
    random.shuffle(all_available_cells)
    
    # Adiciona obstáculos um por um, respeitando a restrição de vértices
    for _ in range(num):
        if not add_obstacle():
            break  # Para se não conseguir adicionar mais obstáculos

def draw_board():
    """Desenha o tabuleiro com fundo branco e linhas de grade"""
    win.fill(WHITE)
    
    # Desenha a borda do tabuleiro
    pygame.draw.rect(win, DARK_GRAY, 
                    (MARGIN - 3, MARGIN - 3, 
                     GRID_SIZE * COLS + 6, GRID_SIZE * ROWS + 6), 2)
    
    # Desenha as linhas da grade
    for row in range(ROWS + 1):
        pygame.draw.line(win, GRAY, 
                         (MARGIN, MARGIN + row * GRID_SIZE), 
                         (MARGIN + COLS * GRID_SIZE, MARGIN + row * GRID_SIZE), 2)
    for col in range(COLS + 1):
        pygame.draw.line(win, GRAY, 
                         (MARGIN + col * GRID_SIZE, MARGIN), 
                         (MARGIN + col * GRID_SIZE, MARGIN + ROWS * GRID_SIZE), 2)
    
    # Desenha os vértices (pontos de interseção)
    for row in range(ROWS + 1):
        for col in range(COLS + 1):
            x = MARGIN + col * GRID_SIZE
            y = MARGIN + row * GRID_SIZE
            pygame.draw.circle(win, BLACK, (x, y), 4)

def draw_obstacles():
    """Desenha os obstáculos como quadrados com borda suave"""
    for row, col in obstacles:
        x = MARGIN + col * GRID_SIZE + 2
        y = MARGIN + row * GRID_SIZE + 2
        
        # Desenha o obstáculo com borda suave
        pygame.draw.rect(win, RED, (x, y, GRID_SIZE - 4, GRID_SIZE - 4), border_radius=3)
        
        # Adiciona um contorno mais escuro
        pygame.draw.rect(win, (139, 0, 0), (x, y, GRID_SIZE - 4, GRID_SIZE - 4), 2, border_radius=3)

def draw_points():
    """Desenha os pontos iniciais e finais com efeito de brilho"""
    start_x = MARGIN + start[1] * GRID_SIZE 
    start_y = MARGIN + start[0] * GRID_SIZE
    end_x = MARGIN + end[1] * GRID_SIZE
    end_y = MARGIN + end[0] * GRID_SIZE
    
    # Ponto inicial com efeito de brilho
    pygame.draw.circle(win, (144, 238, 144), (start_x, start_y), 12)
    pygame.draw.circle(win, GREEN, (start_x, start_y), 8)
    
    # Ponto final com efeito de brilho
    pygame.draw.circle(win, (70, 130, 180), (end_x, end_y), 12)
    pygame.draw.circle(win, BLUE, (end_x, end_y), 8)

def display_info():
    """Exibe informações sobre o número de obstáculos com estilo melhorado"""
    # Fundo da área de informações
    pygame.draw.rect(win, WHITE, (WIDTH, 0, INFO_AREA_WIDTH, HEIGHT))
    pygame.draw.line(win, DARK_GRAY, (WIDTH, 0), (WIDTH, HEIGHT), 2)
    
    # Título com fundo sutil
    pygame.draw.rect(win, (245, 245, 245), (WIDTH + 10, 15, INFO_AREA_WIDTH - 20, 40), border_radius=5)
    title = title_font.render("Controles:", True, (50, 50, 50))
    win.blit(title, (WIDTH + 20, 22))
    
    # Linha decorativa abaixo do título
    pygame.draw.line(win, DARK_GRAY, 
                     (WIDTH + 20, 65), 
                     (WIDTH + INFO_AREA_WIDTH - 20, 65), 1)
    
    # Lista de instruções com ícones
    instructions = [
        ("↑: Adicionar obstáculo", GREEN),
        ("↓: Remover obstáculo", RED),
        ("R: Regenerar todos", BLUE),
        ("ESPAÇO: Aleatório", (128, 0, 128)),  # Roxo
        ("Esc: Sair", DARK_GRAY)
    ]
    
    for i, (instruction, color) in enumerate(instructions):
        # Desenha um pequeno círculo como ícone
        pygame.draw.circle(win, color, (WIDTH + 25, 95 + 35 * i), 6)
        
        # Texto da instrução
        text_surface = info_font.render(instruction, True, BLACK)
        win.blit(text_surface, (WIDTH + 40, 85 + 35 * i))
    
    # Contador de obstáculos em um quadro com borda suave
    pygame.draw.rect(win, (245, 245, 245), 
                    (WIDTH + 15, HEIGHT - 80, INFO_AREA_WIDTH - 30, 60), 
                    border_radius=5)
    pygame.draw.rect(win, DARK_GRAY, 
                    (WIDTH + 15, HEIGHT - 80, INFO_AREA_WIDTH - 30, 60), 
                    1, border_radius=5)
    
    percentage = len(obstacles) / total_cells * 100
    obstacle_text = f'Obstáculos: {len(obstacles)}'
    percentage_text = f'({percentage:.1f}%)'
    
    text_surface1 = counter_font.render(obstacle_text, True, (70, 70, 70))
    text_surface2 = info_font.render(percentage_text, True, (70, 70, 70))
    
    win.blit(text_surface1, (WIDTH + 25, HEIGHT - 70))
    win.blit(text_surface2, (WIDTH + 25, HEIGHT - 40))

def main():
    global num_obstacles, obstacles
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(30)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Ajustar quantidade de obstáculos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if num_obstacles < max_obstacles:
                        if add_obstacle():
                            num_obstacles += 1

                if event.key == pygame.K_DOWN:
                    if num_obstacles > min_obstacles:
                        if remove_obstacle():
                            num_obstacles -= 1
                        
                if event.key == pygame.K_r:
                    num_obstacles = len(obstacles)  # Mantém o mesmo número
                    regenerate_obstacles(num_obstacles)
                    
                if event.key == pygame.K_SPACE:
                    num_obstacles = random.randint(min_obstacles, max_obstacles)
                    regenerate_obstacles(num_obstacles)

                if event.key == pygame.K_ESCAPE:
                    run = False

        draw_board()
        draw_obstacles()
        draw_points()
        display_info()
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()