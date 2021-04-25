Nickel = 25
Dimes = 25
Quater = 25
Ones = 0
Fives = 0
balance = 0

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
                    print("'n' - deposit a nickel")
                    print("'d' - deposit a dime")
                    print("'q' - deposit a quarter")
                    print("'o' - deposit a one dol0lar bill")
                    print("'f' - deposit a five dollar bill")
                    print("'c' - Cancel the purchase")
                    print(f"Payment due is: {int(balance // 100)} dollars and {int(balance % 100)} cents\n")
                    menu = input("Enter any of the above..: ")
                    if menu == "d":
                        balance -= 0.1 * 100
                        print(balance)
                        Dimes += 1


                    elif menu == "n":
                        balance -= 0.05 * 100
                        Nickel += 1

                    elif menu == "q":
                        balance -= 0.1 * 100
                        Quater += 1
                    elif menu == "o":
                        balance -= 1 * 100
                        Ones += 1

                    elif menu == "f":
                        balance -= 5 * 100
                        Fives += 1
                    elif menu == "c":
                        break
                    else:
                        print(menu + " is not valid selection")
                elif new_price < 0:
                    print("illegal entry...")
                elif balance <= 0:
                    change = float(balance * -1)

                    if 0.05 <= change <= 0.09:
                        n = round(change / 0.05, 2)
                        Nickel -= n
                        if Nickel >= n:
                            print(f"\nChange is: {n} Nickel")
                        elif Nickel != 0:
                            rem = n - Nickel
                            print('\nThe nickles are not enough\n'
                                  ''f"Pick {Nickel} from the dispensor\n"
                                  f" Pick {rem} as the balance from...")
                        else:
                            print('')
                    elif 0.1 <= change <= 0.24:
                        d = change / 0.1
                        print(f"\nChange is: {d} dollars")
                    elif 0.25 <= change <= 0.9:
                        q = change / 0.25
                        print(f"\nChange is: {q} Quaters")
                    break
                else:
                    print("Enter correct price foramt")
                    break
        except:
            print("error")
