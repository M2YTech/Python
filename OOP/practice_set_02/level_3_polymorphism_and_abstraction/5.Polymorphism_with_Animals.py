class Dog:
    def sound(self):
        print(f"wow wow")
class Cat:
    def sound(self):
        print(f"meow meow")
class Cow:
    def sound(self):
        print(f"moo moo")

for obj in (Dog(),Cat(),Cow()):
    obj.sound()