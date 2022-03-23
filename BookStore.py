import databasehelper
import book
import sqlite3


class BookStore:
    def __init__(self, address):
        self.__database = databasehelper.Database(address)

        '''if 'books' in kwargs:
            self.books = kwargs['books']
        if 'customers' in kwargs:
            self.customers = kwargs['customers']
        if 'employees' in kwargs:
            self.employees = kwargs['employees']
        if 'manager' in kwargs:
            self.manager = kwargs['manager']'''

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, books):
        self.__books = books

    @property
    def customers(self):
        return self.__customers

    @customers.setter
    def customers(self, customers):
        self.__customers = customers

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employees):
        self.__employees = employees

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager):
        self.__manager = manager

    @property
    def database(self):
        return self.__database

    def searchEmployee(self, employee_id):
        '''for c in self.employees:
            if c.personal_id == employee_id:
                return c
        return None'''
        self.database.search_employee(employee_id)

    def searchCustomer(self, customer_id):
        '''for c in self.customers:
            if c.id == customer_id:
                return c
        return None'''
        self.database.search_customer(customer_id)

    def searchBook(self, book_id):
        '''for c in self.books:
            if c.id == book_id:
                return c
        return None'''
        self.database.search_book(book_id)

    def logAsEmployee(self, employee_username, employee_password):
        for c in self.employees:
            if c.username == employee_username and c.password == employee_password:
                return c
        return None

    def logAsCostumer(self, customer_username, customer_password):
        for c in self.customers:
            if c.username == customer_username and c.password == customer_password:
                return c
        return None

    def add_book(self, book):
        # self.books.insert(book)
        self.database.add_book(book)

    def removeABook(self, book_id):
        # self.books.remove(book)
        self.database.remove_book(book_id)

    def registerACustomer(self, customer):
        # self.customers.insert(customer)
        self.database.add_customer(customer)

    def registerEmployee(self, employee):
        # self.emloyees.insert(employee)
        self.database.add_employee(employee)

    def remove_employee(self, employee_id):
        # self.emloyees.remove(employee_id)
        self.database.remove_employee(self, employee_id)

    def add_book_to_relate_table(self, book_id, customer_id):
        self.database.add_book_to_relate_table(book_id, customer_id)

    def update_book(self, book_id, customer_id):
        self.database.update_book(book_id, customer_id)

    def update_credit(self, credit, customer_id):
        self.database.update_credit(credit, customer_id)

    def update_penalty(self, penalty, personnel_id):
        self.database.update_penalty(penalty, personnel_id)

    def update_extra_time(self, extraTime, reward, id):
        self.database.update_extra_time(self, extraTime, reward, id)

    def __del__(self):
        self.__database.close()
