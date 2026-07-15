from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id, title, borrow_fee):
        self.item_id = item_id
        self.title = title
        self.borrow_fee = borrow_fee

    @abstractmethod
    def calculate_fee(self):
        pass


class Book(LibraryItem):
    def __init__(self, item_id, title, borrow_fee, days_borrowed, daily_rate):
        super().__init__(item_id, title, borrow_fee)
        self.days_borrowed = days_borrowed
        self.daily_rate = daily_rate

    def calculate_fee(self):
        self.borrow_fee = self.days_borrowed * self.daily_rate
        return self.borrow_fee


class Magazine(LibraryItem):
    def __init__(self, item_id, title, borrow_fee, weekly_fee):
        super().__init__(item_id, title, borrow_fee)
        self.weekly_fee = weekly_fee

    def calculate_fee(self):
        self.borrow_fee = self.weekly_fee
        return self.borrow_fee


book = Book(1, "Python Basics", 0, 5, 100)
magazine = Magazine(2, "Tech Today", 0, 300)

print("Book Fee:", book.calculate_fee())
print("Magazine Fee:", magazine.calculate_fee())
