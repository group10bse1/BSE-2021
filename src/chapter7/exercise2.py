file = input('Enter the file name: ')
saa = open(file)
count = 0
totali = 0
for line in saa:
    if 'X-DSPAM-Confidence:' in line:
        print(line[-7:])
        count = count + 1
        totali = totali + float(line[-7:])
avrg = totali/count
print('average:', format(avrg,'.12f'))