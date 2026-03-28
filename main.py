import matplotlib.pyplot as plt

# Дані з ваших таблиць
n = [1000, 2000, 4000, 8000, 10000, 15000, 20000]
best_case = [0.0000, 0.0000, 0.0010, 0.0020, 0.0010, 0.0010, 0.0020]
worst_case = [0.0282, 0.1194, 0.4790, 1.9297, 3.0338, 6.8605, 12.3176]
average_case = [0.0150, 0.0630, 0.2551, 1.0820, 1.5835, 3.6276, 6.4425]

plt.figure(figsize=(10, 6))

# Побудова ліній
plt.plot(n, best_case, label='Найкращий випадок (Best)', marker='o', color='blue')
plt.plot(n, average_case, label='Середній випадок (Average)', marker='s', color='green')
plt.plot(n, worst_case, label='Найгірший випадок (Worst)', marker='^', color='red')

# Налаштування осей та підписів
plt.xlabel('Розмір масиву (n)')
plt.ylabel('Час виконання (сек)')
plt.title('Порівняння часу виконання алгоритму')
plt.xticks(n) # Встановлюємо засічки саме за вашими значеннями n
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()

plt.show()