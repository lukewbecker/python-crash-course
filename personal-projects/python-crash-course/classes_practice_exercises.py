# Writing my first Class!

class Dog:
    '''A simple attempt to model a dog.'''

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")



# Making an instance from the class:
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# class example dot notation:

my_dog = Dog("Wille", 6)
your_dog = Dog("Lucy", 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# Restaruant class practice:

class Restaurant:
    '''A simple attempt to model a restaraunt guide'''

    def __init__(self, restaurant_name, cuisine_type):
        '''initialize name and type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_reseuarant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

sunrise_cafe = Restaurant("Dawn's Sunrise Cafe", "Southern")

luke_food = Restaurant("Luke")
