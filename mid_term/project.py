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
        print("customer code: ", c_code)
        print("Beginning meter reading: ", f_reading)
        print("Ending meter reading: ", e_reading)
        print(gallon)
    else:
        quit()
