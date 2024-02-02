from random import randint

number = randint(1, 100)
print(number)
print('Угадайте число от 1 до 100')

while True:
    # Получаем число от пользователя и сохраняем его в переменную.
    guess = int(input('Введите число: '))
    if guess < number:
        # ...выводим сообщение.
        print('Ваше число меньше того, что загадано.')
    elif guess > number:
        # ...выводим сообщение.
        print('Ваше число больше того, что загадано.')
    elif guess == number:
        # ...прерываем выполнение программы и...
        break

print('Отличная интуиция! Вы угадали число :)')
