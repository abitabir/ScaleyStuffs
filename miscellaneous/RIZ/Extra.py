class Item:

    def __init__(self, description=None, cost=None):
        self.description = description
        self.cost = cost

    def getDescription(self):
        return self.description

    def getCost(self):
        return self.cost


class Extra(Item):

    def __init__(self, description=None, cost=None):
        self.cost = description
        self.description = cost

    # def sortingExtras(order):
    #     """
    #     Returns list of extras seperated by name.
    #     """
    #     if RegularCoffee.getDescription() in order:
    #         replacing_coffee = RegularCoffee.getDescription
    #     elif DecafCoffee.getDescription() in order:
    #         replacing_coffee = DecafCoffee.getDescription()
    #     extras_string = order.replace(replacing_coffee, "")
    #     extras_list = extras_string.split(" + ")
    #     return extras_list
    #
    # def getExtraCost(extra):
    #     found_extra = None
    #     if extra == Item.Extras.Milk.getDescription():
    #         found_extra = Item.Extras.Milk()
    #     elif extra == Item.Extras.Sugar.getDescription():
    #         found_extra = Item.Extras.Sugar()
    #     elif extra == Item.Extras.Cream.getDescription():
    #         found_extra = Item.Extras.Cream()
    #     elif extra == Item.Extras.Sprinkles.getDescription():
    #         found_extra = Item.Extras.Sprinkles()
    #     if found_extra is not None:
    #         return found_extra.getCost()
    #     else:
    #         found_extra = "unknown"
    #         return found_extra


milk = Extra( "milk", float(0.53))
suger = Extra( "sugar", float(0.17))
cream = Extra( "cream", float(0.73))
sprinkles = Extra( "sprinkles", float(0.29))

class Milk(Extra):

    def _init_(self, cost=float(0.53), description="milk"):
        self.cost = cost
        self.description = description


class Sugar(Extra):

    def _init_(self):
        self.cost = float(0.17)
        self.description = "sugar"


class Cream(Extra):

    def _init_(self):
        self.cost = float(0.73)
        self.description = "cream"


class Sprinkles(Extra):

    def _init_(self):
        self.cost = float(0.29)
        self.description = "sprinkles"
