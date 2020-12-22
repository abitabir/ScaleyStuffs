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

"""
1. Write a function that takes as input a tree (defined as above), a start node (e.g. ‘A’), and a
goal (e.g. ‘D’) and returns an ordered list of nodes detailing how the search would progress
if depth-first search was run on the tree. Include code to stop the search if it finds the goal
node. For example, for the above tree: [A, B, D, C] would be returned (or [A, C, B, D],
depending on the implementation).
Test your code with more complicated trees. Try it with a graph instead of a tree. What
happens? Why?

"""

graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}


def dfs(graph, start, goal):  # iterative approach
    visited = []  # aka closed, collection of visited graph nodes
    fringe = [start]  # lifo {for depth first traversal} fringe of expanded but unvisited nodes

    while fringe:  # same as while fringe == []  # same as fringe.pop(-1)
        node = fringe.pop()
        # node = fringe[-1]
        # fringe = fringe[:-1]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            fringe.extend(expanding for expanding in graph[node] if expanding not in visited)

print(dfs(graph, "A", "D"))  # works, returning [A, C, B, D]  # could have also returned [A, B, D, C] order deoending on the implementation
#print(dfs(graph, "A", "C"))  # works, returning [A, C]
#from randomTree_jhs import getTree
#print(dfs(getTree("A, B, C"), "6", "C"))
# idk how to import the random trees to test


"""
Make a copy of your code from part 1 and edit it so that it now implements breadth-first
search instead of depth-first search.
Can you find a way of implementing both breadth-first and depth-first search using the
same search code? How modular can you make your code?
"""

graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E', 'F'], 'D': [], 'E': [], 'F': ['G'], 'G': []}


def bfs(graph, start, goal):
    visited = []  # aka closed, collection of visited graph nodes
    fringe = [start]  # fifo {for breadth first traversal} fringe of expanded but unvisited nodes

    while fringe:  # same as while fringe == []
        node = fringe.pop(0)
        # node = fringe[0]
        # fringe = fringe[1:]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            fringe.extend(expanding for expanding in graph[node] if expanding not in visited)

print(bfs(graph, "A", "G"))  # alphabetical yaaas
graph = {'A': ['B', 'C'], 'B':['D'], 'C':[], 'D':[]}
graph2 = {'A': ['B', 'C'], 'B':['D'], 'C':['E', 'F'], 'D':[], 'E':[], 'F':['G','H'], 'G':[], 'H':[]}
print(dfs(graph, 'A', 'D'))
print(dfs(graph2, 'A', ''))
print(bfs(graph, 'A', ''))
print(bfs(graph2, 'A', ''))

"""
3. Take your representation for the water jug problem from last week’s exercises and
implement in Python. Pass this to your search algorithm and see if you can use it to find a
solution to the problem. Is this the same solution you found manually last week?
"""

# conditions: 0l <= big <= 5l; 0 <= small <= 2l
initial_state = [5, 0]  # where 5 is water in litres in big jug, and 0 is litres of water in small jugh
goal_state = [None, 1]  # goal_state[0] doesn't really matter tbf  # was goal_state = 1  # in either

# four actions methods
def fill_big(previous_state):
    # attempt to pour as much as is feasible from small into big
    big = previous_state[0]
    small = previous_state[1]
    if big != 5 and small != 0:  # avoiding useless computations
        #space_in_big = 5 - big
        pouring = min(5 - big, small)  # if small bigger than space, vs if space bigger than small
        return [big + pouring, small - pouring]

def fill_small(previous_state):
    big = previous_state[0]
    small = previous_state[1]
    if small != 2 and big != 0:
        pouring = min(2 - small, big)
        return [big - pouring, small + pouring]

def dump_big(previous_state):
    big = previous_state[0]
    small = previous_state[1]
    if big != 0:
        return [0, small]

def dump_small(previous_state):
    big = previous_state[0]
    small = previous_state[1]
    if small != 0:
        return [big, 0]


def finding_successors(state):  # state in [big, small] format ~ and clearing up None messes
    output = []
    appending = fill_big(state)
    if appending is not None:
        output.append(fill_big(state))
    appending = fill_small(state)
    if appending is not None:
        output.append(appending)
    appending = dump_big(state)
    if appending is not None:
        output.append(appending)
    appending = dump_small(state)
    if appending is not None:
        output.append(appending)
    return output


def goal_reached(goal, state):
    if len(goal) == 2:
        return goal == state or goal[1] == state[1] or goal[0] == state[0]
    # if isinstance(goal, int):
    #     return goal in state


