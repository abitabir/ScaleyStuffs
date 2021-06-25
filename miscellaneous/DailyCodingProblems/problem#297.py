# https://medium.com/analytics-vidhya/lazy-bartender-problem-return-the-fewest-number-of-drinks-he-must-learn-in-order-to-satisfy-all-549777e83496  # model answer

"""
This problem was asked by Amazon.

At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.
"""

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}


def lazy_bar_tender(preferences):

    def creating_drink_set(preferences):
        drinks = set()
        for drink in preferences:
            drinks.add(drink)
        return drinks

    def drink_most_common_occurences(preferences, drinks):
        mode = {}
        for drink in drinks:
            mode[drink] = [0]
            for person in preferences:
                if drink in preferences[person]:
                    mode[drink][0] += 1
        return mode

    def popping_most_common(preferences, mode):

        def del_satisfied_customers(preferences, max_mode):
            persons_satisfied = []
            for person in preferences:
                if max_mode in preferences[person]:
                    persons_satisfied.append(person)
            for person in persons_satisfied:
                preferences.pop(person)
            return preferences

        max_mode = 0
        for drink in mode:
            if mode[drink][0] > mode[max_mode][0]:
                max_mode = drink
        mode.pop(max_mode)
        preferences = del_satisfied_customers(preferences, max_mode)
        return preferences, max_mode, mode

    def all_customers_satisfied(drink_recipes_learn, preferences):
        if drink_recipes_learn != []:
            output = True
            for customer in preferences:  # this is outer loop to cancel if output never turns false
                if output:  # implicitly if output is True  # was
                    customer_satisfied = False
                    for drink in preferences[customer]:
                        if not customer_satisfied:  # was if customer_satisfied == False but this is more readable ig
                            # aka as long as customer is not satisfied, continue to do this
                            if drink in drink_recipes_learn:
                                customer_satisfied = True
                    output = output and customer_satisfied  # as soon as one unsatisfied customer, cancel outermost loop
                    # so that no need to do unnecessary iterations if it's not gonna work out anyhoo
                else:
                    break
        else:  # catching exceptions cuz nowt in empty list
            output = False
        return output

    drink_recipes_learn = []
    while not all_customers_satisfied(drink_recipes_learn, preferences):
        drinks = creating_drink_set(preferences)
        mode = drink_most_common_occurences(preferences, drinks)
        preferences, max_mode, mode = popping_most_common(preferences, mode)
        drink_recipes_learn.append(max_mode)

    return len(drink_recipes_learn)

print(lazy_bar_tender(preferences))
