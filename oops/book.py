class Book:
    def __init__(self, bookname, price, subject) -> None:
        self.bookname = bookname
        self.subject = subject
        self.price = price

    def __str__(self) -> str:
        return "Name={0}, Subject={1}, Price={2}".format(self.bookname, self.subject, self.price)

b1 = Book("Basic C", 100, "C")
b2 = Book("Adv C", 200, "C")
print(b1, b2)
print(b1, b2)

      