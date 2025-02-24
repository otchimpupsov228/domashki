class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Hero(Person):
    def __init__(self, name, age, superpower):
        super().__init__(name, age)  
        self.superpower = superpower

hero = Hero("Иван", 30, "Летать")
print(f"Имя героя: {hero.name}, Возраст: {hero.age}, Суперспособность: {hero.superpower}")