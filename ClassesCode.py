class Animal:
    """Animal class"""
    def __init__(self, scientific_name, common_name, conservation_status, habitat):
        self.__scientific_name = scientific_name
        self.__common_name = common_name
        self.__conservation_status = conservation_status
        self.__habitat = habitat

@property
def scientific_name(self):
    return self.__scientific_name

@property
def common_name(self):
    return self.__common_name

@property
def conservation_status(self):
    return self.__conservation_status

@property
def habitat(self):
    return self.__habitat

def move(self):
    print("Moving")

#--------------------------------------------------------------

class Book:
    """Book class"""

    def __init__(self, title, author, pages, year_published, publisher, ISBN):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self._year_published = year_published
        self.__publisher = publisher
        self.__ISBN = ISBN

@property
def title(self):
    return self.__title

@property
def author(self):
    return self.__author

@property
def pages(self):
    return self.__pages

@property
def year_published(self):
    return self.__year_published

@property
def publisher(self):
    return self.__publisher

@property
def ISBN(self):
    return self.__ISBN

#---------------------------------------------------------------

class Vehicle:
    """Vehicle class"""

    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

@property
def make(self):
    return self.__make

@property
def model(self):
    return self.__model

@property
def year(self):
    return self.__year

def move(self):
    print("Moving")