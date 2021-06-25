# Abstract data types, commonly abbreviated to ADTs, are a way of classifying data structures based on how they are used
# and the behaviors they provide. They do not specify how the data structure must be implemented but simply provide a
# minimal expected interface and set of behaviors. c/f Data Structure is a concrete implementation of a data type. It’s
# possible to analyze the time and memory complexity of a Data Structure but not from a data type. The Data Structure
# can be implemented in several ways and its implementation may vary from language to language.

class ListNode:

    def __init__(self, data = None):
        self._thisNodeData = data
        self._nextNodeReference = None  # a ListNode contains a reference (arrow) to another ListNode
        # (which is set to None when it is not referencing another ListNode) - it is defined in terms of itself,
        # therefore it is recursive

# to create a small linked list storing 3 then 7 then 12
front_of_list = ListNode()  # a reference to the front/head of the linked list
front_of_list._thisNodeData = 1
front_of_list._nextNodeReference = ListNode(3) # does the same thing but in lesser steps
print(front_of_list._nextNodeReference._thisNodeData == 3)  # ouputs True - yeehawww
front_of_list._nextNodeReference._nextNodeReference = ListNode(5)  # very recursive call, innit
# note: when rearranging linked list structures, it is important to remember that you could lose the remainder of the
# linked list (or a sector) very easily in memory if you lose a reference or rearrange it in a thoughtless way
# e.g let's say we want to rearrange the first linked list from what it currently is 3 -> 7 -> 12 into 3 -> 12 -> 7
# if we referenced 3 -> 7, then we would lose the ListNode which had _thisNodeData attribute of 12 - and what if we'd
# not know the data that it contained - it'd be lost forever T.T
# so therefore it would be better foresight to reference 12 -> 7 before referencing 3 -> 7, as 12 has an empty
# (NoneType) _nextNodeReference attribute and it wouldn't be lost as front_of_list._nextNodeReference._nextNodeReference
# is still referencing the ListNode which keeps 12 as _thisNodeData
