from heapq import heappush, heappop
from typing import Dict, List, Tuple

def dijkstra(
    grafo: Dict[str, List[Tuple[str, float]]], 
    vertice_origem: str
) -> Dict[str, float]:
    """
    Implementa o algoritmo de Dijkstra para encontrar as distâncias mínimas
    a partir de um vértice de origem em um grafo com pesos não-negativos.
    
    :param grafo: Dicionário onde a chave é o vértice (str) e o valor 
                  é uma lista de tuplas (vizinho, peso).
    :param vertice_origem: Vértice a partir do qual as distâncias 
                           serão calculadas.
    :return: Dicionário com a distância de cada vértice até o vértice de origem.
    """
    # Inicializa todas as distâncias como infinito e o vértice de origem com 0
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[vertice_origem] = 0.0

    # Conjunto para marcar vértices visitados e fila de prioridade (min-heap)
    visitados = set()
    fila_prioridade = [(0.0, vertice_origem)]  # (distância_acumulada, vértice)

    while fila_prioridade:
        distancia_atual, vertice_atual = heappop(fila_prioridade)

        # Se este vértice já foi visitado, ignorar para evitar processamento extra
        if vertice_atual in visitados:
            continue
        
        visitados.add(vertice_atual)

        # Percorre todos os vizinhos do vértice atual
        for vizinho, peso in grafo[vertice_atual]:
            distancia_potencial = distancia_atual + peso

            # Se encontrar um caminho menor até o vizinho, atualiza
            if distancia_potencial < distancias[vizinho]:
                distancias[vizinho] = distancia_potencial
                heappush(fila_prioridade, (distancia_potencial, vizinho))

    return distancias

def exibir_distancias(distancias: Dict[str, float], vertice_origem: str) -> None:
    """
    Exibe as distâncias calculadas para cada vértice, em relação ao vértice de origem.

    :param distancias: Dicionário com distâncias mínimas para cada vértice.
    :param vertice_origem: Vértice de origem usado no cálculo das distâncias.
    """
    print(f"\nDistâncias mínimas a partir de '{vertice_origem}':")
    for vertice, distancia in distancias.items():
        print(f" - Distância até {vertice}: {distancia}")

if __name__ == "__main__":
    grafo_exemplo = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 1)],
        "D": [("B", 5), ("C", 1)]
    }

    origem = "A"
    distancias_calculadas = dijkstra(grafo_exemplo, origem)
    exibir_distancias(distancias_calculadas, origem)
