itemsForSale = {"washing machine", "led lights", "stickers", "cameras", "bulbs", "bulbs"}
#print(itemsForSale)
#print(type(itemsForSale))

#Methods
itemsForSale.update(["cups", "plates", "food"])
print(itemsForSale)

Age = {10, 20, 30, 40}
Name = {"Jack", "Joel", "James", "John"}
w = Age.union(Name)
print(w)