def computegrade(score):
    if 1.0 >= score >= 0.0:
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return"B"
        elif score >= 0.7:
            return"C"
        elif score >= 0.6:
            return"D"
        else:
            return"F"
    else:
        return"bad score"


scr = float(input("enter score: "))
print(computegrade(scr))


