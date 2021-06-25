"""
Intelligent Systems 1
Week 4 Lab Sheet
Dr James Stovold
This week we are going to be extending our tree search algorithm to include a heuristic function.
Before you start this lab sheet, ensure you’ve completed last week’s lab sheet so you have a
breadth-first search algorithm that can be used as a starting point.
The example we will be using is Naismith’s Rule. Naismith’s Rule is an estimate for how long it takes
to walk across hilly terrain. The “rule” states that it takes 1 hour to walk 5 km, with an extra hour
added for each 600m of climbing (or 10mins for each 100m of climbing). As such, if you were to
walk up a hill that was precisely 5km long, but with a gradient of 12%, it should take you 2 hours
to complete.
Naismith’s rule should more accurately be termed “Naismith’s heuristic function”, but this doesn’t
have the same ring to it.
We will be building a simple hill-walking planner that tells us the fastest route to travel between
any two castles in the imaginary Pixeldale. In this magical region of the world, descending a hill
takes the same amount of time as walking along the flat. Pixel (autocratic ruler of Pixeldale) is
currently residing in her favourite castle A, but has remembered that she left some cat treats in
her holiday castle J. Because she’s easily distracted by shiny things, she has decided to get you to
determine the fastest route from A to J so she can get her treats without getting distracted.
A roughly-drawn map of Pixeldale is shown below, where each castle has its elevation shown, and
the distance between each castle is shown (conveniently in multiples of 5km). A copy of this map
is also available on the VLE.
The straight-line distances between all castles is provided below:
1. Define a new class that is able to represent the information in the map of Pixeldale above.
I would suggest storing this as a graph where the nodes are castles and the arcs store
information about how long the path is between each castle along with the relative altitude
change. I would also suggest you have a variable to store a heuristic value for each castle.
2. Take a copy of your breadth-first search algorithm from last week. Edit this so that it
implements uniform-cost search for your Pixeldale class above. I’d recommend you have
it print out the nodes it visits in turn.
3. Extend your UCS algorithm to A* by including the heuristic of the straight-line distance
from each castle to J. How well does it work compared with UCS? Does it find the same
solution?
4. Implement Naismith’s rule as a heuristic function. Does this work better or worse than the
straight-line distance?
5. Using the same approach as last week, compare the time taken to find a solution for each
heuristic.
Challenge: Implement iterative-deepening A* search. How much longer does this take to find the
optimal solution compared with A* and UCS? Can you think of a better heuristic than Naismith’s
that might improve the search?
A B C D E F G H I J
A 0 3 3 3 7 7 11 11 15 15
B 0 7 3 7 3 7 11 11 15
C 0 3 3 11 15 7 15 15
D 0 3 7 7 7 15 15
E 0 11 7 3 11 11
F 0 3 7 3 7
G 0 3 3 3
H 0 7 3
I 0 3
J 0
"""


class Castle:
    def __init__(self, name, altitude, neighbours={}, straight_line_distance=None, heuristic_val=None):
        self.name = name
        self.altitude = altitude
        self.neighbours = neighbours  # holds dico with neighbour name and distance from
        self.straight_line_distance = straight_line_distance
        self.heuristic_val = straight_line_distance
        # defaulting to optimistic, underestimating straight line distance if heuristic value not defined
        # self.heuristic_val = naismith_heuristic_function(self, goal)  # could have been, but goal isn't meant to be set upon initialisation, sooo yh

    def set_neighbours(self, neighbours):  # setter, but resetter if they were set upon initialisation
        self.neighbours = neighbours

    def get_neighbours(self):  # getter
        return self.neighbours

    def set_straight_line_distance(self, sld):
        self.straight_line_distance = sld

    def get_straight_line_distance(self):
        return self.straight_line_distance

    def set_heuristic(self, heuristic_val):
        self.heuristic_val = heuristic_val

    def get_heuristic(self):
        return self.heuristic_val

    def get_altitude(self):
        return self.altitude

    def __str__(self):  # returning name instead of <object at point ...> schtuff
        return self.name

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        # for priority queue implementation, if two path costs are equal, returning the first castle alphabetically{? how tho}
        return self.name < other.name

A = Castle("A", 0)
B = Castle("B", 200)
C = Castle("C", 600)
D = Castle("D", 100)
E = Castle("E", 300)
F = Castle("F", 300)
G = Castle("G", 100)
H = Castle("H", 500)
I = Castle("I", 400)
J = Castle("J", 500)

A.set_neighbours({B: 5, C: 5, D: 5})
B.set_neighbours({A: 5, F: 5})
C.set_neighbours({A: 5, E: 5})
D.set_neighbours({A: 5, E: 5, F: 10})
E.set_neighbours({C: 5, D: 5, G: 10, H: 5})
F.set_neighbours({B: 5, D: 10, I: 5})
G.set_neighbours({E: 10, H: 5, J: 5})
H.set_neighbours({E: 5, G: 5, J: 5})
I.set_neighbours({F: 5, J: 5})
J.set_neighbours({G: 5, H: 5, I: 5})

from queue import PriorityQueue


def ucs(start, goal):  # uniform cost search
    visited = []
    fringe = PriorityQueue()
    fringe.put((0, start))
    while not fringe.empty():
        (cost, node) = fringe.get()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return (cost, visited)
            neighbours = node.get_neighbours()
            for (neighbour_node, neighbour_cost) in neighbours.items():
                if neighbour_node not in visited:
                    cumulative_cost = cost + neighbour_cost
                    fringe.put((cumulative_cost, neighbour_node))
    return ("unfound", visited)


print(ucs(A, J))


