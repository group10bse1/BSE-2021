
inital_num = None
number_list = []
while True:
    input_num = input("Enter a list of numbers separated by commas:...")
    numbers = input_num.split(",")
    try:
        for i in numbers:
            num = int(i)

            number_list.append(num)

        print(f"The maximum is {max(number_list)}")
        print(f"The minimum is {min(number_list)}")
    except:
        print("invalid entry check the numbers you have entered")


