# sisIntTabuleiro

# Topicos Principais
- Traçar uma rota na qual tem INICIO e FIM. Terá obstaculos no caminho que deverá ser desviados.
- Caso esteja enxergando o ponto final. Ir direto pra ele
- Caso não esteja enxergando, vai ter que navegar pelos vertices até chegar ao destino.

# Restrições
1. Você so poderá sair de um vertice para o outro.
2. Terá que andar em linha reta a qualquer ponto que estará visivel ao ponto de partida.
3. Não pode atravessar um obstaculo.

# Como Fazer pra ver se está atravessando um obstaculo?
- voces vão ter que interpretar esses pontos(pontos dos obstaculos) como retas.
- tem que calcular se um segmento de reta, Faz interceção com outro segmento de reta
- existe uma equação que calcula se um segmento de reta A e outro segmento de reta B tem uma intercação.(basicamente calcular um determinante)

# parâmetros
1. Um ponto INICIAL e um ponto FINAL. (fixos)
2. Quantidade de obstaculos (variavel)
3. Desenhar os obstaculos em locais aleatórios, e um obstaculo não vai poder sobrepor outro. 


# Objetivo Final do Trabalho
- Encontrar uma rota qualquer. Sem passar pelos obstaculos