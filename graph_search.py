# TASK 2
from collections import deque

# DFS function
def dfs_path(graph, start, end, path=None):
    if path is None:
        path = [] # Ініціалізуємо шлях як порожній список
    path = path + [start]  # Додаємо поточний вузол до шляху
    if start == end:
        return path # Якщо досягли кінцевого вузла, повертаємо шлях
    if start not in graph:
        return None  # Якщо вузол відсутній у графі, повертаємо None
    for node in graph[start]:
        if node not in path:
            new_path = dfs_path(graph, node, end, path) # Рекурсивно шукаємо шлях до сусідніх вузлів
            if new_path:
                return new_path # Якщо знайдено шлях, повертаємо його
    return None # Якщо шлях не знайдено, повертаємо None


# BFS function
def bfs_path(graph, start, end):
    queue = deque([[start]]) # Черга зі списком шляхів, що починаються з початкового вузла
    while queue:
        path = queue.popleft()  # Вибираємо перший шлях із черги
        node = path[-1]  # Останній вузол у шляху
        if node == end:
            return path  # Якщо досягли кінцевого вузла, повертаємо шлях
        for adjacent in graph[node]:
            if adjacent not in path:
                new_path = list(path)  # Створюємо новий шлях, щоб не модифікувати оригінальний
                new_path.append(adjacent)  # Додаємо сусідній вузол до нового шляху
                queue.append(new_path) # Додаємо новий шлях до черги
    return None # Якщо шлях не знайдено, повертаємо None

# Функція для обчислення відстані за шляхом і вагами ребер
def calculate_distance(graph, path):
    if not path:
        return float('inf')  # Return infinity if no path found
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]['weight']
    return distance
