import random


class Value:
    def __init__(self):
        self.number = random.randrange(1, 3)
        self.guess = int(input('Válassz:\n1 - Kő\n2 - Papít\n3 - Olló\n'))
        self.botvalue = self.bot()
        self.pvalue = self.player()

    def bot(self):
        if self.number == 1:
            self.botvalue = str("Kő")
        if self.number == 2:
            self.botvalue = str("Papír")
        if self.number == 3:
            self.botvalue = str("Olló")
        return self.botvalue

    def player(self):
        if self.guess == 1:
            self.pvalue = "Kő"
        if self.guess == 2:
            self.pvalue = "Papír"
        if self.guess == 3:
            self.pvalue = "Olló"
        return self.pvalue

    def compare(self):
        if self.number == self.guess:
            print('Döntetlen! Mert a gép:', self.botvalue, '-t mutatott, Te pedig:', self.pvalue, '-t.')
        if self.number == 1:
            if self.guess == 2:
                print('Nyertél! Mert a gép:', self.botvalue, '-t mutatott, Te pedig:', self.pvalue, '-t.')
            if self.guess == 3:
                print('Vesztettél! Mert a gép:', self.botvalue, '-t mutatott, Te pedig:', self.pvalue, '-t.')
        if self.number == 2:
            if self.guess == 1:
                print('Vesztettél! Mert a gép:', self.botvalue, '-t mutatott, Te pedig:', self.pvalue, '-t.')
            if self.guess == 3:
                print('Győztél! Mert a gép:', self.botvalue, '-t mutatott, Te pedig:', self.pvalue, '-t.')
        if self.number == 3:
            if self.guess == 2:
                print('Vesztettél! Mert a gép:', self.botvalue, '-t mutatott, Te pedig:', self.pvalue, '-t.')
            if self.guess == 1:
                print('Nyertél! Mert a gép:', self.botvalue, '-t mutatott, Te pedig:', self.pvalue, '-t.')


start = Value()
start.compare()
