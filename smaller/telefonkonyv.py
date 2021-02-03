import time


class Phone:
    def __init__(self, name, number):
        self.name = name
        self.number = number


data = Phone(input('Név:'), input('Telefoszám:'))


def hozzaadas():
    with open('telefonkonyv.json', "a", encoding="UTF8") as pb:
        pb.write("{\"name\": \"" + data.name + "\",\n" + " \"phone\": \"" + data.number + "\"},\n")
        pb.close()
        print('Rögzítés sikeres!')
        time.sleep(5)


hozzaadas()
