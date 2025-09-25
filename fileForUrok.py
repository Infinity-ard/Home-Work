import random

class Plant:
    def __init__(self, name):
        self.name = name
        self.water_level = 0

    def to_water(self):
        self.water_level += 1

    def to_loosen(self):
        self.water_level += random.randint(0, 2)


class Game:
    def __init__(self):
        self.plants = []

    def add_plant(self, name):
        self.plants.append(Plant(name))

    def play(self):
        while self.plants:
            print("\nCurrent plants:")
            for plant in self.plants:
                print(f"{plant.name} (Water level: {plant.water_level})")

            for plant in list(self.plants):  # копія списку
                action = input(f"Choose an action for {plant.name} (water/loosen/exit): ").strip().lower()
                if action == "water":
                    plant.to_water()
                    print(f"You watered {plant.name}.")
                elif action == "loosen":
                    plant.to_loosen()
                    print(f"You loosened the soil around {plant.name}.")
                elif action == "exit":
                    print("Exiting the game.")
                    return
                else:
                    print("Invalid action. Please choose again.")

                if plant.water_level >= 5:
                    print(f"{plant.name} has grown and is removed from the game!")
                    self.plants.remove(plant)


# --- Головна програма ---
game = Game()

print("Welcome to game 'Roslynctvo'!")
print("Enter plant names (type 'stop' to finish):")

while True:
    name = input("Enter plant name: ").strip()
    if name.lower() == "stop":
        break
    elif name:
        game.add_plant(name)

if game.plants:
    game.play()
else:
    print("No plants were added. Bye!")

print("Game over!")
