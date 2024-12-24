# Вариант 2. Словарь синонимов
# Вам дан ловарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны. 
# Для слова из словаря, записанного в последней строке, определите его синоним.

n = int(input("Введите количество пар слов: "))

synonyms_dictionary = {}

print("Заполните словарь парами синонимов (через пробел): ")
for _ in range(n):
    word1, word2 = input().split()
    synonyms_dictionary[word1] = word2
    synonyms_dictionary[word2] = word1

word_to_find = input("Введите слово для поиска синонима:").strip()

if word_to_find in synonyms_dictionary:
    print(f"Найденный синоним: {synonyms_dictionary[word_to_find]}")
else:
    print("Синоним не найден")
