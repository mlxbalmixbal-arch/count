num = int(input('введи число'))
for i in range(2, num, 2):
    print(i, end=' ')
print('всего чисел', num // 2 - 1)