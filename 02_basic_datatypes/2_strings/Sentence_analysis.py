import string

sentence = str(input("Enter a sentence: ", ))

sentence = sentence.replace(" " , " ")

print(sentence)

uc = 0
for i in range(len(sentence)):
    if sentence[i].isupper():
        uc = uc + 1
uc_dict = {"Upper Case:" , uc}

lc = 0
for i in range(len(sentence)):
    if sentence[i].islower():
        lc = lc + 1
lc_dict = {"Lower Case:" , lc}

punc = 0
for i in sentence:
    if i in string.punctuation:
        punc = punc + 1
punc_dict = {"Punctuation:" , punc}

tchar = uc + lc + punc
tchar_dict = ["Total characters:" , tchar]

print(uc_dict)
print(lc_dict)
print(punc_dict) 
print(tchar_dict)