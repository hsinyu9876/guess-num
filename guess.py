import random
start = input('請決定隨機數字範圍開始值:')
start = int(start)
end = input('請決定隨機數字範圍結束值:')
end = int(end)

num = random.randint(start, end)
count = 0
while True:
    count += 1 #count = count + 1
    number = input('猜整數數字:')
    number = int(number)
    if number == num:
        print('猜對了!')
        print('這是你猜的第', count, '次')
        break
    elif number > num:
        print('比答案大')
    elif number < num:
        print('比答案小')
    print('這是你猜的第', count, '次')