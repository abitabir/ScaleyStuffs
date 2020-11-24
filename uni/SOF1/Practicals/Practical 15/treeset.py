class TreeSet:

    def __init__(self, root = None):
        self._root = root
        self._left = None
        self._right = None

    def isempty(self):
        return self._root is None

    def __str__(self):
        return '{' + ', '.join([str(element) for element in self._get_values_in_order()]) + '}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(self and other, TreeSet):
            return self._get_values_in_order() == other._get_values_in_order()
        else:
            return NotImplemented("as both operands need to be instances of the TreeSet class")

    def add(self, element):
        if self.isempty():
            self._root = element
            return
        elif element > self._root:
            if self._left is None:
                self._left = TreeSet(element)
            else:
                self._left.add(element)
        elif element < self._root:
            if self._right is None:
                self._right = TreeSet(element)
            else:
                self._right.add(element)
        else: # elif element == self._root:
            return

    def __add__(self, element):
        self.add(element)
        return

    def remove(self, element):
        if self.isempty():
            return KeyError
        elif element < self._root and self._right is not None: # cannot carry out remove operation on NoneType, hum
            self._right.remove(element)
        elif element > self._root and self._left is not None: # elsewise, without latter condition,
            # AttributeError: 'NoneType' object has no attribute 'remove' given additionally if self._leftOR_right
            # are NoneTypes, they won't be able to have the .isempty() method performed unto them
            self._left.remove(element)
        elif element == self._root:
            if self._right is None and self._left is None:
                self._root = None
            elif self._right is None:
                self._root = self._left._root
                self._right = self._left._right
                self._left = self._left._left
            elif self._left is None:
                self._root = self._right._root
                self._left = self._right._left
                self._right = self._right._right
            else: # if both children are present
                replacing = self._right.minvalue()
                self._root = replacing
                self._right.remove(replacing)
        else:  # arrived at the end of a branch and did not find the element ~ all NoneTypes ended here
            return KeyError

    def minvalue(self):
        if self.isempty():
            return float('+inf') # min value found is +infinity otherwise would override the
            # min values on other branch
        elif self._left is None: # if you pass self._left in as parameter of .isempty() won't work as it hasn't
            # been extended as an instance of the class TreeSet LinkedList functionality yet
            return self._root
        else:
            self._left.minvalue()

    def maxvalue(self):
        if self.isempty():
            return float('-inf')
        elif self._right is None:
            return self._root
        else:
            self._right.maxvalue()

    def __contains__(self, element):  # if element in tree will return true or false, hum
        if self.isempty():
            return False
        else:  # basically halving the elements of the set that need to be traversed each time - BINARY SEARCH
            if self._root > element and self._left is not None: # can't call .__contains__() on self._left if it is None because it hasn't had an
                # assignment to TreeSet created yet, so can't call TreeSet methods on it cuz it's NoneType
                self._left.__contains__(element)
            elif self._root < element and self._right is not None:
                self._right.__contains__(element)
            elif self._root == element:
                return True
            else:
                return False

    def _get_values_in_order(self):  # returns list of descending values of set passed in paramter
        output = []
        if not self.isempty():
            if self._left is not None:
                output += self._left._get_values_in_order() # append is twice as fast performance wise than = or +=
                # but here += copies all the elements of the RHS list into the LHS list,
                # as opposed to append which only adds one item to the list
            output.append(float(self._root)) # in order traversal - element added to output
            # i.e. visited after visiting maximum way down left
            if self._right is not None:
                output += self._right._get_values_in_order()
            return output
        return output

    def difference(self, other): # taking away b's elements from a's elements
        elements = self._get_values_in_order()
        other_elements = other._get_values_in_order()
        returning = TreeSet()
        for index in range(len(elements)):
            if elements[index] not in other_elements: # I think traversing list version of other more efficient than
                # traversing our defined via .__contains__()
                returning.add(elements[index])
        return returning

    def __sub__(self, other):  # now a - b (if both are sets) will return the elements of set a without the elements
        # that are also in set b
        return self.difference(other)

    def intersection(self, other):
        elements = self._get_values_in_order()
        other_elements = other._get_values_in_order()
        returning = TreeSet()
        for index in range(len(elements)):
            if elements[index] in other_elements:
                returning.add(elements[index])
        return returning

    def __and__(self, other):   # now a & b (if both are sets) will return the elements of set a that are also in set b
        return self.intersection(other)

    def addall(self, values):
        for element in values:
            self.add(element)
        return

    def union(self, other):
        elements = self._get_values_in_order()
        other_elements_not_in_elements = [element for element in other._get_values_in_order() if element not in elements]
        returning = TreeSet()
        returning.addall(elements + other_elements_not_in_elements)
        return returning

    def __or__(self, other):   # now a | b (if both are sets) will return a set of all the elements
        # in either set a or set b i.e. the union of
        return self.union(other)

    def isdisjoint(self, other):
        return (self & other).isempty()  # self.intersection(other) contains nowt

    def issubset(self, other):  # is self subset of other?
        # return self.union(other) == other  # other == self | other
        return (self - other).isempty()

    def issuperset(self, other):  # is self superset of other?
        # return self.union(other) == self  # self == self | other
        return (other - self).isempty()

    def symmetric_difference(self, other):
        returning = TreeSet()
        self_elements_relative_complement_list = (self - other)._get_values_in_order()
        other_elements_relative_complement_list = (other - self)._get_values_in_order()
        returning.addall(self_elements_relative_complement_list + other_elements_relative_complement_list)
        return returning

    def __xor__(self, other):  # returns symmetric difference of two sets when inputted in form a ^ b
        return self.symmetric_difference(other)

    def discard(self, element):
        try:
            self.remove(element)
        except KeyError:
            return  # catching KeyError programmed into .remove()

    def clear(self): # it is enough to reset head of LinkedList/root of BST to None in order to completely delete the
        # whole abstract data type, as unlike in C and C++ in which you would have to iterate over whole list and free
        # every element, Python has handy garbage collection (technically usually you don't even have to delete ADT as
        # when the lifetime of the head variable {one that points to first element in LinkedList} ends, if you don't
        # have any other references to the list, the list will become unreachable and eligible for collection
        # automatically, buuut not good practice to solely rely upon this, hum)
        # if you want to make the list eligible for collection before the head variable's lifetime ends,
        # setting head = None would work, as would del head. (note: del means unset this variable, not delete this object)
        self = TreeSet()
        # this is the same as
        # self._root = None
        # self._left = None
        # self._left = None
        # so all linkingnesses lost, hum

    def pop(self, popping = None): # popping (i.e. removing and returning) out element with greatest value in TreeSet
        # (could've done random? idk but effort. also isn't popping from the top of a stack or bottom of queue
        # so I coulda popped the root every time if implementing FIFO (or the most deep one if LIFO) principle but
        # task wasn't that specific soooo, it only said arbritary value, though this isn't random selection by chance
        # you can't traverse a set tho and there shouldn't be a pattern, hmmm, confusion)
        if not self.isempty():
            if popping is None:
                popping = self.maxvalue()
            self.remove(popping)
            return popping
        else:
            raise KeyError

tree = TreeSet()
tree2 = TreeSet()
print('empty tree:', tree)
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)
print('8 elements:', tree)

tree2.add(1)
tree2.add(2)
tree2.add(3)


tree.clear()
print(tree)

tree = TreeSet()
print(tree)