# "Карточки"
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# Вводится число N, далее еще N − 1 чисел: номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

n = int(input("N: "))
numbers = []
for _ in range(n - 1):
    numbers.append(int(input("number: ")))

numbers.sort(reverse=True)

next_number = n + 1
for number in numbers:
    if next_number - number == 2:
        print(number + 1)
        break
    next_number = number
else:
    print(1)
