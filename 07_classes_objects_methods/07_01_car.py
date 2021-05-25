'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''
class Car:    
    '''The Car class provides model, year and speed data about specified cars.'''
    def __init__(self, model, year, max_speed=0):
        self.model = model
        self.year = year
        self.speed = max_speed

    def accelerate(self):
        "This method automatically adds 5 km/hr to a car's speed"
        self.max_speed += 5
        return self.max_speed
        
weekend_warrior = Car("Porsche", "2016", 185)
daily_driver = Car("Toyota", "2021", 85)

print(weekend_warrior.model, daily_driver.model)
print(weekend_warrior.year)
print(weekend_warrior.year)
print(daily_driver.model)
print(daily_driver.year)