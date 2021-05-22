doc = open('romeo.txt','r')
lines = doc.readlines()
general_list = []
def fun_split(data):
    line = data.split(' ')
    for word in line:
        for i in general_list:
            if word != i:
                general_list.append(word)

    return line

for line in lines:
    fun_split(line)

# def split_func(data):
#     new_data =data.split(' ')

