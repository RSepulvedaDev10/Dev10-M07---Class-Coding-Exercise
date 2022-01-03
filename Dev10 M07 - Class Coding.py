class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def showDescription(self):
        print(f"This animal is {self.name}, a type of {self.species}, and is {self.age} year(s) old.")
    
    def move(self):
        print("Moving")

class Book:
    def __init__(self, title, author, pages, yearPublished):
        self.title = title
        self.author = author
        self.pages = pages
        self.yearPublished = yearPublished
        
    def showDescription(self):
        print(f"This book is titled {self.title}, which was written by {self.author} in {self.yearPublished}, and has {self.pages} pages in it.")
    
    def open(self):
        print('Opening the book')
        
    def read(self):
        print('Reading the book')
        
    def close(self):
        print('Closing the book')


class Vehicle:
    def __init__(self, name, color, style, mileage, year):
        self.name = name
        self.color = color
        self.style = style
        self.mileage = mileage
        self.year = year
        
    def showDescription(self):
        print(f"This vehicle is a {self.name}, which is a {self.color} {self.style} made in {self.year}, and has a milage of {self.mileage}.")
        
    def changeColor(self, color):
        self.color = color
    
    def start(self):
        print('The vehicle has been started')
        
    def drive(self):
        print('The vehicle is now in motion')
        
    def brake(self):
        print('The vehicle has slowed down')
        
    def stop(self):
        print('The vehicle has stopped')


a = Animal ('dog', 'mammal', 12)
b = Book ('Harry Potter and the Sorcerers Stone', 'JK Rowling', 223, '6/26/1997')
v = Vehicle ('Chrysler 300', 'red', 'sedan', 125000, '1/1/2015')

a.showDescription()
a.move()
b.showDescription()
b.open()
b.read()
b.close()
v.showDescription()
v.changeColor('blue')
v.showDescription()
v.start()
v.drive()
v.brake()
v.stop()