class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def showDescription(self):
        print(f"This animal is a {self.name}, a type of {self.species}, and is {self.age} year(s) old.")
    
    def getName(self):
        print(f"Getting name")
        return self.name
    
    def setName(self, name):
        print(f"Setting name")
        self.name = name
    
    def move(self):
        print(f"{self.name} is moving")
        
    def eat(self):
        print(f"Eating")
        print(f"{self.name} is now nourished")
        
    def rest(self):
        print(f"Resting...")
        print(f"{self.name} is now rested")

class Book:
    def __init__(self, title, author, pages, yearPublished):
        self.title = title
        self.author = author
        self.pages = pages
        self.yearPublished = yearPublished
        
    def showDescription(self):
        print(f"This book is titled '{self.title}', which was written by {self.author} in {self.yearPublished}, and has {self.pages} pages in it.")
        
    def getTitle(self):
        print(f"Getting title")
        return self.title
    
    def setTitle(self, title):
        print(f"Setting title")
        self.title = title
    
    def open(self):
        print(f"Opening '{self.title}'")
        
    def read(self):
        print(f"Reading '{self.title}'")
        
    def close(self):
        print(f"Closing '{self.title}'")


class Vehicle:
    def __init__(self, name, color, style, mileage, year):
        self.name = name
        self.color = color
        self.style = style
        self.mileage = mileage
        self.year = year
        
    def showDescription(self):
        print(f"This vehicle is a {self.name}, which is a {self.color} {self.style} made in {self.year}, and has a milage of {self.mileage}.")
        
    def getName(self):
        print(f"Getting name")
        return self.name
    
    def setName(self, name):
        print(f"Setting name")
        self.name = name
        
    def setColor(self, color):
        print(f"Changing color")
        self.color = color
    
    def start(self):
        print(f"{self.name} has been started")
        
    def drive(self):
        print(f"{self.name} is now in motion")
        
    def brake(self):
        print(f"{self.name} has slowed down")
        
    def stop(self):
        print(f"{self.name} has stopped")


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
v.setColor('blue')
v.showDescription()
v.start()
v.drive()
v.brake()
v.stop()