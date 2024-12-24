def average_ascii(string):
    total = sum(ord(c) for c in string)
    return total / len(string)

def deviation_from_first_string_avg(string, first_string_avg):
    avg = average_ascii(string)
    return (avg - first_string_avg) ** 2

# Находит максимальное среднее значение ASCII среди троек (подстрок длиной 3) внутри строки.
def max_avg_ascii_triplet(string):
    # Если длина строки меньше 3, возвращает 0, так как троек быть не может.
    if len(string) < 3:
        return 0
    max_avg = 0
    # Итерирует по всем тройкам в строке и находит максимальное среднее ASCII значение среди них.
    for i in range(len(string) - 2):
        triplet = string[i:i+3]
        triplet_avg = average_ascii(triplet)
        if triplet_avg > max_avg:
            max_avg = triplet_avg
    return max_avg

def deviation_from_max_triplet_avg(string):
    avg = average_ascii(string)
    max_triplet_avg = max_avg_ascii_triplet(string)
    return (avg - max_triplet_avg) ** 2

def count_mirror_triplets(string):
    count = 0
    for i in range(len(string) - 2):
        triplet = string[i:i+3]
        if triplet[0] == triplet[2]:
            count += 1
    return count

strings = ['abc', 'Hello', 'world', 'xyz']

first_string_avg = average_ascii(strings[0])

sorted_by_avg_ascii = sorted(strings, key=average_ascii)
sorted_by_deviation = sorted(strings, key=lambda s: deviation_from_first_string_avg(s, first_string_avg)) 
sorted_by_triplet_deviation = sorted(strings, key=deviation_from_max_triplet_avg)
sorted_by_mirror_triplets = sorted(strings, key=count_mirror_triplets)

print("Сортировка по среднему весу ASCII:", sorted_by_avg_ascii)
print("Сортировка по отклонению от среднего ASCII первой строки:", sorted_by_deviation)
print("Сортировка по отклонению от максимального ASCII тройки:", sorted_by_triplet_deviation)
print("Сортировка по количеству зеркальных троек:", sorted_by_mirror_triplets)
