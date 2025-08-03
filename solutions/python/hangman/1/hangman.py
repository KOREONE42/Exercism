# Game status categories
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'

class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.guessed_letters = set()

    def guess(self, char):
        # Do not allow any guesses if the game has already ended.
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        # If the character has already been guessed,
        # count it as a failure.
        if char in self.guessed_letters:
            self.remaining_guesses -= 1
        else:
            self.guessed_letters.add(char)
            # If the guessed character is not in the word, it counts as a failure.
            if char not in self.word:
                self.remaining_guesses -= 1

        # Check if the player has won by ensuring every letter in the word is guessed.
        if all(letter in self.guessed_letters for letter in self.word):
            self.status = STATUS_WIN
        # Otherwise, if too many incorrect guesses have been made, the game is lost.
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        # Return the word with unguessed letters replaced by underscores.
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def get_status(self):
        return self.status
