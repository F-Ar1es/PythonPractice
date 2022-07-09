for second_num in range(1,10):
    for first_num in range(1,second_num+1):
        result = second_num * first_num
        print(f"{first_num} * {second_num} = {result}",end="\t")
    print("\r")