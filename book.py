class Book:
    def __init__(self, **kwargs):
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'title' in kwargs:
            self.title = kwargs['title']
        if 'author' in kwargs:
            self.author = kwargs['author']
        if 'genre' in kwargs:
            self.genre = kwargs['genre']
        if 'pages' in kwargs:
            self.pages = kwargs['pages']
        if 'price' in kwargs:
            self.price = kwargs['price']
        if 'count' in kwargs:
            self.count = kwargs['count']

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        self.__pages = pages

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count
