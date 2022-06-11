class Book:
    def __init__(self):
        self.title = "Abc"
        self._IBAN = "i1d123"
        self.__secret_code = "1234"


book = Book()
print(book.title)
print(book._IBAN)
print(book.__secret_code)