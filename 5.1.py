n = int(input("Сколько слов: "))
result = ""

for i in range(n):
    word = input("Введите слово: ")
    result += word + " "

print(result)