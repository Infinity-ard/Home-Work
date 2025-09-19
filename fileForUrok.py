from datetime import datetime

class Pet:
    def __init__(self, name="None", age=0, voice="None"):
        self.name = name
        self.age = age
        self.voice = voice

    def say(self):
        print(f'{self.name} says {self.voice}')

    def get_birthday_year(self):
        current_year = datetime.now().year
        return current_year - self.age


class Cat(Pet):
    def __init__(self, name, age, voice, breed):
        super().__init__(name, age, voice)
        self.breed = breed

    def about(self):
        print(f'{self.name} is {self.age} years old and is a {self.breed}')

class Dog(Pet):
    def __init__(self, name, age, voice, breed):
        super().__init__(name, age, voice)
        self.breed = breed

    def about(self):
        print(f'{self.name} is a {self.age}-year-old {self.breed}')

murchik = Cat("Murchik", 3, "Meow", "British Shorthair")
murchik.say()
murchik.about()
print(f"{murchik.name} was born in {murchik.get_birthday_year()}")

rex = Dog("Rex", 5, "Woof", "German Shepherd")
rex.say()
rex.about()
print(f"{rex.name} was born in {rex.get_birthday_year()}")
