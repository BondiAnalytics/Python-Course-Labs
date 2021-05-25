'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet:
    def __init__(self, size, color) -> None:
        self.size = size
        self.color = color

earth = Planet("Medium", "Blue")
print(earth.color)
    
