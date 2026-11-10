class Book:

    def __init__(self,t,p,pg):
        self.title = t
        self.price = p 
        self.pages = pg

    def __add__(self, other):
        return (self.price + other.price)

b1 = Book("Core Python", 400 , 200)
b2 = Book("Advance Python", 800 , 100)
print(b1 + b2)