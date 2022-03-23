import sqlite3
import book


class Database:
    def __init__(self, address):
        self.address = address
        self.db = sqlite3.connect(self.address)
        self.db.row_factory = sqlite3.Row
        self.cur = self.db.cursor()
        self.make_employe_table()
        self.make_customer_table()
        self.make_book_table()
        self.make_relatebookwithcustomer_table()

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    def make_employe_table(self):
        try:
            table = """ CREATE TABLE employee (
                personnelID INT PRIMARY KEY NOT NULL,
                id INT,
                First_Name CHAR(25),
                Last_Name CHAR(25),
                Username CHAR(10),
                Password CHAR(10),
                DateOfBirth CHAR(10),
                baseIncome INT,
                reward INT,
                penalty INT,
                offHours INT,
                extraTime INT,
                employeetype CHAR(25)
            ); """
            self.cur.execute(table)
        except:
            pass

    def make_customer_table(self):
        try:
            table = """ CREATE TABLE customer (
                id INT PRIMARY KEY NOT NULL,
                First_Name CHAR(25),
                Last_Name CHAR(25),
                Username CHAR(10),
                Password CHAR(10),
                DateOfBirth CHAR(10),
                credit INT
            ); """
            self.cur.execute(table)
        except:
            pass

    def make_book_table(self):
        try:
            table = """ CREATE TABLE book (
                id INT PRIMARY KEY NOT NULL,
                title CHAR(25),
                author CHAR(25),
                genre CHAR(25),
                pages INT,
                price INT,
                count INT
            ); """
            self.cur.execute(table)
        except:
            pass

    def make_relatebookwithcustomer_table(self):
        try:
            table = """ CREATE TABLE relatebookwithcustomer (
                id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
                book_id INT NOT NULL,
                customer_id INT NOT NULL,
                completed_book BOOLEAN
            ); """
            self.cur.execute(table)
        except:
            pass

    def add_book(self, book):
        self.cur.execute(f"""
        INSERT INTO book (id ,title,author,genre,pages,price,count) VALUES ('{book.id}','{book.title}','{book.author}' ,'{book.genre}', '{book.pages}', '{book.price}' ,'{book.count}')
        """)

    def add_book_to_relate_table(self, book_id, customer_id):
        self.cur.execute(f"""
        INSERT INTO book (book_id,customer_id,completed_book) VALUES ('{book_id}','{customer_id}','False')
        """)

    def add_employee(self, employee):
        self.cur.execute(f"""
        INSERT INTO book (First_Name,Last_Name ,Username,Password ,DateOfBirth,baseIncome,
                reward ,
                penalty,
                offHours,
                extraTime,
                employeetype) VALUES ('{employee.name}','{employee.lastname}','{employee.username}' ,'{employee.password}', '{employee.date}', '{employee.baseIncome}', '{employee.reward}', '{employee.penalty}', '{employee.offHours}', '{employee.extraTime}', '{employee.employeetype}')
        """)

    def add_customer(self, customer):
        self.cur.execute(f"""
        INSERT INTO book (First_Name,Last_Name ,Username,Password ,DateOfBirth,credit) VALUES ('{customer.name}','{customer.lastname}','{customer.username}' ,'{customer.password}', '{customer.date}', '{customer.credit}')
        """)

    def remove_book(self, book_id):
        self.cur.execute(f"DELETE FROM book WHERE id = {book_id}")
        self.cur.execute(
            f"DELETE FROM relatebookwithcustomer WHERE book_id = {book_id}")

    def remove_employee(self, employee_id):
        self.cur.execute(f"DELETE FROM employee WHERE id = {employee_id}")

    def update_book(self, book_id, customer_id):
        self.cur.execute('''UPDATE book SET completed_book = True,
                         WHERE customer_id = customer_id AND book_id = book_id;''')

    def update_credit(self, credit, customer_id):
        self.cur.execute('''UPDATE customer SET credit = credit,
                         WHERE customer_id = customer_id;''')

    def update_penalty(self, penalty, personnel_id):
        self.cur.execute('''UPDATE employee SET penalty = penalty,
                         WHERE personnelID = personnel_id;''')

    def update_extra_time(self, extraTime, reward, id):
        self.cur.execute('''UPDATE employee SET extraTime = extraTime , reward = reward
                         WHERE personnelID = id;''')

    def search_employee(self, personal_id):
        res = self.cur.execute(
            f''' SELECT * FROM employee WHERE personal_id = {personal_id}''')
        for i in res:
            return dict(i)

        return None

    def search_customer(self, customer_id):
        res = self.cur.execute(
            f''' SELECT * FROM customer WHERE id = {customer_id}'''
        )
        for i in res:
            return dict(i)

    def search_book(self, book_id):
        res = self.cur.execute(
            f''' SELECT * FROM book WHERE id = {book_id}'''
        )
        for i in res:
            return dict(i)

    def sql(self, query):
        try:
            self.cur.execute(query)
        except sqlite3.Error:
            pass

    def commit(self):
        self.db.commit()

    def close(self):
        self.commit()
        self.db.close()


def main():
    d = Database('test.db')
    d.sql("""
              CREATE TABLE test
              (personal_id INTEGER PRIMARY KEY AUTOINCREMENT,
              message TEXT);
            """)
    print(d.search_employee(2))


if __name__ == '__main__':
    main()
