import time

class Player:
    def blast(self, person):
        print("Gracz razi wroga !")
        time.sleep(2)
        person.die()

class Alien:
    def die(self):
        print("AAA, powiedzcie moim kochanym larwom, że bardzo je kocham. Umieram!")

class Alien2():
    def die(self):
        print("Umieram, pozdrówcie wszystkich orków")


hero = Player()
enemy = Alien()
hero.blast(enemy)