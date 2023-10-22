import random

class farm_pet:

    def __init__(self, name, boredom, hunger):
        self.name = name
        self.boredom = boredom
        self.hunger = hunger

    def __str__(self):
        obiekt = self.name + " " + str(self.boredom) + " " + str(self.hunger)
        return obiekt


    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def talk(self):
        print("Wof Wof jestem pies rasy Critter a moje imię to", self.name, "a mój poziom szczęscia wynosi",
            self.boredom + self.hunger, "i jestem", self.mood, "(a)")
        self.__pass_time()

    def eat(self, porcja):
        #portion = int(input("Ile porcji karmy chcesz dać pupilkom?"))
        #print("Wof Wof mniam , dziękuje za", portion, "porcję jedzonka")
        self.hunger -= int(porcja)
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, czas):
        #time = int(input("Ile czasu chcesz się z nami pobawić?"))
        #print("Wof Wof, dziękuje za", time, " jednostek zabawy")
        self.boredom -= int(czas)
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    @property
    def mood(self):
        a = self.boredom + self.hunger
        if 0 <= a < 20:
            m = "szczęśliwy"
        elif 20 <= a < 40:
            m = "ukontentowany"
        else:
            m = "smutny"

        return m

table1 = []


def main():
    table = ["Aria", "Bary", "Lucky", "Tosia", "Benny", "Bella"]
    table1 = []
    number = random.randint(1, 6)
    for i in range(1, number):
        c = random.choice(table)
        i = farm_pet(c, random.randint(0, 31), random.randint(1, 31))
        table.remove(c)
        table1.append(i)

    print("Wof Wof urodziły się:")

    for pet in table1:
        print(pet)

    print(""""
        Instrukcja obsługi Crittera:
        0 - zakończ program
        1 - porozmawiaj z pupilem
        2 - nakarm pupila
        3 - pobaw się z pupilem
        """
          )

    choice = " "

    while choice != 0:
        choice = int(input("Co chcesz zrobić ze swoimi pupilami?:"))
        if choice == 1:
            for i in table1:
                i.talk()
        elif choice == 2:
            portion = input("Ile porcji jedzenia chcesz dać pupilom?:")
            for i in table1:
                i.eat(int(portion))
            print("Wof Wof dziękujemy za", portion, "porcji jedzenia")
        elif choice == 3:
            time = input("Ile jednostek czasu chcesz poświęcić pupilom?:")
            for i in table1:
                i.play(int(time))
            print("Wof Wof dziękujemy za", time, "jednostek czasu zabawy")

    print("Wof Wof, dziękujemy za wspólny czas, do zobaczenia")


main()