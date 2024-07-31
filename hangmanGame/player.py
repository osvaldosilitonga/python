import random


class Player:
    __w = ("mouse", "keyboard", "monitor", "tumbler", "motorcycle", "airplane", "computer", "cardboard")
    __words = ""
    result = []

    def __init__(self, chance):
        self.chance = chance
        self.__generate_random_words()

    def __generate_random_words(self):
        self.__words = random.choice(self.__w)

        for _ in range(len(self.__words)):
            self.result.append("-")

    def check_character(self, char):
        is_found = False
        for i in range(len(self.__words)):
            if self.__words[i] == char:
                self.result[i] = char
                is_found = True

        if not is_found:
            self.chance -= 1

    def is_win(self):
        return True if '-' not in self.result else False

    def get_info(self):
        result = ' '.join(self.result)

        print("*** Status ***")
        print(f"Chance: {self.chance}")
        print(f"Result: {result}")
