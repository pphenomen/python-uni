import sqlite3
from flask import Flask, request, render_template_string, send_file
import xml.etree.ElementTree as ET
import os

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('music.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        conn = get_db()
        cursor = conn.cursor()
        
        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        ''')

        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            artist_id INTEGER,
            year INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id)
        );
        ''')

        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS tracks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            album_id INTEGER,
            duration INTEGER,
            FOREIGN KEY (album_id) REFERENCES albums(id)
        );
        ''')

        # Очистка данных перед вставкой
        cursor.execute("DELETE FROM artists;")
        cursor.execute("DELETE FROM albums;")
        cursor.execute("DELETE FROM tracks;")
        
        # Заполнение таблиц
        cursor.execute(""" 
                       INSERT INTO artists (name) VALUES
                       ('Drake'),
                       ('Eminem'),
                       ('Kanye West');
                       """)
        cursor.execute(""" 
                       INSERT INTO albums (title, artist_id, year) VALUES 
                       ('Scorpion', 1, '2018'),
                       ('Encore', 2, '2004'), 
                       ('Donda', 3, 2021);
                       """)
        cursor.execute(""" 
                       INSERT INTO tracks (title, album_id, duration) VALUES
                       ('Elevate', 1, '185'),
                       ('Nonstop', 1, '239'),
                       ('Evil Deeds', 2, '259'),
                       ('Mosh', 2, '317'),
                       ('Jail', 3, '297'),
                       ('Moon', 3, '156');
                       """)
        conn.commit()

# Стартовая страница
@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM artists')
    artists = cursor.fetchall()

    # Запрос для получения самого длинного трека для каждого альбома
    cursor.execute('''
        SELECT albums.title AS album_title, tracks.title AS track_title, MAX(tracks.duration) AS max_duration
        FROM tracks
        JOIN albums ON tracks.album_id = albums.id
        GROUP BY albums.id
        ORDER BY max_duration DESC;
    ''')
    longest_tracks = cursor.fetchall()  # Убедитесь, что это результат запроса, а не функция

    return render_template_string('''
    <html>
    <body>
        <h1>Артисты</h1>
        <ul>
        {% for artist in artists %}
            <li>{{ artist['name'] }}</li>
        {% endfor %}
        </ul>
        
        <h2>Добавление артиста</h2>
        <form action="/add_artist" method="POST">
            <label for="name">Имя артиста:</label><br>
            <input type="text" id="name" name="name"><br><br>
            <input type="submit" value="Добавить артиста">
        </form>
        
        <h2>Экспорт артистов в XML</h2>
        <form action="/export_artists" method="GET">
            <input type="submit" value="Экспорт в XML">
        </form>
        
        <h2><a href="/albums">Посмотреть альбомы</a></h2>
        <h2><a href="/tracks">Посмотреть треки</a></h2>
        <h2><a href="/longest_tracks">Посмотреть треки</a></h2>
    
    </body>
    </html>
    ''', artists=artists, longest_tracks=longest_tracks)


# Добавление нового исполнителя
@app.route('/add_artist', methods=['POST'])
def add_artist():
    name = request.form['name']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO artists (name) VALUES (?)', (name,))
    conn.commit()
    return index()

# Экспорт исполнителей в XML
@app.route('/export_artists', methods=['GET'])
def export_artists():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM artists')
    artists = cursor.fetchall()

    root = ET.Element("artists")
    for artist in artists:
        artist_elem = ET.SubElement(root, "artist")
        ET.SubElement(artist_elem, "id").text = str(artist['id'])
        ET.SubElement(artist_elem, "name").text = artist['name']
    
    tree = ET.ElementTree(root)
    # Сохраняем файл на сервере
    xml_file = "artists.xml"
    tree.write(xml_file)
    
    # Отправляем файл пользователю для скачивания
    return send_file(xml_file, as_attachment=True)

# Запрос на вывод альбомов
@app.route('/albums')
def show_albums():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT albums.title, artists.name, albums.year FROM albums
                      JOIN artists ON albums.artist_id = artists.id''')
    rows = cursor.fetchall()
    
    result = "<h1>Albums</h1><ul>"
    for row in rows:
        result += f"<li>Title: {row['title']}, Artist: {row['name']}, Year: {row['year']}</li>"
    result += "</ul>"
    return result

# Запрос на вывод треков
@app.route('/tracks')
def show_tracks():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT tracks.title, albums.title AS album_title, tracks.duration FROM tracks
                      JOIN albums ON tracks.album_id = albums.id''')
    rows = cursor.fetchall()
    
    result = "<h1>Tracks</h1><ul>"
    for row in rows:
        result += f"<li>Title: {row['title']}, Album: {row['album_title']}, Duration: {row['duration']} seconds</li>"
    result += "</ul>"
    return result

# Запрос на вывод самого длинного трека для каждого альбома
@app.route('/longest_tracks')
def longest_tracks():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT albums.title AS album_title, tracks.title AS track_title, MAX(tracks.duration) AS max_duration
        FROM tracks
        JOIN albums ON tracks.album_id = albums.id
        GROUP BY albums.id
        ORDER BY max_duration DESC;
    ''')
    rows = cursor.fetchall()
    
    result = "<h1>Самые долгие треки в каждом альбоме</h1><ul>"
    for row in rows:
        result += f"<li>Album: {row['album_title']}, Track: {row['track_title']}, Duration: {row['max_duration']} seconds</li>"
    result += "</ul>"
    return result

# Запуск приложения
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
