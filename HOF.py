def add(n1,n2):
    sum = n1+n2
    return sum
print(add(10,4))

print(lambda n1,n2 : n1+n2)(5,6)

def square(num):
    sq = num**2
    return sq
print(square(5))

print((lambda num : num**2) (4))

div = lambda n1,n2 : n1/n2
print(div(10,5))

area = lambda length,width : length*width
#print(area(10,5))

si = lambda p,r,t : p*(r/100)*t
print(si(100000,10,2))

profit = lambda mrp,cp : f'{(mrp-cp)/cp *100} %'
print(profit(3000,2000))