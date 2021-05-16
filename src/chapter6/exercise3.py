def count(string_p, letter_p):
    count_x = 0
    for letter in string_p:
        if letter == letter_p:
            count_x = count_x + 1
    return count_x
word = input('Enter word:')
letter_x = input('Enter letter:')
print(count(word, letter_x))