class Vector:

    def __init__(self, vector_elements = None): # constructor only takes one parameter, list of floats
        # design decision is to store element s of vector in list [a, b, c]
        if vector_elements is None:
            self._vector = [];
        else:
            self._vector = [float(element) for element in vector_elements]

    def __str__ (self):
        # this method enables us to print content of instance using print fucntion
        # decision to represent vectors in '<a, b, c>' string format
        output_string = "<" + ", ".join([str(element) for element in self._vector]) + ">"
        return output_string

    def dim (self):
        # gets dimension of the vector i.e. number of elements
        return len(self._vector)

    def get(self, index):
        # returns value of element at position index in vector
        if index < len(self._vector):
            return self._vector[index]
        else:
            raise IOError("Index provided is out of range!")

    def set(self, index, value):
        # sets element at position index to given value
        if isinstance(index, int) and (isinstance(value, float or int)):
            self._vector[index] = value
            return
        else:
            raise TypeError("Index provided must be of type int and value of type int.or float!")

    def scalar_product(self, scalar):
        """ Returns new Vector containing the scaled product of the operation,
         without modifying the calling instance (the original vector).

        :param scalar: must be int or float else TypeError raised.
        :return: scaled vector product as new Vector.
        """
        if isinstance(scalar, float or int):
            return Vector([float(element*scalar) for element in self._vector])
        else:
            raise TypeError("Scalar provided must be of type int or float.")

    def add(self, other_vector):
        # emulates the vector addition operator
        if not isinstance(self and other_vector, Vector):
            raise TypeError("Both operands being added must be instances of Vector!")
        elif self.dim() != other_vector.dim():
            raise ValueError("Both vector operands must have the same dimension...")
        else:
            return Vector([float(self.get(index) + other_vector.get(index)) for index in range(self.dim())])

    def equals(self, other_vector):
        # determines whether or not the two instances of Vector passed as parameters into the function are equals
        # in terms of their having the same values at the same positions, returning False elsewise
        # (self == other_vector does not produce expected result:  the == operator returns
        # True only if the two vectors are physically stored at the same memory address, it does not compare
        # the content of the two vectors)
        if not isinstance(self and other_vector, Vector): # checking if object is of certain type
            raise TypeError("The two input parameters're not instances of the same class, smh")
        else:
            return self._vector == other_vector._vector


lst1 = [3, 2, 5]
vctr1 = Vector(lst1.copy()) # instance attribute _vector
vctr2 = Vector([7, 67, 0])
print(vctr1.dim())
print(vctr1.add(vctr2))
print(vctr2)