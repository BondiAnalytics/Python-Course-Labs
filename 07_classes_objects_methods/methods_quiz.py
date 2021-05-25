# class Car:    
#     '''The Car class provides model, year and speed data about specified cars.'''
#     def __init__(self, model, year, speed=0):
#         self.model = model
#         self.year = year
#         self.speed = speed

#     def accelerate(self):
#         "This method automatically adds 5 km/hr to a car's speed"
#         self.speed += 5
#         return self.speed

#     def brake(self):
#         "This method automatically substracts 5 km/hr to a car's speed"
#         self.speed -= 5
#         return self.speed

#     def honk_horn(self):
#         '''Prints a statement about honking a horn.'''
#         print(f"{self.model} goes 'beep' beep'")

# MY_CAR = Car("Toyota", "1975")

# print(MY_CAR.speed)

# MY_CAR = Car("Zatava", "2001", 30)
# MY_CAR.accelerate()
# MY_CAR.accelerate()
# MY_CAR.brake()
# print(MY_CAR.speed)

# MY_CAR = Car("Rust bucket", "1987")
# MY_CAR.honk_horn()


class Class1:
    def __init__(self, x):
        self.x = x

class Class2(Class1):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

b = Class2(1,5)
print(b.y + b.x)