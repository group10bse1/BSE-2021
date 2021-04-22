count = 0
total = 0
average = 0
# using a loop to repeatedly get numbers
while True:
    number = input("Enter a number: ")
    if number == "done":
        print(total, count, average)
        break
        # breaking out of the loop to stop receiving inputs from user
    else:
        try:
            number = float(number)
            # for every number perform actions in loop below
            while True:
                count = int(count + 1)
                total = int(total + number)
                average = total/count
                break
                # end of for every number loop
            continue  # go to the top of loop where we get user enters number
        except:
            print('Invalid input')
            continue

