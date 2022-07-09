def digital_sorting():
    '''
    将传入的范围传入, 分类出奇数列表和偶数列表
    返回值为 even_number_set 和 odd_number_set 皆为列表
    '''
    even_number_set = []
    odd_number_set = []
    for num in set_range:
        if num % 2 == 0:
            even_number_set.append(num)
        if num % 2 == 1:
            odd_number_set.append(num)

    return even_number_set, odd_number_set

def print_sum():
    '''
    从范围直接取值,计算总和并打印
    '''
    total = 0
    for number in set_range:
        total = total + number
    print(total)

def print_even_number():
    '''
    从数字分类的函数返回值中取偶数列表, 进行加法运算后打印
    '''
    even_number_total = 0
    for even_number in digital_sorting()[0]:
        even_number_total = even_number_total + even_number
    print(f"In this range, the sum of the even numbers is {even_number_total}")

def print_odd_number():
    '''
    从数字分类的函数返回值中取奇数列表, 进行加法运算后打印
    '''
    odd_number_total = 0
    for odd_number in digital_sorting()[1]:
        odd_number_total = odd_number_total + odd_number
    print(f"In this range, the sum of the odd numbers is {odd_number_total}")
    
if __name__ == "__main__":
    first_num = int(input("input your first number: "))
    end_num = int(input("input your end num: "))
    set_range = list(range(first_num, end_num+1))
    
    print_sum()
    print_even_number()
    print_odd_number()