'''
@author: Lilian
'''

###################EXERCISE 2###################################################
# Constants
METER_PER_INCH = 0.0254
INCHES_PER_FEET = 12

feet = int(input('Enter the number of feet:'))
inches = int(input('Enter the number of inches:'))
number_meters = (feet * INCHES_PER_FEET + inches) * METER_PER_INCH
print(feet,'feet',inches,'inches is equivalent to', number_meters,'meters')

metres = float(input('Enter the number of metres:'))
number_inches = int(metres/METER_PER_INCH)
feet = number_inches//INCHES_PER_FEET
inches = number_inches % INCHES_PER_FEET
print(metres,'metres is equivalent to', feet, 'feet and',inches,'inches.')



###################EXERCISE 4###################################################
weight = float(input('Enter the number of Kg of banana you want to order: '))
cost = 3 * weight
if cost >50:
    cost += 1.50
else:
    cost += 4.99

print('The cost of the order is:', cost)


###################EXERCISE 5###################################################
age = int(input('Enter your age: '))
max_rate = 208 - 0.7 * age
rate = int(input('Enter your current heart rate: '))

# Be careful, the order of the conditions in the if-elif-else does matter. If I
# swap the second and third condition, the logic will be incorrect. The program
# will return something, but it will be incorrect.

if rate >= 0.9 * max_rate:
    print('Interval training')
elif rate >= 0.7 * max_rate:
    print('Threshold training')
elif rate >= 0.5 * max_rate:
    print('Aerobic training')
else:
    print('Couch potato')
    
###################EXERCISE 6###################################################
size_a = float(input('Enter the length of the first side of the triangle: '))
size_b = float(input('Enter the length of the second side of the triangle: '))
size_c = float(input('Enter the length of the third side of the triangle: '))

semi_perimeter = (size_a + size_b + size_c)/2
area = pow(semi_perimeter
           * (semi_perimeter - size_a)
           * (semi_perimeter - size_b)
           * (semi_perimeter - size_c),
           0.5)
print('The area of the triangle is', area)

