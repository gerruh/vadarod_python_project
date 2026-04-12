from abc import ABC, abstractmethod

# 14.7
'''
Сделайте класс Pet
абстракным, добавьте
метод voice. Подумайте
какой метод вам сделать
абстрактным, т.е. что вам
удобно будет
переопределять.
Проверьте, чтобы
подклассы Dog, Cat, Parrot
работали, т.е. вы могли
создавать обеъкты.
'''

# 14.8
'''
Добавьте в класс Pet дескриптор,
чтобы нельзя было задать
отрицательный возраст или 0
'''

# 14.9
'''
Добавьте в класс Pet валидацию,
чтобы у питомца было имя и хозяин.
'''


class NonNegative:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value <= 0:
            raise AttributeError(f"{self.name} should be non-negative, got {value}.")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class NotNull:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value is None or (isinstance(value, str) and not value.strip()):
            raise AttributeError(f"{self.name} should not be None or empty string, got {value}.")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance.__dict__[self.name] is None:
            raise AttributeError(f"{self.name} should not be None, got {instance.__dict__[self.name]}.")
        return instance.__dict__[self.name]


class Pet(ABC):
    age = NonNegative()
    name = NotNull()
    master = NotNull()

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

    @abstractmethod
    def voice(self):
        pass


class Cat(Pet):
    def voice(self):
        print(self.name, "meows")


class Parrot(Pet):
    def fly(self):
        print(f"{self.name} flies")

    def voice(self):
        print(f"{self.name} sings")


class Doggo(Pet):
    def voice(self):
        print(f"{self.name} barks")


dog = Doggo("Doggo", 1, "Gerruh")
dog.run()
dog.jump()
dog.birthday()
dog.sleep()
dog.voice()

cat = Cat("Catto", 4, "Gerruh")
cat.run()
cat.jump()
cat.birthday()
cat.sleep()
cat.voice()

parrot = Parrot("Parrotto", 5, "Gerruh")
parrot.run()
parrot.jump()
parrot.birthday()
parrot.sleep()
parrot.fly()
parrot.voice()
