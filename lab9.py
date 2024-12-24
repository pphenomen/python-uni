import matplotlib.pyplot as plt

class Polygon:
    def __init__(self, id, vertices):
        if len(vertices) < 3:
            raise ValueError("Многоугольник должен иметь минимум 3 вершины.")
        self.id = id
        self.vertices = vertices  # Список координат вершин

    def move(self, delta_x, delta_y):
        self.vertices = [(x + delta_x, y + delta_y) for x, y in self.vertices]

    def get_full_box(self):
        x_coords, y_coords = zip(*self.vertices)
        return min(x_coords), max(x_coords), min(y_coords), max(y_coords)

    def plot(self, ax, color='blue'):
        x_coords, y_coords = zip(*self.vertices)
        x_coords = list(x_coords) + [x_coords[0]]  # Добавляем первую вершину в конец списка, чтобы замкнуть многоугольник
        y_coords = list(y_coords) + [y_coords[0]]
        ax.plot(x_coords, y_coords, color=color)
        ax.fill(x_coords, y_coords, color=color, alpha=0.3)

class Quad(Polygon):
    def __init__(self, id, vertices):
        if len(vertices) != 4:
            raise ValueError("Квадрат должен иметь ровно 4 вершины.")
        super().__init__(id, vertices)

class Pentagon(Polygon):
    def __init__(self, id, vertices):
        if len(vertices) != 5:
            raise ValueError("Пятиугольник должен иметь ровно 5 вершин.")
        super().__init__(id, vertices)

# Проверка пересечения
def is_intersect(quad, pentagon):
    quad_full_box = quad.get_full_box()
    pentagon_full_box = pentagon.get_full_box()

    # Проверка не находятся ли прямоугольники полностью по разные стороны друг от друга 
    return not (quad_full_box[1] < pentagon_full_box[0] or pentagon_full_box[1] < quad_full_box[0] or quad_full_box[3] < pentagon_full_box[2] or pentagon_full_box[3] < quad_full_box[2])

try:
    square = Quad("Квадрат", [(0, 0), (4, 0), (4, 4), (0, 4)])
    pentagon = Pentagon("пятиугольник", [(1, 1), (3, 1), (4, 3), (2, 5), (0, 3)])
    
    # Перемещаем объекты
    square.move(1, 1)
    pentagon.move(-5, -5)

    # Визуализация
    fig, ax = plt.subplots()

    square.plot(ax, color='blue') 
    pentagon.plot(ax, color='green')

    # Проверяем пересечение
    if is_intersect(square, pentagon):
        print(f"{square.id} и {pentagon.id} пересекаются.")
    else:
        print(f"{square.id} и {pentagon.id} не пересекаются.")

    # Настройки отображения
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_aspect('equal', 'box')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Визуализация объектов')
    plt.grid(True)
    plt.show()

except ValueError as e:
    print(f"Ошибка значения: {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
