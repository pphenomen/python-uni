import csv
from datetime import datetime, timedelta
from charset_normalizer import detect


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = detect(raw_data)
        return result['encoding']


def parse_time_spent(time_str):
    try:
        days, hours, minutes, seconds = 0, 0, 0, 0

        if 'дн.' in time_str:
            parts = time_str.split('дн.')
            days = int(parts[0].strip())
            time_str = parts[1].strip() if len(parts) > 1 else ''

        if 'ч.' in time_str or 'час.' in time_str:
            parts = time_str.split('ч.') if 'ч.' in time_str else time_str.split('час.')
            hours = int(parts[0].strip())
            time_str = parts[1].strip() if len(parts) > 1 else ''

        if 'мин.' in time_str:
            parts = time_str.split('мин.')
            minutes = int(parts[0].strip())
            time_str = parts[1].strip() if len(parts) > 1 else ''

        if 'сек.' in time_str:
            parts = time_str.split('сек.')
            seconds = int(parts[0].strip())

        return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    except (IndexError, ValueError):
        raise ValueError(f"Некорректный формат времени: {time_str}")


def filter_test_results(file_path, max_time, exact_score):
    results = []

    encoding = detect_encoding(file_path)

    with open(file_path, 'r', encoding=encoding) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Фамилия'].startswith('Среднее') or row['Имя'].startswith('Среднее'):
                continue

            if row['Состояние'] != 'Завершено':
                continue

            try:
                time_spent = parse_time_spent(row['Затраченное время'])
                score = float(row['Оценка/10,00'].replace(',', '.'))
            except ValueError as e:
                print(f"Ошибка при обработке строки: {e}. Исходные данные: {row}")
                continue

            if time_spent > max_time and score == exact_score:
                results.append(f"{row['Фамилия']} {row['Имя']}")

    return sorted(results)


file_path = "2 - 1.csv"
max_time = timedelta(minutes=30)
exact_score = 10.0

matching_results = filter_test_results(file_path, max_time, exact_score)

print("Количество участников:", len(matching_results))
print("Список участников:")
for participant in matching_results:
    print(participant)