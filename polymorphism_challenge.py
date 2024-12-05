# polymorphism_challenge.py

# Base class for Animals and Vehicles with a common method move()
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def move(self):
        print("Running")

class Bird(Animal):
    def move(self):
        print("Flying")

# Create objects of each class
car = Car()
plane = Plane()
dog = Dog()
bird = Bird()

# Call move() on each object (Polymorphism in action)
def move_animal_or_vehicle(vehicle_or_animal):
    vehicle_or_animal.move()

# Using polymorphism to call the same method 'move' on different objects
move_animal_or_vehicle(car)
move_animal_or_vehicle(plane)
move_animal_or_vehicle(dog)
move_animal_or_vehicle(bird)
