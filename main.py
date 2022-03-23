from BookStore import BookStore
from customer import Customer
from person import Person
from user import User
from Date import Date
from book import Book
from BookStore import BookStore


def main():
    current_shop = BookStore("information.db")
    birth = Date(day=14, month=7, year=1381)
    firstcustomer = Customer(name='fateme', lastname='yazdan',
                             id=1, username='fate', password='fa@tt', date=birth, credit=200000, store=current_shop)
    FirstBook = Book(id=1, title="midnigthlibrary", author='g',
                     genre='ra', pages=200, price='200000', count=20)

    current_shop.add_book(FirstBook)


if __name__ == '__main__':
    main()
