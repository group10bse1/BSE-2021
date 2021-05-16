str = 'X-DSPAM-Confidence:0.8475'
index = str.find(':')
number = str[index+1:]
number_float = float(number)
print(number_float)