class student:

    def __init__(self,r,n,m):
        self.roll_no = r
        self.name = n
        self.marks = m

obj = student(1, "Jay" , 85)

print(obj.name)
print(obj.roll_no)
print(obj.marks)

obj.marks = 100
print(obj.marks)

obj2 = student(12, "Payal" ,95)
print(obj2.name)
print(obj2.roll_no)
print(obj2.marks)


print(type(obj))
print(id(obj))        