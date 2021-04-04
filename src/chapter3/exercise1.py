# a program to compute employee fee
hours = int(input('Enter hours:'))
rate = float(input('Enter rate:'))
# calculating hours above 40
eth = (hours - 40)
# for hours above forty
if hours > 40:
    pay = ((eth * 1.5 * rate) + (40 * rate))
    print(pay)
# for hours less than or equal to 40
else:
    pay2 = (rate * hours)
    print(pay2)
