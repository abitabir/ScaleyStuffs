def scalar_product(scalar, vector):
    product = []
    for val in vector:
        product.append(val*scalar)
    return(product)

def vector_addition(vector1, vector2):
    addition_sum = []
    for i in range(3):
        addition_sum.append(vector1[i] + vector2[i])
    return(addition_sum)

vector = []
vector.append(float(input("Enter the first of the three elements in the vector.")))
vector.append(float(input("Enter the second of the three elements in the vector.")))
vector.append(float(input("Enter the third of the three elements in the vector.")))

choice = str(input("If you want to do vector addition, enter 'a'. If you want to have a scalar product returned, enter 'b'."))
if choice == "b":
    print("Enter the scalar with which you want to multiply the vector", vector)
    scalar = float(input("and have the scalar product returned."))
    print("The scalar product is:", scalar_product(scalar, vector))
elif choice == "a":
    vector1 = vector
    vector2 = []
    print("Enter the first of the three elements in the second vector, which you want to add to the first vector:", vector1)
    vector2.append(float(input("here.")))
    vector2.append(float(input("Enter the second of the three elements in the second vector.")))
    vector2.append(float(input("Enter the third of the three elements in the second vector.")))
    print(vector2)
    print("The vector addition sum (to the nearest two decimal places) is:", vector_addition(vector1, vector2))
