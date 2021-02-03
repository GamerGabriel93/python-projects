class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def pdata(self):
        return 'Player  Name:{}  Hp:{}   At:{}'.format(self.name, int(self.hp), self.attack)


class Enemy:
    def __init__(self, ename, ehp, eattack):
        self.ename = ename
        self.ehp = ehp
        self.eattack = eattack

    def edata(self):
        return 'Enemy  Name:{}  Hp:{}   At:{}'.format(self.ename, int(self.ehp), self.eattack)


def print_data():
    print(player.pdata())
    print(eplayer.edata())


player = Character('Karmen', 100, 20)
eplayer = Enemy('Seal', 100, 18)

print(player.pdata())
print(eplayer.edata())

while eplayer.ehp > 0 and player.hp > 0:
    move = int(input('\nWhat would you like to do?\n1 - Attack\n2 - Defending\n'))
    if move == 1:
        eplayer.ehp = eplayer.ehp - player.attack
        if eplayer.ehp <= 0:
            eplayer.ehp = 0
            print('Player WIN')
        print_data()
    if move == 2:
        player.hp = player.hp - eplayer.eattack / 2
        if player.hp <= 0:
            player.hp = 0
            print('Enemy WIN')
        print_data()
