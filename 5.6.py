import time
import random
import sys

# Збільшуємо ліміт рекурсії для великих масивів
sys.setrecursionlimit(2000000)

def merge_sort_timed(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort_timed(A, p, q)
        merge_sort_timed(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    left = A[p:q+1]
    right = A[q+1:r+1]
    i = j = 0
    k = p
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1

def measure_time(case_type, sizes):
    results = []
    for n in sizes:
        if case_type == "best":
            arr = list(range(n))  # Вже відсортований
        elif case_type == "worst":
            arr = list(range(n, 0, -1))  # У зворотному порядку
        else:
            arr = [random.randint(0, n) for _ in range(n)] # Випадковий
            
        start_time = time.time()
        merge_sort_timed(arr, 0, len(arr) - 1)
        end_time = time.time()
        
        results.append((n, round(end_time - start_time, 2)))
        print(f"Розмір {n} для {case_type} готовий...")
    return results

# Розміри підбираються так, щоб перший результат був ~8-10 сек.
# Якщо твій ПК дуже швидкий, збільш ці числа вдвічі.
test_sizes = [500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000]

print("--- Початок замірів (це може зайняти 5-10 хв) ---")
best_results = measure_time("best", test_sizes)
avg_results = measure_time("average", test_sizes)
worst_results = measure_time("worst", test_sizes)

print("\nРезультати для звіту:")
for name, res in [("Найкращий", best_results), ("Середній", avg_results), ("Найгірший", worst_results)]:
    print(f"\nТаблиця для: {name}")
    print("Розмір (n) | Час (сек)")
    for n, t in res:
        print(f"{n} | {t}")