try:
    hand = open('mbox-short.txt')
    count = 0
    for line in hand:
        words = line.split()
        if (len(words) == 0) or (words[0] != 'From'):
            continue
        count += 1
        print(words[1])
    print(f'{count} empty')
except:
    print('file not found')