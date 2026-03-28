import matplotlib.pyplot as plt

# Дані з таблиць
n = [500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000]

best_case = [1.24, 2.58, 4.02, 5.37, 6.95, 8.37, 9.81]
average_case = [1.72, 3.64, 5.83, 8.11, 10.6, 12.9, 15.27]
worst_case = [1.25, 2.56, 4.0, 5.4, 6.93, 8.33, 9.86]

# Створення графіка
plt.figure(figsize=(10, 6))

plt.plot(n, best_case, marker='o', linestyle='-', label='Найкращий випадок')
plt.plot(n, average_case, marker='s', linestyle='-', label='Середній випадок')
plt.plot(n, worst_case, marker='^', linestyle='--', label='Найгірший випадок')

# Налаштування осей та заголовка
plt.title('Залежність часу виконання від розміру масиву (n)')
plt.xlabel('Розмір масиву (n)')
plt.ylabel('Час (сек)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Відображення
plt.tight_layout()
plt.show()