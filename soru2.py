# Union-Find veri yapısı (Döngü oluşup oluşmadığını kontrol etmek için)
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            self.parent[item] = self.find(self.parent[item])
            return self.parent[item]
    
    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            self.parent[root1] = root2
            return True
        return False

def kruskal_mst(vertices, edges):
    mst = [] # Minimum Spanning Tree kenarları
    ds = DisjointSet(vertices)
    
    # Kenarları ağırlıklarına göre küçükten büyüğe sırala
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    total_cost = 0
    
    for u, v, weight in sorted_edges:
        # Eğer iki düğüm zaten bağlı değilse (döngü oluşturmuyorsa) ekle
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight
            
    return mst, total_cost

# Görseldeki veriler (Düğümler ve Kenarlar)
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('C', 'D', 3),
    ('C', 'E', 8),
    ('D', 'E', 4),
    ('D', 'F', 6),
    ('E', 'F', 1)
]

mst_edges, min_cost = kruskal_mst(vertices, edges)

print("--- Minimum Yayılan Ağaç (MST) Sonucu ---")
print("Seçilen Kenarlar:")
for u, v, w in mst_edges:
    print(f"{u} - {v}: {w}")
print(f"Toplam Ağırlık: {min_cost}")