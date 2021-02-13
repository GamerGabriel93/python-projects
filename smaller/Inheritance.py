class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s. ' %(self.name, food))


class Dog(Animal):

    def fetch(self, thing):
        print('%s goes after the %s!' %(self.name, thing))


class Cat(Animal):

    def swatsrting(self):
        print('%s shreds the string!' %(self.name))


d = Dog('Ranger')
c = Cat('MeOW')

d.fetch('ball')
c.swatsrting()
d.eat('Dog food')
c.eat('Cat food')
