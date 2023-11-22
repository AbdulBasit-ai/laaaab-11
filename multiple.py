
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Bird:
    def fly(self):
        print(f"{self.name} can fly")


class Parrot(Animal, Bird):
    def talk(self):
        print(f"{self.name} can mimic human speech")


parrot_obj = Parrot("Polly")


print("Calling speak(), fly(), and talk() on Parrot object:")
parrot_obj.speak()
parrot_obj.fly()
parrot_obj.talk()
