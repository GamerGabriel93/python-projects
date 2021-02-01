from time import sleep


class Time:
    """New time class"""

    def kiir_ora(self):
        if ido.masodperc < 10:
            ido.masodperc = str(0) + str(ido.masodperc)
        if ido.perc < 10:
            ido.perc = str(0) + str(ido.perc)
        if ido.ora < 10:
            ido.ora = str(0) + str(ido.ora)
        print(str(ido.nap) + ". DAY" + " - " + str(self.ora) + ":" + str(self.perc) + ":" + str(self.masodperc))
        ido.masodperc = int(ido.masodperc)
        ido.perc = int(ido.perc)
        ido.ora = int(ido.ora)


ido = Time()
ido.nap = 0
ido.ora = 0
ido.perc = 0
ido.masodperc = -1

while ido.ora < 24:
    while ido.perc < 60:
        while ido.masodperc < 60:
            sleep(1)
            ido.masodperc = ido.masodperc + 1
            Time.kiir_ora(ido)
            if ido.masodperc == 59:
                ido.masodperc = -1
                ido.perc = ido.perc + 1
                if ido.perc == 60:
                    ido.perc = 0
                    ido.ora = ido.ora + 1
                    if ido.ora == 24:
                        ido.ora = 0
                        ido.nap = ido.nap + 1
