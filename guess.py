import random
num = random.randint(1,100)

while True:
    number = input("猜整數數字:")
    number = int(number)
    if number == num:
        print("猜對了!")
        break
    elif num < number:
        print('比答案大')
    elif num > number:
        print('比答案小')