from random import randint


class RollDices:

    def roll(self):
        rolled_first_dice = randint(1, 6)
        rolled_second_dice = randint(1, 6)
        return rolled_first_dice,rolled_second_dice


