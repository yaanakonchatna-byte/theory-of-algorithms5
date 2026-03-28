import matplotlib.pyplot as plt

def draw_merge_sort(arr, x, y, width):
    # Відображаємо поточний вузол (масив)
    plt.text(x, y, str(arr), style='italic', weight='bold',
             bbox={'facecolor': 'white', 'alpha': 0.8, 'pad': 5},
             ha='center', va='center')

    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Малюємо лінії до дочірніх вузлів
    plt.plot([x, x - width/2], [y - 0.8, y - 1.8], 'k-', lw=1, alpha=0.5)
    plt.plot([x, x + width/2], [y - 0.8, y - 1.8], 'k-', lw=1, alpha=0.5)

    # Рекурсивно малюємо ліву та праву частини
    draw_merge_sort(left_half, x - width/2, y - 2, width/2)
    draw_merge_sort(right_half, x + width/2, y - 2, width/2)

# Налаштування графіка
plt.figure(figsize=(12, 8))
plt.axis('off')
plt.title("Графічна схема розбиття масиву (Merge Sort)", fontsize=14)

# Твій масив
data = [8, 3, 1, 7, 0, 10, 2, 5, 9, 4]
draw_merge_sort(data, 0, 10, 10)

plt.show()