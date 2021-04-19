# calculating final value of investment
def investment(initial, rate, time, number):
    print(initial*(1 + rate/number)**(time*number))


c = input("enter initial amount: ")
r = input("enter rate: ")
t = input("enter time: ")
n = input("enter number of times: ")
try:
    c = int(c)
    r = float(r)
    t = int(t)
    n = int(n)
except:
    print("Enter numeric inputs")
    exit()
investment(c, r, t, n)
