class Person:
    def __init__(self, name='Ulday', age=23, book='The count of Monte Cristo'):
        self.name = name
        self.age = age
        self.book = book

    def print_person(self):
        print("Person")
        print("name=", self.name)
        print("age=", self.age)
        print("book=", self.book)

    def return_person(self):
        return "Person: name = "+self.name +", age = "+str(self.age) +", book = "+self.book

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setBook(self, book):
        self.book = book

    def __str__(self):
        return self.return_person()
