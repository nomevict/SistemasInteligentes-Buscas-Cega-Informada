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
GREEN = (34, 139, 34)  # Verde mais escuro para o ponto inicial
BLUE = (25, 25, 112)   # Azul marinho para o ponto final
RED = (220, 20, 60)    # Vermelho crimson para obstáculos
GRAY = (200, 200, 200) # Grade
LIGHT_BLUE = (173, 216, 230)  # Cor de fundo do tabuleiro
DARK_GRAY = (105, 105, 105)   # Cor para bordas

# Inicializa pygame
pygame.init()
win = pygame.display.set_mode((WIDTH + INFO_AREA_WIDTH, HEIGHT))
pygame.display.set_caption("Tabuleiro com Obstáculos Variáveis")

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
    """Desenha o tabuleiro com linhas de grade e fundo estilizado"""
    win.fill(WHITE)
    
    # Desenha o fundo do tabuleiro
    pygame.draw.rect(win, LIGHT_BLUE, 
                    (MARGIN - 5, MARGIN - 5, 
                     GRID_SIZE * COLS + 10, GRID_SIZE * ROWS + 10))
    
    # Desenha a borda do tabuleiro
    pygame.draw.rect(win, DARK_GRAY, 
                    (MARGIN - 5, MARGIN - 5, 
                     GRID_SIZE * COLS + 10, GRID_SIZE * ROWS + 10), 3)
    
    # Desenha as linhas da grade
    for row in range(ROWS + 1):
        pygame.draw.line(win, GRAY, 
                         (MARGIN, MARGIN + row * GRID_SIZE), 
                         (MARGIN + COLS * GRID_SIZE, MARGIN + row * GRID_SIZE))
    for col in range(COLS + 1):
        pygame.draw.line(win, GRAY, 
                         (MARGIN + col * GRID_SIZE, MARGIN), 
                         (MARGIN + col * GRID_SIZE, MARGIN + ROWS * GRID_SIZE))
    
    # Desenha o padrão de tabuleiro de xadrez
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                x = MARGIN + col * GRID_SIZE + 1
                y = MARGIN + row * GRID_SIZE + 1
                pygame.draw.rect(win, (240, 248, 255), (x, y, GRID_SIZE - 1, GRID_SIZE - 1))

def draw_obstacles():
    """Desenha os obstáculos como quadrados com efeito de sombra"""
    for row, col in obstacles:
        x = MARGIN + col * GRID_SIZE + 2
        y = MARGIN + row * GRID_SIZE + 2
        
        # Sombra para efeito 3D
        pygame.draw.rect(win, (139, 0, 0), (x + 3, y + 3, GRID_SIZE - 5, GRID_SIZE - 5))
        pygame.draw.rect(win, RED, (x, y, GRID_SIZE - 4, GRID_SIZE - 4))

def draw_points():
    """Desenha os pontos iniciais e finais com efeito de brilho"""
    start_x = MARGIN + start[1] * GRID_SIZE + GRID_SIZE // 2
    start_y = MARGIN + start[0] * GRID_SIZE + GRID_SIZE // 2
    end_x = MARGIN + end[1] * GRID_SIZE + GRID_SIZE // 2
    end_y = MARGIN + end[0] * GRID_SIZE + GRID_SIZE // 2
    
    # Efeito de brilho (círculos concêntricos)
    pygame.draw.circle(win, (144, 238, 144), (start_x, start_y), 14)
    pygame.draw.circle(win, GREEN, (start_x, start_y), 10)
    
    pygame.draw.circle(win, (70, 130, 180), (end_x, end_y), 14)
    pygame.draw.circle(win, BLUE, (end_x, end_y), 10)

def display_info():
    """Exibe informações sobre o número de obstáculos com estilo melhorado"""
    # Fundo da área de informações
    pygame.draw.rect(win, (245, 245, 245), 
                    (WIDTH, 0, INFO_AREA_WIDTH, HEIGHT))
    pygame.draw.line(win, DARK_GRAY, (WIDTH, 0), (WIDTH, HEIGHT), 2)
    
    # Título
    title = title_font.render("Controles:", True, (50, 50, 50))
    win.blit(title, (WIDTH + 20, 30))
    
    # Linha decorativa abaixo do título
    pygame.draw.line(win, DARK_GRAY, 
                     (WIDTH + 20, 65), 
                     (WIDTH + INFO_AREA_WIDTH - 20, 65), 2)
    
    # Lista de instruções com ícones
    instructions = [
        ("↑: Aumentar obstáculos", GREEN),
        ("↓: Diminuir obstáculos", RED),
        ("R: Regenerar obstáculos", BLUE),
        ("ESPAÇO: Aleatório", (128, 0, 128)),  # Roxo
        ("Esc: Sair", DARK_GRAY)
    ]
    
    for i, (instruction, color) in enumerate(instructions):
        # Desenha um pequeno ícone
        pygame.draw.rect(win, color, (WIDTH + 20, 85 + 35 * i, 10, 10))
        
        # Texto da instrução
        text_surface = info_font.render(instruction, True, BLACK)
        win.blit(text_surface, (WIDTH + 40, 80 + 35 * i))
    
    # Contador de obstáculos em um quadro destacado
    pygame.draw.rect(win, (230, 230, 250), 
                    (WIDTH + 15, HEIGHT - 80, INFO_AREA_WIDTH - 30, 60), 
                    border_radius=5)
    
    percentage = len(obstacles) / total_cells * 100
    obstacle_text = f'Obstáculos: {len(obstacles)}'
    percentage_text = f'({percentage:.1f}%)'
    
    text_surface1 = counter_font.render(obstacle_text, True, (70, 70, 70))
    text_surface2 = counter_font.render(percentage_text, True, (70, 70, 70))
    
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