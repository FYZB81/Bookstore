import user
import person
import BookStore


class income_error(BaseException):
    def __init__(self, msg):
        super().__init__(msg)


class Employee(user.User, person.Person):
    def __init__(self, **kwargs):
        user.User().__init__(**kwargs)
        person.Person().__init__(**kwargs)
        if 'personnelID' in kwargs:
            self.personnelID = kwargs['personnelID']
        if 'baseIncome' in kwargs:
            self.baseIncome = kwargs['baseIncome']
        if 'reward' in kwargs:
            self.reward = kwargs['reward']
        if 'penalty' in kwargs:
            self.penalty = kwargs['penalty']
        if 'offHours' in kwargs:
            self.offHours = kwargs['offHours']
        if 'extraTime' in kwargs:
            self.extraTime = kwargs['extraTime']
        if 'store' in kwargs:
            self.store = kwargs['store']
        if 'employeetype' in kwargs:
            self.employeetype = kwargs['employeetype']

    @property
    def personnelID(self):
        return self.personnelID

    @personnelID.setter
    def personnelID(self, personnelID):
        self.personnelID = personnelID

    @property
    def baseIncome(self):
        return self.__baseIncome

    @baseIncome.setter
    def baseIncome(self, baseIncome):
        self.__baseIncome = baseIncome

    @property
    def reward(self):
        return self.__reward

    @reward.setter
    def reward(self, reward):
        self.__reward = reward

    @property
    def penalty(self):
        return self.__penalty

    @penalty.setter
    def penalty(self, penalty):
        self.__penalty = penalty

    @property
    def offHours(self):
        return self.__offHours

    @offHours.setter
    def offHours(self, offHours):
        self.__offHours = offHours

    @property
    def extraTime(self):
        return self.__extraTime

    @extraTime.setter
    def extraTime(self, extraTime):
        self.__extraTime = extraTime

    @property
    def store(self):
        return self.__store

    @store.setter
    def store(self, store):
        self.__store = store

    @property
    def employeetype(self):
        return self.__employeetype

    @employeetype.setter
    def employeetype(self, employeetype):
        self.__employeetype = employeetype

    def leave(self, num):
        self.__offHours += num
        if self.offHours > 15:
            tmp = (self.offHours - 15) * 1000000
            if tmp > self.income:
                raise income_error('income will negative')
            else:
                self.__penalty = tmp
                self.store.update_penalty(self.penalty, self.id)

    def extraTime(self, num):
        self.__extraTime += num
        self.__reward = num * 100000
        self.store.update_extra_time(self.extraTime, self.reward, self.id)

    def income(self):
        return self.baseIncome + self.reward - self.penalty

    def CustomerInfo(self, customer_id):
        print(self.store.database.search_customer(customer_id))

    def show_information(self):
        return f""" 
        id : {self.id}
        name: {self.name}
        lastname: {self.lastname}
        username: {self.username}
        password: {self.password}
        date of birth : {self.date}
        personal_id: {self.personnelID}
        """
