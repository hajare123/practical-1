class Employee:

    e_company = "TCS"

    def __init__(self,nm,sal,em):
        print(f"self = {id(self)}")
        self.name = nm
        self.salary = sal
        self.email = em


    def display(self):
        print(self.name)
        print(self.salary)
        print(self.email)
        print(self.e_company)

obj = Employee("Raj",25000,"raj@gmail.com","TKA")
obj2 = Employee("Rohan",25000,"rohan@gmail.com","TKA")
print(id(obj))
obj.display()
obj2.display()

def add(n1,n2):
    pass