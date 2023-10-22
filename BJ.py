import gry, karty

class BJ_Card(karty.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank)
            if v > 10:
                v = 10
        else:
            v = None

        return v

class BJ_Deck(karty.Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(suit, rank))

class BJ_Hand(karty.Hand):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        rep = self.name + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        for card in self.cards:
            t += card.value

        contain_ace = False

        for card in self.cards:
            if card = BJ_Card.ACE_VALUE:
                contain_ace = True

        if contain_ace and t <= 11:
            t += 10

        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    def is_hitting(self):
        response = gry.ask_yes_no("\n" + self.name ", chcesz dobrać kartę? (T/N): ")
        return response == "t"

    def bust(self):
        print(self.name, "ma furę")
        self.lose()

    def lose(self):
        print(self.name, "przegrywa.")

    def win(self):
        print(self.name, "wygrywa.")

    def push(self):
        print(self.name, "remisuje.")


class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "ma furę.")

    def flip_first_card(self):
        first_card = self.cards[0]
        flip_card.flip()

class BJ_Game:
    def __init__(self, name):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.player.append(player)

        self.dealer = BJ_Dealer("Rozdający")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shufle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

def __additional_cards(self, player):
    while not player.is_busted() and player .is_hitting():
        self.deck.deal([player])
        print(player)
        if player.is_busted():
            player.bust()

