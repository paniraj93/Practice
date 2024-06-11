# Single Inheritance
class Animal:
    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("The dog barks.")

# Multiple Inheritance
class FlyingAnimal(Animal):
    def fly(self):
        print("The animal flies.")

class Bird(FlyingAnimal):
    def sound(self):
        print("The bird chirps.")

# Multilevel Inheritance
class Mammal(Animal):
    def feed_young(self):
        print("The mammal feeds its young.")

class Cat(Mammal):
    def sound(self):
        print("The cat meows.")

# Hierarchical Inheritance
class Fish(Animal):
    def swim(self):
        print("The fish swims.")

class Shark(Fish):
    def attack(self):
        print("The shark attacks.")

class Tuna(Fish):
    def school(self):
        print("The tuna schools.")

# Hybrid Inheritance
class Reptile(Animal):
    def bask(self):
        print("The reptile basks.")

class Snake(Reptile):
    def hiss(self):
        print("The snake hisses.")

class Crocodile(Reptile, Mammal):
    def hunt(self):
        print("The crocodile hunts.")

# Create instances and call methods
print("Single Inheritance")
dog = Dog()
dog.sound()

print("Multiple Inheritance")
bird = Bird()
bird.sound() 
bird.fly()

print("Multilevel Inheritance")
cat = Cat()
cat.sound() 
cat.feed_young()

print("Hierarchical Inheritance")
shark = Shark()
shark.swim()
shark.attack()

print("Hierarchical Inheritance")
tuna = Tuna()
tuna.swim()
tuna.school()

print("Hybrid Inheritance")
snake = Snake()
snake.bask() 
snake.hiss()

print("Hybrid Inheritance")
crocodile = Crocodile()
crocodile.bask()
crocodile.feed_young()
crocodile.hunt()