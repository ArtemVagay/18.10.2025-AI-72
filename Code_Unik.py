import random
import math
island_size = 0
while True:
    island_size = int(input("Введите размер острова(минимум: 2, максимум 4): "))
    if island_size > 1 and island_size < 5:
        break
    print("Ошибка!")
matrix_size = island_size * 15
island_count = random.randint(island_size - 1, island_size)
matrix = [["🌊" for i in range(matrix_size)] for j in range(matrix_size)]

def island_maker(radius, num_points):
    for i in range(num_points):
        radius = radius * (random.randint(10, 15) // 10)
        angle = math.radians(random.randint(0, 360))
        center_x = round(radius * math.cos(angle))
        center_y = round(radius * math.sin(angle))
        for y in range(matrix_size):
            for x in range(matrix_size):
                if x == center_x + matrix_size // 2 and y == center_y + matrix_size // 2:
                    matrix[y][x] = "🌴"
                for _ in range(matrix_size):
                    if x == center_x + matrix_size // 2 + random.randint(-island_size // 2, island_size // 2) and y == center_y + matrix_size // 2 + random.randint(-island_size // 2, island_size // 2):
                        matrix[y + random.randint(-1, 1)][x] = "🌴"
                        matrix[y][x + random.randint(-1, 1)] = "🌴"
                        matrix[y - random.randint(-1, 1)][x] = "🌴"
                        matrix[y][x - random.randint(-1, 1)] = "🌴"
                        matrix[y + random.randint(-1, 1)][x + random.randint(-1, 1)] = "🌴"


island_maker(0, 1)
island_maker(island_size * 5, island_count)

leave = False
while not leave:
    if not leave:
        for y in range(matrix_size):
            if not leave:
                for x in range(matrix_size):
                    if matrix[y][x] == "🌴":
                        rnd = random.randint(0, 1000)
                        if x == matrix_size // 2 + random.randint(-island_size // 4, island_size // 4) and y == matrix_size // 2 + random.randint(-island_size // 4, island_size // 4):
                            if rnd == 1:
                                if matrix[y - 1][x] == "🌊":
                                    matrix[y + 1][x] = "❌"
                                elif matrix[y + 1][x] == "🌊":
                                    matrix[y - 1][x] = "❌"
                                elif matrix[y][x + 1] == "🌊":
                                    matrix[y][x - 1] = "❌"
                                elif matrix[y][x - 1] == "🌊":
                                    matrix[y][x + 1] = "❌"
                                elif matrix[y - 1][x - 1] == "🌊":
                                    matrix[y + 1][x + 1] = "❌"
                                elif matrix[y + 1][x + 1] == "🌊":
                                    matrix[y - 1][x - 1] = "❌"
                                elif matrix[y - 1][x + 1] == "🌊":
                                    matrix[y + 1][x - 1] = "❌"
                                elif matrix[y + 1][x - 1] == "🌊":
                                    matrix[y - 1][x + 1] = "❌"
                                else:
                                    matrix[y][x] = "❌"
                                leave = True
                                break

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()