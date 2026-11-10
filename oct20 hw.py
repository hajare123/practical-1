class Restaurant:
    def __init__(self, name, price):
        self.name = name
        self.price = price

r1 = Restaurant("Puzze hut", 250)
r2 = Restaurant("Dominos", 400)
r3 = Restaurant("Burger King", 180)
r4 = Restaurant("Cafe Coffee Day", 300)
r5 = Restaurant("McDonalds", 220)

Restaurant_list = []
Restaurant_list = [r1]
Restaurant_list = [r2]
Restaurant_list = [r3]
Restaurant_list = [r4]
Restaurant_list = [r5]

for obj in Restaurant_list:
    if obj.price > 250:
        print(f"Expensive: {obj.name} --> price: {obj.name}")
    else:
        print(f"Afforadabale: {obj.price} --> price: {obj.price}")