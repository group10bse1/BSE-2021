# program of whether people can vote according to their age
age = input("enter your age:")
try:
    age = int(age)
# for the age of 18 and above
    if age >= 18:
        print("you can vote")
# for the age between 0 to 17
    elif age >= 0:
        print('Too young to vote')
# for the age less than 0
    else:
        print('You are a time traveller ')
# for the age not in integer form
except:
    age = str(age)
    print("Enter only integers as age")
    exit()
