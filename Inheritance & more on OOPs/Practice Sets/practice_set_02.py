class Animal:
    def eat(self):
        print("the dog eats")

class Pets(Animal):
    def sleep(self):
        print("The dog also sleeps")

class Dog(Pets):
    def bark(self):
        print("woof woof")

access = Dog()
access.bark()