# 定义一个函数
def divisor(x, y):
    # 获取最小值
    if x > y:
        small = y
    else:
        small = x

    for i in range(1, small + 1):
        if ((x % i == 0) and (y % i == 0)):
            a = i
    b = a * (x // a) * (y // a)
    print(x, '和', y, '的最大公约数为：{}'.format(a))
    print(x, '和', y, '的最小公倍数为：{}'.format(b))

# 调用greast_common_divisor(num1,num2)函数
divisor(int(input('input x:')), int(input('input y:')))