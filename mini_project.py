# Mini Project in opps
class Book:
    #class attribute
    book_name = "A personal history book"
    def __init__(self, author, price):
        #instance attribute
        self.author = author
        self.price = price
    #instance method
    def display(self):
        print(f"Book Name: {self.book_name}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
#class method to display book name
    @classmethod
    def display_book_name(cls):
        print(f"Book Name: {cls.book_name}")
#static method to check if the book is expensive
    @staticmethod
    def is_expensive(price):
        if price > 200:
            return True
        
#creat amount and test the methods
book1 = Book("Imran khan", 395)
book1.display()
Book.display_book_name()
print(f"Is the book expensive? {Book.is_expensive(395)}")
#validate the book price
price = 450
print(f"Is the book expensive? {Book.is_expensive(price)}")
print(f"Is the book expensive? {Book.is_expensive(150)}")