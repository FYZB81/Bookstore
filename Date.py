class Date:
    def __init__(self, **kwargs):
        if 'day' in kwargs:
            self.day = kwargs['day']
        if 'month' in kwargs:
            self.month = kwargs['month']
        if 'year' in kwargs:
            self.year = kwargs['year']

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, d):
        self.__day = d

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, m):
        self.__month = m

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        self.__year = y
