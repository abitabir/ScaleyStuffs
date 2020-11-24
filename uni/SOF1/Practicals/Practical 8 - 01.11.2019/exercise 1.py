stock = {
 "banana": 6,
 "apple": 0,
 "orange": 32,
 "pear": 15
}
prices_in_pence = {
 "banana": 40,
 "apple": 20,
 "orange": 15,
 "pear": 30
}
basket_1 = {
 "banana": 4,
 "pear": 3
}
basket_2 = {
 "apple": 1,
 "pear": 3
}

#1.

def basket_price(basket, stock, prices):
    given_basket_price = 0
    for fruit in basket.keys():
        if (fruit not in prices 
            or fruit not in stock 
            or stock[fruit] < basket[fruit]):
            return(-1)
        else:
            given_basket_price += basket[fruit] * prices[fruit]
    return(given_basket_price)    

print(basket_price(basket_1, stock, prices_in_pence))

#2.

def checkout(basket, stock, prices):
    total = basket_price(basket, stock, prices)
    for fruit in basket:
        stock[fruit] -= basket[fruit]
        if stock[fruit] < 0:
            return(-1, "stock remains unchanged")
    return("stock is now", stock, "and basket price is", total)

print(checkout(basket_2, stock, prices_in_pence))

#3.

def add_stock(items, stock):
    for fruit in items:
        stock.update({fruit: stock.get(fruit, 0)+items[fruit]})
    return("stock is now", stock)

print(add_stock({"apple":5, "kiwi":10}, stock))

#4.

def price_increase(increase, prices):
    for fruit in prices:
        prices[fruit] = round(prices[fruit]*(1+increase))
    return("prices are now", prices)

print(price_increase(0.2, prices_in_pence))