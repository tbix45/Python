class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        self.pet_health_energy()
        return self

    def pet_health_energy(self):
        return f"Health {self.health} Energy {self.energy}"

    def noise(self):
        return self.noise
        # return self


class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f'Feeding {self.pet.name} {food}!')
            self.pet.eat()
        else:
            print("We need more food!")
        return self

    def bathe(self):
        self.pet.noise()


my_treats = ["burger", "pie", "ham"]
my_pet_food = ["apple", "grape", "pear"]

fido = Pet("Fido", "Dog", ["Sit", "Speak", "Rollover"], "WOOF")

tom = Ninja("Tom", "Bixler", fido, my_treats, my_pet_food)

tom.feed()
tom.feed()
tom.feed()
tom.feed()
tom.bathe()
# tom.walk().pet_health_energy()
