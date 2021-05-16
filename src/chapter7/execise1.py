file = input("Enter a file name: ")
fhand = open(file)
for line in fhand:
    line_new = line.strip()
    print(line_new.upper())