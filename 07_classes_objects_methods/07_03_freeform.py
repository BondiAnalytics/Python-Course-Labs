'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

from typing import SupportsFloat


class Running_shoes:
    def __init__(self, weight, surface, distance = 0):
        self.weight = weight
        self.surface = surface
        self.distance = distance

    def buy(self):
        if 250 - int(self.distance) <= 0:
            print(f"You've run {(250 - self.distance)*-1} extra miles in these shoes, so it's time to buy new ones.")
        else:
            print("Let's go for a run!")


class Golf_clubs:
    def __init__(self, distance, accuracy, price):
        self.distance = distance #yards
        self.accuracy = accuracy #bad, better, best
        self.price = price #integer
    
    def __str__(self):
        return f'$ {self.price} gets you clubs that can go {self.distance} yards, but have {self.accuracy} accuracy'

class trails:
    def __init__(self, distance, conditions, surface_type):
        self.distance = distance #miles
        self.conditions = conditions #muddy, steep, flat, etc
        self.surface_type = surface_type #paved, smooth, rocky
    
    def __add__(self, other):
        distance = self.distance + other.distance
        return distance

my_shoes = Running_shoes("9oz", "Track", 252) 
my_shoes2 = Running_shoes("10oz", "Trail", 30)
print(my_shoes.buy())
print(my_shoes2.buy())

my_clubs = Golf_clubs(200, "better", 900)
my_clubs2 = Golf_clubs(100, "bad", 200)
print(str(my_clubs))
print(str(my_clubs2))

my_trails = trails(5, "steep", "rocky")
my_trails2 = trails(26.2, "flat", "paved")
print(f'{my_trails.distance} miles')
print(f'{my_trails2.distance} miles')