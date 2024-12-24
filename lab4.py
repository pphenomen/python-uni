# Вариант 8, Задания: 8, 20, 32, 44, 56
def find_two_smallest_indexes(arr):
    if len(arr) < 2:
        return "Массив должен содержать хотя бы два элемента"
    
    first_min_index = arr.index(min(arr))
    # копируем массив и заменяем минимальный элемент на бесконечность
    arr_copy = arr[:]
    arr_copy[first_min_index] = float('inf')
    second_min_index = arr_copy.index(min(arr_copy))
    
    return first_min_index, second_min_index

def find_missing_numbers(arr):
    min_num = min(arr)
    max_num = max(arr)
    
    full_set = set(range(min_num, max_num + 1)) # преобразуем диапазон в множество для удобства операций
    missing_numbers = sorted(list(full_set - set(arr)))
    
    return missing_numbers

def count_local_max(arr):
    local_max_count = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            local_max_count += 1
    return local_max_count

def check_alternation(arr):
    for i in range(1, len(arr)):
        current_is_integer = arr[i].is_integer() if isinstance(arr[i], float) else isinstance(arr[i], int)
        previous_is_integer = arr[i-1].is_integer() if isinstance(arr[i-1], float) else isinstance(arr[i-1], int)
        
        if (current_is_integer and previous_is_integer) or (not current_is_integer and not previous_is_integer):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def calculate_average_non_primes(arr):
    primes = [x for x in arr if is_prime(x)]
    
    if not primes:
        return "Нет простых чисел"
    
    prime_avg = sum(primes) / len(primes)
    # создаем список непростых чисел > среднее простых
    non_primes = [x for x in arr if not is_prime(x) and x > prime_avg]
    
    if not non_primes:
        return "Нет непростых чисел, превышающих среднее простых"
    
    return sum(non_primes) / len(non_primes)

def user_menu():
    tasks = [
        "Найти индексы двух наименьших элементов массива",
        "Найти все пропущенные числа в массиве",
        "Найти количество локальных максимумов",
        "Проверить, чередуются ли целые и вещественные числа в массиве",
        "Посчитать среднее арифметическое непростых элементов, которые больше, чем среднее арифметическое простых"
    ]

    while True:
        print("\nВыберите задачу:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            
        choice = input("Введите номер задачи(для выхода из программы введите exit): ")
        if choice.lower() == 'exit':
            print("Завершение программы")
            break
        
        try:
            choice = int(choice)
            if choice < 1 or choice > 5:
                print("Ошибка: введите номер задачи от 1 до 5")
                continue
        except ValueError:
            print("Ошибка: введите корретный номер или 'exit'")
        
        try:
            if choice != 4:
                arr = list(map(int, input("Введите целочисленный массив через пробел: ").split()))
            else: 
                arr = list(map(float, input("Введите массив чисел (целых и вещественных) через пробел: ").split()))
        except ValueError:
            print("Ошибка: введите корректные числа")
            continue
        
        if choice == 1:
            result = find_two_smallest_indexes(arr)
        elif choice == 2:
            result = find_missing_numbers(arr)
        elif choice == 3:
            result = count_local_max(arr)
        elif choice == 4:
            result = check_alternation(arr)
        elif choice == 5:
            result = calculate_average_non_primes(arr)
        
        print("Результат:", result)
        
if __name__ == "__main__":
    user_menu()
        