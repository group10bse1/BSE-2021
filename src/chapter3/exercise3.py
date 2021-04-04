# a program to grade
score = input("enter score:")
# checking for the range of scores
try:
    score = float(score)
    if 1.0 >= score >= 0.0:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
    else:
        print("Bad score")
except:
    score = str(score)
    print("Bad score")
    exit()



