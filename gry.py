class Player:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.score + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezpośrednio zamiast go zaimportować")