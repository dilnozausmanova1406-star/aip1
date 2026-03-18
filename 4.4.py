primary_colors = ["красный", "синий", "желтый"]

color1 = input("Введите первый основной цвет: ").lower()
color2 = input("Введите второй основной цвет: ").lower()

mix = {
    frozenset(["красный", "синий"]): "Фиолетовый",
    frozenset(["красный", "желтый"]): "Оранжевый",
    frozenset(["синий", "желтый"]): "Зеленый"
}

if color1 not in primary_colors or color2 not in primary_colors or color1 == color2:
    print("Ошибка: нужно ввести два разных основных цвета (красный, синий, желтый)")
else:
    print("Результат смешивания:", mix[frozenset([color1, color2])])