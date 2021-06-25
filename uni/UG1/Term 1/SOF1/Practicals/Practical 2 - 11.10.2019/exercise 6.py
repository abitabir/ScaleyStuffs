a = int(input("Enter the first of the lengths of one side of the triangle that you wish to work out the area of via Heron's formula."))
b = int(input("Enter the second of the lengths of one side of the triangle that you wish to work out the area of via Heron's formula."))
c = int(input("Enter the third of the lengths of one side of the triangle that you wish to work out the area of via Heron's formula."))

s = (a + b + c)/2

triangle_area = round((pow((s*(s-a)*(s-b)*(s-c)), 0.5)), 3)

print("The area of a triangle with sides of length:", a, ",", b, "and", c, "(via the use of that great and very late ancient inventor Hero of Alexandria's formula) has area", triangle_area, "to three decimal places.")
