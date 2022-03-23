import user
import person


class crediterror(BaseException):
    def __init__(self, msg):
        super().__init__(msg)


class counterror(BaseException):
    def __init__(self, msg):
        super().__init__(msg)


class Customer(user.User, person.Person):
    def __init__(self, **kwargs):
        user.User().__init__(**kwargs)
        person.Person().__init__(**kwargs)
        if 'credit' in kwargs:
            self.credit = kwargs['credit']
        if 'books' in kwargs:
            self.books = kwargs['books']
        if 'completebooks' in kwargs:
            self.completebooks = kwargs['completebooks']
        if 'store' in kwargs:
            self.store = kwargs['store']

    @property
    def credit(self):
        return self.__credit

    @credit.setter
    def credit(self, credit):
        self.__credit = credit

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, books):
        self.__books = books

    @property
    def completebooks(self):
        return self.__completebooks

    @property
    def store(self):
        return self.__store

    @store.setter
    def store(self, store):
        self.__store = store

    @completebooks.setter
    def completebooks(self, completebooks):
        self.__completebooks = completebooks

    def buybook(self, book):
        if book.count > 0:
            book.count -= 1
            self.__books.append(book)
            self.store.add_book_to_relate_table(book.id, self.id)
            if self.__credit > book.price:
                self.__credit = self.__credit - book.price
            else:
                raise crediterror('credit is not enough')
        else:
            raise counterror('book is not available in bookstore')

    def setABookAsCompleted(self, book):
        self.completebooks.append(book)
        self.store.update_book(book.id, self.id)

    def increaseCredit(self, add):
        self.credit += add
        self.store.update_credit(self.credit, self.id)

    def show_information(self):
        return
        f""" 
        id : {self.id}
        name: {self.name}
        lastname: {self.lastname}
        username: {self.username}
        password: {self.password}
        date of birth : {self.date}
        """
