class HangMan:
    # sets the correct word for the game
    def __init__(self, some_thing):
        self.correct_word = some_thing

    # gets the number of guesses allowed
    def getGuesses(self):
        self.amount_of_guesses = int(input("Number of guesses: "))

    # sets the number of hints allowed
    def getHints(self):
        valid = False
        while valid == False:
            self.amount_of_hints = int(input("Number of hints: "))
        if self.amount_of_hints < self.amount_of_guesses:
            valid = True
        return
        print("Too many hints!!!")

    def play(self):
        self.getGuesses()
        self.getHints()
        self.display()

    def display(self):
        # number of attempts left
        # the hang man letter squence
        # apple
        # _ _ _ _ _
        print("the correct word:", self.correct_word)
        print("number of guesses:", self.amount_of_guesses)
        print("Number of hints", self.amount_of_hints)


def main():
    hangMan = HangMan("apple")
    hangMan.play()

if __name__ == "__main__":
    main()
