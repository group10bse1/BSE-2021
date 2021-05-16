fname = input('Enter file name:')
if fname == 'na na boo boo':
    print("NA NA BOO BOO To YOU -You have punk'd!'")
    quit()
count = 0
try:
    fopen = open(fname)
    for line in fopen:
         if line.startswith('Subject'):
             count = count + 1
    print('There were ', count, ' subject lines in', fname)
except:
    print('File cannot be opened: ', fname)
    quit()
