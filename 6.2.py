def dir(x):
    return 100 / x

try:
    num = float(input("Введите число: "))
    print("Результат:", dir (num))

except ValueError:
    print("Ошибка: введено не число")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
except Exception:
    print("Неизвестная ошибка")