def investiment(initial, rate, time, number):
    print(initial*(1 + rate/number)**(time*number))


c = int(input("enter initial: "))
r = float(input("enter rate: "))
t = int(input("enter time: "))
n = int(input("enter number: "))
investiment(c, r, t, n)


