def merge_sort(arr, level=0, side="Origin"):
    indent = "  " * level
    print(f"{indent}[{side}] Сортуємо: {arr}")

    if len(arr) <= 1:
        return arr

    # 1. Поділ (Divide)
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], level + 1, "Left")
    right_half = merge_sort(arr[mid:], level + 1, "Right")

    # 2. Злиття (Merge)
    return merge(left_half, right_half, level, indent)

def merge(left, right, level, indent):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    print(f"{indent}  => Результат злиття: {merged}")
    return merged

# Твій масив із 10 чисел
data = [8, 3, 1, 7, 0, 10, 2, 5, 9, 4]
sorted_data = merge_sort(data)
print(f"\nКінцевий результат: {sorted_data}")