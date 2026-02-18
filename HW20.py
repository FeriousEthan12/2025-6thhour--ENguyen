#Name: Ethan Nguyen
#Class: 6th Hour
#Assignment: HW20

#1. Create a class containing a def function that in its self and 3 other attributes for store items (stock, cost, and weight).
class items:
    def __init__(self,stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight

    def double_cost(self):
        self.cost *= 2

    def discount_one_forth(self):
        self.stock *= 1/4
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
milk = items(12, 15, 3)
candybag = items(10, 10, 1)
breadbags = items(20, 12, 6)
#3. Print the stock of all three objects and the cost of the second store item.
print(milk.stock, candybag.stock, breadbags.stock)
print(f"Candybags cost is", candybag.cost,"$")
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
candybag.double_cost()
print(f"Candybags new cost is", candybag.cost,"$")

#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
print(f"There is", breadbags.stock, "Breadbags left")
breadbags.discount_one_forth()
print(f"There is", breadbags.stock, "Breadbags left")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.

del milk
try:
    print(milk.weight)
except:
    raise Exception("The milk is gone")