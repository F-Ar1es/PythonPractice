year_input = input("输入年份:")

if year_input.isdigit():
    year = int(year_input)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")
else:
    print("请输入数字年份,例如:2000")