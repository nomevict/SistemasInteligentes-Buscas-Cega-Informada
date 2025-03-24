import random
import math
import matplotlib.pyplot as plt
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
    tentativas = 0
    max_tentativas = largura_tabuleiro * altura_tabuleiro  # Definir o número máximo de tentativas baseado no tamanho do tabuleiro
    while len(obstaculos) < num_obstaculos:
        novo_x = random.uniform(0.5, largura_tabuleiro - 0.5)
        novo_y = random.uniform(0.5, altura_tabuleiro - 0.5)
        novo_obstaculo = (novo_x, novo_y)

        # Verifica colisões com obstáculos existentes, ponto inicial e ponto final
        colisao = any(calcular_distancia(novo_obstaculo, obst) < 1.5 for obst in obstaculos) or \
                  calcular_distancia(novo_obstaculo, ponto_inicial) < 1.5 or \
                  calcular_distancia(novo_obstaculo, ponto_final) < 1.5

        # Adiciona se não houver colisão
        if not colisao:
            obstaculos.append(novo_obstaculo)
        
        tentativas += 1

        # Verificar se há tentativas suficientes ou espaço suficiente no tabuleiro
        if tentativas > max_tentativas:  # Quando a quantidade de tentativas ultrapassa a capacidade do tabuleiro
            print("Espaço insuficiente para adicionar todos os obstáculos.")
            break

# Adicionar obstáculos de forma distribuída
adicionar_obstaculo()

# Exibir os obstáculos adicionados (apenas para teste)
print(f"Obstáculos adicionados: {len(obstaculos)}")

# Função para plotar o tabuleiro
def plotar_tabuleiro():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plota os obstáculos como quadrados azuis com tamanho 1
    for obstaculo in obstaculos:
        ax.add_patch(plt.Rectangle((obstaculo[0] - 0.5, obstaculo[1] - 0.5), 1, 1, color='blue'))

    # Plota o ponto inicial e final com a cor vermelha
    ax.add_patch(plt.Circle(ponto_inicial, 0.6, color='red'))  # Ponto inicial
    ax.add_patch(plt.Circle(ponto_final, 0.6, color='red'))    # Ponto final

    # Configura os eixos
    ax.set_xlim(0, largura_tabuleiro)
    ax.set_ylim(0, altura_tabuleiro)
    ax.set_aspect('equal')
    
    # Remove as grades internas, mantendo os eixos visíveis
    plt.grid(False)
    plt.axhline(color='black')  # Linha horizontal (eixo x)
    plt.axvline(color='black')  # Linha vertical (eixo y)

    # Função de zoom com o mouse
    def onselect(eclick, erelease):
        # Ajusta os limites dos eixos conforme a área selecionada
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        ax.set_xlim(min(x1, x2), max(x1, x2))
        ax.set_ylim(min(y1, y2), max(y1, y2))
        plt.draw()

    # Adiciona o widget de seleção de área para zoom
    rectangle_selector = RectangleSelector(ax, onselect, useblit=True, button=[1], minspanx=5, minspany=5, spancoords='pixels', interactive=True)

    plt.show()

# Plotar o tabuleiro com os obstáculos e ativar o zoom
plotar_tabuleiro()
