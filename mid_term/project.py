# entering customer's code repeatedly.
while True:
    c_code = input('Enter customer code: ')
    if c_code == "r" or c_code == "c" or c_code == "i":
        f_reading = input("Enter beginning meter reading: ")
        e_reading = input("Enter ending meter reading: ")
        if int(e_reading) < int(f_reading):
            em_reading = int(e_reading) + 1000000000
        else:
            em_reading = int(e_reading)
        gallon = (int(em_reading)-int(f_reading))/10
        if c_code == "r":
            bill = format((5 + 0.0005 * gallon), ".2f")
        elif c_code == "c":
            if gallon <= 4000000:
                bill = format(1000, ".2f")
            else:
                a_gallon = gallon - 4000000
                bill = format((a_gallon * 0.00025 + 1000), ".2f")
        # calculating gallons and bills for customer code i
        else:
            if gallon <= 4000000:
                bill = format(1000, ".2f")
            elif gallon <= 10000000:
                bill = format(2000, ".2f")
            else:
                a_gallon = gallon - 10000000
                bill = format((a_gallon * 0.00025 + 2000), ".2f")
        # displaying outputs.
        print("customer code: ", c_code)
        print("Beginning meter reading: ", f_reading)
        print("Ending meter reading: ", e_reading)
        print("Gallons of water used: ", gallon)
        print("Amount billed: "+"$" + str(bill))
    else:
        quit()
