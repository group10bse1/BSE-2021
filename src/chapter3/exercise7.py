yes = "Sure , I can work with this"
no = "No thanks , I can find something better"
hate = "No way"
k = "Kampala"
m = 'Mbarara'
s = 'Space'
location = input("Enter location:")
pay = input("Enter the pay:")
try:
    location = str(location)
    pay = int(pay)
    if location.lower() == m.lower():
        if pay > 4000000:
            print(yes)
        else:
            print(no)
    elif location.lower() == k.lower():
        if pay >= 10000000:
            print(yes)
        else:
            print(hate)
    elif location.lower() == s.lower():
        print(yes)
    else:
        if pay >= 6000000:
            print(yes)
        else:
            print(no)
except:
    location = float(location)
    print("Enter a word")
    exit()
    pay = str(pay)
    print("Enter a value")
    exit()