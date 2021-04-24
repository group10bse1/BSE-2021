Nickel = 25
Dimes = 25
Quater = 25
Ones = 0
Fives = 0
balance = None

while True:
    print('Stock is as follows')
    print('Nickel ' + str(Nickel))
    print('Dimes ' + str(Dimes))
    print('Quater ' + str(Quater))
    print('One ' + str(Ones))
    print('Five ' + str(Fives))

    user_prompt = input("Enter the purchase price xx.xx:  ")
    if user_prompt == "q":
        print("Quited....")
        break
    elif user_prompt != "q":
        try:

            new_price = 100 * float(user_prompt)
            # num_decimal = input_data.split('.')
            balance = new_price

            while True:
                if new_price > 0 and (new_price % 0.5 == 0) and balance > 0:
                    print("'n' - deposit a nickel\n")
                    print("'d' - deposit a dime\n")
                    print("'q' - deposit a quarter\n")
                    print("'o' - deposit a one dollar bill\n")
                    print("'f' - deposit a five dollar bill\n")
                    print("'c' - Cancel the purchase\n")
                    print(f"Payment due is: " + str(balance))
                    menu = input("Enter any of the above..: ")
        except:
            print("error")
