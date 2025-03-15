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
GREEN = (0, 255, 0)  # Ponto inicial
BLUE = (0, 0, 255)  # Ponto final
RED = (255, 0, 0)  # Obstáculo
GRAY = (200, 200, 200)  # Grade

# Inicializa pygame
pygame.init()
win = pygame.display.set_mode((WIDTH + INFO_AREA_WIDTH, HEIGHT))
pygame.display.set_caption("Tabuleiro com Obstáculos Variáveis")

# Criando a grade de pontos (vértices nas interseções)
points = [(row, col) for row in range(ROWS) for col in range(COLS)]

# Define o ponto inicial e final
start = (0, 0)  # Canto superior esquerdo
end = (ROWS - 1, COLS - 1)  # Canto inferior direito

# Definição do número mínimo e máximo de obstáculos
total_cells = ROWS * COLS
min_obstacles = int(total_cells * 0)  
max_obstacles = int(total_cells * 0.25)  
num_obstacles = random.randint(min_obstacles, max_obstacles)

def generate_obstacles(num):
    """Gera um conjunto de obstáculos sem sobreposição"""
    all_cells = [(r, c) for r in range(ROWS) for c in range(COLS) if (r, c) != start and (r, c) != end]
    random.shuffle(all_cells)
    num = min(num, len(all_cells))
    selected_cells = all_cells[:num]
    return set(selected_cells)

# Gera os obstáculos iniciais
obstacles = generate_obstacles(num_obstacles)

def draw_board():
    """Desenha o tabuleiro com linhas de grade"""
    win.fill(WHITE)
    for row in range(ROWS + 1):
        pygame.draw.line(win, GRAY, 
                         (MARGIN, MARGIN + row * GRID_SIZE), 
                         (WIDTH - MARGIN, MARGIN + row * GRID_SIZE))
    for col in range(COLS + 1):
        pygame.draw.line(win, GRAY, 
                         (MARGIN + col * GRID_SIZE, MARGIN), 
                         (MARGIN + col * GRID_SIZE, HEIGHT - MARGIN))

def draw_obstacles():
    """Desenha os obstáculos como quadrados"""
    for row, col in obstacles:
        x = MARGIN + col * GRID_SIZE
        y = MARGIN + row * GRID_SIZE
        pygame.draw.rect(win, RED, (x, y, GRID_SIZE, GRID_SIZE))

def draw_points():
    """Desenha os pontos iniciais e finais"""
    start_x = MARGIN + start[1] * GRID_SIZE
    start_y = MARGIN + start[0] * GRID_SIZE
    end_x = MARGIN + end[1] * GRID_SIZE
    end_y = MARGIN + end[0] * GRID_SIZE
    pygame.draw.circle(win, GREEN, (start_x, start_y), 8)
    pygame.draw.circle(win, BLUE, (end_x, end_y), 8)

def display_info():
    """Exibe informações sobre o número de obstáculos"""
    font = pygame.font.SysFont('Arial', 20)
    
    # Fundo da área de informações
    pygame.draw.rect(win, WHITE, (WIDTH, 0, INFO_AREA_WIDTH, HEIGHT))
    
    # Texto de título
    title = font.render("Controles:", True, BLACK)
    win.blit(title, (WIDTH + 20, 20))
    
    # Lista de instruções
    instructions = [
        "↑: Aumentar obstáculos",
        "↓: Diminuir obstáculos",
        "R: Regenerar obstáculos",
        "ESPAÇO: Aleatório",
        "Esc: Sair"
    ]
    
    for i, instruction in enumerate(instructions):
        text_surface = font.render(instruction, True, BLACK)
        win.blit(text_surface, (WIDTH + 20, 60 + 30 * i))
    
    # Contador de obstáculos
    percentage = len(obstacles) / total_cells * 100
    text = f'Obstáculos: {len(obstacles)} ({percentage:.1f}%)'
    text_surface = font.render(text, True, BLACK)
    win.blit(text_surface, (WIDTH + 20, HEIGHT - 50))

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
                        num_obstacles += 1
                        obstacles = generate_obstacles(num_obstacles)

                if event.key == pygame.K_DOWN:
                    if num_obstacles > min_obstacles:
                        num_obstacles -= 1
                        obstacles = generate_obstacles(num_obstacles)
                        
                if event.key == pygame.K_r:
                    obstacles = generate_obstacles(num_obstacles)
                    
                if event.key == pygame.K_SPACE:
                    num_obstacles = random.randint(min_obstacles, max_obstacles)
                    obstacles = generate_obstacles(num_obstacles)

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
