
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class Bulldog(Dog):
    def run(self):
        print(f"{self.name} runs slowly")

animal_obj = Animal("Generic Animal")
dog_obj = Dog("Buddy")
bulldog_obj = Bulldog("Rocky")

print("Calling speak() on Animal object:")
animal_obj.speak()

print("\nCalling speak() on Dog object:")
dog_obj.speak()

print("\nCalling speak() and run() on Bulldog object:")
bulldog_obj.speak()
bulldog_obj.run()
