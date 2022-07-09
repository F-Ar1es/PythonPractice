import random

mun = random.randint(1, 100)
answer = True
print("我是一个 1 到 100 之间的数字")
guess_time = 0

while answer and guess_time < 3:
    guess = int(input("请输入你猜的数字:"))
    if mun == guess:
        print("你猜对了")
        answer = False
    elif mun > guess:
        print("你猜的数字小了")
        guess_time += 1
    elif mun < guess:
        print("你猜的数字大了")
        guess_time += 1
else:
    print("你已经猜错3次啦, 下次再来吧")
    print("我的数字是:", mun)