import numpy as np
import matplotlib.pyplot as plt

# Параметры функции
A = 1 / 26
alpha = -151.515
omega = 1582

# Время
t = np.linspace(0, 0.1, 1000)  # Увеличиваем количество точек для более гладкого графика

# Функция
y = A * np.exp(alpha * t) * np.sin(omega * t)

# Построение графика
plt.figure(figsize=(12, 6))
plt.plot(t, y, label=r'$\frac{1}{26} e^{-151.515t} \sin(1582t)$', color='maroon')

# Добавление легенды и меток осей
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')
plt.legend()

# Включение основной сетки
plt.grid(True, which='major', linestyle='-', linewidth=0.5)

# Включение мелкой сетки с использованием MinorTicks
plt.minorticks_on()
plt.grid(True, which='minor', linestyle=':', linewidth=0.5)

# Нанесение осей координат
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Улучшение внешнего вида заголовка
plt.title('График функции $\\i(t)$', fontdict={'fontsize': 16, 'fontweight': 'bold'})

# Отображение графика
plt.show()
