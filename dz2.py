class Pet:
    def __init__(self, name, age, species, hunger=50, energy=70):
        self.name = name
        self.age = age
        self.species = species
        self.hunger = hunger
        self.energy = energy

    def show_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age} лет")
        print(f"Вид: {self.species}")
        print(f"Голод: {self.hunger}")
        print(f"Енергія: {self.energy}")


# Пример использования:
dog = Pet("Бобик", 3, "Собака", hunger=30, energy=80)
cat = Pet("Мурка", 2, "Кот", hunger=60, energy=50)

dog.show_info()
print("-----")
cat.show_info()
