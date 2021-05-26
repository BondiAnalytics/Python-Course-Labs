'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

words = []

with open("words.txt", "r") as fin:
    for line in fin.readlines():
        line = line.rstrip()
        words.append(line)

print(min(words, key=len))
print(max(words, key=len))
print(len(words))