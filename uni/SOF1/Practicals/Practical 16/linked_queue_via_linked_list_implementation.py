# from listnode import Node  # if had class Node in separate file/module named listnode, would import it in as so

class LinkedQueue:

    def __init__(self):
        # to ensure we can pop element at front efficiently, we must have pointer to front of queue - this is done via
        # _front attribute, and to ensure we can efficiently enqueue element at back, we have _back attribute pointer
        self._back = None  # pointer references bottom of the queue which is first to be out - FIFO principle
        self._front = None  # pointer references Node at top of queue, new additions linked/added here
        # both node pointers set initially to None until a node assigned to them

    def __str__(self):
        return "LinkedQueue([" + str(self._front) + "])"

    def enqueue(self, value):  # enqueue(self, value) pushes the value to the back of the queue
        new_node = Node(value)
        if self._front is None:  # (and by implementation, self._back is None)
            self._front = new_node  # assigning front pointer to first node addition
            self._back = new_node  # assigning back pointer to the first and only node in the linked stack
        else:
            # self._back._next should always be none, technically, no limitations of space implemented in this ADT
            # order matters elsewise will lose a node XO
            self._back._next = new_node  # assigning next attribute/pointer from self._back to the new node
            self._back = new_node  # we must remember to modify the variable pointing to the back of the queue,
            # self._back to the node containing the latest addition of a value to the queue
        return

    def pop(self):  # pop(self) removes and returns the value from front of queue, raising ValueError if queue empty
        if self._front is None:
            raise ValueError("Cannae pop empty queue...")
        else:
            popping_node = self._front  # saving reference to node of popping data value in temporary variable so not
            # lost during changing assignments
            self._front = self._front._following  # self._front now references what self.top._next (used to before change)
            # reference
            if self._front is None:  # if we removed the last remaining element in the stack
                self._back = self._front  # we set back and front pointers to the same null empty node
            popping_node._following = None  # this is optional, sets the reference to the next node from the popped node as
            # None as it is not part of linked list anymore, so technically shouldn't contain reference to next element
            # - not that it can be accessed in the first place though, hummies
            return popping_node._data  # returning the popped node's data value

    def peek(self):
        if self._front is None:  # gotta do this individually so program doesn't cry out error NoneType contains no such
            # attribute/method
            return None
        else:
            return self._front._data

    def __len__(self):
        count = 0
        current_node = self._front
        while current_node is not None:  # or current_node != self._back
            # we know that this is end condition of the queue ~ so stopping counting then
            current_node = current_node._following
            count += 1
        return count


class Node:

    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next

    def __str__(self):  # LinkedQueue._top or LinkedQueue._bottom or LinkedQueue._top(._next)^n is inputted as self,
        # and this returns the contents of one (List)Node
        if self._data is None:
            return ""  # returning "" as opposed to "None"
        elif self._next is None:
            return str(self._data)  # returning just contents of data if it is end of (or gap in) queue
        else:
            return str(self._data) + ", " + str(self._next)  # returning contents of current node but also recursively
            # inputting the next node in the linked queue into conversion to string method


lqueue = LinkedQueue()
lqueue.enqueue(1)
lqueue.enqueue(2)
lqueue.enqueue(3)
print(lqueue)
print(lqueue.pop())
print(lqueue)
print(lqueue.pop())
print(lqueue)
print(lqueue.pop())
print(lqueue)
