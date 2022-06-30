class Zoo:
    __animals = 0

    def __init__(self, name_of_the_zoo):
        self.name_of_the_zoo = name_of_the_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''

        if species == 'mammal':
            result += f"{species.capitalize()}s in {self.name_of_the_zoo}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"{species.capitalize()}es in {self.name_of_the_zoo}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"{species.capitalize()}s in {self.name_of_the_zoo}: {', '.join(self.birds)}\n"

        result += f"Total animals: {self.__animals}"

        return result


name_of_the_zoo = input()
zoo = Zoo(name_of_the_zoo)
number = int(input())

for x in range(number):
    current_species, current_animal = input().split()

    zoo.add_animal(current_species, current_animal)

species_to_print = input()

print(zoo.get_info(species_to_print))
