import random
import time
import os


# Number Guesser in OOP python
class GuessNumber:
    def __init__(self, xx, tip):
        self.x = xx
        self.guess = tip

    def tippek(self):
        while self.guess != self.x:
            os.system('cmd /c "cls"')
            self.x = int(input("Sajnos nem az a szám! Gondoltam egy másikra!\n"))
        else:
            print('Eltaláltad! A gondolt szám a(z):', number.x)
            time.sleep(5)


number = GuessNumber(random.randrange(1, 10),
                     int(input('Gondoltam egy számra 1 és 10 között!\nMelyik számra gondoltam?\n')))

print(number.tippek())
