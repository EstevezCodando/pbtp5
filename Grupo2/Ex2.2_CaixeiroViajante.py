import math
from typing import Dict, Tuple, List

def calcular_distancia(cidade1: Tuple[float, float], cidade2: Tuple[float, float]) -> float:
    """
    Calcula a distância euclidiana entre duas cidades representadas por coordenadas (x, y).
    """
    x1, y1 = cidade1
    x2, y2 = cidade2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def encontrar_vizinho_mais_proximo(
    cidade_atual: str, 
    cidades: Dict[str, Tuple[float, float]], 
    nao_visitadas: List[str]
) -> str:
    """
    Dada a cidade atual, encontra a cidade mais próxima entre as não visitadas,
    usando distância euclidiana.
    
    :param cidade_atual: Nome (str) da cidade onde estamos.
    :param cidades: Dicionário { nome_cidade: (x, y) } com coordenadas das cidades.
    :param nao_visitadas: Lista de nomes de cidades ainda não visitadas.
    :return: Nome da cidade mais próxima.
    """
    menor_distancia = float('inf')
    cidade_proxima = None
    
    for prox_cidade in nao_visitadas:
        dist = calcular_distancia(cidades[cidade_atual], cidades[prox_cidade])
        if dist < menor_distancia:
            menor_distancia = dist
            cidade_proxima = prox_cidade
    
    return cidade_proxima

def tsp_vizinho_mais_proximo(
    cidades: Dict[str, Tuple[float, float]], 
    cidade_inicial: str
) -> Tuple[List[str], float]:
    """
    Resolve (de forma aproximada) o Problema do Caixeiro Viajante (TSP)
    usando a heurística do Vizinho Mais Próximo (Nearest Neighbor).
    
    :param cidades: Dicionário { nome_cidade: (x, y) }.
    :param cidade_inicial: Nome da cidade de onde partiremos.
    :return: (rota, distancia_total)
             rota: Lista de cidades na ordem em que foram visitadas.
             distancia_total: Distância total percorrida.
    """
    # Conjunto / lista de cidades não visitadas, exceto a inicial
    nao_visitadas = [c for c in cidades if c != cidade_inicial]
    
    rota = [cidade_inicial]
    distancia_total = 0.0
    cidade_atual = cidade_inicial

    # Enquanto ainda houver cidades não visitadas
    while nao_visitadas:
        # Encontra a cidade mais próxima e atualiza a distância
        proxima_cidade = encontrar_vizinho_mais_proximo(cidade_atual, cidades, nao_visitadas)
        distancia_total += calcular_distancia(cidades[cidade_atual], cidades[proxima_cidade])
        
        # Marca a cidade escolhida como visitada
        nao_visitadas.remove(proxima_cidade)
        rota.append(proxima_cidade)
        cidade_atual = proxima_cidade

    # (Opcional) Se quiser voltar à cidade inicial para fechar o ciclo:
    # distancia_total += calcular_distancia(cidades[cidade_atual], cidades[cidade_inicial])
    # rota.append(cidade_inicial)

    return rota, distancia_total

def exibir_rota(rota: List[str], distancia_total: float) -> None:
    """
    Exibe a rota obtida e a distância total percorrida.
    """
    print("\nRota encontrada pelo Vizinho Mais Próximo:")
    print(" -> ".join(rota))
    print(f"Distância total: {distancia_total:.2f}")

if __name__ == "__main__":
    cidades_exemplo = {
        "A": (0, 0),
        "B": (1, 5),
        "C": (5, 2),
        "D": (6, 6),
        "E": (8, 3)
    }
    
    # Definimos "A" como cidade de partida
    cidade_inicial_exemplo = "A"
    
    # Executa a heurística do Vizinho Mais Próximo
    rota_resultante, distancia = tsp_vizinho_mais_proximo(
        cidades_exemplo, 
        cidade_inicial_exemplo
    )
    
    # Exibe o resultado
    exibir_rota(rota_resultante, distancia)
