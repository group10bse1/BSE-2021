# computing pay and overtime
def computepay(hours, rate):
    if hours <= 40:
        return hours*rate
    overtime = hours-40
    return 40*rate + overtime * 1.5 * rate


hrs = int(input("enter hours: "))
rte = int(input("enter rate: "))
print(computepay(hrs, rte))
# printing pay finally

