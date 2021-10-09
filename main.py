class HangMan:
    # sets the correct word for the game
    def __init__(self, word):
        self.correct_word = word
        self.correct_word = list(self.correct_word)
        self.guess_list = []
        for _ in range(len(self.correct_word)):
            self.guess_list.append("_ ")
        self.guess_list.append("\n")

    # validates if argument is a float
    def __isNumber(self, number) -> bool:
        # validate user input is a number
        try:
            number = int(number)
            return True
        except:
            print("not a number. Please enter a number")
            return False

    # gets the number of guesses allowed
    def getGuesses(self):
        valid = False
        while not valid:
            self.amount_of_guesses = input("Number of guesses: ")
            if not self.__isNumber(self.amount_of_guesses):
                continue
            valid = True
            self.amount_of_guesses = int(self.amount_of_guesses)


    # sets the number of hints allowed
    def getHints(self):
        valid = False
        while not valid:
            self.amount_of_hints = input("Number of hints: ")
            if not self.__isNumber(self.amount_of_hints):
                continue

            self.amount_of_hints = int(self.amount_of_hints)

            if self.amount_of_hints < self.amount_of_guesses:
                valid = True
                return
            print("Too many hints!!!")


    # validates user guess
    def __validate_user_guess(self, letter):
        try:
            found_letter = self.correct_word.index(letter)
            self.guess_list[found_letter] = self.correct_word[found_letter]
            self.correct_word[found_letter] = None
            print("correct guess!!!")
            return True
        except:
            print("guess is incorrect!")
            return False


    # gets a single guess from user
    def get_user_guess(self):
        self.display()
        keep_going = True
        while keep_going:
            single_guess = input("Please enter a guess: ")
            self.__validate_user_guess(single_guess)
            if self.amount_of_guesses == 0:
                print("stop game")
                keep_going = False
                break
            self.amount_of_guesses -= 1
            self.display()


    def display(self):
        print("Number of attempts: ", self.amount_of_guesses)
        # print("Hints:", self.amount_of_hints)
        # print("correct word is", self.correct_word)
        for i in self.guess_list:
            print(i, end="")


    # Play game
    def play(self):
        self.getGuesses()
        # print(self.amount_of_guesses)
        self.getHints()
        self.get_user_guess()


def main():
    hangMan = HangMan("apple")
    hangMan.play()

if __name__ == "__main__":
    main()
