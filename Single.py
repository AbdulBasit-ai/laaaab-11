# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Creating instances of the classes
animal_obj = Animal("Generic Animal")
dog_obj = Dog("Buddy")

# Calling methods of the classes
print("Calling speak() on Animal object:")
animal_obj.speak()

print("\nCalling speak() on Dog object:")
dog_obj.speak()
