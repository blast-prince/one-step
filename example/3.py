import random

secret = random.randint(1, 100)
print("我已经想好了一个1到100之间的数字！")

while True:
    guess = input("你猜是多少？")
    guess = int(guess)
    
    if guess < secret:
        print("太小了，再试试！")
    elif guess > secret:
        print("太大了，再试试！")
    else:
        print("恭喜你猜对了！")
        break

input("按回车键结束...")