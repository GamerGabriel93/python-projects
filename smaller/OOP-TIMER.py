import time


class Ora:
    def __init__(self, ora, perc, masod):
        self.masod = masod
        self.perc = perc
        self.ora = ora

    def mas(self):
        while 60 > self.masod:
            print(f"{self.ora}:{self.perc}:{self.masod}")
            self.masod += 1
            time.sleep(1)
            if self.masod == 60:
                self.masod = 0
                return self.masod

    def per(self):
        while self.perc < 60:
            self.mas()
            if self.masod == 0:
                self.perc = self.perc + 1
                if self.perc == 60:
                    self.perc = 0
                    return self.perc

    def hor(self):
        while self.ora < 24:
            self.per()
            if self.perc == 0:
                self.ora = self.ora + 1
                if self.ora == 24:
                    self.ora = 0
                    return self.ora


ido = Ora(0, 0, 0)
ido.hor()
