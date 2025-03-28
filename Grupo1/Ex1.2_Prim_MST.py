from heapq import heappush, heappop
from typing import Dict, List, Tuple

def prim(
    grafo: Dict[str, List[Tuple[str, float]]], 
    vertice_inicial: str
) -> List[Tuple[str, str, float]]:
    """
    Implementa o algoritmo de Prim para calcular a Árvore Geradora Mínima (MST)
    de um grafo não direcionado e ponderado.

    :param grafo: Dicionário onde cada chave é um vértice (str) e o valor
                  é uma lista de tuplas (vizinho, peso).
    :param vertice_inicial: Vértice de onde partiremos para construir a MST.
    :return: Lista de arestas que compõem a Árvore Geradora Mínima, 
             no formato [(u, v, peso), ...].
    """
    mst = []  # Armazenará as arestas que compõem a MST
    visitados = set([vertice_inicial])  # Conjunto de vértices incluídos na MST
    arestas_disponiveis = []

    # Adiciona as arestas do vértice inicial na fila de prioridade
    for vizinho, peso in grafo[vertice_inicial]:
        heappush(arestas_disponiveis, (peso, vertice_inicial, vizinho))

    # Enquanto houver arestas candidatas e ainda houver vértices fora da MST
    while arestas_disponiveis and len(visitados) < len(grafo):
        peso, vertice_u, vertice_v = heappop(arestas_disponiveis)

        # Se o vértice v ainda não foi visitado, esta é a aresta de menor custo para conectá-lo
        if vertice_v not in visitados:
            visitados.add(vertice_v)
            mst.append((vertice_u, vertice_v, peso))

            # Adiciona à fila todas as arestas a partir do novo vértice v
            for novo_vizinho, novo_peso in grafo[vertice_v]:
                if novo_vizinho not in visitados:
                    heappush(arestas_disponiveis, (novo_peso, vertice_v, novo_vizinho))

    return mst

def exibir_mst(mst: List[Tuple[str, str, float]]) -> None:
    """
    Exibe as arestas da Árvore Geradora Mínima (MST) resultante,
    incluindo os vértices conectados e o peso de cada aresta.

    :param mst: Lista de arestas (u, v, peso) que formam a MST.
    """
    print("\nÁrvore Geradora Mínima (MST) encontrada:")
    for u, v, peso in mst:
        print(f"{u} - {v} (peso: {peso})")

if __name__ == "__main__":
    grafo_exemplo = {
        "A": [("B", 2), ("C", 3)],
        "B": [("A", 2), ("C", 1), ("D", 4)],
        "C": [("A", 3), ("B", 1), ("D", 5)],
        "D": [("B", 4), ("C", 5)]
    }

    vertice_inicial = "A"
    resultado_mst = prim(grafo_exemplo, vertice_inicial)
    exibir_mst(resultado_mst)
