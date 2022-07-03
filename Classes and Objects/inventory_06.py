# Create a class Inventory. The __init__ method should accept only the __capacity: of the inventory.
# Each inventory should also have an attribute called items - empty list, where all the items will be stored.
# The class should also have 3 methods:

# •	add_item() - adds the item in the inventory if there is space for it. Otherwise, return "not enough room in the inventory"
# •	get_capacity() - return the value of __capacity
# •	__repr__() - return "Items: {items}.\nCapacity left: {left_capacity}"
# The items should be separated by ", "

class Inventory:
    def __init__(self, __capacity):
        self.capacity = __capacity
        self.items = []

    def add_item(self, item):
        if self.capacity == len(self.items):
            return "not enough room in the inventory"
        self.items.append(item)

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity - len(self.items)}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
