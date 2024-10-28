def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])  # Якщо знайдено точний збіг

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Після завершення циклу визначаємо верхню межу
    if left < len(arr):
        upper_bound = arr[left]
    else:
        upper_bound = None  # Якщо не знайдено жодного елемента, що більше або рівне target

    return (iterations, upper_bound)

# Тестуємо функцію
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5]
target_value = 1.5
result = binary_search(sorted_array, target_value)

print(result)  # (кількість ітерацій, верхня межа)