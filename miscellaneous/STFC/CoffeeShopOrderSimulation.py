"""
Question 1
You have been asked to take over developing software for calculating bills at a new hip coffee shop 'Coffee Snobs'.
Luckily, because they believe in the purity of the bean, they only offer two types of coffee 'regular' ($2.11) and 'decaf' ($1.51)



Part A:

Create three classes called Beverage, RegularCoffee and DecafCoffee.
RegularCoffee and DecafCoffee must inherit from Beverage.

Each class should define two public methods:
   * getCost() that returns the appropriate cost of the coffee as a float
   * getDescription() that returns the name of the type of coffee as a string

Note: Beverage can return any value you like for these methods.




Part B:

Six months later, they have decided to go all out on the extras, so each coffee can have none, any or all (but no more than one of each) of the following:
    'milk' ($0.53), 'sugar' ($0.17), 'cream' ($0.73) and 'sprinkles' ($0.29)

And they also sell various cakes: muffins ($2.03), flapjacks ($2.59) and panettone ($2.88)

The manager wants you to write software to calculate and output the cost of any order.
The orders are given as comma-separated string of the form:
    "1 x regular + milk + sugar, 1 x decaf + sprinkles"

For example, for table one's order the input and output would be:
    Input: "1 x regular + milk + sugar, 1 x decaf + sprinkles, 2 x muffins"
    Output: "Final bill is $8.67"

However, there is a catch: the previous developer wrote three classes called Beverage, RegularCoffee and DecaffCoffee. We’d like you to use these still for the purpose of this exercise!
# coded all this in 2hrs approx. I do not know
# if it was submitted while I was carrying it out last time,
# because I got a HTTP 404 error, so I am resubmitting it again
# apologies for the confusion
"""


# coded all this in 2hrs approx. I do not know
# if it was submitted while I was carrying it out last time,
# because I got a HTTP 404 error, so I am resubmitting it again
# apologies for the confusion

# needs much working on but eh


class Item:

    def _init_(self):
        self.cost = None
        self.description = None

    def getCost(self):
        return self.cost

    def getDescription(self):
        return self.description

    def figureItem(self, unknown_order_string):
        item = None
        if DecafCoffee().getDescription() in unknown_order_string:
            item = DecafCoffee()
        elif RegularCoffee().getDescription() in unknown_order_string:
            item = RegularCoffee()
        elif Cakes.Muffin().getDescription() in unknown_order_string:
            item = Cakes.Muffin()
        elif Flapjacks().getDescription() in unknown_order_string:
            item = Flapjacks()
        elif Panettone().getDescription() in unknown_order_string:
            item = Panettone()
        else:
            item = "unknown"
        return item


class Beverage(Item):

    def _init_(self):
        self.cost = None
        self.description = "A typical beverage."
        self.extras = (DecafCoffee.getDescription() or RegularCoffee.getDescription()) in self.description

    class Extra(Item):

        def _init_(self):
            self.cost = None
            self.description = None
            self.options = None

        def sortingExtras(order):
            """
            Returns list of extras seperated by name.
            """
            if RegularCoffee.getDescription() in order:
                replacing_coffee = RegularCoffee.getDescription
            elif DecafCoffee.getDescription() in order:
                replacing_coffee = DecafCoffee.getDescription()
            extras_string = order.replace(replacing_coffee, "")
            extras_list = extras_string.split(" + ")
            return extras_list

        def getExtraCost(extra):
            found_extra = None
            if extra == Item.Extras.Milk.getDescription():
                found_extra = Item.Extras.Milk()
            elif extra == Item.Extras.Sugar.getDescription():
                found_extra = Item.Extras.Sugar()
            elif extra == Item.Extras.Cream.getDescription():
                found_extra = Item.Extras.Cream()
            elif extra == Item.Extras.Sprinkles.getDescription():
                found_extra = Item.Extras.Sprinkles()
            if found_extra is not None:
                return found_extra.getCost()
            else:
                found_extra = "unknown"
                return found_extra

        class Milk(Item.Extras):

            def _init_(self):
                self.cost = float(0.53)
                self.description = "milk"

        class Sugar(Item.Extras):

            def _init_(self):
                self.cost = float(0.17)
                self.description = "sugar"

        class Cream(Item.Extras):

            def _init_(self):
                self.cost = float(0.73)
                self.description = "cream"

        class Sprinkles(Item.Extras):

            def _init_(self):
                self.cost = float(0.29)
                self.description = "sprinkles"


class RegularCoffee(Beverage):

    def _init_(self):
        self.cost = float(2.11)
        self.description = "regular"


class DecafCoffee(Beverage):

    def _init_(self):
        self.cost = float(1.51)
        self.description = "decaf"


class Cakes(Item):

    def _init_(self):
        self.cost = None
        self.description = "sweet"


class Muffins(Cakes):

    def _init_(self):
        self.cost = float(2.03)
        self.description = "muffin"


class Flapjacks(Cakes):

    def _init_(self):
        self.cost = float(2.59)
        self.description = "flapjacks"


class Panettone(Cakes):

    def _init_(self):
        self.cost = float(2.88)
        self.description = "panettone"


class Orders:

    def _init_(self, orders=None):  # defaults to None if nowt inputed
        if orders is not None:
            self.orders = self.splittingOrders(orders)
            self.cost = self.calculatingTotalCost(self.orders)
            self.returning = "Final bill is $" + str(self.cost)

    def inputOrder(self, orders):
        if self.order is not None:
            self.orders = self.splittingOrders(orders)
            self.cost = self.calculatingTotalCost(self.orders)
            self.returning = "Final bill is $" + str(self.cost)
        return

    def giveOutput(self, orders):
        return self.returning

    def splittingOrders(self, orders):
        orders = orders.split(", ")
        return orders

    def sortingOrder(self, item_order):
        item_order = item_order.split(" x ")
        item_quantity = item_order[0]
        item = item_order[1]
        return item_quantity, item

    def calculatingTotalCost(self, orders):
        total_cost = float(0)
        for item_order in orders:
            item_quantity, item = self.sortingOrder(item_order)
            item_cost = self.getUnknownItemCost(item)
            total_cost += float(float(item_quantity) * item_cost)
        return total_cost

    def getUnknownItemCost(self, order):
        unknown_item = Item()
        now_known_item = unknown_item.figureItem(order)
        if now_known_item != "unknown":
            known_cost = now_known_item.getCost()
            if isinstance(now_known_item, Beverage):
                additional_costs = self.getBeverageExtrasCosts(order)
                known_cost += additional_costs
        else:
            known_cost = -1
        return known_cost

    def getBeverageExtrasCosts(self, order):
        extras = Beverage.Extra.sortingExtras(order)
        additional_costs = 0
        for extra in extras:
            additional_costs += Beverage.Extra.getExtraCost(extra)
        return additional_costs
