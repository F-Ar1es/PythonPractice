def judge_grade():
    if 0 <= after_judge <= 100:
        if after_judge >= 90:
            print("grade = A")
        elif after_judge >= 80:
            print("grade = B")
        elif after_judge >= 70:
            print("grade = C")
        elif after_judge >= 60:
            print("grade = D")
        else:
            print("grade = E")
    else:
        print(error_massage)

if __name__ == "__main__":
    while True:
        try:
            error_massage = "Incorrect input, please check."
            score = input("Input your score: ")
            
            if str.isdigit(score) == True:
                after_judge = float(score)
                judge_grade()
            else:
                print(error_massage)
        except KeyboardInterrupt():
            break