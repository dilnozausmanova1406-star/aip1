import random

a = random.randint(1, 10)
b = random.randint(1, 10)

print(f"{a} + {b} = ", end="")
answer = int(input())

if answer == a + b:
    print("Правильно!")
else:
    print("Неправильно. Ответ:", a + b)