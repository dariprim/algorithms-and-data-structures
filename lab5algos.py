import heapq

def dinam_prog(graph, start, end):
    # Инициализация
    dist = {node: float('infinity') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    
    # Используем приоритетную очередь
    priority_queue = [(0, start)]  # (расстояние, вершина)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Если мы уже нашли более короткий путь, пропускаем
        if current_distance > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Если найден более короткий путь
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Восстановление пути
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = prev[current_node]
    path.reverse()

    return dist[end], path

if __name__ == "__main__":
    # Пример графа в виде словаря
    graph = {
        'A': {'B': 6, 'D': 7,'E': 7 },
        'B': {'F': 1, 'C': 5},
        'C': {'G': 3, 'D': 2},
        'D': {'G': 1},
        'E': {'G': 8, 'F': 4},
        'F': {'G': 4},
        'G': {}
    }

    start = 'A'
    end = 'G'
    distance, path = dinam_prog(graph, start, end)

    print(f"Кратчайшее расстояние от {start} до {end}: {distance}")
    print(f"Путь: {' -> '.join(path)}")


print("------------------------------------------------------------------------------------------")

def dijkstra(graph, start):
    dist = {node: float('infinity') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return dist, prev

def get_shortest_path(prev, end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = prev[current_node]
    path.reverse()
    return path

def find_shortest_paths(graph, pairs):
    results = {}
    for start, end in pairs:
        dist, prev = dijkstra(graph, start)
        path = get_shortest_path(prev, end)
        results[(start, end)] = (dist[end], path)
    return results

if __name__ == "__main__":
    # Пример графа в виде словаря
    graph = {
        'A': {'B': 6, 'E': 2},
        'B': {'A': 6, 'E': 1, 'F': 5,'C': 9, 'G': 3 },
        'C': {'G': 8, 'B': 2, 'D': 1},
        'D': {'C': 12, 'G': 3, 'H': 4},

        'E': {'A': 2, 'B': 2, 'F': 7 },
        'F': {'B': 5, 'E': 7, 'G': 4},
        'G': {'F': 4, 'H': 16, 'B': 3,'C': 8, 'D': 3},
        'H': {'D': 4, 'G': 16}
    }

    # Пары вершин для поиска кратчайшего пути
    pairs = [('A', 'H'), ('B', 'H'), ('F', 'D')]
    
    results = find_shortest_paths(graph, pairs)

    for (start, end), (distance, path) in results.items():
        if distance == float('infinity'):
            print(f"Нет пути от {start} до {end}.")
        else:
            print(f"Кратчайшее расстояние от {start} до {end}: {distance}")
            print(f"Путь: {' -> '.join(path)}")
