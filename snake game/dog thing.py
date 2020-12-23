x = 9
y = 9
snake_location = [x, y]
snake_life = True


class Animal:
    def __init__(self, size, color, name):
        self.size = size
        self.color = color
        self.name = name

    def make_sound(self):
        pass

    def print(self):
        print(f"size: {self.size}")


class Dog(Animal):

    def __init__(self, size, color, name, tail_length):
        Animal.__init__(self, size, color, name)
        self.tail_length = tail_length

    def bark(self):
        print(f"My color is {self.color}")

    def eat(self, food):
        pass


dog = Dog("black")

dog2 = Dog("white")

dog.print()
dog2.bark()
