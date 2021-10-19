class Animal(object):
    def __init__(self, name=None):
        self.name = name

    def shout(self):
        print('...')

class Dog(Animal):
    def __init__(self, name=None):
        super(Dog, self).__init__(name)

    def shout(self):
        print('ワンワン')

class Cat(Animal):
    def __init__(self, name=None):
        super(Cat, self).__init__(name)

    def shout(self):
        print('ニャー')

class Elephant(Animal):
    def __init__(self, name=None):
        super(Elephant, self).__init__(name)

    def shout(self):
        print('パオーン')

if __name__ == '__main__':
    animals = [Dog(), Cat(), Elephant()]
    for a in animals:
        a.shout()
