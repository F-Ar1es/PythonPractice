import random

stop = True
other_time = True
first_time = 0
roll_time = 0

win_list = [7,11]
lost_list = [2,3,12]
roll_list = []

def roll():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = int(a+b)
    
    return c

while stop:
    first_roll = roll()
    if first_roll in win_list and first_time == 0:
        print(f"Your are winner,the first roll is {first_roll}")
        stop = False
    elif first_roll in lost_list and first_time == 0:
        print(f"you lost, the first roll is {first_roll}")
        stop = False
    else:
        roll_list.append(first_roll)
        print(f"first roll is {first_roll}")
        while other_time:
            again = roll()
            if again in roll_list:
                print(f"{again}, happen again.congratulations")
                stop = False
                other_time = False
            elif again == 7:
                print("Oh no,the devil is coming")
                stop = False
                other_time = False
            else:
                roll_list.append(again)
                roll_time + 1
                print(roll_list)