'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]


for item in famous_quotes:
    quote_string = item["quote"]
    full_name_string = item["full_name"]
    #print(quote, full_name)
    full_name_split = full_name_string.split()
    #print("\""+ quote + "\"" + " - " + full_name_split[1] + ", " + full_name_split[0])
    print(f"{quote_string} - {full_name_split[1]}, {full_name_split[0]}")

    # item['quote'] + item['full_name']
    # print(item['quote'] + item['full_name'])

# quotes = [i["quote"] for i in famous_quotes]
# #print(quotes)

# full_names = [i["full_name"] for i in famous_quotes]
# full_names = [word for line in full_names for word in line.split()]
# full_names.remove("W.")
# #print(full_names)

# first_names = []
# for index, first_name in enumerate(full_names):
#      if index % 2 == 0:
#           first_names.append(first_name)
# #print(first_names)

# last_names = []
# for index, last_name in enumerate(full_names):
#      if index % 2 != 0:
#          last_names.append(last_name)
# #print(last_names)

# attributed_quotes = []
# for i in attributed_quotes:
#      attributed_quotes.append(f"{quotes[i]}, - {last_names[i]}, {first_names[i]}")

# print(attributed_quotes)