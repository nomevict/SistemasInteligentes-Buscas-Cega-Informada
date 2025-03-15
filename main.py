import pygame
import random

# Configuração do tabuleiro
WIDTH, HEIGHT = 700, 700  # Tamanho da tela considerando a margem
ROWS, COLS = 8, 8
GRID_SIZE = 600 // COLS  # Tamanho dos quadrados do tabuleiro
MARGIN = 50  # Margem ao redor do tabuleiro

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Ponto inicial
BLUE = (0, 0, 255)  # Ponto final
RED = (255, 0, 0)  # Obstáculo
GRAY = (200, 200, 200)  # Grade

# Inicializa pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tabuleiro com Obstáculos")

# Criando a grade de pontos (vértices nas interseções)
points = [(row, col) for row in range(ROWS + 1) for col in range(COLS + 1)]

# Define o ponto inicial e final
start = (0, 0)  # Canto superior esquerdo
end = (ROWS, COLS)  # Canto inferior direito

# Gera obstáculos sem sobreposição nem colados
num_obstacles = 6  # Número de obstáculos a serem gerados
obstacles = set()

while len(obstacles) < num_obstacles:
    row = random.randint(0, ROWS - 2)
    col = random.randint(0, COLS - 2)
    
    # Verifica se o obstáculo colide ou está colado com outro
    is_valid = True
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if (r, c) in obstacles:
                is_valid = False
                break
        if not is_valid:
            break
    
    if is_valid:
        obstacles.add((row, col))

def draw_board():
    """Desenha o tabuleiro com linhas de grade"""
    win.fill(WHITE)
    for row in range(ROWS + 1):
        pygame.draw.line(win, GRAY, 
                         (MARGIN, MARGIN + row * GRID_SIZE), 
                         (WIDTH - MARGIN, MARGIN + row * GRID_SIZE))  # Linhas horizontais
    for col in range(COLS + 1):
        pygame.draw.line(win, GRAY, 
                         (MARGIN + col * GRID_SIZE, MARGIN), 
                         (MARGIN + col * GRID_SIZE, HEIGHT - MARGIN))  # Linhas verticais

def draw_obstacles():
    """Desenha os obstáculos como quadrados e coloca as arestas em vermelho"""
    for row, col in obstacles:
        x = MARGIN + col * GRID_SIZE
        y = MARGIN + row * GRID_SIZE
        pygame.draw.rect(win, WHITE, (x, y, GRID_SIZE, GRID_SIZE))  # Fundo branco
        pygame.draw.line(win, RED, (x, y), (x + GRID_SIZE, y), 3)  # Topo
        pygame.draw.line(win, RED, (x, y), (x, y + GRID_SIZE), 3)  # Esquerda
        pygame.draw.line(win, RED, (x + GRID_SIZE, y), (x + GRID_SIZE, y + GRID_SIZE), 3)  # Direita
        pygame.draw.line(win, RED, (x, y + GRID_SIZE), (x + GRID_SIZE, y + GRID_SIZE), 3)  # Base

def draw_points():
    """Desenha os pontos nas interseções das linhas do tabuleiro"""
    for row, col in points:
        color = GREEN if (row, col) == start else BLUE if (row, col) == end else BLACK
        pygame.draw.circle(win, color, 
                           (MARGIN + col * GRID_SIZE, MARGIN + row * GRID_SIZE), 5)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_board()
        draw_obstacles()
        draw_points()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
