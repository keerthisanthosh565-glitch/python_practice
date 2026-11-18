#********************************************#
#********** method overriding*********#
class Animal:
    def move(self):
        print("Animl walks")

class Frog(Animal):
    def move(self):
        print("frog jump")

Frog = Frog()
Frog.move()     # excute 

#*********************************************#

class Animal:
    def sound(self):
        print("Animal making sound")

class Cat (Animal):
    def sound(self):
        print("moon")

class Dog(Animal):
    def sound(self):
        print("woff")

cat = Cat()
cat.sound()

dog = Dog()
dog.sound()

#********************************#

class Vehicle:
    def start(self):
        print("vehicle starting")

class Car(Vehicle):
    def start(self):
        print("car starts using key")

class Electric_bike(Vehicle):
    def start(self):
        print("bike push button")

car= Car()
car.start()

electric_bike = Electric_bike()
electric_bike.start()

#********************************************#

