"""
função Busca_Gulosa(puzzle inicial, puzzle objetivo):

    fila = [puzzle inicial]

    visitados = conjunto vazio()

    

    função heurística(puzzle atual, puzzle objetivo):

        soma = 0

        para cada número em puzzle atual:

            posição atual = encontrar posição(puzzle atual, número)

            posição objetivo = encontrar posição(puzzle objetivo, número)

            soma = soma + calcular distância_manhattan(posição atual, posição objetivo)

        retorne soma

    

    enquanto fila não estiver vazia:

        estado atual = remover menor heurística(fila)

        se estado atual == puzzle objetivo:

            retorne caminho

        para cada movimento em movimentos possíveis(estado atual):

            novo estado = gerar novo estado(estado atual, movimento)

            se novo estado não foi visitado:

                fila.adicionar(novo estado)

                visitados.adicionar(novo estado)



    retorne "não há solução"



função encontrar posição(puzzle, número):

    para i de 0 até tamanho(puzzle) - 1:

        para j de 0 até tamanho(puzzle[i]) - 1:

            se puzzle[i][j] == número:

                retorne (i, j)

    retorne NULL



função calcular distância_manhattan(pos1, pos2):

    (linha1, coluna1) = pos1

    (linha2, coluna2) = pos2

    retorne |linha1 - linha2| + |coluna1 - coluna2|



função movimentos possíveis(puzzle):

    movimentos = []

    encontrar posição vazia (linha vazia, coluna vazia)

    para direção em ["Cima", "Baixo", "Esquerda", "Direita"]:

        novo puzzle = gerar novo estado(puzzle, direção, linha vazia, coluna vazia)

        se novo puzzle é válido e não foi visitado:

            movimentos.adicionar(novo puzzle)

    retorne movimentos



função gerar novo estado(puzzle, direção, linha vazia, coluna vazia):

    se direção == "Cima":

        nova linha = linha vazia - 1

        se nova linha >= 0:

            troca puzzle[linha vazia][coluna vazia] com puzzle[nova linha][coluna vazia]

    se direção == "Baixo":

        nova linha = linha vazia + 1

        se nova linha < tamanho(puzzle):

            troca puzzle[linha vazia][coluna vazia] com puzzle[nova linha][coluna vazia]

    se direção == "Esquerda":

        nova coluna = coluna vazia - 1

        se nova coluna >= 0:

            troca puzzle[linha vazia][coluna vazia] com puzzle[linha vazia][nova coluna]

    se direção == "Direita":

        nova coluna = coluna vazia + 1

        se nova coluna < tamanho(puzzle[linha vazia]):

            troca puzzle[linha vazia][coluna vazia] com puzzle[linha vazia][nova coluna]

    retorne puzzle



função principal:

    puzzle inicial = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

    puzzle objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    resultado = Busca_Gulosa(puzzle inicial, puzzle objetivo)

    imprima resultado
"""