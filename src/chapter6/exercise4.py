# number of times letter a appears in banana
def county(string_p, letter_p):
    count_x = 0
    for letter in string_p:
        if letter == letter_p:
            count_x = string_p.count(letter)
    return count_x


word = 'banana'
letter_x = "a"
print(county(word, letter_x))
