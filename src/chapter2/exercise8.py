# Defining initial amount
# C is initial investment
C = float(input("Enter initial count C:"))
# r is yearly rate
r = float(input("enter rate in the decimal r: "))
# n is number of times the interest is compounded per year
n = int(input("Enter the number of times interest is compounded n:"))
# t is the number of years until maturation
t = int(input("enter the years until maturation t: "))
# p is the final value of investment
p = C*(1+(r/n))**(n*t)
# final_value
final_value = round(p, 2)
print(final_value)
# End
