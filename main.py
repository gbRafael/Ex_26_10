import networkx as nx

# Criar um grafo do mapa
G = nx.Graph()

# Adicione os pontos do mapa e suas conexões com pesos
G.add_edge("Torre", "Fase1", weight=2)
G.add_edge("Fase1", "Fase2", weight=3)
G.add_edge("Fase1", "Fase3", weight=4)
G.add_edge("Fase3", "Fase4", weight=7)
G.add_edge("Fase4", "Fase5", weight=8)
G.add_edge("Fase5", "Fase6", weight=9)
G.add_edge("Fase6", "Fase7", weight=10)
G.add_edge("Fase7", "Fase8", weight=11)
G.add_edge("Fase8", "Fase9", weight=12)
G.add_edge("Fase9", "Fase10", weight=13)
G.add_edge("Fase10", "Fase11", weight=14)
G.add_edge("Fase11", "Fase12", weight=15)
G.add_edge("Fase12", "Fase13", weight=16)
G.add_edge("Fase13", "Fase14", weight=17)
G.add_edge("Fase14", "Fase15", weight=18)
G.add_edge("Fase15", "Fase16", weight=19)
G.add_edge("Fase16", "Fase17", weight=20)
G.add_edge("Fase17", "Fase18", weight=21)
G.add_edge("Fase18", "Fase19", weight=22)
G.add_edge("Fase19", "Fase20", weight=23)

# Adicione o ponto de início (Torre) e as 20 fases
fases = ["Fase1", "Fase2", "Fase3", "Fase4", "Fase5", "Fase6", "Fase7", "Fase8", "Fase9", "Fase10", "Fase11", "Fase12", "Fase13", "Fase14", "Fase15", "Fase16", "Fase17", "Fase18", "Fase19", "Fase20"]
G.add_nodes_from(["Torre"] + fases)

# Função para calcular o menor caminho
def calcular_menor_caminho(mapa, origem, destino):
    try:
        caminho = nx.shortest_path(mapa, source=origem, target=destino, weight="weight")
        distancia = nx.shortest_path_length(mapa, source=origem, target=destino, weight="weight")
        return caminho, distancia
    except nx.NetworkXNoPath:
        return None, float("inf")

# Defina os pesos para as conexões entre as fases
pesos = {
    ("Fase1", "Fase4"): 5,
    ("Fase2", "Fase5"): 6,
    # Continue definindo pesos para todas as conexões necessárias
}

# Adicione os pesos ao grafo
G.add_edges_from(pesos.keys(), weight=0)

# Calcular o menor caminho para cada ponto (fase)
for destino in fases:
    caminho, distancia = calcular_menor_caminho(G, "Torre", destino)
    if caminho:
        print(f"Menor caminho para {destino}: {caminho} (Distância: {distancia})")
    else:
        print(f"Não há caminho para {destino}")
