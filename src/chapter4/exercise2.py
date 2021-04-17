# calculating final value of investment
def investment(initial, rate, time, number):
    print(initial*(1 + rate/number)**(time*number))


c = int(input("enter initial amount: "))
r = float(input("enter rate: "))
t = int(input("enter time: "))
n = int(input("enter number of times: "))
investment(c, r, t, n)


