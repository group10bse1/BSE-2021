# entering customer's code repeatedily.
while True:
    c_code = input('Enter customer code: ')
    if c_code == "r" or c_code == "c" or c_code == "i":
        print("customer code", c_code)
    else:
        quit()