def water_jug_problem(state, goal, percept_sequence=[]):  # percept_sequence i.e. history  # I would also like a history of actions
    successor_states = finding_successors(state)
    percept_sequence.append(state)

    if goal_reached(goal, state):
        print(percept_sequence, "GOAL REACHED - SUCCESS!!! XD")
        return True
    if len(successor_states) == 0:
        return False

    for successor in successor_states:
        # loop through options not gone through
        if successor not in percept_sequence:
            # algorithms that forget their history are doomed to repeat it, unnecessarily so
            if water_jug_problem(successor, goal, percept_sequence):
                # this recursive function is split into two parts kinda, so need to return True here again
                # to exit the iteration, since the recursion has already been exited from
                return True
    return False  # no goal found in subtrees


print(water_jug_problem(initial_state, goal_state))



def finding_successors_better(current_state, depth=1):
    steps = {}
    state = current_state.copy()  # else changes the global variable at times as lists are mutable
    big = state[0]
    small = state[1]
    if big > 0:
        steps[str(depth) + ". Dump Big"] = dump_big(state)
        if small < 2:
            steps[str(depth) + ". Fill Small"] = fill_small(state)
    if small > 0:
      steps[str(depth) + ". Dump Small"] = dump_small(state)
      if big < 5:
        steps[str(depth) + ". Fill Big"] = fill_big(state)
    return steps


def water_jug_depth_limited_dfs(state, goal, depth=1, successful_output=[]):
    # this one, inspired by model answers, gives steps to get to solution as well yaaaaaaay XD
    if goal_reached(state, goal):  # goal reached?
        return True
    if depth > 10:
        # stopping infinite loops from repeated states ~ also recursive depth limited dfs
        return False
    successors = finding_successors_better(state, depth)
    if len(successors) == 0:
        # cancel efforts if no successors
        return False

    for key, value in successors.items():
        # looping through valid options - no checking if in history in this implementation because depth limited already handles it
        if water_jug_depth_limited_dfs(value, goal_state, depth + 1):  # goal found in subtree
            successful_output.insert(0, key)  # inserts this value at position 0
            return successful_output
    return False  # since no goal found in subtrees


print(water_jug_depth_limited_dfs(initial_state, goal_state))

"""
The Python ‘time’ package allows you to measure the amount of time taken to execute a
given piece of code. For example:
>>> import time
>>> tic = time.perf_counter()
>>> run_my_function()
>>> toc = time.perf_counter()
>>> toc – tic
4.382719374
Use this package to measure how long it takes depth-first search and breadth-first search
to find the goal in your water jug problem.
If you test your timing code multiple times, you may find it returns different values each
time. Why might this be? How could you get around this issue?  # due to background processes going on beyond our control
"""

class Fringe():
    # so generic I can't do anything but copy most of it
    def __init__(self, fifo):
        self.fringe_list = []
        if fifo:  # aka is defined as a queue
            self.is_queue = True
        else:  # aka is defined as a stack
            self.is_queue = False

    def next(self):  # basically getter
        if self.is_queue:
            return self.fringe_list.pop(0)
        else:
            return self.fringe_list.pop()

    def count(self):
        return len(self.fringe_list)

    def append(self, val):  # basically setter
        self.fringe_list.append(val)

def tree_search(graph, start, goal, fringe):
    visited = []
    fringe.append(start)
    while fringe.count() > 0:
        node = fringe.next()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            for neighbour in graph[node]:
                if neighbour not in visited:
                    fringe.append(neighbour)
    return visited

graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
graph2 = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E', 'F'], 'D': [], 'E': [], 'F': ['G','H'], 'G': [], 'H': []}

fringe_queue = Fringe(True)
fringe_stack = Fringe(False)

print(tree_search(graph2, 'A', '', fringe_queue))  # aka fifo aka bfs
print(tree_search(graph2, 'A', '', fringe_stack))  # aka lifo aka dfs

import numpy as np
import time

# timingsssss ~ ticktock
tic = time.perf_counter()
tree_search(graph2, 'A', '', fringe_queue)
toc = time.perf_counter()
print("BFS time: " + str(toc - tic))

tic = time.perf_counter()
tree_search(graph2, 'A', '', fringe_stack)
toc = time.perf_counter()
print("DFS time: " + str(toc - tic))

# more consistent timing over various iterations
# however note that appending takes a longer time than assignment
tic = []
toc = []
for i in range(1, 10):
    tic.append(time.perf_counter())
    tree_search(graph2, 'A', '', fringe_queue)
    toc.append(time.perf_counter())
difference = np.subtract(toc, tic)  # cooooool XD
print("BFS average timing: " + str(np.mean(difference)))

tic = []
toc = []
for i in range(1, 10):
    tic.append(time.perf_counter())
    tree_search(graph2, 'A', '', fringe_stack)
    toc.append(time.perf_counter())
difference = np.subtract(toc, tic)
print("DFS average timing: " + str(np.mean(difference)))





