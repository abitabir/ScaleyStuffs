class Vector:
    # we shall try to improve the functionality of the class vector from Practical 15
    # by overloading existing operators and refactoring your code
    # try to ensure backwards compatibility with the previous version of this class Vector in Practical 14,
    # so alll the tests from the previous practical should still work

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

    def dim(self):
        return len(self._vector)

    def get(self,
            index):  # refactored from previous practical to ensure no duplication of code. Method kept for backward compatibility.
        return self[index]

    def set(self, index,
            value):  # refactored from previous practical to ensure no duplication of code. Method kept for backward compatibility.
        self[index] = value

    def scalar_product(self,
                       scalar):  # refactored from previous practical to ensure no duplication of code. Method kept for backward compatibility.
        return scalar * self

    def add(self,
            other):  # refactored from previous practical to ensure no duplication of code. Method kept for backward compatibility.
        return self + other

    def equals(self,
               other):  # refactored from previous practical to ensure no duplication of code. Method kept for backward compatibility.
        return other == self

# changing from here onwards
    def __eq__(self, other_vector):
        # instead of using .equal() method - overriding the == operator
        if not isinstance(self and other_vector, Vector): # checking if object is of certain type
            return NotImplemented
        else:
            return self._vector == other_vector._vector

    def __ne__(self, other_vector):
        # overriding the existing python != operator
        if not isinstance(self and other_vector, Vector):  # checking if object is of certain type
            return NotImplemented
        else:
            return self._vector != other_vector._vector

    def __add__(self, other_vector):
        # can override __add__ method to overload the + operator
        # with vector addition operator being commutative i.e v1 + v2 == v2 + v1
        if not isinstance(self and other_vector, Vector):
            raise TypeError("Both operands being added must be instances of Vector!")
        elif self.dim() != other_vector.dim():
            raise ValueError("Both vector operands must have the same dimension...")
        else:
            return Vector([float(self.get(index) + other_vector.get(index)) for index in range(self.dim())])

    def __rmul__(self, scalar):
        # can override __mul__ method to overload the * operator with constrictions that 3 * v1 is allowed
        # but v1 * 3 is not, where 3 is a scalar and v1 is an instance of Vector
        # however in order to implement this order of acceptance's accepting, we override the __rmul__ operator instead,
        # which takes in the paramater to the right (from onlooker's perspective) of the operand first
        # and looks into the methods that that parameter's class which it is an instance of contains, hum
        """only scalar * vector is allowed.
         vector * scalar is not valid, hence implementing only __rmul__."""
        if isinstance(scalar, float or int) and isinstance(self, Vector):
            return Vector([float(element*scalar) for element in self._vector])
        else:
            return NotImplemented

    def __iadd__(self, other_vector):
        # implements programming shortcut for v1 += v2 as opposed to the
        # (slightly lollies) more longwinded way of v1 = v1 + v2
        return self + other_vector

    def __imul__(self, scalar):
        # implements programming shortcut for v1 *= scalar as opposed to the
        # (slightly lollies) more longwinded way of v1 = 3 * v1 (remember scalar first order XOS)
        return scalar * self

    def __getitem__(self, key):
        if isinstance(key, int or float):
            return self._vector[key]
        else:
            return TypeError

    def __setitem__(self, key, value):
        if isinstance(key and value, int or float):
            self._vector[key] = float(value)
            return
        else:
            return TypeError

lst1 = [3, 2, 5]
vctr1 = Vector(lst1.copy()) # instance attribute _vector
vctr2 = Vector([7, 67, 0])
print(vctr1.dim())
print(vctr1.add(vctr2))
print(vctr2)