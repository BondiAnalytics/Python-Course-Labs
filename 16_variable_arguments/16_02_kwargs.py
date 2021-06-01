'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def race_distances(**kwargs):
    for i, k in kwargs.items():
        print(i, k)

race_distances(June = '5k', July = '5k', August = '5k', September = '10k')