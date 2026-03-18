color1 = input("Введите первый основной цвет (красный, синий, желтый): ").lower()
color2 = input("Введите второй основной цвет (красный, синий, желтый): ").lower()

if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
    print("Фиолетовый")
elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
    print("Оранжевый")
elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
    print("Зеленый")
else:
    print("Ошибка: нужно ввести два разных основных цвета")