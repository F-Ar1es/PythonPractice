# 设置一个空列表用于接收符合要求的完美数
wanmei = []
# 遍历1到10000的所有数字
for i in range(1, 1000):
    # 设置一个空列表用于接收数字i的所有的整除因子
    list_eve = []
    for j in range(1, i + 1):
        if i % j == 0:
            list_eve.append(j)
    # 所有整除因子去除数字i本身，list_eve列表变为真因子列表
    list_eve.remove(i)
    temp_he = 0
    for h in list_eve:
        temp_he += h
    # 真因子列表各项之和等于数字i本身，那么i为完美数，将i加入完美数列表
    if temp_he == i:
        wanmei.append(i)
# 打印结果
print(wanmei)