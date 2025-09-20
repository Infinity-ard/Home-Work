class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.book = None

    def take_book(self, book):
        self.book = book
        print(f"{self.name} взяв книгу '{book.title}' автора {book.author}")

    def info(self):
        if self.book:
            print(f"Студент: {self.name}, група: {self.group}, книга: {self.book.title}")
        else:
            print(f"Студент: {self.name}, група: {self.group}, книги немає")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b1 = Book("Кобзар", "Тарас Шевченко")
b2 = Book("Лісова пісня", "Леся Українка")

s1 = Student("Іван", "КН-21")
s2 = Student("Оксана", "ІТ-23")

s1.take_book(b1)
s2.take_book(b2)

s1.info()
s2.info()
