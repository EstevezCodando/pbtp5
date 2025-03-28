# PBTP5 - Algoritmos e Segurança de Redes

Este repositório reúne implementações de **5 grupos** de exercícios, abrangendo:
1. **Caminhos Mínimos e Árvores Geradoras** (Dijkstra e Prim),
2. **Problemas NP-Completos com Heurísticas** (Mochila e Caixeiro Viajante),
3. **Comunicação Segura com TLS** (Servidor e Cliente TLS),
4. **Network Scanning e Packet Sniffing** (Scapy para varredura ARP e detecção de ARP spoofing).

Cada grupo possui um ou mais arquivos correspondentes, com exemplos de uso e instruções adicionais.

---

## 📂 Estrutura do Repositório

### **Grupo 1: Caminhos Mínimos e Árvores Geradoras**

1. [Ex1_Dijkstra_Cmin.py](Grupo1/Ex1_Dijkstra_Cmin.py)  
   - **Algoritmo de Dijkstra (Caminhos Mínimos)**  
   - Encontra o caminho mínimo de um vértice de origem para todos os outros vértices em um grafo ponderado.  
   - O grafo é representado por um dicionário onde cada chave é um vértice e seu valor é uma lista de tuplas `(vizinho, peso)`.

2. [Ex1.2_Prim_MST.py](Grupo1/Ex1.2_Prim_MST.py)  
   - **Algoritmo de Prim (Árvore Geradora Mínima)**  
   - Calcula a MST de um grafo não direcionado e ponderado.  
   - Seleciona arestas de menor peso, conectando todos os vértices sem formar ciclos.

---

### **Grupo 2: Problemas NP-completos com Heurísticas**

1. [Ex2.1_MochilaGulosa.py](Grupo2/Ex2.1_MochilaGulosa.py)  
   - **Problema da Mochila usando heurística gulosa**  
   - Ordena itens pela razão valor/peso e os adiciona à mochila até atingir a capacidade máxima.  
   - Exemplo de abordagem aproximada para o problema da mochila (Knapsack).

2. [Ex2.2_CaixeiroViajante.py](Grupo2/Ex2.2_CaixeiroViajante.py)  
   - **TSP (Caixeiro Viajante) com heurística do Vizinho Mais Próximo**  
   - Inicia em uma cidade e escolhe sempre a cidade não-visitada mais próxima.  
   - Abordagem simples para problemas de roteamento.

---

### **Grupo 3: Comunicação Segura com TLS**

1. [Ex3.1_ServidorTLS.py](Grupo3/Ex3.1_ServidorTLS.py)  
   - **Servidor TLS (Echo)**  
   - Cria um socket seguro (SSL/TLS) que recebe mensagens de um cliente e as devolve (echo).  
   - Utiliza um certificado autoassinado (`server.crt` + `server.key`).

2. [Ex3.1_ClienteTLS.py](Grupo3/Ex3.1_ClienteTLS.py)  
   - **Cliente TLS**  
   - Conecta-se ao servidor TLS acima, envia uma mensagem e imprime a resposta de eco.  
   - Pode validar o certificado do servidor.

> **Outros arquivos**:
> - `server.crt`, `server.key` – Certificado e chave privada autoassinados para uso no servidor TLS.

---

### **Grupo 4: Network Scanning e Packet Sniffing**

1. [Ex4.1_Scapy.py](Grupo4/Ex4.1_Scapy.py)  
   - **Varredura ARP**  
   - Utiliza a biblioteca **Scapy** para enviar requisições ARP em um intervalo de IPs (ex: `192.168.1.0/24`).  
   - Exibe IP e MAC dos hosts que responderem (hosts ativos).  
   - Necessário executar com privilégios (ex.: `sudo`).

2. [Ex4.2_ArpSniff.py](Grupo4/Ex4.2_ArpSniff.py)  
   - **Detecção de ARP Spoofing**  
   - Monitora pacotes ARP e verifica se um mesmo IP aparece com MACs diferentes.  
   - Emite alerta de possível ARP spoofing.  
   - Também requer privilégios para capturar pacotes de rede.

---


