print('''
      ------------------------------------------
      | Input inch like "10.43 inch"           |
      | Input cm like "20.3 cm"                |
      | conversion arrives decimally hind two. |
      | Enter "Ctrl" + "c" exit the program    |
      ------------------------------------------
      ''')

def split_input():
    '''
    分割输入, 返回一个数值和单位
    '''
    feed_in_list = feed_in.split(" ")
    value = float(feed_in_list[0])
    unit = feed_in_list[1]
    
    return value,unit
    
def inch2cm():
    '''
    根据公式直接换算树脂后打印
    '''
    unconverted = round(split_input()[0], 2)
    result = round((unconverted * 2.54), 2)
    print(f"{feed_in} = {result} cm")
    print(notice)


def cm2inch():
    '''
    根据公式直接换算树脂后打印
    '''
    unconverted = round(split_input()[0], 2)
    result = round((unconverted /  2.54), 2)
    print(f"{feed_in} = {result} inch")
    print(notice)
    
if __name__ == '__main__':
    '''
    主程序, 分割输入后, 根据单位执行对应函数
    '''
    while True:
        try:
            feed_in = input("Input you numerical value: ")
            notice = "According to Python's rounding rules, The result might be different"
            if split_input()[1] == 'inch':
                inch2cm()
            elif split_input()[1] == 'cm':
                cm2inch()
            else:
                print("Input error, please check it then try again.")
        except KeyboardInterrupt:
            break