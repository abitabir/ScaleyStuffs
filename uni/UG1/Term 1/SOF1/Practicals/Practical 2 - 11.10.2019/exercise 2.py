#1.
stones_to_convert = int(input("Enter the number of stones you want to convert into kilograms."))
pounds_to_convert = int(input("Enter any remaining pounds you want to additionally convert into kilograms along with the stones you entered above."))

total_in_pounds = ((stones_to_convert*14)+pounds_to_convert)

print("So you want to convert the total of")
print(total_in_pounds)
answer = str(input("pound(s) into kilograms? Type y if correct and n if incorrect."))

if answer == "y":
    total_in_kilograms = round((total_in_pounds/2.205), 3)
    print("The value of", total_in_pounds, "pound(s) is approximately equivalent to", total_in_kilograms)
    
elif answer == "n":
    stones_to_convert = int(input("Enter the number of stones you want to convert into kilograms."))
    pounds_to_convert = int(input("Enter any remaining pounds you want to additionally convert into kilograms along with the stones you entered above."))
    total_in_pounds = (stones_to_convert*14) + pounds_to_convert
    total_in_kilograms = total_in_pounds/2.205
    print("The value of", total_in_pounds, "pound(s) is approximately equivalent to", total_in_kilograms, ".")

else:
     print("You have not inputted a valid answer.")

#2.
kilograms_to_convert = int(input("Enter the number of kilograms you want to convert into stones and pounds."))

total_in_stones = kilograms_to_convert/6.35

integer_of_stones = kilograms_to_convert//6.35

remaining_pounds = round(((total_in_stones - integer_of_stones)*14), 3)

print("The value of", kilograms_to_convert, "kilograms is approximately equivalent to", integer_of_stones, "stones and", remaining_pounds, "pounds (to three decimal points).")

#damn, I really went all out there smh... did waaay more code than prof Lilian dude's model answers T.T smh. I did completely different approach...

#3.
feet = int(input("Enter the number of feet."))
inches = int(input("Enter the number of inches."))

metres = round((((feet*12) + inches)/39.37), 7)

print(feet, " feet, ", inches, " inches is equivalent to ", metres, " metres to three decimal points, hum.")

#4.
total_in_metres = int(input("Enter the number of metres you want to convert into feet and inches."))
total_in_inches = int(total_in_metres/0.0254)
feet = total_in_inches//12
inches = total_in_inches % 12
print(total_in_metres,'metres is equivalent to', feet, 'feet and',inches,'inches.')
