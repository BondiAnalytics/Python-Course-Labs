'''
Using f-strings, print out the name, last name, and favorite
office supply item of each person in the given dictionary,
formatted like so:

LASTNAME, Name           Office supply item
LONGERLASTNAME, Name     Office supply item

'''

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

for item in office:
    #print(item)
    last_name = item['full_name']
    last_name_list = last_name.split()
    #print(last_name_list)
    favorite_item = item["item"]
    #print(favorite_item)
    Office_supply = "Office supply: "
    LIST = (f"LASTNAME, {last_name_list[1]} {Office_supply : >25} {favorite_item} \n"
            f"LONGERLASTNAME, {last_name} {Office_supply : >5} {favorite_item}")
    print(LIST)
    

counter = 0

for i in range(5):
    string_counter = ""
    for j in range(10):
        string_counter += count() + " "
        count += 1
print(counter)
