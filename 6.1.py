def dir(n):
    if n % 3 == 0:
        return True
    else:
        return False

num = int(input("Введите число: "))

if dir(num):
    print("Делится на 3")
else:
    print("Не делится на 3")