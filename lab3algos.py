import time
import sys
sys.setrecursionlimit(10000000)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def power(a, n):
    if n < 0:
        return None  # Обработка некорректного значения
    if n == 0:
        return a  
    return (a * power(a, n - 1))/factorial(n)


def compute_sequence(num_elements):
    sequence = []
    for i in range(num_elements):
        sequence.append(power(a,i))
    return sequence

num_elements = 100
a = 3
start_time = time.time()

# Вычисляем последовательность
result_sequence = compute_sequence(num_elements)

# Определяем время выполнения
end_time = time.time()
execution_time = end_time - start_time

# Выводим результаты
print(f"Последовательность a(n) для n = 0 до {num_elements - 1}: {result_sequence}")
print(f"Время выполнения программы: {execution_time:.10f} секунд")
