print("Трассировка элементов интегральных схем")
def trace_ic(size):
    grid = [['.' for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:  # пример простой трассировки
                grid[i][j] = '*'
    
    for row in grid:
        print(' '.join(row))

sizes = [10, 20, 30]
for size in sizes:
    print(f"Трассировка для {size}x{size}:")
    trace_ic(size)
    print()

print("Оптимальное расписание работы четырех процессоров")
def optimal_schedule(tasks):
    processors = [[] for _ in range(4)]
    processor_times = [0] * 4

    for task in sorted(tasks):  # Сортируем задачи по времени
        min_processor = processor_times.index(min(processor_times))
        processors[min_processor].append(task)
        processor_times[min_processor] += task

    return processors

tasks = [2, 3, 5, 1, 4, 6, 7, 8, 9, 2, 5]  # Пример времён задач
schedule = optimal_schedule(tasks)

for i, processor in enumerate(schedule):
    print(f"Процессор {i+1}: Задачи {processor}, Общее время {sum(processor)}")

print("Алгоритм оптимальной упаковки (жадный)")
def pack_items(items, box_size):
    boxes = []
    items.sort(reverse=True)  # Сортируем по убыванию

    while items:
        box = []
        current_size = 0

        for item in items[:]:  # Итерируем по копии списка
            if current_size + item <= box_size:
                box.append(item)
                current_size += item
                items.remove(item)

        boxes.append(box)

    return boxes

items = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]  # 12 предметов
box_size = 6
packed_boxes = pack_items(items, box_size)

for i, box in enumerate(packed_boxes):
    print(f"Ящик {i+1}: Предметы {box}, Общий размер {sum(box)}")

print("Программа моделирования эвристического алгоритма")
def greedy_algorithm(data):
    # Предположим, что data - это список значений
    sorted_data = sorted(data, reverse=True)
    selected = []

    while sorted_data:
        selected.append(sorted_data.pop(0))  # Жадный выбор

    return selected

data = [5, 3, 8, 6, 2, 7, 1, 4]
result = greedy_algorithm(data)

print(f"Результат эвристического алгоритма: {result}")
