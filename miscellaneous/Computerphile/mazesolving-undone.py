# inspired by https://www.youtube.com/watch?v=rop0W4QDOUI

# converts maze with black wall and white entrances/spaces {constraints} into array and returns pathfinding
# and checks from hole in wall all top left right down and sees where it can go, storing visited T/F in separate array
# initially using naive floodfill approach
# inherently allows itself to backtrack using the data structure

class Maze():

    def __init__(self, start):
        self.start = start


class Node:

    def __init__(self):
        self.north
        self.east
        self.south
        self.west


def onePathFinder():
    """
    Converts maze into graph by creating nodes in memory for each square in graph that a decision is to be made.
    :return:
    """


# INCOMPLETE

