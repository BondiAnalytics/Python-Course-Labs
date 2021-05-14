#A sixth solution using lamba. It's not quite as elegant as Solution 05, but it's easier to read.

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
unsorted_list.sort(key=lambda a: a[1])
sorted_list = unsorted_list
print(sorted_list)