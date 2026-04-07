def dilya(ticket):
    digits = list(ticket)
    length = len(digits)
    half = length // 2
    sum1 = 0
    sum2 = 0
    i = 0
    while i < half:
        sum1 = sum1 + int(digits[i])
        i = i + 1

    i = half
    while i < length:
        sum2 = sum2 + int(digits[i])
        i = i + 1

    if sum1 == sum2:
        return True
    else:
        return False
dilya_input = input("Введите номер билета: ")
if dilya(dilya_input):
    print("Счастливый билет")
else:
    print("Несчастливый билет")