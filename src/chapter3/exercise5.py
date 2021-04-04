# payment for the wedding
guests = input("enter number of guests:")
try:
    guests = int(guests)
    if guests <= 50:
        print("$4000")
    elif guests <= 100:
        print("$10,000")
    elif guests <= 200:
        print("$15,000")
    else:
        print("$20,000")
except:
    guests = str(guests)
    print("enter figure of the guests")
    exit()

