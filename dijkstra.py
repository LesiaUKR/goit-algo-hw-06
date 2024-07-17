# TASK 3
import heapq
import pandas as pd

def dijkstra(graph, start):
    # Ініціалізуємо відстані до всіх вузлів графу як нескінченність, крім початкового вузла
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) # Вибираємо вузол з найменшою відстанню
        
        if current_distance > distances[current_node]:
            continue # Якщо поточна відстань більша за збережену, ігноруємо цей вузол
        
        # Оновлюємо відстані до всіх сусідніх вузлів через поточний вузол
        for neighbor, attributes in graph[current_node].items():
            weight = attributes['weight']
            distance = current_distance + weight

             # Якщо знайдена коротша відстань до сусіда, оновлюємо її і додаємо в чергу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def save_dijkstra_results_to_md(graph, filename="dijkstra_results.md"):
    all_distances = {}

    # Запускаємо алгоритм Дейкстри для кожного вузла графу
    for node in graph:
        distances = dijkstra(graph, node)
        all_distances[node] = distances
    
    df = pd.DataFrame(all_distances).transpose() # Створюємо DataFrame з отриманих відстаней
    
    # Зберігаємо DataFrame у файл Markdown
    with open(filename, 'w') as file:
        file.write(df.to_markdown())
    
    return df
