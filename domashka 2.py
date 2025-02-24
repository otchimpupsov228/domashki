import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def eat(self):
        self.energy += 10
        print(f"{self.name} поел и доволен!")

    def sleep(self):
        self.energy += 20
        print(f"{self.name} сладко спит...")

    def play(self):
        if self.energy > 10:
            self.energy -= 15
            print(f"{self.name} играет и веселится!")
        else:
            print(f"{self.name} устал и хочет спать.")

    def live_one_day(self):
        action = random.choice([self.eat, self.sleep, self.play])
        action()

cat = Cat("Мурзик")
for _ in range(5):
    cat.live_one_day()
