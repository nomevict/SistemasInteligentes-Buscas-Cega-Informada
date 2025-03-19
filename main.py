import matplotlib.pyplot as plt 
import random
import math
from matplotlib.widgets import RectangleSelector

# Configuração do tabuleiro
largura_tabuleiro = int(input("Digite a largura do tabuleiro: "))
altura_tabuleiro = int(input("Digite a altura do tabuleiro: "))
num_obstaculos = int(input("Digite a quantidade de obstáculos: "))

# Ponto inicial e final
ponto_inicial = (0, 0)
ponto_final = (largura_tabuleiro - 1, altura_tabuleiro - 1)

# Lista para armazenar os obstáculos
obstaculos = []

# Função para calcular a distância entre dois pontos
def calcular_distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Função para adicionar obstáculos respeitando a distância mínima e limites do tabuleiro
def adicionar_obstaculo():
    while len(obstaculos) < num_obstaculos:
        novo_x = random.uniform(0, largura_tabuleiro - 1)
        novo_y = random.uniform(0, altura_tabuleiro - 1)
        novo_obstaculo = (novo_x, novo_y)
        
        # Verifica se o novo obstáculo está a uma distância aceitável dos outros
        # e se está dentro dos limites do tabuleiro
        # Garante que o obstáculo não se sobreponha ao ponto inicial ou final
        if all(calcular_distancia(novo_obstaculo, obst) > 1 for obst in obstaculos) and \
           0 <= novo_x < largura_tabuleiro and 0 <= novo_y < altura_tabuleiro and \
           calcular_distancia(novo_obstaculo, ponto_inicial) > 1 and \
           calcular_distancia(novo_obstaculo, ponto_final) > 1:
            obstaculos.append(novo_obstaculo)

# Adicionar obstáculos de forma distribuída
adicionar_obstaculo()

# Função para plotar o tabuleiro
def plotar_tabuleiro():
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Plota os obstáculos como quadrados azuis com tamanho 1
    for obstaculo in obstaculos:
        # Garante que o obstáculo não saia dos limites do tabuleiro
        if 0 <= obstaculo[0] < largura_tabuleiro and 0 <= obstaculo[1] < altura_tabuleiro:
            ax.add_patch(plt.Rectangle((obstaculo[0] - 0.5, obstaculo[1] - 0.5), 1, 1, color='blue'))
    
    # Plota o ponto inicial e final com a cor vermelha (aumentando o tamanho do círculo)
    ax.add_patch(plt.Circle(ponto_inicial, 0.6, color='red'))  # Ponto inicial em vermelho, maior
    ax.add_patch(plt.Circle(ponto_final, 0.6, color='red'))    # Ponto final em vermelho, maior
    
    ax.set_xlim(0, largura_tabuleiro)
    ax.set_ylim(0, altura_tabuleiro)
    ax.set_aspect('equal')
    plt.grid(True)

    # Permite interação para selecionar o zoom
    def onselect(eclick, erelease):
        xmin, xmax = sorted([eclick.xdata, erelease.xdata])
        ymin, ymax = sorted([eclick.ydata, erelease.ydata])
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
        plt.draw()

    # Cria um "zoom" interativo
    selector = RectangleSelector(ax, onselect, useblit=True, button=[1])

    plt.show()

# Plotar o tabuleiro com os obstáculos
plotar_tabuleiro()
