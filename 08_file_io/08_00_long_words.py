'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

words = []

with open("words.txt", "r") as fin:
    for line in fin.readlines():
        line = line.rstrip()
        words.append(line)

long_words = []

for word in words:
    if len(word) > 20:
        long_words.append(word)

print(long_words)
print(len(long_words))