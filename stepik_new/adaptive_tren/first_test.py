
#word_list = input().split(' ')

test_string = 'Beautiful is better than ugly. Explicit is better than implicit.'
word_list = sorted(test_string.split(' '))
letters = []
for words in word_list:
    letters.append(len(words))

print (word_list)
print(letters)
letters = sorted(letters)
print(letters)
qwe = []
for letter in letters:
    qwe.append(str(letter))
print(qwe)

