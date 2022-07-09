import math

side1 = int(input("input side1: "))
side2 = int(input("input side2: "))
side3 = int(input("input side3: "))
    
side_set = [side1,side2,side3]
side_set.sort()

if side_set[0] + side_set[1] > side_set[2]:
    perimeter = side1 + side2 + side3
    
    s = (perimeter) / 2
    d = s * (s-side1) * (s-side2) * (s-side3)
    area = math.sqrt(d)
    
    print("\n")
    print("conversion arrives decimally hind two.")
    print("According to Python's rounding rules, The result might be different")
    print("-------------------------------------------------------------------")
    print("perimeter: %.2f" % perimeter)
    print("area: %.2f" % area)
else:
    print("Unable to form a triangle")

