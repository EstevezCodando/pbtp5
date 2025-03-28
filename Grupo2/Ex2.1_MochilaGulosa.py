def mochila_gulosa(capacidade: float, itens: list[tuple[float, float]]) -> tuple[float, list[tuple[float, float]]]:
    """
    Resolve o Problema da Mochila 0/1 usando um algoritmo guloso conforme o da aula,
    ordenando os itens pela melhor razão valor/peso.

    :param capacidade: Capacidade máxima da mochila.
    :param itens: Lista de tuplas (peso, valor).
    :return: Uma tupla (valor_total, itens_selecionados), onde
             valor_total é o valor máximo obtido e itens_selecionados
             é a lista de itens (peso, valor) realmente colocados na mochila.
    """
    # 1. Ordena os itens de forma decrescente pela razão valor/peso
    itens_ordenados = sorted(itens, key=lambda x: x[1] / x[0], reverse=True)
    
    peso_atual = 0.0
    valor_total = 0.0
    itens_selecionados = []

    # 2. Percorre os itens ordenados e seleciona o item se couber
    for peso, valor in itens_ordenados:
        if peso_atual + peso <= capacidade:
            itens_selecionados.append((peso, valor))
            peso_atual += peso
            valor_total += valor
        # Como é 0/1, se não couber inteiro, não adiciona

    return valor_total, itens_selecionados

def calcular_peso_e_valor_total(itens_selecionados: list[tuple[float, float]]) -> tuple[float, float]:
    """
    Dada a lista de itens selecionados, retorna o peso e valor totais.
    """
    peso_total = sum(item[0] for item in itens_selecionados)
    valor_total = sum(item[1] for item in itens_selecionados)
    return peso_total, valor_total

def exibir_itens_mochila(
    itens_selecionados: list[tuple[float, float]],
    peso_total: float,
    valor_total: float
) -> None:
    """
    Exibe cada item (peso, valor) que entrou na mochila, 
    além dos totais acumulados.
    """
    print("Itens selecionados:")
    for i, (peso, valor) in enumerate(itens_selecionados, start=1):
        print(f" - Item {i}: Peso = {peso}, Valor = {valor}")
    print(f"\nPeso total: {peso_total}")
    print(f"Valor total: {valor_total}")

if __name__ == "__main__":
    itens_exemplo = [(10, 60), (20, 100), (30, 120), (40, 150)]
    capacidade_mochila = 70

    valor_maximo, itens_escolhidos = mochila_gulosa(capacidade_mochila, itens_exemplo)
    peso_total, valor_total = calcular_peso_e_valor_total(itens_escolhidos)
    
    exibir_itens_mochila(itens_escolhidos, peso_total, valor_total)
    print(f"\nValor máximo que pode ser carregado na mochila: {valor_maximo}")
