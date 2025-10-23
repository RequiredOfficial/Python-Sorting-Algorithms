import random
import time

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0 # сравнения
    swaps = 0 # перестановки
    arr_copy = arr.copy() # работаем с копией массива
    
    start_time = time.perf_counter() # таймер
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swaps += 1
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    return arr_copy, comparisons, swaps, execution_time

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    arr_copy = arr.copy()
    
    start_time = time.perf_counter()
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
            swaps += 1
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    return arr_copy, comparisons, swaps, execution_time

def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    arr_copy = arr.copy()
    
    start_time = time.perf_counter()
    
    for i in range(1, n):
        key = arr_copy[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr_copy[j] > key:
                arr_copy[j + 1] = arr_copy[j]
                swaps += 1
                j -= 1
            else:
                break
        
        arr_copy[j + 1] = key
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    return arr_copy, comparisons, swaps, execution_time

def main():
    sizes = [100, 500, 1000]  # Размеры массивов
    
    for size in sizes:
        print(f"ТЕСТИРОВАНИЕ АЛГОРИТМОВ СОРТИРОВКИ (размер массива: {size})")
        print("=" * 150)
        # Тестовые массивы
        ascending = list(range(1, size + 1))
        descending = list(range(size, 0, -1))
        random_arr = [random.randint(1, 10000) for _ in range(size)]
        
        print(f"{'ТИП МАССИВА':<20} {'BUBBLE SORT':<35} {'SELECTION SORT':<35} {'INSERTION SORT':<35}")
        print(f"{'':<20} {'(Сравн/Перест/Время)':<35} {'(Сравн/Перест/Время)':<35} {'(Сравн/Перест/Время)':<35}")
        print("-" * 125)
        
        test_arrays = [
            ("По возрастанию", ascending),
            ("По убыванию", descending),
            ("Случайный", random_arr)
        ]
        
        for name, array in test_arrays:
            _, bubble_comp, bubble_swap, bubble_time = bubble_sort(array)
            _, selection_comp, selection_swap, selection_time = selection_sort(array)
            _, insertion_comp, insertion_swap, insertion_time = insertion_sort(array)
            
            # Результаты
            print(f"{name:<20} {f'{bubble_comp}/{bubble_swap}/{bubble_time:.6f}':<35} {f'{selection_comp}/{selection_swap}/{selection_time:.6f}':<35} {f'{insertion_comp}/{insertion_swap}/{insertion_time:.6f}':<35}")
        
        print("\n")

if __name__ == "__main__":
    main()