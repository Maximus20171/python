sec = int(input('Введите число секунд '))
hour = sec // 3600
minute = sec // 60 - hour * 60
second = sec % 60
print(f'{hour:02d}:{minute:02d}:{second:02d}')