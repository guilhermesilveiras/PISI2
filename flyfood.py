import itertools

# função para ler a matriz do arquivo (tentando ignorar a primeira linha)
def ler_matriz(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    
    matriz = []
    # ignorar a primeira linha (que contém as dimensões da matriz)
    for linha in linhas[1:]:
        matriz.append(linha.split())
    
    return matriz

# função para encontrar os pontos de entrega na matriz
def encontrar_pontos(matriz):
    pontos = {}
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != '0':
                pontos[matriz[i][j]] = (i, j)
    return pontos

# função para calcular a distância entre dois pontos (distância Manhattan)
def distancia(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# função para calcular o custo total de uma permutação de pontos de entrega
def calcular_custo(pontos, ordem):
    custo_total = 0
    # distância de R ao primeiro ponto da ordem
    custo_total += distancia(pontos['R'], pontos[ordem[0]])
    
    # distância entre os pontos na ordem dada
    for i in range(len(ordem) - 1):
        custo_total += distancia(pontos[ordem[i]], pontos[ordem[i + 1]])
    
    # distância do último ponto da ordem de volta para R
    custo_total += distancia(pontos[ordem[-1]], pontos['R'])
    
    return custo_total

# função principal que resolve o problema com permutations
def encontrar_menor_rota(pontos):
    entregas = [p for p in pontos.keys() if p != 'R']
    
    # gerar todas as permutações dos pontos de entrega
    permutacoes = itertools.permutations(entregas)
    
    # inicializa a variável de menor custo e melhor ordem
    menor_custo = float('inf')
    melhor_ordem = None
    
    # itera sobre todas as permutações e calcula o custo
    for ordem in permutacoes:
        custo = calcular_custo(pontos, ordem)
        if custo < menor_custo:
            menor_custo = custo
            melhor_ordem = ordem
    
    return melhor_ordem

# função principal
def main(arquivo):
    matriz = ler_matriz(arquivo)
    pontos = encontrar_pontos(matriz)
    melhor_ordem = encontrar_menor_rota(pontos)
    
    return ' '.join(melhor_ordem)

# exemplo de uso
arquivo = 'matriz5.txt'
resultado = main(arquivo)
print(resultado)
