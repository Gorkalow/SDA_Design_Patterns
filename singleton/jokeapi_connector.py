import json
import time
from typing import Dict, Union

import requests

from singleton.singleton_metaclass import SingletonMeta


class JokeAPIConnector(metaclass=SingletonMeta):
    def __init__(self):
        self.BASE_URL: str = "https://jokeapi.dev/"
        # header pokazuje, że będziemy komunikować się z api w formacie json
        self.headers: Dict[str, str] = {"Accept": "application/json"}
        self._response: Union[requests.Request, None] = None
        #istotne przy potrzebie delaya
        self._delay: int = 2
    def _build_path(self, *args: str) ->str:
        return f"{self.BASE_URL}/{'/'.join(args)}?type=single"

    @staticmethod
    def _build_error_message(status_code: int, message: str) -> Dict[str, str]:
        return {"Error": f"{status_code}:{message}"}

    def get_joke(self, category: str = "Any") -> Union[Dict, str]:
        time.sleep(self._delay)
        self._response = requests.request("GET", self._build_path("joke", category), headers=self.headers)
        if self._response.ok:
            return json.loads(self._response.text).get("joke")
        #przy użyciu .["joke"] zamiast .get("joke") będzie KeyError
        else:
            error = json.loads(self._response.text)
            return self._build_error_message(self._response.status_code, error['message'])

#Zadanie dla chętnych - rozbudować connecotor przez zmianę buid_path...

if __name__=='__main__':
    joke = JokeAPIConnector()
    print(joke.get_joke())
    joke2 = JokeAPIConnector()
    print(joke.get_joke())

