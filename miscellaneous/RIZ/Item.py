class Item:

    def __init__(self, description=None, cost=None):
        self.description = description
        self.cost = cost

    def getDescription(self):
        return self.description

    def getCost(self):
        return self.cost

item1 = Item("Cofee", "2.5")

print(item1.getDescription() + " " + item1.getCost())

