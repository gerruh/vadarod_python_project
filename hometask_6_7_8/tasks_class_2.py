# 14_4
'''
Добавить классу Dog
приватный
атрибут - master.
Создать метод
get_master() который
возвращает значение
атрибута master.
'''


class Dog:
    __master: str = "Gerruh"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_master(self) -> str:
        return self.__master


a = Dog("Drive", 1)
print(a.get_master())

# 14.5
'''
Создать три класса: Dog, Cat, Parrot.
Атрибуты каждого класса: name, age,
master.
Каждый класс содержит
конструктор и методы: run, jump,
birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный
метод fly, Cat - meow, Dog - bark.
'''

# 14.6
'''
Создать родительский класс Pet,
содержащий все общие методы
классов
Dog, Cat, Parrot. Унаследовать Dog,
Cat, Parrot от класса Pet. Удалить в
дочерних классах те методы, которые
имеются у родительского класса.
Создать объект каждого класса и
вызвать все его методы.
'''


class Pet:
    def __init__(self, name: str, age: int, master: str):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(self.name, "is running.")

    def jump(self):
        print(self.name, "is jumping.")

    def birthday(self):
        self.age += 1
        print(f"It's {self.name}'s birthday, the age is {self.age}.")

    def sleep(self):
        print(self.name, "is sleeping.")


class Cat(Pet):
    def __init__(self, name: str, age: int, master: str):
        Pet.__init__(self, name, age, master)

    def meow(self):
        print(f"{self.name} meows")


class Parrot(Pet):
    def __init__(self, name: str, age: int, master: str):
        Pet.__init__(self, name, age, master)

    def fly(self):
        print(f"{self.name} flies")


class Doggo(Pet):
    def __init__(self, name: str, age: int, master: str):
        Pet.__init__(self, name, age, master)

    def bark(self):
        print(f"{self.name} barks")


dog = Doggo("Doggo", 3, "Gerruh")
dog.run()
dog.jump()
dog.birthday()
dog.sleep()
dog.bark()

cat = Cat("Catto", 4, "Gerruh")
cat.run()
cat.jump()
cat.birthday()
cat.sleep()
cat.meow()

parrot = Parrot("Parrotto", 5, "Gerruh")
parrot.run()
parrot.jump()
parrot.birthday()
parrot.sleep()
parrot.fly()