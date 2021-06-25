"""
Implementing a Deque ADT, using a circular doubly linked list representation.
{note:
 -> circular linked list is a list where the last list node of the list points to the first
 -> doubly linked list is a list whose nodes have a pointer to the preceding node as well as the following one
}
The methods should be fast and take the same amount of operations.
"""


class LinkedDeque:

    class _Node():
        """ _Node is an inner class of LinkedDeque - we can define classes within classes, just like we can do classes
        within classes. This is useful when one needs to declare private internal data structure, such as a list node.
        """

        def __init__(self, data=None, preceding=None, following=None):
            self._data = data  # setting data (if inputted, else None) to attribute of self ~ a node being initialised
            self._preceding = preceding  # setting reference to previous node
            self._following = following  # setting reference to next node

        def __str__(self):
            if self is None:
                return None
            elif self._following is None:
                return str(self._data)
            else:
                return str(self._data) + ", " + str(self._following)

    def __init__(self, values=None):  # creates empty deque
        self._front = None
        if values is not None:  # refactoring __init__ so that providing a list of values
            # e.g. dequeA = LinkedDeque([1, 2, 3])  # creates a deque containing all those values
            for val in values:
                self.append(val)

    def str(self):
        try:
            nodes = ', '.join([str(node._data) for node in self])
        except TypeError:  # error raised when trying to access nonexistent _data attribute of NoneType
            nodes = None
        finally:
            return "LinkedDeque([" + nodes + ")]"

    def __str__(self):
        output = "LinkedDeque(["
        if self._front is not None:
            output += str(self._front._data)  # gotta do once before while condition
            current_node = self._front._following
            while current_node != self._front:
                output += ", " + str(current_node._data)
                current_node = current_node._following
        output += "])"
        return output

    def append(self, value):  # add an element to the right side of the deque (the end of the linked list)
        if self._front is None:
            self._front = LinkedDeque._Node(value, self._front, self._front)
            # it is circular, so we must ensure that a single element links to itself
            self._front._preceding = self._front
            self._front._following = self._front
        else:
            new_node = LinkedDeque._Node(value, self._front._preceding, self._front)  # need to call outer_class.inner_class() cuz it belongs to the outer class
            new_node._preceding._following = new_node
            self._front._preceding = new_node
            # self._front need not be changed
            return

    def append_left(self, value):  # add an element to the left side of the deque (the front of the linked list)
        self.append(value)
        self._front = self._front._preceding  # literally does the same thing without the hassle of Lilian's code imo
        # quite very inexperienced though I am XOS

    def pop(self):  # remove and return the rightmost element - that is, the last element in the linked list
        if self._front is None:
            raise ValueError("Cannae pop empty Deque ADT, smh")
        elif self._front._preceding  is self._front:  # if only one element in deque
            popping_node = self._front
            self._front = None
        else:
            popping_node = self._front._preceding  # assigning temp variable to reference of node of value being popped
            self._front._preceding._preceding._following = self._front
            self._front._preceding = self._front._preceding._preceding
            popping_node._following = None
            popping_node._preceding = None
            # no associations with LinkedDeque now (not mandatory)
        return popping_node._data

    def pop_left(self):  # remove and return the leftmost element (that is first element in the linked deque)
        if self._front is None:
            raise ValueError("Cannae pop empty Deque ADT, smh")
        elif self._front._following is self._front:  # if only one element in deque
            popping_node = self._front
            self._front = None
        else:
            popping_node = self._front  # assigning temp variable to reference of node of value being popped
            self._front._following._preceding = self._front._preceding  # or popped._previous._next = self._front._next
            self._front._preceding._following = self._front._following  # self._front._next._previous = popped._previous
            self._front = self._front._following
            popping_node._following = None
            popping_node._preceding = None
            # no associations with LinkedDeque now (not mandatory)
        return popping_node._data

    def __len__(self):
        count = 0
        if self._front is not None:
            count += 1
            current_node = self._front._following
            while current_node._following is not self._front:
                current_node = current_node._following
                count += 1
        return count

    def __eq__(self, other):  # not that clean but oh well
        output = False
        if len(self) == len(other):
            if self._front is None and other._front is None:  # aka if len(self._front) == len(other._front) == 0:
                output = True
            elif self._front._following is self._front and other._front._following is other._front:
                # if both linked deques only have one node in
                output = self._front._data == other._front._data
            elif not (self._front is None or other._front is None) and not (self._front._following is self._front or other._front._following is other._front):
                output = self._front._data == other._front._data
                current_node_self = self._front._following
                current_node_other = other._front._following
                while current_node_self._following is not self._front and output:  # definite terminating condition and
                    # loop ender if corresponding (in terms of order in different deques) nodes's datas different
                    # need not worry about current_node_other._following being not other._front cuz are same length
                    current_node_self = current_node_self._following
                    current_node_other = current_node_other._following
                    output = current_node_self._data == current_node_other._data
            # no else as else contains all the Falses
        return output

    def __getitem__(self, key):
        if self._front is None:
            raise IndexError("Cannot retrieve item from an empty instance of the class LinkedDeque")
        elif key < 0:  # deal with negative indexes like built in collections do
            key = key + len(self)
        elif key > len(self):
            key = key - len(self)  # shouldn't rrreaaally
        elif key == 0:
            return self._front._data
        count = key - 1
        current_node = self._front._following
        while count > 0 and current_node is not self._front:  # was once ~ while count < len(self) - 1:
            current_node = current_node._following
            count -= 1
        if current_node is self._front:  # or count < 0  # should rrreaaally
            raise IndexError
        return current_node._data

    def get_item(self, key):  # gets item from key provided
        return self.__getitem__(key)

    def get_key(self, item):  # gets key from item provided
        if self._front is None:
            raise IndexError("Cannot retrieve an(y) item from an empty instance of the class LinkedDeque")
        index = 0
        current_node = self._front
        while index < len(self):
            if item == current_node._data:
                return index  # of where the item parameter found - if it was
            current_node = current_node._following  # preconditions (as in variable changed after change lollies)
            index += 1
        return "No such item found in LinkedList provided"

    def __setitem__(self, key, value):  # sets item at key to value
        if self._front is None:
            if key == 0:
                self._front._data = value
            else:
                raise IndexError("Cannot set item at given index out of bounds for this instance of class LinkedDeque")
        elif key < 0:  # deal with negative indexes like built in collections do
            key = key + len(self)
        count = key - 1
        current_node = self._front._following
        while count > 0 and current_node is not self._front:  # was once ~ while count < len(self) - 1:
            current_node = current_node._following  # preconditions (as in variable changed after change lollies)
            count -= 1
        if current_node is self._front or count < 0:
            raise IndexError
        current_node._data = value
        return

    def __delitem__(self, key):
        if self._front is None:
            raise IndexError("Cannot delete data at index from an empty instance of the class LinkedDeque")
        elif key < 0:  # deal with negative indexes like built in collections do
            key = key + len(self)
        elif key == 0:
            self._front._data = None
            return
        count = key - 1
        current_node = self._front._following
        while count > 0 and current_node is not self._front:  # was once ~ while count < len(self) - 1:
            current_node = current_node._following
            count -= 1
        if current_node is self._front or count < 0:
            raise IndexError
        current_node._data = None
        return

    def del_via_key(self, key):  # deletes node at index provided
        return self.__delitem__(key)

    def del_via_item(self, value):  # deletes node containing value provided
        if self._front is None:
            raise IndexError("Cannot delete an(y) item from an empty instance of the class LinkedDeque")
        index = 0
        current_node = self._front
        while index < len(self):
            if value == current_node._data:
                current_node._data = None
                return
            current_node = current_node._following  # preconditions (as in variable changed after change lollies)
            index += 1
        raise ValueError("No such item found in LinkedList provided")

    def __add__(self, other):
        if len(self) == 0:
            return other
        elif len(other) == 0:
            return self
        else:
            returning = LinkedDeque()
            # gonna traverse through self first and add its elements to new deque
            current_node = self._front
            count = 0
            while count < len(self) + 1:
                returning.append(current_node._data)
                current_node = current_node._following
                count += 1
            # gonna traverse through other last and add its elements to new deque
            current_node = other._front
            count = 0
            while count < len(other) + 1:
                returning.append(current_node._data)
                current_node = current_node._following
                count += 1
            return returning


ldeque = LinkedDeque()
ldeque.append(7)
ldeque.append(8)
ldeque.append(9)
ldeque.append_left(6)
ldeque2 = LinkedDeque([6, 7, 8, 9])
print(ldeque2 + ldeque)
print(ldeque2.get_key(7))
print(ldeque == ldeque2)
print(ldeque)
print(ldeque.pop())
print(ldeque)
print(ldeque.pop())
print(ldeque)
print(ldeque.pop_left())
print(ldeque)
print(ldeque.pop_left())
print(ldeque)
print(ldeque.pop())
print(ldeque)