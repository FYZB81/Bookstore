class Person:
    def __init__(self, **kwargs):
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'lastname' in kwargs:
            self.lastname = kwargs['lastname']
        if 'id' in kwargs:
            self.id = kwargs['id']

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
