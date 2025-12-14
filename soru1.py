import heapq

def dijkstra_shortest_path(graph, start, end):
    # Başlangıç düğümü için mesafe 0, diğerleri sonsuz
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Yolu takip etmek için (önceki düğümleri saklar)
    previous_nodes = {node: None for node in graph}
    
    # Öncelik kuyruğu (Priority Queue): (mesafe, düğüm)
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Eğer hedef düğüme ulaştıysak ve en kısa yolu bulduysak
        if current_distance > distances[current_node]:
            continue
        
        # Komşuları kontrol et
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Daha kısa bir yol bulunduysa güncelle
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # Yolu oluştur (Geriye doğru izleme)
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]
        
    return path, distances[end]

# Görseldeki veriler (Yönlü Graf)
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'C': 5, 'E': 2},
    'C': {'F': 8},
    'D': {'B': 2, 'E': 6},
    'E': {'F': 3},
    'F': {}
}

start_node = 'A'
end_node = 'F'

path, cost = dijkstra_shortest_path(graph, start_node, end_node)

print(f"--- En Kısa Yol Sonucu ({start_node} -> {end_node}) ---")
print(f"İzlenen Yol: {' -> '.join(path)}")
print(f"Toplam Maliyet: {cost}")