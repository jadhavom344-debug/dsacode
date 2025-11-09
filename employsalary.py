# Program: Sort employee salaries using Selection Sort and Bubble Sort

# Sample list of salaries
salaries = [45000.50, 32000.75, 78000.20, 56000.90, 91000.00, 47000.80, 62000.45]

# 1️⃣ Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap
    return arr

# 2️⃣ Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
    return arr

# Perform sorting
sel_sorted = selection_sort(salaries.copy())
bub_sorted = bubble_sort(salaries.copy())

# Display results
print("Salaries sorted using Selection Sort (Ascending):", sel_sorted)
print("Salaries sorted using Bubble Sort (Ascending):", bub_sorted)

# Display top 5 highest salaries
print("\nTop 5 highest salaries:")
print(sorted(salaries, reverse=True)[:5])
