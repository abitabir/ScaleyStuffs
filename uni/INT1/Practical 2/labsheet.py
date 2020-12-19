"""
For this lab, we will initially build a search tree algorithm based on a pre-defined tree, rather than
a problem representation. Then, towards the end we will look at how to adapt our algorithm to
work with the implicit search tree from a problem.
We can define a graph in Python using a dictionary:
graph = {'A': ['B', 'C'], 'B':['D'], 'C':[], 'D':[]}
which defines a graph that looks like this:
D <- B <- A -> C
If you require random graphs for testing purposes, there is some Python code on the VLE which
will provide this for you.

"""