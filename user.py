import Date


class User:
    def __init__(self, **kwargs):
        if 'username' in kwargs:
            self.username = kwargs['username']
        if 'password' in kwargs:
            self.password = kwargs['password']
        if 'date' in kwargs:
            self.date = kwargs['date']

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, u):
        self.__username = u

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, p):
        self.__password = p

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date
