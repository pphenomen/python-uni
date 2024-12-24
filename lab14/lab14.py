import xml.etree.ElementTree as ET

# Функция для парсинга OSM файла и извлечения гостиниц
def parse_osm(file_path):
    hotels = []

    # Парсим XML
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Ищем элементы с тегами tourism=hotel
    for element in root.findall(".//node") + root.findall(".//way"):
        tags = {tag.get('k'): tag.get('v') for tag in element.findall(".//tag")}
        if 'tourism' in tags and tags['tourism'] == 'hotel':
            name = tags.get('name', 'Unknown')  # Если имя отсутствует, используем 'Unknown'
            hotels.append(name)

    return hotels

# Пути к 
file1_path = "lab14/2.osm"
file2_path = "lab14/2 - 2.osm"

# Парсим файлы
hotels_file1 = parse_osm(file1_path)
hotels_file2 = parse_osm(file2_path)

# Объединяем, удаляем дубликаты и сортируем
all_hotels = sorted(set(hotels_file1 + hotels_file2))

# Вывод результатов
print(f"Количество гостиниц: {len(all_hotels)}")
print("Список гостиниц:")
for hotel in all_hotels:
    print(hotel)