# setting straight line distances from all nodes to J
A.set_straight_line_distance(15)
B.set_straight_line_distance(15)
C.set_straight_line_distance(15)
D.set_straight_line_distance(15)
E.set_straight_line_distance(11)
F.set_straight_line_distance(7)
G.set_straight_line_distance(3)
H.set_straight_line_distance(3)
I.set_straight_line_distance(3)
J.set_straight_line_distance(0)

# setting precalculated heuristics from a _function_ f(n)
A.set_heuristic(30)
B.set_heuristic(20)
C.set_heuristic(20)
D.set_heuristic(20)
E.set_heuristic(15)
F.set_heuristic(10)
G.set_heuristic(5)
H.set_heuristic(5)
I.set_heuristic(5)
J.set_heuristic(0)


def a_star(start, goal):  # a* search
    visited = []
    path_cost = 0
    fringe = PriorityQueue()
    fringe.put((start.get_heuristic(), 0, start))
    while not fringe.empty():  # for every node
        (_, cost, node) = fringe.get()  # the heuristic isn't really used so denoted by _
        if node not in visited:
            visited.append(node)
            if node == goal:
                return (cost, visited)
            neighbours = node.get_neighbours()
            for (neighbour_node, neighbour_cost) in neighbours.items():
                if neighbour_node not in visited:
                    heuristic_recalculation = cost + neighbour_cost + neighbour_node.get_heuristic()
                    cumulative_cost = cost + neighbour_cost
                    fringe.put((heuristic_recalculation, cumulative_cost, neighbour_node))
    return ("unfound", visited)

print(a_star(A, J))



# compareing averages between usc and a*
### or alternative ways of timings with less timing actually required

from numpy import subtract, median
from time import perf_counter

tic = []
tac = []
toe = []

for i in range(10):
  tic.append(perf_counter())
  ucs(A, J)
  tac.append(perf_counter())
  a_star(A, J)
  toe.append(perf_counter())

ucs_avg = median(subtract(tac, tic))
ucs_avg = median(subtract(toe, tac))

print("UCS Average: " + str(ucs_avg))
print("A* Average: " + str(ucs_avg))



# wordy

tic = []
toc = []
for iteration in range(10):
    tic.append(perf_counter())
    a_star(A, J)
    toc.append(perf_counter())
average_time_taken = median(subtract(toc, tic))
print("Average Time Taken for A* Search Informed Using Straight Line Distances: ", average_time_taken)


def naismith_heuristic_function(start, goal):  # estimate for walking across hilly terrain that takes not descension into account
    climbing_height_time_in_hrs = (goal.get_altitude() - start.get_altitude()) / 600 if start.get_altitude() < goal.get_altitude() else 0
    # 0 cuz descending height is same as walking on level ground, according to this model
    # 10 mins added for every 100m of climbing (aka vertical)
    # easier to do it 1hr/600m == (1/600)hr/m
    walking_length_time_in_hrs = start.get_straight_line_distance() / 5
    # relies upon previous input of sld betwixt start castle node and end castle node
    # takes 12 mins for every 1 km of walking (aka horizontal)
    time_taken = climbing_height_time_in_hrs + walking_length_time_in_hrs
    return time_taken


# redefining heuristics (could have also done from class but then progression wouldn't have been seen)
# (from castle node to predefined goal J) being calculated to the castle nodes
# too repetitive, man
# A.set_heuristic(naismith_heuristic_function(A, J))
# B.set_heuristic(naismith_heuristic_function(B, J))
# C.set_heuristic(naismith_heuristic_function(C, J))
# D.set_heuristic(naismith_heuristic_function(D, J))
# E.set_heuristic(naismith_heuristic_function(E, J))
# F.set_heuristic(naismith_heuristic_function(F, J))
# G.set_heuristic(naismith_heuristic_function(G, J))
# H.set_heuristic(naismith_heuristic_function(H, J))
# I.set_heuristic(naismith_heuristic_function(I, J))
# J.set_heuristic(naismith_heuristic_function(J, J))
castle_graph = [A, B, C, D, E, F, G, H, I, J]
for castle_node in castle_graph:
    castle_node.set_heuristic(naismith_heuristic_function(castle_node, J))

print(a_star(A, J))  # does anything change with the new fancy pants heuristic, hmmmm?
# works worse than the sld than tbf X0S


tic = []
toc = []
for iteration in range(10):
    tic.append(perf_counter())
    a_star(A, J)
    toc.append(perf_counter())
average_time_taken = median(subtract(toc, tic))
print("Average Time Taken for A* Search Informed Using Naismith's Heuristic Function: ", average_time_taken)


# challenge


def a_star_iterative_deepening(start, goal, tao=10, deepening=0, depth=0, visited=[], fringe=PriorityQueue()):
    fringe.put((start.get_heuristic(), 0, start))
    while not fringe.empty():
        deepening += tao  # need to have seperate constant else tao wouldn't remain constant
        while depth <= deepening:
            (_, cost, node) = fringe.get()
            if node not in visited:
                depth += 1
                if node == goal:
                    return (cost, visited)
                visited.append(node)
                neighbours = node.get_neighbours()
                for (neighbour_node, neighbour_cost) in neighbours.items():
                    if neighbour_node not in visited:
                        heuristic_recalculation = cost + neighbour_cost + neighbour_node.get_heuristic()
                        cumulative_cost = cost + neighbour_cost
                        fringe.put((heuristic_recalculation, cumulative_cost, neighbour_node))
    return ("unfound", visited)

print(a_star_iterative_deepening(A, J))  # idk why it doesn't give full [A, C, B, D, F, E, H, I, J] as opposed to [A, C, B, D, F, E, H, I] needs rechecking but not enough time so yh
