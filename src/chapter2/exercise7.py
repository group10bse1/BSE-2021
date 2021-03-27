# defining the dollar notes
d20 = 20
d10 = 10
d5 = 5
d1 = 1
# defining the dollar coins
quarter = 0.25
dimes = 0.1
nickel = 0.05
penny = 0.01
#  defining user input
amount = float(input("Enter an amount to make change for :"))
print("Your change is:")
# calculating the twenties
twenties = int(amount//d20)
print(str(twenties) + " twenties")
# calculating the tens
t_balance = (amount % d20)
tens = int(t_balance//d10)
print(str(tens) + " ten")
#  calculating fives
tens_balance = (t_balance % d10)
fives = int(tens_balance//d5)
print(str(fives) + " five")
# calculating ones
fives_balance = (tens_balance % d5)
ones = int(fives_balance//d1)
print(str(ones) + " ones")
# calculating quaters
ones_balance = (fives_balance % d1)
quarters = int(ones_balance // quarter)
print(str(quarters) + " quarters")
# calculating dimes
quarter_balance = (ones_balance % quarter)
dimes_n = int(quarter_balance // dimes)
print(str(dimes_n) + " dimes")
# calculating nickels
dimes_balance = (quarter_balance % dimes)
nickels_n = int(dimes_balance // nickel)
print(str(nickels_n) + " nickels")
# calculating penny
nickel_balance = (dimes_balance % nickel)
penny_n = int(nickel_balance // penny)
print(str(penny_n) + " pennies")