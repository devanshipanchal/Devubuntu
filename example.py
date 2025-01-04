class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):  # Overriding the sound method
        return "Woof!"

# Usage
animal = Animal()
print(animal.sound())  # Output: Some generic animal sound

dog = Dog()
print(dog.sound())     # Output: Woof!
