# 2. Дана строка, состоящая из символов латиницы. Необходимо проверить, упорядочены ли строчные символы этой строки по возрастанию
def is_lowercase_sorted(s):
    lowercase_letters = []
    
    for char in s:
        if char.islower():
            lowercase_letters.append(char)
    
    return lowercase_letters == sorted(lowercase_letters)

s = "aBcDeFg"
print(is_lowercase_sorted(s))

# 10. Дана строка. Необходимо подсчитать количество букв "А" в этой строке 
def count_a(s):
    count = s.count('a')
    
    return f"Количество букв 'а' в строке: {count}"

s = "banana apple analysis"
print (count_a(s))

# 17 Дана строка в которой записан путь к файлу. Необходимо найти имя файла без расширения
import os
path = "C:\Program Files\Git\cmd\git.exe"
print("Имя файла без расширения: ")
print(os.path.basename(path).split('.')[0])

