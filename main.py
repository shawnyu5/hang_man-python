import os
class HangMan:
    # sets the correct word for the game
    def __init__(self, word):
        self.correct_word = word
        self.correct_word = list(self.correct_word)
        self.guess_list = []
        self.amount_of_guesses = 1
        self.amount_of_hints = 0

        # fill guess list with "_" for length of correct word
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
            word_length = len(self.correct_word)
            try:
                self.amount_of_guesses = int(input(f"Number of guesses(correct word is {word_length} letters long): "))
            except:
                # if input is not a number
                print("invalid guesses")
                continue
            # if guess is less than length of correct word
            if self.amount_of_guesses < word_length:
                print("invalid guesses")
                continue
            valid = True
            self.amount_of_guesses = int(self.amount_of_guesses)


    # sets the number of hints allowed
    def getHints(self):
        valid = False
        while not valid:
            try:
                self.amount_of_hints = int(input("Number of hints: "))
            except:
                print("invalid number")
                continue

            if self.amount_of_hints < self.amount_of_guesses and self.amount_of_hints < len(self.correct_word):
                valid = True
                self.__reveal_hints()
                return
            print("Too many hints!!!")


    # reveals the hints
    def __reveal_hints(self):
        sequence = []
        # make a list of the number of hints. ie 5 hints => list from 0 - 4
        for i in range(len(self.correct_word)):
            sequence.append(i)

        for i in range(self.amount_of_hints):
            # reveal letter word
            self.guess_list[sequence[i]] = self.correct_word[sequence[i]]
            # delete the revealed letter
            self.correct_word[sequence[i]] = None

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
            if self.__terminate_game():
                print("Congrats!!!")
                exit(0)

    # determine if game should be terminated
    def __terminate_game(self):
        for key, value in enumerate(self.guess_list):
            if value == "_":
                return False
        return True


    def display(self):
        print()
        print("Number of attempts: ", self.amount_of_guesses)
        # print("Hints:", self.amount_of_hints)
        # print("correct word is", self.correct_word)
        for i in self.guess_list:
            print(i, end="")


    # Play game
    def play(self):
        self.getGuesses()
        self.getHints()
        self.get_user_guess()


def main():
    hangMan = HangMan("apple")
    hangMan.play()

if __name__ == "__main__":
    main()
