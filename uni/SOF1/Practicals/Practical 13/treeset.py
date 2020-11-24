btree = [8, [3, [1, [], []], [6, [4, [], []], [7, [], []]]], [10, [], [14, [13, [], []], []]]]


def isempty(treeset):
    return treeset == [];


def maxvalue(treeset):
    if isempty(treeset):
        return float('-inf');
    elif treeset[2] == []:
        return treeset[0];
    else:
        maxvalue(treeset[2]);


def minvalue(treeset):
    if isempty(treeset):
        return float('inf');
    elif treeset[1] == []:
        return treeset[0];
    else:
        minvalue(treeset[1]);


def add(element, treeset):
    if isempty(treeset):
        treeset.append(element);  # changing mutable original list, hum
        treeset.append([]);
        treeset.append([]);
        return;
    elif element > treeset[0]:
        add(element, treeset[2]);
    elif element < treeset[0]:
        add(element, treeset[1]);
    else:
        return;


def getvalues(treeset):
    output = ""

    def _getvalues(treeset, output):
        if not isempty(treeset):
            output = getvalues(treeset[2], output);
            output += str(treeset[0]) + " ";
            output = getvalues(treeset[1], output);
        return output;

    return output;


def contains(element, treeset):
    if isempty(treeset):
        return False;
    else:
        if treeset[0] > element:
            contains(element, treeset[2]);
        elif treeset[0] < element:
            contains(element, treeset[1]);
        elif treeset[0] == element:
            return True;


def _is_leaf(treeset):
    return treeset != [] and treeset[1] == [] and treeset[2] == [];

def remove(element, treeset):
    if isempty(treeset):
        return;
    elif (not isempty(treeset[1])) and element < treeset[0]:
        # no guarantee that treeset[0] has existing left child without the not condition
        remove(element, treeset[1]);
    elif (not isempty(treeset[1])) and element > treeset[0]:
        remove(element, treeset[2]);
    elif element == treeset[0]:
        if _is_leaf(treeset):
            treeset.clear();
        elif isempty(treeset[1]):
            treeset[0] = treeset[2][0];  # need to do individually elsewise will have [[treeset[2]] - not in syntax
            treeset[1] = treeset[2][1];
            treeset[2] = treeset[2][2];
        elif isempty(treeset[2]):  # if treeset[2] is the empty child
            treeset[0] = treeset[1][0];
            treeset[2] = treeset[1][2];
            treeset[1] = treeset[1][1];  # cannot swap this line and the preceding for some reason =_=
        else:
            replacing = minvalue(treeset[2]);
            treeset[0] = replacing;
            remove(replacing, treeset[2]);
    else:  # arrived at the end of a branch and did not find the element
        return;

remove(7, btree)
print(btree)
remove(6, btree)
print(btree)
remove(14, btree)
print(btree)
remove(4, btree)
print(btree)

"""
Lilian Blot SOFTWARE 1
SOFTWARE 1 PRACTICAL
Binary Trees
Week 8 – Practical 13
In this practical, we will consider binary trees and their nested lists representation. As a
reminder, the data representation has the following properties:
i. An empty tree is an empty list
ii. A tree is a list containing 3 elements
iii. The data of the root
• The left child
• The right child
• The left child and right child are also lists
containing 3 elements
iv. A leaf is a list of 3 elements, where the first
element is the data of the leaf node, the second
and third elements are empty list.
The binary tree above (which is also a binary search tree) can be represented by the nested
list:
[8, [3, [1,[],[]],[6,[4,[],[]],[7,[],[]]]],
 [10,[],[14,[13,[],[]],[]]]]
Exercise 1:
i. Implement the function maxvalue(btree) that returns the maximum value in the
general binary tree, −∞ if the tree is empty. Similarly, implement the function
minvalue(btree) that returns the minimum value in the tree, +∞ if the tree is
empty.
Lilian Blot Software 1
P a g e | 2
Problem:
For the reminder of the practical, we assume that the Set Abstract Data Type (ADT) is
implemented using a BST, and the tree representation used is nested lists. You should
implement all the code for this problem in a file named treeset.py. The aim of this
exercise is to write a series of function to fulfil the Set API.
i. isempty(treeset) that returns True if the tree is empty, False otherwise.
ii. add(element, treeset) that adds the element to the set treeset if it is
not already in the set, do nothing otherwise. treeset should be modified in place,
that is treeset is mutated by the function. Note that after the addition of the
element, the resulting tree should still be a BST. The function does not return a
value.
ii. maxvalue(treeset) that returns the maximum value in the set, −∞ if the tree is
empty.
iii. minvalue(treeset) that returns the minimum value in the set, +∞ if the tree is
empty.
iv. getvalues(treeset) returns a list containing all the element of the set in
decreasing order.
v. contains(element, treeset) returns True if element is in the set, False
otherwise.
vi. equals(treeset _a, treeset _b) return True if the two sets contain the
same elements, False otherwise. It should be noted that the trees representing the
two sets might be different as shown below. Nonetheless, the function should return
True in this case as the two sets contain the same elements 5, 19,21, and 25.
Example: The two trees represent the same set {5,19,21,25}.
Lilian Blot Software 1
P a g e | 3
vii. remove(element, treeset) remove the element from the set. The method does not
return a value. This is a more difficult problem, and the algorithm describe next
should help you.
Binary search tree. Removing a node
Remove operation on binary search tree is more complicated, than add and search.
Basically, in can be divided into two stages:
1. search for a node to remove;
2. if the node is found, run remove algorithm.
Remove algorithm in detail
Now, let's see more detailed description of a remove algorithm. There are three cases,
which are described below.
1. Node to be removed has no children. This case is quite simple we just disposes
off the node.
Example: Remove -4 from a BST.
2. Node to be removed has one child. It this case, node is cut from the tree and
algorithm links single child (with it's subtree) directly to the parent of the removed
node.
Example: Remove 18 from a BST.
Lilian Blot Software 1
P a g e | 4
3. Node to be removed has two children. This is the most complex case.
a) find a minimum value in the right subtree;
b) replace value of the node to be removed with found minimum. Now, right
subtree contains a duplicate!
c) apply remove to the right subtree to remove a duplicate.
Notice, that the node with minimum value has no left child and, therefore, it's
removal may result in first or second cases only.
Example: Remove 12 from a BST. (a) find element in the tree, (b) find minimum
element in the right subtree of the node to be removed. In current example it is 19. (c)
Replace 12 with 19. Notice, that only values are replaced, not nodes. Now we have
two nodes with the same value. (d)Then remove 19 from the right subtree.
(a) (b)
(c) (d)
"""
