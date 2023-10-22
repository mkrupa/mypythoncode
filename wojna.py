import random


class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.suit + " " + self.rank
        return rep

class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for i in self.cards:
                rep += str(i) + " "
        else:
            rep = "<pusta>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def populate(self):
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.add(Card(rank, suit))

    def shufle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for hand in hands:
            for i in range(per_hand):
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("brak kart, nie mogę dalej rozdawać")

class Unprintable_Card(Card):
    def __str__(self):
        return "<utajniona>"

class Positonable_Card(Card):
    def __init__(self, rank, suit, face_up = True):
        super(Positonable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positonable_Card, self).__str__()
        else:
            rep = "XX"

        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up



def losowanie():
    global indeks_a
    global indeks_b
    global indeks_c
    global indeks_d

    a = random.choice(Card.RANKS)
    indeks_a = Card.RANKS.index(a)

    b = random.choice(Card.SUITS)
    indeks_b = Card.SUITS.index(b)

    indeks_c = ""
    indeks_d = ""

    while True:
        c = random.choice(Card.RANKS)
        indeks_c = Card.RANKS.index(c)

        d = random.choice(Card.SUITS)
        indeks_d = Card.SUITS.index(d)

        if indeks_c != indeks_a or indeks_d != indeks_b:
            return a,b,c,d
            break
        else:
            continue

tabela = []
tabela = losowanie()
#print(tabela)

card1 = Card(tabela[0], tabela[1])
card2 = Positonable_Card(tabela[2], tabela[3])



print("Karta gracza 1:", card1)
print("Karta gracza 2:", card2)

if indeks_a > indeks_c:
    print("Wygrał gracz 1")
elif indeks_a < indeks_c:
    print("Wygrał gracz 2")
else:
    if indeks_b > indeks_d:
        print("Wygrał gracz 1")
    elif indeks_b < indeks_d:
        print("Wygrał gracz 2")
    else:
        print("Mamy remis! Ale to nie może już wystąpić ;)")


