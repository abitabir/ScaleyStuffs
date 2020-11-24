class LinkedStack:

    def __init__(self):
        self._top = None

    def __str__(self):
        return "LinkedStack([" + str(self._top) + "])"  # this uses the .__str__() method of the Node class - this is
        # basically the frontend stuff

    def push(self, value):  # push(self, value) pushes the value onto the top of the stack
        new_node = Node(value)
        if self._top is None:
            self._top = new_node
        else:
            new_node._next = self._top  # since there is a whole list after the self._top, need to make sure it is kept
            # and that the top of the stack is moved to the second latest (now latest after .pop()) addition
            self._top = new_node
        return

    def pop(self):  # pop(self) removes and returns the value at top of stack, raising ValueError if stack empty
        if self._top is None:
            raise ValueError
        # elif self._top._next is None: # don't need this cuz Node.__str__() method takes care of confusing exceptions
        #     returning = self._top._data
        #     self._top._data = None
        #     return returning
        # elif self._top._next._next is None:
        #     returning = self._top._data
        #     self._top._data = self._top._next
        #     self._top._next = None
        #     return returning
        else:
            popping_node = self._top  # reference to node of popping data value
            # OR popping_value = self._top._data # accessing stack attribute, and from there accessing node attribute
            # but then would need to return popping_value only (no ._data attribute suffix)
            self._top = self._top._following  # self._top now references what self.top._next references - nothing being lost
            # self._top._next = self._top._next._next  # don't need to do this as we are losing one node - not
            # rearranging all the elements as we would in an array's having elements added or removed
            popping_node._following = None  # this is optional, sets the reference to the next Node as None as it is not
            # part of linked list anymore, so shouldn't contain reference to next element - not that it can be accessed
            # in the first place though, hummies
            return popping_node._data  # returning the popped node's data value

    def peek(self):
        if self._top is None:  # gotta do this so program doesn't crash on unawares user XOS - will get NoneType has
            # no such attribute/method {they are only defined in the Node and LinkedStack clases} for NoneType elsewise
            # when trying to carry out things on the object
            return None
        else:
            return self._top._data

    def __len__(self):
        # count = 0
        # currentNode = self._top  ## both of these are references, remember
        # nextNode = self._top._next  ## if stack is empty, both of these will contain None (as when new LinkedStack
        # initialised in Node's __init__() method, ._data and ._next attributes default to None if not provided),
        # and program won't crash in assignment to a NoneType so no conditions needed yet - however when getting ._next
        # of NonType will crash so condition needed in next line
        # while nextNode._next is not None:  #  {also yh vars shouldn't be in lowerCamelCase cuz python!}
        #     currentNode = nextNode
        #     nextNode = nextNode._next
        #     count += 1
        # return count
        # this could all be condensed down to: ~ don't need the next_node variable
        count = 0
        current_node = self._top
        while current_node._following is not None:
            current_node = current_node._following
            count += 1
        return count


class Node:

    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next

    def __str__(self):  # LinkedStack._top is inputted as self, and this returns the contents of one (List)Node
        if self._data is None:
            return ""
        elif self._next is None:
            return str(self._data)
        else:
            return str(self._data) + ", " + str(self._next)


lstack = LinkedStack()
lstack.push(1)
lstack.push(2)
lstack.push(3)
print(lstack.pop())
print(lstack.pop())
print(lstack.pop())