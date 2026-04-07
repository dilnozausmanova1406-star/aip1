def dilya_magic(day, month, year):
    if day * month == year % 100:
        return True
    else:
        return False

dilya_date = input("Введите дату (ДД.ММ.ГГГГ): ")
parts = dilya_date.split(".")

day = int(parts[0])
month = int(parts[1])
year = int(parts[2])

if dilya_magic(day, month, year):
    print("Магическая дата")
else:
    print("Не магическая")