class Point(object):

    @staticmethod
    def distance(p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def translate(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    @property
    def x(self):  # this is the getter
        return self._x

    @x.setter
    def x(self, value):  # this is the setter
        if isinstance(value, str):
            self._x = float(value)
        elif isinstance(value, float) or isinstance(value, int):
            self._x = float(value)
        else:
            raise TypeError('some useful message to be added!')

    @property
    def y(self):  # this is the getter
        return self._y

    @y.setter
    def y(self, value):  # this is the setter
        if isinstance(value, str):
            self._y = float(value)
        elif isinstance(value, float) or isinstance(value, int):
            self._y = float(value)
        else:
            raise TypeError('some useful message to be added!')

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

    def __repr__(self):
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'


class Polygon(object):

    def __init__(self, vertices):
        self._vertices = vertices[:]  # shallow copying cuz don't want mutations

    def __str__(self):
        return '<' + ', '.join(map(str, self._vertices)) + '>'

    def __repr__(self):
        return 'Polygon([' + ', '.join(map(Point.__repr__, self._vertices)) + '])'

    def isadjacent(self, p1, p2):
        if p1 not in self._vertices or p2 not in self._vertices:
            return False

        index_p1 = self._vertices.index(p1)  # returns the position at the first occurrence of the specified value
        index_p2 = self._vertices.index(p2)
        if ((index_p1 == 0 and index_p2 == len(self._vertices) - 1)
                or (index_p2 == 0 and index_p1 == len(self._vertices) - 1)):
            return True

        if (abs(index_p1 - index_p2) == 1):
            return True

        return False

    ############### WRITE YOUR CODE BELOW ###########################

    def isvertex(self, point):
        return point in self._vertices

    def split(self, p1=None, p2=None):
        if p1 is None or p2 is None:
            raise TypeError
        elif p1 == p2 or self.isadjacent(p1, p2) or not (self.isvertex(p1) and self.isvertex(p2)):
            raise ValueError
        else:
            index_p1 = self._vertices.index(p1)
            index_p2 = self._vertices.index(p2)
            poly1 = Polygon(self._vertices[index_p1:index_p2 + 1])
            poly2 = Polygon(self._vertices[index_p2:] + self._vertices[:index_p1 + 1])
            returning = set()
            returning.add(poly1)
            returning.add(poly2)
            return returning

    def cost(self):
        triangulations = set()
        triangulations.add(self.triangulation(self._vertices))
        self.triangulation(self._vertices[:1])

        cost = 0
        return float(cost)

    def point_pairs_combinations_set(self, vertices):
        vertices = self._vertices[::]  # shallow copy if vertices not provided
        # stepping up to challenge and acc doing this recursively
        # or easier to just
        # from itertools import combinations
        # return combinations(vertices, 2)
        # though you have to iterate through it and convert to list or somt

        def _combos(lst, combos=set(), current_point=None):
            if lst == []:  # lastth case
                return
            elif current_point is None:  # first iteration
                _combos(lst[1:], combos, lst[0])
            else:
                adding = [current_point, lst[0]]
                combos.add(frozenset(adding))  # this function WAS returning a set of frozen sets, HOWEVER Point class is not hashable so list it is
                _combos(lst[1:], combos, current_point)
                _combos(lst[1:], combos, lst[0])
            return combos
        return _combos(vertices)

    def validating_combos(self, combos, valid_combos=[]):
        # recursively... T.T
        checking = combos.pop()  # can pop regardless of combos being instance of set (random one popped) or list (last one popped)
        if not self.isadjacent(checking[0], checking[1]):
            valid_combos.append(checking)
        validating_combos(combos, valid_combos)
        return valid_combos

    def triangulation(self, vertices, triangulations=set()):
        combos = self.point_pairs_combinations()
        valid_combos = validating_combos()
        #triangulations.add(#split(i) for i in valid_combos) # but recursively
        return

def validating_combos(combos, valid_combos=set()):
            # recursively... T.T
            checking = combos.pop()
            if not combos[0].Polygon.isadjacent(combos[1]):
                valid_combos.add(checking)
            validating_combos(combos, valid_combos)
            return valid_combos

# p1 = Point(3, 4)
# p2 = Point(4, 6)
# adding = set()
# adding.add(p1)
# adding.add(p2)
# st = []
# st.update(adding)


#print(validating_combos(st))


def point_pairs_combinations(vertices=None):
    # stepping up to challenge and acc doing this recursively
    # or easier to just
    # from itertools import combinations
    # return combinations(vertices, 2)
    # though you have to iterate through it and convert to list or somt
    def _combos(lst, combos=[], current_point=None):
        if lst == []:  # lastth case
            return
        elif current_point is None:  # first iteration
            _combos(lst[1:], combos, lst[0])
        else:
            adding = [current_point, lst[0]]
            combos.append(adding)
            # combos.add(frozenset(adding))  # this function WAS returning a set of frozen sets, HOWEVER Point class is not hashable so list it is
            _combos(lst[1:], combos, current_point)
            _combos(lst[1:], combos, lst[0])
        return combos

    return _combos(vertices)

print(point_pairs_combinations([1, 2, 3, 4, 5, 6]))

