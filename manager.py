import Employee
import BookStore

class Manager(Employee.Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'store' in kwargs:
            self.store = kwargs['store']
    @property
    def store(self):
        return self.__store

    @store.setter
    def store(self, store):
        self.__store = store

    def hireEmployee(self,employee):
        self.store.registerEmployee(employee)

    def fireEmployee(self,employee):
        self.store.remove_employee(employee)

    def employeeInfo(self,employees_id):
        print(self.store.database.search_employee(employees_id))

    def addABook(self,book):
        self.store.add_book(book)

    def removeABook(self,book):
        self.store.removeABook(book)
