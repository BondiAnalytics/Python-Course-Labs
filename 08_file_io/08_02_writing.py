'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

words = []

with open("words.txt", "r") as fin:
    for line in fin.readlines():
        line = line.rstrip()
        words.append(line)

words.reverse()

# print(words[0:10])

words_str = ""
for word in words:
    words_str += str(word) + " "

#print(words_str[0:10])

with open("words_reverse.txt", "w") as fout:
    fout.write(words_str)