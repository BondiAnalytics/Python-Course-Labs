'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.

Tip: Use an if statement in the listcomp

'''

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

fish_list = list(fish_tuple)

print([i for i in fish_list if i[-4:] == "fish"])

# fishy = []
# for i in fish_tuple:
#