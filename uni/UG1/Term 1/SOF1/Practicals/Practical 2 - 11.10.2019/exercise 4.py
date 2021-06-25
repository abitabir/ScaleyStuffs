#A fruit company sells bananas for £3.00 a kilogram plus £4.99 per order for postage and packaging. If an order is over £50.00, the P&P is reduced to {TO, NOT BY!} £1.50. Write a script that will take the number of kilo of bananas as a user input and print the cost of that order.

weight = int(input("Enter the kilograms of bananas you are (quite cleverly so) buying from our fruit company =)"))

cost = weight*3

if cost > 50:
    cost += 1.50
else:
    cost += 4.99

print("The total cost of", weight, "kilograms of bananas, along with the P&P (postage and packaging is graciously reduced by us if your order over £50.00!) is", cost)
