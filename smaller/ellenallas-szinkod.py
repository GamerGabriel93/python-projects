# Itt az f-string nélkül nem tudom formázni a mérföldet

"""class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def prin(self):
        print("The {} car has {} miles.".format(self.color, self.mileage))


c1 = Car("blue", 20_000)
c2 = Car("red", 30_000)

c1.prin()
c2.prin()"""

# Itt az f-string miatt tudom formázni a mérföldet
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def prin(self):
        print(f"The {self.color} car has {self.mileage:,} miles.")


c1 = Car("blue", 20_000)
c2 = Car("red", 30_000)

c1.prin()
c2.prin()
