import random
from typing import List, Union, Dict

from singleton.jokeapi_connector import JokeAPIConnector


class MyJokes:
    def __init__(self):
        self._jokes = []

    # tabela z ogromną ilością żartów

    def get_joke(self) -> str:
        return random.choice(self._jokes)


class JokeAPIAdapter(JokeAPIConnector, MyJokes):
    def __init__(self):
        super().__init__()

    def get_joke(self, category: str = "Any") -> Union[Dict, str]:
        return JokeAPIConnector.get_joke(self)


if __name__ == "__main__":

    joke = JokeAPIAdapter()
    print(joke.get_joke())
