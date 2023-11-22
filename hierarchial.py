
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")


animal_obj = Animal("Generic Animal")
dog_obj = Dog("Buddy")
cat_obj = Cat("Whiskers")


print("Calling speak() on Animal object:")
animal_obj.speak()

print("\nCalling speak() on Dog object:")
dog_obj.speak()

print("\nCalling speak() on Cat object:")
cat_obj.speak()
