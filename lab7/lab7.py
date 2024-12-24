from collections import deque
import random

# Задача 1. Нахождение количества различных пар кандидатов с суммарным рейтинговым баллом не менее K 
def count_valid_pairs(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        N, K = map(int, first_line.split())
        
        ratings = []
        for line in file:
            ratings.append(int(line.strip()))

    ratings.sort()

    count = 0
    left = 0
    right = N - 1

    # Поиск пар с суммарным рейтингом >= K
    while left < right:
        if ratings[left] + ratings[right] >= K:
            count += (right - left)  # все кандидаты от left до right образуют пару с right
            right -= 1  # переходим к следующему кандидату справа
        else:
            left += 1  # увеличиваем левый указатель

    return count

filename_A = '27-169bb.txt'
filename_B = '27-169b.txt'

result_A = count_valid_pairs(filename_A)
result_B = count_valid_pairs(filename_B)

print(f"Количество пар для файла A: {result_A}")
print(f"Количество пар для файла B: {result_B}")

# Задача 2. Генерация файла с натуральными числами и создание файла с произведениями
def generate_file_f(filename, count, min_val, max_val):
    # Генерирует файл с натуральными числами в заданном диапазоне
    with open(filename, 'w') as file:
        for _ in range(count):
            number = random.randint(min_val, max_val)
            file.write(f"{number}\n")

def generate_file_g(input_file, output_file):
    # Считает числа из файла, формирует произведения и записывает их в новый файл
    with open(input_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    
    cumulative_product = 1
    with open(output_file, 'w') as file:
        for number in numbers:
            cumulative_product *= number
            file.write(f"{cumulative_product}\n")

# Генерация файла f.txt и создание файла g.txt с произведениями для задачи 2
generate_file_f('f.txt', count=10, min_val=1, max_val=10)
generate_file_g('f.txt', 'g.txt')

# Вывод содержимого файла g для проверки результата задачи 2
print("Содержимое файла g:")
with open('g.txt', 'r') as file:
    print(file.read())