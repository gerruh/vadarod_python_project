import datetime

# 14.1
'''
Создайте класс Person и его
атрибуты: имя, фамилия,
возраст, пол
Создайте 2 объекта: Васю и
Катю
'''


class Person:
    def __init__(self, name: str, surname: str, age: int, gender: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender


person_male: Person = Person("Вася", "Пупкин", 15, "М")
person_female: Person = Person("Катя", "Мотя", 22, "Ж")

# 14.2
'''
Создайте класс Porsche с
одним статическим
атрибутом (модель) и
несколькими
динамическими. Создайте 2
порша
'''


class Porsche:
    model: int = 911

    def __init__(self, color: str, mileage: int):
        self.color = color
        self.mileage = mileage


porsche_1: Porsche = Porsche("blue", 10000)
porsche_2: Porsche = Porsche("red", 45000)

# 14.3
'''
Переделайте класс Person:
установите возраст по
дефолту 1 и пол – мужской.
Создайте Васю младенца и
Катю.
Посмотрите их атрибуты пол
и возраст
'''


class Person_Alt:
    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.age = 1
        self.gender = gender


infant_1: Person_Alt = Person_Alt("Вася", "Пупкин", "М")
infant_2: Person_Alt = Person_Alt("Катя", "Мотя", "Ж")

print(f"Пол infant_1 - {infant_1.gender}, Возраст infant_1 - {infant_1.age}")
print(f"Пол infant_2 - {infant_2.gender}, Возраст infant_2 - {infant_2.age}")

# 14.4
'''
Добавьте в класс Person
метод, который считает и
выводит в каком году
родился человек. Как
параметр вам понадобится
текущий год.
Создайте Васю и вызовите
этот метод
Считается, что у Васи уже был
др в этом году
'''


class PersonWithYearBorn(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str):
        Person.__init__(self, name, surname, age, gender)
        self.year_born: int = datetime.datetime.now().year - self.age

    def born(self) -> int:
        return self.year_born


vasya: PersonWithYearBorn = PersonWithYearBorn("Вася", "Пупкин", 20, "М")
print(vasya.born())

# 14.5
'''
Добавьте в класс Porsche
метод, который считает
пробег, а также выводит
пробег и сколько за сегодня
проехал порш.
Создайте 1 порш и 2 раза
вызовите метод
'''


class PorscheWithMileage(Porsche):
    def __init__(self, color: str, mileage: int):
        Porsche.__init__(self, color, mileage)
        self._today_mileage: int = 0

    @property
    def today_mileage(self) -> int:
        return self._today_mileage

    @today_mileage.setter
    def today_mileage(self, value: int) -> None:
        self.mileage += value
        self._today_mileage = value

    def all_mileages(self) -> str:
        return f"Пробег за сегодня - {self.today_mileage}, общий пробег - {self.mileage}"


porsche_3: PorscheWithMileage = PorscheWithMileage("green", 20000)
porsche_3.today_mileage = 200
print(porsche_3.all_mileages())
porsche_3.today_mileage = 500
print(porsche_3.all_mileages())

# 14.6
'''
Расширьте в классе Person
метод, который считает год
рождения: добавьте вывод,
что человек пойдет в армию в
таком-то году, если это
мужчина допризывного
возраста.
Считается, что в армию
забирают с 18 лет
Создайте Васю допризывного
возрата и Катю. Вызовите для
каждого объекта этот метод.
'''


class PersonArmy(PersonWithYearBorn):
    def __init__(self, name: str, surname: str, age: int, gender: str):
        PersonWithYearBorn.__init__(self, name, surname, age, gender)

    def born(self) -> tuple[int, str]:
        if self.gender == "Мужской":
            return self.age, f"пойдёт в армию в {self.year_born + 18} году"
        else:
            return self.age, f"девочки не ходят на срочку"


vasya_army_1: PersonArmy = PersonArmy("Вася", "Пупкин", 33, "Мужской")
vasya_army_1_army_info = vasya_army_1.born()
print(f"{vasya_army_1.name} находится в возрасте {vasya_army_1_army_info[0]} лет, {vasya_army_1_army_info[1]}")

vasya_army_2: PersonArmy = PersonArmy("Катя", "Мотя", 18, "Женский")
vasya_army_2_army_info = vasya_army_2.born()
print(f"{vasya_army_2.name} находится в возрасте {vasya_army_2_army_info[0]} лет, {vasya_army_2_army_info[1]}")

# Hometask_14_1
'''
Создать класс Dog.
Класс имеет четыре
атрибута: height, weight, name, age. Класс
имеет три метода: jump, run, bark. Каждый
метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все
методы
объекта и вывести на экран все его
атрибуты.
'''


class Dog:
    def __init__(self, name: str, height: int, weight: int, age: int):
        self.name: str = name
        self.height: int = height
        self.weight: int = weight
        self.age: int = age

    @staticmethod
    def jump() -> None:
        print("Прыгаю")

    @staticmethod
    def run() -> None:
        print("Бежать")

    @staticmethod
    def bark() -> None:
        print("Гавкать")


dog_instance = Dog("Драйв", 1, 10, 2)
dog_instance.jump()
dog_instance.run()
dog_instance.bark()
print(dog_instance.__dict__)

# Hometask_14_2
'''
Добавить в класс Dog метод change_name.
Метод
принимает на вход новое имя и меняет
атрибут имени у
объекта. Создать один объект класса.
Вывести имя.
Вызвать метод change_name. Вывести имя.
'''


class DogSub(Dog):
    def __init__(self, name: str, height: int, weight: int, age: int):
        Dog.__init__(self, name, height, weight, age)

    def change_name(self, name: str):
        self.name = name


dogsub_instance = DogSub("Драйв", 1, 10, 2)
print(dogsub_instance.name)
dogsub_instance.change_name("Гордон")
print(dogsub_instance.name)
