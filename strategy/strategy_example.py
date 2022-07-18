import random
from abc import ABC, abstractmethod


class MatureLanguageFilterStrategy(ABC):
    @abstractmethod
    def modify(self, text: str, word: str) -> str:
        pass


class RemoveWordStrategy(MatureLanguageFilterStrategy):
    def modify(self, text: str, word: str) -> str:
        return text.replace(word, "")


class StarWordStrategy(MatureLanguageFilterStrategy):
    def modify(self, text: str, word: str) -> str:
        return text.replace(word, '*' * len(word))


class MessWordStrategy(MatureLanguageFilterStrategy):
    def modify(self, text: str, word: str) -> str:
        letters = list(word)
        messed_word = word
        while messed_word == word:
            random.shuffle(letters)
            messed_word = "".join(letters)
        return text.replace(word, messed_word)


class MatureLanguageFilterStrategyProvider:
    def get_strategy(self, strategy_type: str) -> MatureLanguageFilterStrategy:
        if strategy_type.lower() == "remove":
            return RemoveWordStrategy()
        elif strategy_type.lower() == "star":
            return StarWordStrategy()
        elif strategy_type.lower() == "mess":
            return MessWordStrategy()


if __name__ == '__main__':
    choice = input("Choose strategy [remove|star|mess]: ")
    text_to_filter = "Holly cow! Now I have to cow go there myself!"
    strategy = MatureLanguageFilterStrategyProvider().get_strategy(choice)
    output = strategy.modify(text_to_filter, "cow")
    print(output)
