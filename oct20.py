class Laptop:
    def __init__(self, n, p, b, c):
        self.name = n
        self.price = p
        self.brand = b
        self.color = c

pro1 = Laptop("Sumsung", 70000, "Sumsung", "gray")
pro2 = Laptop("Dell", 50000, "Dell", "black")
pro3 = Laptop("HP", 90000, "HP", "cilver")
pro4 = Laptop("Lenovo", 80000, "Lenovo", "gray")
pro5 = Laptop("Sumsung", 95000, "Sumsung", "black")

Laptop_list = []
Laptop_list.append(pro1)
Laptop_list.append(pro2)
Laptop_list.append(pro3)
Laptop_list.append(pro4) 
Laptop_list.append(pro5)

print("Laptop List:")

for i in Laptop_list:
    print("Name:", i.name)
    print("Price:", i.price)
    print("Brand:", i.brand)
    print("Color:", i.color)
    print("**********************")