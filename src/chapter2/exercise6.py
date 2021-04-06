#d represents distance between points
#x1 and y1 represent the first coordinates
#x2 and y2 represent the second coordinates
#sqrt represents the calculated distances between the two points
x1 = int(input("x1= "))
y1 = int(input("y1= "))
x2 = int(input('x2='))
y2 = int(input("y2= "))
d = (x2-x1)**2+(y2-y1)**2
sqrt = d**0.5
print(sqrt)

